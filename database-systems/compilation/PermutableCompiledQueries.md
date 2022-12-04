## Permutable Compiled Queries: Dynamically Adapting Compiled Queries without Recompiling (2020)

Prashanth Menon, Amadou Ngom, Lin Ma, Todd C. Mowry, and Andrew Pavlo.

Available [here](https://www.pdl.cmu.edu/PDL-FTP/Database/p101-menon.pdf).

### Big Idea

Generate code with an additional layer of indirection to allow dynamic adaptation of compiled queries without introducing additional compilation overhead.

### Summary

The authors propose a technique called _permutable compiled queries_ (PCQ). PCQ enables the implementation of various adaptive query processing (AQP) techniques in a database system that employs query compilation in its execution engine. In "traditional" AQP, the query plan that is currently being executed is swapped out with a more efficient plan in response to runtime metrics collection (in the event that the runtime metrics do not match those estimated by the optimizer prior to beginning execution). This introduces issues in systems that employ query compilation, however, because of the additional cost imposed by the compilation process (hundreds of milliseconds for embedded compilers e.g. LLVM, seconds for external compilers e.g. GCC). 

PCQ bridges the gap between these two techniques by adding an additional layer of indirection at the code generation stage for the query plan. The program generated with PCQ has built-in support for metrics collection and dynamic updating of program control flow through the use of higher-order functions and function pointers. This allows a system that employs query compilation to take advantage of adaptive query processing techniques.

### Commentary

The premise on which this paper is built is that the time required to compile (or recompile) a query prohibits the employment of "traditional" adaptive query processing techniques. Is this still the case with the advent of systems like Umbra that report incredibly low-latency query compilation (on the order of interpreted engines) while still achieving high throughput with fully-optimized native queries, in the steady-state?

The specific instances in which PCQ is employed in this paper include:
- Filter Predicate Ordering: The optimal order of filter predicates must strike the correct balance between two competing factors: the complexity of the predicate (how expensive it is to evaluate, per tuple) and its selectivity (evaluating more selective predicates first means that we do less overall work). The optimal order of filter predicates may change as the data distribution in the underlying table changes.
- Aggregation Hashtable Optimization: "hot" keys in an aggregation hashtable can be handled by a separate, optimized code path that elides probing the hashtable.
- Adaptive Joins: In the case of hash joins (which is what this paper assumes) the implementation of the join-hashtable can be adaptively selected for the current data distribution (concise hashtable for working sets that fit in L3, chaining hashtable otherwise). More importantly, the order in which table are joined in a multi-way join can be dynamically selected through PCQ.  

One interesting design point that I was confused about upon first reading this paper: in PCQ, the TPL program itself is augmented to support dynamic adaptivity. My first though was that this adds additional complexity to the query program that is not strictly necessary, and that it might be possible to instead "pull" the adaptive aspects of the compiled plan out of the TPL program itself into logic that is external to the compiled program. I think this might work for natively-compiled queries because we could simply "monkey-patch" the code with updated function pointers in order to install dynamic updates in response to changing conditions. However, this might actually add complexity instead of removing it because it would (a) make execution on the VM more difficult, how do we monkey-patch the VM with a swapped function pointer, would it be analogous to the native example? and (b) would likely require additional synchronization between the "external" thread that will perform the update and the "internal" thread that is actually executing the code of the query.

In the end, the more I think about it, the more convinced I am that containing all of the logic for adaptivity (metrics collection + dynamic control flow updates) is the more elegant approach to this problem. The compiled query remains completely self-contained, which makes it significantly easier to reason about, and is just good software engineering: the less the program relies on internal implementation details of the runtime, the better.

One downside of PCQ is that it is eager - it appears that it will always generate code with an additional indirection layer **and** perform runtime metrics collection even in the event that the underlying distribution of the data is static - adaptivity is pure overhead, and actually leads to worse performance than a totally static plan. How might we address this issue, and introduce an aspect of laziness to PCQ so that we only pay for its overhead when we actually need it?

### Questions

- In the _Commentary_ section above, I claim that it is "good software engineering" to decouple the program from the runtime, in this case, to decouple the TPL program that implements the query from the database system that runs it to get a result. I stand by this claim, in general, but I also think that **this might not be applicable when performance is the primary goal**. For instance, I think of systems like Umbra that rewrite the entire query compilation stack (i.e. generating their own IR that is more efficient than LLVM IR, writing their own backend that lowers from Umbra IR to native x86) in order to squeeze better performance from their system. Perhaps this tightly-integrated co-design is what is required in high-performance engineering. When do we need to sacrifice software engineering principles to achieve better performance? How do we know when this line should be crossed, and when we need to respect it?

### Further Reading

- Grizzly: Efficient Stream Processing through Adaptive Query Compilation (2020)
- [Adaptive Execution of Compiled Queries (2018)](AdaptiveExecutionCompiledQueries.md)
- How Good are Query Optimizers, Really? (2015)
- [Relaxed Operator Fusion for In-Memory Databases: Making Compilation, Vectorization, and Prefetching Work Together at Last (2017)](RelaxedOperatorFusion.md)
- Dynamic Speculative Optimizations for SQL Compilation in Apache Spark (2020)
