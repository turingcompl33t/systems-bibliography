## Voodoo - A Vector Algebra for Portable Database Performance on Modern Hardware (2016)

Holger Pirk, Oscar Moll, Matei Zaharia, and Sam Madden.

Available [here](https://cs.stanford.edu/~matei/papers/2016/vldb_voodoo.pdf).

### Summary

The authors present _Voodoo_, a vector-oriented intermediate representation ("algebra" in the parlance of the paper) intended to enable efficient database query processing on many hardware platforms. _Voodoo_ provides an abstraction layer between the query plan produced by the database system optimizer and the target hardware on which the system runs. Through this layer of abstraction, _Voodoo_ provides portability of the code generation system within the DBMS, while also enabling support for optimizations on _Voodoo_ itself that might otherwise go uncaptured.

### Commentary

_Voodoo_ appears to market itself as a target intermediate representation for database systems that generate code for query execution. As an example, instead of generating a TPL AST, NoisePage might generate _Voodoo_ (the AST directly? textual form?) and then use a _Voodoo_ backend to generate efficient native code for the target hardware.

The critical property that makes _Voodoo_ interesting is the ability to generate low-level, high-performance code from a high-level abstraction that isn't (at least, theoretically) a pain to work with and hand-optimize. This seems similar in spirit to the work done by the team out the programming languages department at Purdue regarding Lightweight Modular Staging and the LegoBase system. It appears that this ability will become the new standard. Umbra, the successor system to HyPer, also pursues something similar, creating their own intermediate representation rather than relying on LLVM IR directly (although the motivations for this may be orthogonal).

The authors note in the introductory section that many systems are betting on in-memory analytics as the next big thing in database systems. This paper was written back in 2016. Since then, Andy has begun to express sentiments that in-memory systems may not hold the same promise that he once thought they did. I wonder if this impacts the relevance of the work done on _Voodoo_?

One really cool aspect of _Voodoo_ that appears basically as a side-effect of its high-level, declarative nature is the fact that similar application techniques translate to structurally similar code as it is expressed in _Voodoo_. In a low-level language like C++, one might get lost in the details between specific parallelism implementations (e.g. threads vs GPU). In contrast, _Voodoo_ largely abstracts over these details, making the code easier to reason about.

Finally, one concept that seems to pop up again and again in these papers is the distinction between imperative and declarative code. It appears that, to facilitate automated optimization (e.g. from a compiler / optimizer) we should favor declarative code over imperative code. This in and of itself is a reason to learn a higher-level, functional language like Haskell - it teaches one to express programs in a declarative way, allowing us to get out of the optimizer's way.

### Questions

- The authors claim that high-performance depends on both the underlying hardware as well as the specifics of the data being processed - there is no one dominant processing strategy for a hardware platform across all data processing tasks. What is an example of this being the case?

### Further Reading

- Building Efficient Query Engines in a High-Level Language (2014)
- Generating Code for Holistic Query Evaluation (2010)
- Efficiently Compiling Efficient Query Plans for Modern Hardware (2011)
