## Tupleware: Redefining Modern Analytics (2014)

Andrew Crotty, Alex Galakatos, Kayhan Dursun, Tim Kraska, Ugur Cetintemel, and Stan Zdonik

Available [here](https://arxiv.org/abs/1406.6667).

### Summary

This paper describes the Tupleware analytics framework. Tupleware fills a gap similar to that served by Hadoop and Spark (i.e. distributed analytics) but is intended for the "common use case". Where Hadoop and Spark are (nominally) intended for use on large clusters with hundreds or thousands of unreliable nodes on (up to) petabytes of data, Tupleware is intended to operate on smaller clusters (~30 nodes) with relatively reliable hardware, on terabytes of data.

The differentiating factors of Tupleware are:
- A new programming model based on a new algebra inspired by functional programming patterns
- The ability to express the workflow in terms of user-defined functions implemented in a variety of source languages (anything that has a backend that targets LLVM)
- Optimizations that may be applied at different levels of the stack, allowing for "hybrid" optimizations that incorporate additional knowledge of the low-level semantics of the job, thereby improving performance

### Commentary

I am primarily interested in Tupleware because of their claims to support compilation and code generation. The analytics platform does do this, but it actually turned out to be somewhat less interesting than I envisioned.

User of Tupleware express their workflow in terms of user defined functions written in a source language of choice - e.g. Python, C/C++, Julia, etc. The user utilizes the Tupleware API to interact with the platform and defines their job using a set of pre-defined operations provided by the Tupleware library (this is something of a hidden depdenency, users can only write their workflows in languages for which Tupleware provides API bindings, they don't explicitly call this out in the paper). The authors claim the programming model is more flexible than MapReduce and SQL, but the constraint that workflows must be defined in terms of Tupleware's optimizations still makes it feel somewhat limited.

The real secret-sauce of Tupleware (if any) comes from their ability to introspect on the user defined functions and use the information obtained during this process to perform more effective optimizations at a relatively low-level of the overall plan. Tupleware applies three types of optimizations:
- DBMS-only: typical DBMS query optimizer style optimizations (e.g. predicate pushdown)
- Compiler-only: applied to low-level generated code (LLVM IR?); examples include SIMD vectorization and function inlining (it definitely sounds like these could just be vanilla LLVM passes)
- DBMS + Compiler ("adaptive"): applies pipelinining and / or operator-at-a-time optimizations on a case-by-case basis

The third optimization type is the novelty here. Tupleware is able to apply these optimizations on a case-by-case basis because they introspect on the user-defined functions that they are attempting to optimize. This allows them to select the appropriate optimization strategy based on the specifics of the job.

### Questions

- Although Hadoop and Spark might have been designed with the intent to be run at scales that most people don't see, it appears that both of these frameworks can be applied relatively successfully to the scales at which Tupleware is aimed. Is this the case? If so, is Tupleware really necessary..?

### Further Reading

- Building Efficient Query Engines in a High-Level Language (2014)
- [Generating Code for Holistic Query Evaluation (2010)](../compilation/GeneratingCodeHolisticEvaluation.md)
- [Efficiently Compiling Efficient Query Plans for Modern Hardware (2011)](../compilation/EfficientlyCompilingEfficientQueryPlans.md)
- Compiled Query Execution Engine Using JVM (2006)
- OptiML: An Implicitly Parallel Domain-Specific Language for Machine Learning (2011)
- Code Generation for In-Memory Data Analytics (2019)