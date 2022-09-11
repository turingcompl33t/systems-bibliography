## Adaptive Code Generation for Data-Intensive Analytics (2021)

Wanda Zhang, Junyoung Kim, Kenneth A. Ross, Eric Sedlar, and Lukas Stadler

Available [here](http://www.vldb.org/pvldb/vol14/p929-zhang.pdf).

### Summary

This paper presents a novel technique for applying DBMS-style adaptive optimizations to a wider variety of analyics applications. The major contribution of the paper is an extension of the adaptive optimization approach from Vectorwise to a more flexible programming paradigm that allows it to be applied to applications that exist outside of a DBMS context. A performance evalution of the framework shows that the approach yield improved performance in both DBMS contexts (benchmarked with TPC-H) as well as ad-hoc analytics applications (a data-intensive application written in JavaScript).

### Commentary

This paper implements an adaptive optimization framework on top of the GraalVM with the help of Truffle. Graal is an ecosystem for dynamic compilation while Truffle is a "self-optimizing runtime system" that sits on top of Graal and enables automatic re-writing of the AST for optimization purposes based on the runtime feedback from Graal. This is insanely cool technology.

The authors apply this runtime system to analytics applications. The observation on which they base their approach, which originally comes from the Vectorwise paper, is that the nature of the data being processed by an analytical application may change over time, and some characteristics of the data that might change may in turn affect the optimizations that should be applied to achieve optimal performance. This necessitates updating the optimizations applied to the underlying code at runtime in response to changing data. The approach adopted by Vectorwise and recapitulated by the authors of this paper is to generate multiple versions of an analytics plan and apply each to a subset of the data. Then, based on the performance results observed on this subset (e.g. runtime) the best plan is chosen and used to execute the remainder of the data processing. Furthermore, the system also responds to changes in the data, monitoring (for instance) large increases in runtime with the current plan.

Examples of optimizations include the order in which predicates are applied and / or branchless plans and SIMD vectorization (on or off).

The technology here is super cool and obviously very advanced, but it still feels like a bit of a hack to me. For instance, the system is not accessible to a "consumer" in any useful way. The authors of the paper express their analytics (including the TPC-H queries) in plain Javascript code that is then "stringified" and subsequently fed into Truffle to be parsed to an AST. This is crazy.

### Questions

- In the paper the authors only consider relatively-small analytical workloads (e.g. the programs consist of a single tight loop that implements the entirety of the workload). Does this approach scale to more complex analytics? Does the number of plans just blow up, making it infeasible?

### Further Reading

The _related works_ section of this paper is a treasure trove of great resources. I had to work hard to narrow it down to even the relatively-large list below.

- FAD.js: Fast JSON Data Access Using JIT-Based Speculative Optimizations (2017)
- An Architecture for Compiling UDF-Centric Workflows (2015)
- Compiling PL/SQL Away (2019)
- PL/SQL Without the PL (2020)
- Everything You Always Wanted to Know About Compiled and Vectorized Queries but Were Afraid to Ask (2018)
- Adaptive Execution of Compiled Queries (2018)
- Efficiently Compiling Efficient Query Plans for Modern Hardware (2011)
- The Java Hotspot Server Compiler (2001)
- Self-Driving Database Management Systems (2017)
- Micro-Adaptivity in Vectorwise (2013)
- Dynamic Speculative Optimizations for SQL Compilation in Apache Spark (2020)
- Truffle: A Self-Optimizing Runtime System (2012)
- One VM to Rule Them All (2013)