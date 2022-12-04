## Efficiently Compiling Efficient Query Plans for Modern Hardware (2011)

Thomas Neumann

Available [here](https://www.vldb.org/pvldb/vol4/p539-neumann.pdf).

### Summary

The author presents a novel approach to query execution via efficient compilation to native code. The primary architectural contributions of the paper include:

- Implementation of a _data-centric_ query execution engine. In contrast to the traditional _operator-centric_ execution engine strategy, boundaries between operators in the physical query plan are blurred during code generation. This helps improve data locality during query execution and limits the need for materialization of temporary results.
- Implementation of a _push-based_ query execution engine. In contrast to the traditional _pull-based_ execution engine strategy, tuples are pushed from the bottom of the plan tree upwards towards their parent operators. This model enables the author to achieve an implementation in which tuples are pushed from one pipeline-breaker operator to the next, effectively keeping tuples in registers as long as possible.
- Native code generation with the LLVM compiler infrastructure. Previous approaches to native code generation target generation of C code which is then passed through a standard C compiler like GCC to produce native code. This introduces a significant amount of overhead during compilation. In contrast, the author of this paper utilizes LLVM to generate LLVM IR directly and subsequently uses the LLVM JIT API to produce native code. This greatly reduces the overhead of native compilation.

### Commentary

One thing that I did not fully understand the first time I read this paper was the interaction between the LLVM and C++ components of the implementation. At first, I was under the (naive) impression that the entirety of the query plan was converted to LLVM IR and subsequently natively compiled. Naturally, this is a horrible approach to this problem for a number of reasons. First, generating the IR for the entirety of the query plan would be difficult and perhaps prohibitively expensive on its own. Furthermore, using the LLVM JIT to then compile all this IR to native code would also prove costly - not as costly as running C source through a production compiler, but still more expensive than necessary.

Instead of this naive approach, the author merely uses LLVM to "glue together" the complex operators that are written in C++ and precompiled. This makes the code generation much simpler than it would otherwise be if one were to attempt to dynamically generate the entire query plan.

### Questions

- If the operators themselves are written in C++ and precompiled, how is it that the majority (~99%) of the overall execution time for the query is spent in natively compiled LLVM code? I am confused because it seems that these two claims are contradictory.

### Further Reading

- [MonetDB/X100: Hyper-Pipelining Query Execution (2005)](../execution/MonetDBX100.md)
- [Generating Code for Holistic Query Evaluation (2010)](GeneratingCodeHolisticEvaluation.md)
- Compiled Query Execution Engine using JVM (2006)