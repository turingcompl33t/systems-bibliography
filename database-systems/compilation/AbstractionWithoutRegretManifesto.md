## Abstraction Without Regret in Database Systems Building: A Manifesto (2014)

Christoph Koch.

Available [here](http://sites.computer.org/debull/A14mar/p70.pdf).

### Big Idea

Leverage advances in compiler technology and generative programming to enable development of database systems in high-level (productive) programming languages without sacrificing performance.

### Summary

The author presents his thoughts on the future of development in high-performance database systems. As the title suggests, the author advocates for the use of high-level programming languages as a means of increasing productivity and safety (memory, concurrency, etc.) in database systems development. Further, he claims that by taking advantage of advances in compiler technology and using techniques like _generative programming_, we can develop database systems in these high-level languages without sacrificing the performance of low-level languages (e.g. C). In some cases, the systems developed in high-level languages may even outperform state-of-the-art systems developed in C.

### Commentary

The abstract of this manifesto begins with a great observation: we always hear the quote about how "all problems in computer science can be solved with another level of indirection" but we rarely hear the final part of the quotation "except for those problems caused by too many levels of indirection". Performance is one such problem - poor performance is (often) caused by an excessive use of abstraction and indirection. Indeed, performance problems may be solved by _removing_ levels of indirection, rather than adding them.

The author observes some patterns in database systems programming that I have observed myself. Foremost among these is the leaking of abstractions among different, logically distinct components of the database. The author uses the example of the page abstraction. Database pages are intended for a single purpose: storing data. Accordingly, they should be the sole concern of the storage manager. However, practicality dictates that other components invade this abstraction - the recovery subsystem being one such example. Ultimately, my feeling is that it is this leaking of abstractions that makes any large software project (not just database systems) difficult to work in and maintain.

The author follows up this observation by stating that high-level programming languages provide a greater number of facilities to help us prevent abstractions from leaking. I don't disagree with this, but I also think that there is not much that can be done on the language level to truly stop us (programmers) from leaking abstractions. Ultimately this is an issue that must be addressed through better software engineering, not a "better" programming language.

The author recognizes compilers as a "tool for removing levels of indirection, automatically". This is a great observation. Even though I have been working on database compilers for some time now and I know this is why code generation and compilation give better performance, it is nice to boil it down and make it explicit like this.

A key observation in this paper is that we can dramatically improve performance by "teaching the compiler about collections". Most of the code that we write is (at bottom) an algorithm over some collection. If we limit the collections that we use in our implementation, and then teach our compiler about these collections via a DSL, we can get powerful optimizations that cut through the high abstraction level provided by the language to generate efficient low-level code.

To put a bow on this point: _The central abstract data type shall be the focal point of all domain-specific optimizations_.

### Questions

- The author claims that high-level algorithmic choices (e.g. `JOIN` operator) matter more than low-level implementation details. This is a nice generalization, and is largely what we are taught in our undergraduate algorithms course, but is this always true? At what point do the performance characteristics for insertion sort in C and quicksort in Python cross over? I suppose in the limit...
- To now, I have been thinking of the approaches to compiled queries advocated in _Efficiently Compiling Efficient Query Plans for Modern Hardware_ (and its successors) and in _Building Efficient Query Engines in a High-Level Language_ (and its successors) as fundamentally different approaches to the same problem. Is this actually the case? What is truly different between these two approaches? What techniques do they share?

### Further Reading

- Jet: An Embedded DSL for High-Performance Big Data Processing (2012)
- DBToaster: A SQL Compiler for High-Performance Delta Processing in Main-Memory Databases (2009)
- Compiling Transaction Programs (2013)
- Legobase: Building Efficient Query Engines in a High-Level Language (2014)
- Lightweight Modular Staging: A Pragmatic Approach to Runtime Code Generation and Compiled DSLs (2012)
- Optimizing Data Structures in High-Level Programs: New Directions for Extensible Compilers based on Staging (2013)
- The End of an Architectural Era (It's Time for a Complete Rewrite) (2007)
- A Gentle Introduction to Multi-Stage Programming (2003)
