## The DBToaster White Paper (2014)

The DBToaster Consortium.

Available [here](https://dbtoaster.github.io/papers/whitepaper.pdf).

### Big Idea

Recursively compile standing aggregation queries to C++ or Scala code and use this to perform incremental view maintenance (IMV).

### Summary

The authors present an overview of DBToaster, a compiler framework for SQL queries. DBToaster compiles SQL queries to C++ or Scala code that implements extremely efficient incremental view maintenance. The key insight is the transformation of the input query to an internal calculus on which it is possible to compute derivatives, in the mathematical sense. The compiler then uses these derivatives to determine how updates to the database impact a particular view.

### Commentary

I'll reserve commentary for the other DBToaster publications.

### Questions

- What happened to DBToaster? Is this project still alive? With the magnitude of the performance improvements they are claiming, I would have to think this system would be more popular, unless something happened that caused progress to stall or the authors were not able to deliver on these claims.

### Further Reading

N/A
