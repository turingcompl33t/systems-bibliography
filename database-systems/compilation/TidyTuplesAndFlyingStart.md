## Tidy Tuples and Flying Start: Fast Compilation and Fast Execution of Relational Queries in Umbra (2021)

Timo Kersten, Viktor Leis, and Thomas Neumann.

Available [here](http://db.in.tum.de/people/sites/kersten/Tidy%20Tuples%20and%20Flying%20Start%20Fast%20Compilation%20and%20Fast%20Execution%20of%20Relational%20Queries%20in%20Umbra.pdf)

### Big Idea

Design a code generation system from the ground-up for low-latency query compilation.

### Summary

The authors present the query compilation pipeline in _Umbra_. The infrastructure is described in the context of three primary technical contributions:
- The _Tidy Tuples_ code generation framework
- The Umbra intermediate representation
- The _Flying Start_ compiler backend for the Umbra IR

The authors implement each of these three features in the Umbra DBMS. An experimental evaluation shows that Umbra achieves query latency that rivals that of non-compiled systems (i.e. standard query interpretation as in Postgres) while simultaneously enabling steady-state throughput that matches or exceeds that of HyPer.

### Commentary

This paper is so full of interesting ideas that I am going to break up the _Commentary_ section into three distinct subsections, one for each of the primary contributions of the paper.

**Tidy Tuples**

_Tidy Tuples_ is the name the authors use to describe their framework for code generation. In the case of Umbra, code generation translates from the physical relational algebra operators of the plan tree to an Umbra IR program. 

One interesting thing the authors note in the introduction in reference to their code generation framework is that the "question of how to build a code generator is not yet settled." As evidence of this, they cite the three papers: _Building Efficient Query Engines in a High-Level Language_, _How to Architect a Query Compiler_, and _How to Architect a Query Compiler, Revisited_. I found this observation interesting because it seems that the Umbra team has indeed "settled" the issue of how to build a code generator - they generate fast code with extremely low latency. What more do we want from our code generators?

The authors praise the LB2 code generator implementation for its type safety and maintainability. However, they also point out that the compilation latency of the LB2 approach is far too high - 1000x slower than what Umbra is able to achieve. The authors claim that they adopt ideas from the LB2 implementation in their own code generator. The best I can figure, the primary technique from LB2 that Umbra implements is the expressiveness of the code generation API. The importance of this should not be underestimated. For example, in NoisePage, we manually invoke operations at the code generation layer to insert bytecode instructions into the TPL program. In contrast, in Umbra, you would never manually manipulate the program at the code generation layer. Instead, you would program some logic (e.g. the implementation of a chaining hashtable) in a manner that is familiar to single-stage programming (i.e. "normal programming" that is not intended to generate code) and rely on operator overloading on the `SQLValue` type to translate operations into the corresponding code generation calls to actually construct the program. This is an extremely important idea, and is definitely something that the NoisePage code generation engine would benefit from.

But, backing up, the authors describe Tidy Tuples as a framework for code generation with two primary goals: principled, maintainable design and low-latency code generation. Tidy Tuples is composed of the following logical layers:
- Operator Translators
- Data Structures
- Tuples
- SQL Values
- Codegen API

The most important aspect of this design is the fact that low-level code generation details are hidden by the lower layers of the stack. This implies that high-level constructs like a hash join translator or the implementation of a join hashtable are implemented in a familiar, easy to read and maintain style where intent is expressed directly, and the lower layers take care of the details of generating code to "realize" these high-level operations in the Umbra IR program. Of course, hiding implementation details behind abstractions is nothing new in software engineering, but this is definitely something that we have overlooked in the implementation of the NoisePage bytecode generator.

**Umbra IR**

The Umbra intermediate representation is a major engineering achievement, but there is less novel material to address in this section of the paper.

The key takeaway is that the authors choose to implement their own intermediate representation, Umbra IR, instead of using an existing intermediate representation such as LLVM IR, such that they can implement codesign of the instruction set with the database system. That is, they design the intermediate representation with the goals of use in their database system in mind. Specifically, they design Umbra IR for a more efficient program representation than LLVM IR. LLVM IR is designed for maximum flexibility such that complex optimization passes may be performed on the intermediate representation (think of all of the optimization passes that LLVM supports, the IR must enable these complex optimizations by supporting nearly unlimited access to and manipulation of the underlying program). In contrast, the Umbra IR is not designed for complex optimization passes, therefore the authors can sacrifice much of the flexibility of LLVM IR to get a more efficient implementation that is faster to read and write.

Umbra IR also adds some database-system specific instructions, but these are still relatively low-level. For instance, Umbra IR supports checked arithmetic and null-check instructions.

**Flying Start**

The final technical contribution of this paper, _Flying Start_, is a compiler backend designed for low-latency translation of Umbra IR to native x86 machine code. First off, we need to take a sentence or two to appreciate the fact that the Umbra team _wrote their own compiler backend_ in order to get the best possible performance out of their system. I have never written a compiler backend, but from all of my work with LLVM, this is always the area of the system that is reserved for true hardcore compiler people - a place where not even those who are comfortable with low-level program manipulation in LLVM IR typically dare to go. This is an extremely impressive engineering accomplishment. For instance, this implies that the Umbra team had to write their own register allocator. This is a well-studied problem in compilers so they had a solid foundation on which to base their implementation, but it is still a non-trivial undertaking.

Flying Start replaces the LLVM IR interpreter in HyPer in the adaptive query execution mechanism used within Umbra. This implies that it is designed for low-latency compilation and subsequent execution. Obviously the big difference here is that there is no longer any interpreter involved - all of the strategies available to the adaptive execution framework operate directly on native code. Therefore, Flying Start heavily prioritizes fast compilation of native x86.

The author achieve low-latency compilation by implementing an extremely "simple" single-pass compiler. Each Umbra IR instruction is translated to a fixed sequence of native x86 instructions. Minimal optimizations are performed during native code generation, including some constant folding , a separate dead-code elimination pass, lazy calculation of addresses (to take advantage of complex x86 addressing modes), and fusion of comparisons and branches (to avoid manual stores and subsequent loads from the flags register).

**Bringing it all Together**

In the _Related Work_ section, the authors present something of a timeline (or evolution) of code generation for database systems. 

First, they describe how HyPer generates LLVM IR directly from relational algebra operators. Naturally, this approach has proven wildly successful, and the performance of HyPer has stood the test of time (it seems that it is _still_ the baseline for high-performance analytics against which all new systems are compared). However, a major downside of code generation in HyPer is that it is relatively low-level - translating directly from relational algebra to LLVM IR is a big step down the abstraction hierarchy, making the code required to accomplish this complex and difficult to maintain. 

The approach proposed in _How to Architect a Query Compiler_ is a response to this concern. In that paper, the authors propose to use the well-established compiler technique of _progressive lowering_ to gently traverse multiple abstraction levels from the relational algebra operators of the query plan down to a final intermediate representation or machine code. This is a nice, principled approach, but comes with its own drawbacks in the form of high compilation latency and the added complexity of multiple, interacting intermediate representations. 

Finally, in _How to Architect a Query Compiler, Revisited_, the authors propose a distinct approach in which all code generation is performed in a single step: with the help of the Lightweight Modular Staging library, the authors use _generative programming_ to specialize an interpreter for a particular query plan. Again, this approach is principled, and the Umbra team goes so far as to call it "elegant", but, like the previous approach, it suffers from high compilation latency.

Therefore, the authors of this paper claim that there approach combines the best ideas of these prior approaches to the problem of code generation. They utilize an adaptive execution model as in HyPer. They utilize a multi-layered approach within the Tidy Tuples code generation infrastructure as in LegoBase that limits the complexity required at each abstraction level, but stop short of creating full-fledged intermediate representations - the query plan is still lowered to Umbra IR in a single step. Finally, they use the host language (C++) type system to make the code generator both expressive and safe as in LB2, but do not go so far as to implement a complete interpreter that is then specialized to realize query compilation.

This is the first time, in any of these papers, that I have seen a nice chronology of ideas and their connection among one another. I think this topic deserves a bit more attention - how all of these different approaches to code generation fit together and build on one another. How different are they, really?

### Questions

- The authors use the example of systems like Tableau that automatically generate SQL queries based on user interaction with a graphical interface as the motivation for the need for low-latency query compilation. In these situations, high-latency compilation results in a noticeable degradation of the user experience. How important is this use case? Is the demand for meeting this need growing or shrinking?

### Further Reading

- [Efficient Generation of Machine Code for Query Compilers (2020)](EfficientGenerationFlounderIR.md)
- Just-In-Time Data Virtualization: Lightweight Data Management with ViDa (2015)
- [Adaptive Execution of Compiled Queries (2018)](AdaptiveExecutionCompiledQueries.md)
- Evaluating End-to-End Optimization for Data Analytics Applications in Weld (2018)
- Thriving in the No Man's Land Between Compilers and Databases (2019)
