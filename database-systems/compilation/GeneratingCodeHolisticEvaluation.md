## Generating Code for Holistic Query Evaluation (2010)

Konstantinos Krikellas, Stratis D. Viglas, and Marcelo Cintra.

Available [here](https://15721.courses.cs.cmu.edu/spring2017/papers/20-compilation/krikellas-icde2010.pdf).

### Summary

The authors present HIQUE - a new database system that uses _holistic query evaluation_ to improve the performance of analytical queries. HIQUE applies a new approach to code generation via code templates for each query plan operator that are instantiated and compiled to native code for each query. Generating native code for each query removes many of the overheads imposed by the traditional _iterator_ model of query evaluation by reducing the number of functions calls, reducing the number of instructions executed, and improving the cache locality of the execution engine, among others.

### Commentary

This is typically presented as the "first" example of code generation execution engines in the "modern era" - i.e. after System R. For some reason, until now, I was always under the impression that HIQUE represented a naive approach to code generation (what I actually thought that it did is unclear...) but I don't see any techniques in this paper that immediately cry out for revision, even with the benefit of hindsight.

On the flip side, however, it is amazing to note that this paper was published in 2010 - just one year before Thomas Neumann published _Efficiently Compiling Efficient Query Plans for Modern Hardware_. Needless to say, the approach presented in that paper is quite a bit more advanced than the one presented here.

One major difference between these two approaches is the amount of code generated for each query. In HIQUE, C source code is generated for every operator, and this is all eventually natively compiled. In contrast, HyPer does not natively compile the majority of the operator implementations in its query plan. Instead, it JIT-compiles the "glue" portions of the plan that connect the C++ implementations of operators. At runtime, my understanding is that HyPer is not JITing _most_ of the code that it executes for each query, and rather relies on the fact that all of these operator implementations are AOT-compiled in the HyPer DBMS binary itself.

The overhead of the naive approach to compilation used in HIQUE (generate C source, fork() + exec() GCC to compile to shared object) is often held up as one of its primary limitations. However, this argument seems less compelling to me after working in this space for a bit longer. Code generation and native compilation appears to be a much better fit for analytical workloads rather than transactional ones (do the reductions in latency really matter when  they are already so small?). The authors cite the typical overhead for optimized compilation at ~500ms. For an analytical workload, how detrimental is this additional latency? It seems that the potential savings are massive, for relatively low downside.

One potentially-useful idea I had while reading this paper: the authors talk about holistic query evaluation as taking both the query (operations) and the underlying hardware into account when generating the code that implements the query. However, does this overlook the data? How can we take the data into account when generating code? Perhaps this is what the work by Prashanth is really all about. His techniques enable us to improve the efficiency of operators in a compiled query engine in response to "new information" about the underlying data. What are other approaches to this problem? Are there other aspects of query evaluation (i.e. not operators, data, or hardware) that need to be taken into account when generating code?

### Questions

- Is there a place for code generation and native compilation in transactional workloads? Did this time already pass? Or is it yet to come?
- Is a hand-coded C program that implements a particular query plan the best that we can ever hope to do? The "generative programming" approaches to query compilation also use this example as the standard against which they measure their approach.

### Further Reading

- Monet: A Next-Generation DBMS Kernel for Query-Intensive Applications (2002)
- Query Evaluation Techniques for Large Databases (1993)
