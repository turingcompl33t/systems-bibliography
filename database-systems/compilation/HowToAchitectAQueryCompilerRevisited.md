## How to Architect A Query Compiler Revisited (2018)

Ruby T. Tahboub, Gregory M. Essertel, and Tiark Rompf

Available [here](https://www.cs.purdue.edu/homes/rompf/papers/tahboub-sigmod18.pdf).

### Summary

The authors propose a novel approach to the architecture of a query compiler. They distinguish their new approach relative to two existing "classes" of query compiler architectures. The first of these is the single-pass, low-level approach, for which the HyPer system serves as the archetype (this is the architecture described in _Efficiently Compiling Efficient Query Plans for Modern Hardware_ [2011]). The other class of query compiler architecture is the multi-pass, high-level approach, for which the DBLAB system serves as the archetype (this is the architecture described in _How to Architect a Query Compiler_ [2016]).

In contrast to these two approaches, the authors present a novel approach to the architecture of a query compiler based on the concept of interpreter specialization. Under this approach, the authors claim to achieve the best of both of the two aforementioned approaches: a high-level implementation abstraction (the interpreter is implemented in Scala) that generates efficient compiled queries without the added complexity of multiple internal intermediate representations.

### Commentary

As the summary above suggests, there appear to be two primary dimensions of interest for query compiler architectures (at least as it is presented in this paper):

- Implementation Abstraction Level: high-level vs low-level
- Required Compilation Passes: single-pass vs multi-pass

These dimensions immediately suggest a taxonomy of query compiler architectures that we can visualize in a tabular format:

| X | **Low-Level** | **High-Level** |
| --- | --- | --- |
| **Single-Pass** | HyPer | LB2 |
| **Multi-Pass** | ??? | DBLAB |

I find myself agreeing with much of the what the authors have to say regarding the _principles_ of query compiler architecture and how it integrates with the larger picture of database systems research (e.g. at one point the authors note that a DBMS effectively _is_ a compiler and I love this analogy). However, I can't say that I am particularly fond of the details of their approach and implementation. This might be a result of the fact that it is so different from the existing approaches with which I am familiar, and it might be the case that I warm to it after reading more about Lightweight Modular Staging, which I plan to do next.

Fundamentally, I think my reservation comes from the impression that the specialized interpreter that is used to implement the query compiler in this architecture is not "modular" and extensible in the same way that the approach used by DBLAB is. For instance, how does one go about disabling certain optimizations in this approach? Or adding new optimizations? Again, because the architecture in DBLAB uses a familiar strategy for implementing the query compiler, I know exactly how to answer these questions, whereas here I am still somewhat lost.

### Questions

- What is the difficulty involved in debugging a query compiler built according to the approach described in this paper? For instance, we know that with a more "traditional" multi-level IR approach (as in DBLAB) debugging consists of verifying the correctness of the IR at each abstraction level. What is the analog here?

### Further Reading

- Precision Performance Surgery for PostgreSQL LLVM-based Expression Compilation (2015)
- An Architecture for Compiling UDF-Centric Workflows (2015)
- Partial Evaluation of Computation Process - An Approach to a Compiler-Compiler (1971)
- Building Efficient Query Engines in a High-Level Language (2014)
- [Efficiently Compiling Efficient Query Plans for Modern Hardware (2011)](EfficientlyCompilingEfficientQueryPlans.md)
- Functional Pearl: A SQL to C Compiler in 500 Lines of Code (2015)
- [Lightweight Modular Staging: A Pragmatic Approach to Runtime Code Generation and Compiled DSLs (2010)](../../programming-languages/codegen/LightweightModularStaging.md)
- [How to Architect a Query Compiler (2016)](HowToAchitectAQueryCompiler.md)
- Runtime Specialization of PostgreSQL Query Executor (2017)
