## Compilation in the Microsoft Hekaton Engine (2014)

Craig Freedman, Erik Ismert, and Per-Ake Larson.

Available [here](https://15721.courses.cs.cmu.edu/spring2016/papers/freedman-ieee2014.pdf).

### Summary

The authors provide an overview of the memory-optimized OLTP engine for Microsoft SQL Server, _Hekaton_, with a specific focus on the implementation of native compilation in the Hekaton execution engine. Hekaton is capable of compiling SQL queries and stored procedures expressed in T-SQL to native machine code. The high-level strategy used in the Hekaton engine is translation of the query plan, through two intermediate representations (described below) into C source code which is then compiled and linked via MSVC to a DLL that is subsequently loaded into the SQL Server process. Experiments show that native compilation reduces the number of instructions executed by up to 15x.

### Commentary

Right off the bat I was surprised to see that Hekaton is intended for use in OLTP engines - it seems that native compilation, especially via the mechanism that Hekaton uses, introduces too much latency to each query to achieve any reasonable throughput (or at least the throughput we need for transactional workloads, especially on a system as popular as SQL Server). But the authors clarify this point that compilation in Hekaton is intended for observe-one-execute-many (possibly millions) queries. This is an important takeaway: I don't think there are any systems that are capable of natively compiling ad-hoc queries for OLTP applications. Even HyPer, which I imagine has the lowest-latency compilation process (perhaps SingleStore is competitive?) is intended for in-memory analytics, rather than transactions.

One interesting aspect of this work is the fact that Hekaton supports native compilation of stored procedures expressed in T-SQL. They claim that it supports all of the standard control flow structures, but then don't make much more of this fact. Perhaps this is because they ultimately generate C source code, and translation from an imperative language (T-SQL) to another imperative language (C) is not all that complicated?

The key observation that led the Microsoft team to focus on native compilation in Hekaton bears repeating here: in order to go 10x faster, the execution engine must execute 90% fewer instructions. In order to go 100x faster, the execution engine must execute 99% fewer instructions. These are sobering statistics. 

One other principle that is illustrated in this paper (and really all of the others that do code generation, although never explicitly stated): generality often kills performance, and the solution to this is to introduce specialization. Or, from Onur Mutlu's course on computer architecture, "performance through heterogeneity."

The overview of the process for stored procedure compilation is as follows:
- Optimized query plan (existing SQL Server infrastructure)
- Mixed Abstract Tree (MAT), essentially an enriched form of the query plan
- Pure Imperative Tree (PIT), essentially an in-memory AST representation for C source code (I envision this as something similar to what GCC might produce while compiling C source, at least at some point in its stack...)
- C source code generation, naturally this step is pretty straightforward after we have the PIT
- Native compilation

### Questions

- Are we nearing the limit of what we might be able to achieve in terms of query execution latency? How can we reduce the number of instructions further than native compilation (other than smarter native compilation)?

### Further Reading

- Hekaton: SQL Server's Memory-Optimized OLTP Engine (2013)
- Efficiently Compiling Efficient Query Plans to Modern Hardware (2011)
