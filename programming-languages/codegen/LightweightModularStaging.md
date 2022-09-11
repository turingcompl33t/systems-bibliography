## Lightweight Modular Staging: A Pragmatic Approach to Runtime Code Generation and Compiled DSLs (2010)

Tiark Rompf and Martin Odersky.

Available [here](https://www.researchgate.net/publication/45581394_Lightweight_Modular_Staging_A_Pragmatic_Approach_to_Runtime_Code_Generation_and_Compiled_DSLs). Interestingly enough, this paper appears somewhat difficult to get the full-text for, despite being a foundational work in this space.

### Big Idea

Use the type system in a "suitably-expressive" host language to distinguish between computational "stages" in a generative programming framework, implemented as a library.

### Summary

The authors present _Lightweight Modular Staging_ (LMS), a library-based approach to multi-stage programming and code generation. In LMS, the library utilizes the type system of the host programming language to distinguish between the _stages_ at which computations are performed. For instance, the type `Int` denotes an integer that is evaluated at the runtime of the program, while the type `Rep[Int]` represents a computation that generates code that will ultimately yield an `Int`. This approach to multi-staging makes for an extremely lightweight and productive approach to generative programming. 

Currently, the library is implemented only in Scala, but the authors claim there is nothing in the implementation that limits it to this language and that it might implemented in any suitably-expressive host language.

### Commentary

I've been thinking about LMS for some time now, and I finally got around to reading the paper. Perhaps I didn't pay sufficient attention while reading it, but I don't think it contributed significantly to improving my understanding of how the library works. Ultimately I think I still need to play around with the library and generate some code for a tiny embedded DSL to actually internalize what the library brings to the table. Naturally I am primarily interested in this library because it is the driving force behind the Legobase and LB2 code generation engines, which seem like really compelling approaches to runtime code generation for database systems.

The authors point out a really interesting tension in software engineering: building large, complex software systems requires constructing abstractions that hide implementation details through indirection. However, this often comes at the cost of performance because the additional indirection creates runtime overhead. The authors claim that code generation (and LMS in particular) is one mechanism for bridging this gap.

In addition to its many other benefits that I will elide here, LMS has the benefit of not requiring a distinct semantic analysis stage for generated code. Because LMS is implemented as a library, it is very shallowly-embedded in the host language, so the host language type system is capable of performing all necessary semantic analysis.

The authors present a "first principles" example of LMS and how it differs from potential, alternative approaches to generative programming as a library. Specifically, they describe how it might be possible to use a string representation of the generated code as the target of code generation. This works, but lacks any structural information that is necessary to perform optimizations. Instead, LMS uses a graph representation internally to represent the generated code.

In the related works section, the authors briefly describe multi-stage programming languages, which, as the name suggests, are programming languages specifically designed for writing multi-stage programs. I don't know enough about them to offer a coherent opinion either way, but I wonder if it might be effective to attempt to author a DBMS code generation engine in an MSP language.

### Questions

- LMS is obviously a very interesting system, and it has proven very effective in a variety of contexts. However, at bottom, it appears to be merely an efficient / productive method for generating something akin to an AST that might then be compiled further to bytecode or native code. Is the primary difference that it is shallowly-embedded in the host language, rather than being deeply embedded (i.e. essentially a standalone programming language)? If not, what is it that I am missing?

### Further Reading

- Runtime Code Generation in C++ as a Foundation for Domain-Specific Optimisation (2004)
- Language Virtualization for Heterogeneous Parallel Computing (2010)
- Domain Specific Embedded Compilers (1999)
