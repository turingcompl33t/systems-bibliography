## Everything You Always Wanted to Know About Compiled and Vectorized Queries But Were Afraid to Ask (2018)

Timo Kersten, Viktor Leis, Alfons Kemper, Thomas Neumann, Andrew Pavlo, and Peter Boncz.

Available [here](http://www.vldb.org/pvldb/vol11/p2209-kersten.pdf).

### Big Idea

Code generation and vectorization represent two fundamentally different approaches to query execution that both yield competitive performance on analytical workloads. The two approaches do exhibit some performance differences that manifest under certain conditions and also imply some non-performance-related tradeoffs that are worth considering when designing an new engine.

### Summary

The authors present a first-of-its-kind apples-to-apples comparison between two different execution engine architectures: compilation and vectorization. Implementation of compilation is modeled on HyPer's data-centric code generation approach, while vectorization is modeled on the VectorWise implementation. Despite the differences between these two approaches, the authors' find in their experimental evaluation that both designs offer similar, competitive performance on analytical workloads. However, as one might expect, the two approaches do present different strengths and weaknesses when it comes to performance, and also imply some additional considerations such as code maintenance, profiling, and debugging.

### Commentary

The final tally of strengths and weaknesses of each approach includes the following salient points:
- Code generation excels on computationally-intensive workloads (those that are not memory bound?) because it executes fewer instructions
- Vectorization results in greater cache locality (but the difference is not huge)
- SIMD data parallelization is possible in both approaches
- Morsel-driven parallel execution is possible in both approaches

Some non-performance considerations:
- A code generation engine appears more difficult to implement and maintain because it is by definition a meta-program (code that generates code, rather than executing directly)
- Likewise, a code generation engine is more difficult to profile because it typically implies operator fusion, which makes it hard to pinpoint the operators in the plan that are consuming the most time (operator fusion is not necessarily a requirement of code generation, but without it we lose the benefits of register-residence in the push-based execution model)
- Vectorization does seem a bit less flexible than code generation, however, because it implies a (at least to my eye) convoluted implementation strategy for certain operators as a consequence of operating on vectors of tuples

### Questions

- The authors use Peloton with Relaxed Operator Fusion as an example of an engine that starts to bridge the gap between compilation and vectorization. Has there been any more movement in this direction since Prashanth's paper (2017)? 
- Is this an idea that is worth pursuing, or is the added complexity of trying to combine both paradigms not worth the potential performance benefit?

### Further Reading

- [Apache Spark as a Compiler: Joining a Billion Rows per Second on a Laptop (2016)](../compilation/SparkAsACompiler.md)
- An Architecture for Compiling UDF-Centric Workflows (2015)
- Compilation in the Microsoft SQL Server Hekaton Engine (2014)
- Exploring Query Compilation Strategies for JIT (2018)
- [Relaxed Operator Fusion for In-Memory Databases: Making Compilation, Vectorization, and Prefetching Work Together at Last (2017)](../compilation/RelaxedOperatorFusion.md)
- Weld: Rethinking the Interface Between Data-Intensive Applications (2017)
- A Common Runtime for High Performance Data Analysis (2017)
- [How to Architect a Query Compiler (2016)](../compilation/HowToAchitectAQueryCompiler.md)
- Vectorization vs Compilation in Query Execution (2011)
- How to Architect a Query Compiler, Revisited (2018)
