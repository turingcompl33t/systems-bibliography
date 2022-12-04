## Flare: Optimizing Apache Spark with Native Compilation for Scale-Up Architectures and Medium-Size Data (2018)

Gregory M. Essertel, Ruby Y. Tahboub, James M. Decker, Kevin K. Brown, Kunle Olukotun, and Tiark Rompf.

Available [here](https://www.cs.purdue.edu/homes/rompf/papers/essertel-osdi18.pdf).

### Summary

The authors present _Flare_, a framework for accelerating the performance of Apache Spark jobs by optimizing for "medium-size" workloads that do not require distributed computation. The distinguishig feature of _Flare_ is its application of code generation (implemented with generative programming via the Lightweight Modular Staging library for Scala) techniques from memory-optimized database systems (e.g. HyPer) to improve the performance of Spark jobs.

### Commentary

_Flare_ integrates with Spark via its supported APIs. If one implements a Spark job in Scala, for instance, they can simply wrap a Spark `DataFrame` in a function call to create and return a new `FlareDataFrame` that will use the _Flare_ runtime to execute the job.

An interesting analogy emerges in the compilation of Spark jobs. A single Spark job may result in a multi-query plan produced by the Spark optimizer. This challenges the existing code generation system for Spark (Tungsten). This is analogous to the idea of pipelines and pipeline-breaker operators in a SQL query plan in a relational database.

The full code generation pipeline for _Flare_ is still a bit vague, but I believe it proceeds something like:
- User submits Spark job (via some API)
- Spark optimizer (_Catalyst_) produces an optimized query plan
- _Flare_ takes the output from the optimizer and produces a staged computation graph (by expressing the query plan in Scala code via the LMS library)
- _Flare_ then relies on LMS to compile this code to C source code
- _Flare_ invokes (`fork()` + `exec()`?) a C compiler to compile the source to native code
- _Flare_ runs the resulting binary in its own process (?)

Note that _Flare_ is designed for non-distributed use of Spark. This should be relatively clear from the above description of the _Flare_ code generation process - no consideration is given to distributed computation.

One final aspect of interest is the handling of UDFs in _Flare_. _Flare_ is capable of optimizing arbitrary UDFs that are specified as part of Spark jobs. However, the big caveat here is that users of the framework that want to benefit from native compilation of UDFs need to express the UDF with the help of the LMS library in Scala. To me, this suggests that UDFs must be implemented in Scala in order for code generation to be possible.

### Questions

- The authors state that _Flare_ applies some lighweight optimizations to the query prior to generating code for it. How are these optimizations applied? On what intermediate representation are they applied? Are they working directly on Scala source code? This seems like a needless recapitulation of work that has already been done (many times) on other intermediate representations, but I know these guys from Purdue love Scala...
- In the commentary section above, I note that UDFs must(?) be expressed in Scala with the help of the Lighweight Modular Staging library in order for the _Flare_ framework to retain the ability to generate code for them. Is this actually the case? If so, is _Flare_ still able to generate code for the remainder of the query and leave the UDF untouched, treating it as a black box for which code is not generated? Now that I think about this, this seems unlikely, given that the final execution strategy is to compile the entire query to native code and execute it in its own process. How would this invoke an arbitrary Scala function on the JVM? Ugly...

### Further Reading

- [Spark SQL: Relational Data Processing in Spark (2015)](../optimization/SparkSQLRelationalProcessingSpark.md)
- An Architecture for Compiling UDF-Centric Workflows (2015)
- Hekaton: SQL Server's Memory-Optimized OLTP Engine (2013)
- Building Efficient Query Engines in a High-Level Language (2014)
- [Generating Code for Holistic Query Evaluation (2010)](GeneratingCodeHolisticEvaluation.md)
- Code Generation for Efficient Query Processing in Managed Runtimes (2014)
- [Weld: A Common Runtime for High Performance Data Analytics (2017)](WeldCommonRuntimeAnalytics.md)
- Voodoo: A Vector Algebra for Portable Database Performance on Modern Hardware (2016)
- Delite: A Compiler Infrastructure fr Performance-Oriented Embedded Domain-Specific Languages (2014)
- A Gentle Introduction to Multi-Stage Programming (2004)
