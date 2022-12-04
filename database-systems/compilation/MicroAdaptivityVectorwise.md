## Micro Adaptivity in Vectorwise (2013)

Bogdan Raducanu, Peter Boncz, and Marcin Zukowski.

Available [here](https://15721.courses.cs.cmu.edu/spring2020/papers/14-compilation/p1231-raducanu.pdf).

**Big Idea:** It is difficult or impossible to determine the most effective primitive implementation a priori, so generate many variations of each primitive and dynamically learn the implementation that is the most efficient for the current workload at runtime.

### Summary

The authors present the concept of micro adaptivity and its applications to the database system Vectorwise. In this micro adaptivity framework, different variations of the low-level operations that are used to implement operators in Vectorwise (_primitives_) are generated and maintained by the system. At query runtime, different primitive instances are applied to query processing, performance statistics for the primitive instance are recorded, and a learning algorithm selects the primitive instance that achieves the best performance for the given configuration (e.g. hardware platform, data distribution, etc.)

### Commentary

This paper connects once again to the big idea from Onur Mutlu: performance through heterogeneity. This time we augment this heterogeneity with some profile-guided decision making. It is amazing how often this idea comes up, perhaps just one of the fundamental principles of computer science.

A cool benefit of a vectorized execution engine that I did not foresee is the fact that it makes profiling easier. The authors point out that a significant amount of time (CPU cycles) is spent in the primitive function implementations, making it easy to see which of these primitives are important for the performance of different queries.

At the end of the paper's conclusion, the authors (essentially) say that the complexity of modern computer systems renders us (humans) incapable of reasoning about the performance implications of our decisions. The stack has grown so deep and complex that is now impossible for us to foresee all of the effects of even the smallest changes we make in our code. Micro adaptivity is something of a response to this: if we can't reason about it, at least we can come up with a bunch of different alternatives and learn the best one from experience. I'm not sure I like this sentiment (performance engineering is getting too hard so we must just throw up our hands and rely on experiments and samples) but at the same time it certainly feels like this is the way things are heading. Interesting potential sub-field in computer science: "engineering predictable performance."

One of the ways that the authors vary the primitive implementation is by compiling them with different compilers. They observe that the performance across compilers in aggregate is similar, but that the compilers do perform at different levels across specific primitive implementations. This is a somewhat interesting observation, but actually the more that I think about it pretty much expected. The authors of each compiler must necessarily focus on different aspects of optimization, so we get different code generation.

Finally, in the section on future work, the authors mention the potential of application of micro adaptivity to JIT compilation. I am slightly confused as to what the application might be here... Do we JIT under different conditions and compare the performance of the various JITed implementations? Or are they talking about the choice of "to JIT or not to JIT"?

### Questions

- What is the overhead imposed by micro adaptivity? For instance, there must be some cost during the "exploration" phase of the learning algorithm, before enough is learned to being "exploiting" the most efficient implementation. What is this cost? Is there a way to tune this parameter? Can we set a cutoff for queries on which we might want to apply adaptivity and those that we do not?

### Further Reading

- [MonetDB/X100: Hyper-Pipelining Query Execution (2005)](../execution/MonetDBX100.md)
- Improving Hash Join Performance Through Prefetching (2007)
- Vectorization vs. Compilation in Query Execution (2011)
