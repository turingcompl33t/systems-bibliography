## Functional Style SQL UDFs With a Capital 'F' (2020)

Christian Duta and Torsten Grust

Available [here](https://db.inf.uni-tuebingen.de/staticfiles/publications/functional-style-UDFs.pdf).

### Summary

The authors present a framework for compiling SQL UDFs that exhibit a specific functional style to plain SQL via recursive common table expressions. The translation results in logic that may subsequently be inlined into the calling query, enabling more efficient execution by relational engines. Furthermore, additional processing during compilation allows the framework to apply additional optimizations and avoid redundant computation via well-known functional programming concepts.

### Commentary

This paper appears to present a special case of the Apfel UDF compiler framework. In the _Compiling PL/SQL Away_ paper, the focus is on iterative control flow (e.g. `if/else`, `while`, and `for`) and how such constructs may be translated to an equivalent SQL expression. In contrast, this paper focuses on how to compile UDFs that are already expressed in terms of "functional" SQL to a more efficient form via recursive common table expressions. It is important to note the distinction here: no PL/SQL is involved in these functional SQL UDFs, the input language for the UDF is plain SQL. The contribution from this paper therefore does not come from gains from compiling the input UDF to a different language (it is already expressed in SQL) but rather by compiling to a form that the database system is able to execute more efficiently. Furthermore, the authors introduce several optimizations (well-known from the functional programming community?) to take advantage of the functional nature of the input UDF, such as call-graph pruning and memoization.

I love the algorithm used to efficiently execute the functional SQL UDF. In brief:
- Construct a call graph for the program, which consists of a dependency graph of all of the recursive invocations of the UDF
- Evaluate the call-graph bottom-up, memoizing results and eliding redundant computations

Naturally, once we have an explicitly dependency graph of the computations required to run the program, we open ourselves up to some awesome efficiency gains through concurrency / parallelization. This practically screams for a thread pool and a queue of work that consists of nodes in the graph whose dependencies are fully satisfied.

This paper also (finally) includes an explicit declaration that the answer to the issues surrounding imperative execution in relational databases will be found at the intersection of the database, compilers, and programming language communities. The authors express the sentiment that their compiler (Apfel) can be a key component in the "in-database programming puzzle" and that this problem is likely only to grow as the need to bring computation to the data increases with data volumes.

### Questions

- Is this functionality implemented as part of the Apfel framework? Although it does not _really_ share much of the same functionality (the compilation pipelines appear to be totally distinct between the two, which makes sense considering the source languages are different) one could argue that Apfel could be the one-stop-shop for UDF compilation, in which case it might make sense to include this pipeline as well.

### Further Reading

- FunSQL: It is Time to Make SQL Functional (2012)
- Compiling PL/SQL Away (2019)
- Extracting Equivalent SQL from Imperative Code in Database Applications (2016)
- Using Automatic Peristent Memoization to Facilitate Data Analysis Scripting (2011)
- PL/SQL Without the PL (2020)
- A History of Haskell: Being Lazy with Class (2007)
- Postgres 12 Documentation (Adds Support for Inlining?)
- Froid: Optimization of Imperative Programs in a Relational Database (2018)
- Debunking the "Expensive Procedure Call" Myth, or Procedure Call Implementations Considered Harmful, or LAMBDA: The Ultimate GOTO (1977)
