## Relaxed Operator Fusion for In-Memory Databases: Making Compilation, Vectorization, and Prefetching Work Together At Last (2017)

Prashanth Menon, Todd C. Mowry, and Andrew Pavlo.

Available [here](https://par.nsf.gov/servlets/purl/10066914).

### Big Idea

Relax the tuple-at-a-time processing model in compilation-based query engines in order to get additional performance benefits from vectorized computations and memory prefetching.

### Summary

The authors present the _relaxed operator fusion_ (ROF) technique for compilation-based query execution engines. In ROF, we no longer generate a single loop for each pipeline in the code generated for a query plan, and instead insert "stages" at intermediate points in the pipeline where batches of tuples are temporarily materialized. This batching mechanism allows certain operations to take advantage of additional optimizations that achieve better CPU performance, namely SIMD vectorization and explicit prefetching. 

### Commentary

The most interesting aspect of this paper, from an engineering perspective, is the interplay between the query optimizer and the execution engine. In this system (Peloton) it appears that the query optimizer and the execution engine are tightly integrated. 

For instance, the authors state that it is the query optimizer that constructs pipeline boundaries. In contrast, the spiritual successor to this system (NoisePage) does not do any explicit pipeline construction in the optimizer. Instead, pipelines are constructed implicitly during code generation by the operator translators themselves. This is a double-edged sword, it appears. First, it is nice to decouple the optimizer from the execution engine because it makes it possible for the optimizer to be used with a different execution engine (if this ever proved necessary). On the flip side, constructing pipelines in the optimizer makes the process more explicit and gives us (potentially) more control. In NoisePage, the process is "decentralized" in a way, which might make it more difficult to apply some of the more advanced pipeline optimizations that are proposed in this paper.

More important than the construction of pipelines, however, is the optimizer's role in implementing relaxed operator fusion. It is the query optimizer that determines which pipelines should have stages inserted. Cases in which the optimizer might choose to do so include:
- Whenever a scan operator is encountered that has a SIMD-compatible predicate
- Whenever an operator requires random access to a temporary data structure whose size exceeds the capacity of the last-level cache

Obviously, the latter of these two instances is far more complicated than the former. This relies on a number of complex metrics, including cardinality estimation as well as the internal implementation details of the data structure itself (e.g. what is the overhead imposed by the data structure, in addition to the tuple data itself?).

The heart of relaxed operator fusion is the observation that, if we can feed certain operators vectors of many tuples instead of individual tuples (as is typically done in data-centric code generation engines) then we can get additional CPU efficiency gains from vectorization and prefetching. Breaking up the single tight loop of a pipeline into an outer loop for the pipeline composed of inner loops for each stage allows this batching of tuples to take place.

### Questions

- In the introductory section of this paper, the authors anticipate that most future OLAP applications will utilize in-memory database systems because of the declining cost of DRAM. This prediction was made in 2017. Have we reached a point where we can say with confidence that this prediction did not prove accurate?
- Relaxed operator fusion introduces nested loops into control flow that would otherwise have been a tight loop. This introduces additional branches into the generated code for the loop predicate(s). What is the overhead of these additional branches? How much do we pay for introducing this control flow into a loop that used to be tight?

### Further Reading

- Improving Hash Join Performance through Prefetching (2004)
- Asynchronous Memory Access Chaining (2015)
- Compiler-based Prefetching for Recursive Data Structures (1996)
- Design and Evaluation of a Compiler Algorithm for Prefetching (1992)
