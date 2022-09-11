## Adaptive Execution of Compiled Queries (2018)

Andre Kohn, Viktor Leis, and Thomas Neumann.

Available [here](https://15721.courses.cs.cmu.edu/spring2020/papers/14-compilation/kohn-icde2018.pdf).

### Big Idea

Adaptively execute queries using one of three execution mechanisms (interpretation, unoptimized native compilation, optimized native compilation) to get the best of low-latency and high-throughput evaluation.

### Summary

The authors present a technique for the adaptive execution of compiled queries in which the execution method for a query fragment is determined at runtime based on the time taken for the fragment to execute. 

Adaptive execution always begins by directly interpreting the imperative intermediate representation (an optimized translation of LLVM IR) on an interpreter. After a certain threshold time has been reached (1ms), an algorithm is evaluated each time a query fragment finishes to determine the execution method that should be used for future fragments. If the algorithm determines that the fragment should be executed natively (the cost of compilation will be "worth it"), the fragment is compiled in the background as the query continues to execute via interpretation. Finally, the compiled version of the fragment is swapped out for the interpreted version once compilation finishes.

Adaptive execution achieves the benefits of both low-latency query evaluation for short-lived queries and the high-throughput evaluation for long-running queries. This dramatically improves the user experience in certain settings.

### Commentary

This paper is an absolute powerhouse of great ideas. This probably could be split into a couple of distinct papers.

The key components of the design of the adaptive execution system are:
- A fast bytecode interpreter, specialized for database queries
- A method of accurately tracking query progress during execution
- A way of dynamically switching between the execution modes for the query (i.e. interpreted to compiled)

The authors observed that, in their system, the primary bottleneck in compilation is the native compilation phase, which is to say that parsing, semantic analysis, query optimization, etc. are negligible in terms of the overall time required to compile a query. This brings up an important point that we should always keep in mind: measure (profile) first before trying to optimize!

The authors observe that not all code paths in an imperative program for a query plan are equally important - some may be only executed once, and may process only a small number of tuples. For this reason, they recognize the necessity of making adaptive execution fine-grained. Instead of adaptively compiling an entire query, they adaptively compile at the granularity of individual pipelines. This also synchronizes nicely with the concept of morsel-driven parallelism and how data is distributed among parallel workers in the system.

Perhaps the most interesting aspect of the system is how they manage to seamlessly switch between interpreted and natively compiled execution modes. From my understanding, this actually is a really beautiful work of software engineering that follows directly from the _worker_ abstraction that they use in HyPer:
- They maintain a table of function pointers to each of the pipeline functions in the query plan
- When a query is natively compiled, they simply swap the function pointer in this table from the entry point that goes to the interpreter with the new, natively compiled version of the pipeline
- Workers consult the table each time they complete processing of a morsel - the unit of data processing in the system

The fundamental idea at work here is that a worker consumes both a function and the data on which it operates (a morsel) each time it comes back for additional work to execute. This concept of providing the data to the worker to process, as well as the function to execute, seems to make the mechanism for switching from interpreted to compiled pipelines relatively painless. Truly, this is a beautiful achievement!

On an unrelated note, the authors must manually implement register allocation for their virtual machine because they directly execute an optimized version of LLVM IR (which has an infinite set of registers). To do this, they develop a new, linear time register allocation algorithm... Which on its own would likely be a paper-worthy result in the compilers community. This is insane.

### Questions

- In NoisePage, what is the breakdown between the different phases of the compilation process? How does code generation compare to the time taken for native compilation with LLVM?
- Suppose we wanted to implement adaptive execution in NoisePage. Our interpreter operates on our custom bytecode representation, rather than LLVM IR. How much more difficult would this make the process of switching between interpreted and compiled implementations for pipeline functions?

### Further Reading

- Hekaton: SQL Server's Memory-Optimized OLTP Engine (2013)
- Compilation in the Microsoft SQL Server Hekaton Engine (2014)
- Code Generation: The Inner Sanctum of Database Performance (2016)
- Apache Spark as a Compiler: Joining a Billion Rows per Second on a Laptop (2016)
- Runtime Code Generation in Cloudera Impala (2014)
- DBToaster: Higher-Order Delta Processing for Dynamic, Frequently Fresh Views (2014)
- Just-in-Time Data Virtualization: Lightweight Data Management with ViDa (2015)
- Weld: A Common Runtime for High Performance Data Analytics (2017)
- How Good Are Query Optimizers, Really? (2015)
- Morsel-Driven Parallelism: A NUMA-Aware Query Evaluation Framework for the Many-Core Age (2014)
- Micro-Specialization: Dynamic Code Specialization of Database Management Systems (2012)
