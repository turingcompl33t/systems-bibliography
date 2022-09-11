## Efficient Generation of Machine Code for Query Compilers (2020)

Henning Funke, Jan Muhlig, and Jens Teubner.

Available [here](http://dbis.cs.tu-dortmund.de/cms/de/publications/2020/x64jit/damon2020-submission.pdf).

### Big Idea

Create a custom intermediate representation optimized for use in a query compiler to reduce compilation time.

### Summary

The authors present _Flounder IR_, an intermediate representation for query compilation. Flounder IR is designed for use in database systems that utilize query compilation; accordingly, it prioritizes two things:
- Simple translation from query plan operators to Flounder IR
- Efficient (low-latency) translation from Flounder IR to native code

The intermediate representation introduces several novel features that help it realize these two goals. Experimental evaluation shows that compilation latency with Flounder IR is significantly lower than that achieved by LLVM with no optimizations (up to 265ms vs up to 10ms) while the code quality and execution time remain relatively similar.

### Commentary

The authors of this paper make the same observation that the Umbra team does (_Tidy Tuples and Flying Start_): LLVM is great, but its general purpose design is actually too heavyweight for our purposes in the query compilation space. We can take advantage of the narrowness of the domain to construct a "domain-specific compiler" that gets better performance than the general-purpose LLVM compiler infrastructure.

The authors note that adaptive execution is an alternative approach to dealing with high compilation latencies in query compilation systems. However, they dismiss this as a viable solution because of the engineering effort involved in implementing such a system.

On this point, it is interesting to note that the Umbra team takes much the same approach to low-latency compilation that the Flounder IR team does, yet they also integrate their custom intermediate representation and compiler backend in the context of an adaptive execution engine. Perhaps the Flounder IR team would do something similar if they had the engineering resources to devote to the problem (or time).

The "lightweight abstractions" that Flounder IR introduces to aid in code generation from the query plan include:
- Virtual registers (similar to LLVM IR)
- Function calls
- Constant loads with large (64-bit) immediates

The latter two are really just syntactic sugar that saves us (the authors of the code generator) from having to do some tedious programming on our own. It is the first abstraction, virtual registers, where Flounder IR distinguishes itself. Specifically, the authors observe that **query compilers use virtual registers in a much simpler way than one might observe in general purpose code**: they hold tuple attribute data within the tight loop of a pipeline. Flounder IR takes advantage of this observation by **adding instructions to the IR that make virtual register lifetimes explicit**, allowing them to skip live-range analysis for virtual registers entirely. This drastically simplifies the register allocation algorithm.

It is interesting to note that the authors make no mention of whether Flounder IR is a static single assignment intermediate representation. They do not provide many extended examples of the IR in the paper, but examination of the few samples they do give us suggests the answer is "no." This might make sense, however, when we account for the fact that the IR is not intended for optimization, and is rather merely a stepping-stone from the query plan to native code. 

### Questions

- Both Flounder IR and Umbra make a "big deal" of register allocation. Obviously it is a computationally complex problem (NP-complete), but do either of these groups have any empirical evidence for the costliness of register allocation in the overall context of query compilation?

### Further Reading

- Fast, Effective Dynamic Compilation (1996)
- Generating Custom Code for Efficient Query Execution on Heterogenous Processors (2018)
- Adaptive Execution of Compiled Queries (2018)
- Efficiently Generating Efficient Query Plans for Modern Hardware (2011)
