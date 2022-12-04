## DBToaster: A SQL Compiler for High-Performance Delta Processing in Main-Memory Databases (2009)

Yanif Ahmad and Christoph Koch.

Available [here](https://dbtoaster.github.io/papers/vldb2009-dbtoaster-demo.pdf).

### Big Idea

Compile standing view queries to highly-efficient C++ or Scala code to achieve order-of-magnitude performance improvements in incremental view maintenance (IMV).

### Summary

The authors present a demonstration of DBToaster, a compiler framework for standing SQL queries. DBToaster achieves order-of-magnitude performance improvements over existing relational databases and stream processing systems using a novel incremental view maintenance approach in which the compiler computes derivatives (and higher-order derivatives) of each standing query. When the database is updated by incoming events (inserts, updates, and deletes), the framework uses these derivatives to determine how each view is affected by the event.

### Commentary

The idea of computing derivatives of SQL queries in DBToaster is incredibly cool, and something I am definitely interested in learning more about. That said, the code generation and compilation aspects of the system don't actually appear that novel, or at the very least are under-developed as presented in this paper.

At first I was confused by the authors claims - if they actually achieve the speedups they claim, how is the system not more popular? But after reading I see that it is only applicable in certain constrained scenarios - namely, it cannot be used for ad-hoc queries of any kind.

### Questions

N/A

### Further Reading

N/A