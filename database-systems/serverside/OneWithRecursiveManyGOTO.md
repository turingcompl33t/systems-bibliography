## One `WITH RECURSIVE` is Worth Many `GOTO`s (2021)

By Denis Hirn and Torsten Grust.

Available [here](https://db.inf.uni-tuebingen.de/staticfiles/publications/with-recursive-goto.pdf). Video overview available [here](https://www.youtube.com/watch?v=lqWhfU3SNRI).

### Summary

The authors present a framework (_Apfel_) that performs source-to-source compilation from PL/SQL (the focus is on the Postgres PL/pgSQL dialect) to plain SQL (SQL standard 1999 compliant). The framework is intended to remove the overhead of context switching between the relational and imperative execution engines in database systems that utilize interpreted query execution. The framework described in this paper is a continuation of the effort first described in _Compiling PL/SQL Away_, and it distinguishes itself from prior work in _Froid_ by adding support for arbitrary iterative control flow. The framework is implemented as a standalone compiler that does not invade the internals of the DBMS.

The purposes of this paper, in contrast to the two previous papers published on the topic of the Apfel framework, are:
- To describe the compilation pipeline in full
- Present the translation rules for the compilation pipeline
- Study the runtime and memory behavior for the compiler's output queries

### Commentary

The paper identifies a cool optimization with Postgres' UDF interpreter implementation: for simple expressions, the UDF interpreter takes a "fast path" in which it directly invokes the relational engine's expression evaluator. This elides the overhead of calling into the relational engine at the "top level" by skipping many of the steps involved. However, this comes at the cost of making the abstraction boundary somewhat more porous, which might make the code more difficult to reason about and maintain.

The paper includes a detailed description of each stage of the compilation process. The process appears relatively similar to that described in the original paper (_Compiling PL/SQL Away_) but is described here in far greater detail. Furthermore, there is an additional step - "trampoline style" - that is applied to the ANF intermediate representation before(?) translation to plain SQL that I do not yet fully understand.

The authors revisit the "iterative CTE" variant of common table expressions - applicable to properly tail-recursive CTEs. With tail-calls only, there is no need for a "stack", so only the "most recent" version of the working table for the common table expression is maintained. This results in significant space (memory) savings. 

The authors make an important observation near the end of the paper. They point out that we observe poor runtime performance for PL/SQL _despite_ the fact that it is implemented directly in the database system kernel, and thus is as close to the underlying data as we might move the computation. This highlights the depth of the impedance mismatch between declarative SQL and imperative PL/SQL programs.

### Questions

- Was the "trampoline" step included in the compiler descibed in _Compiling PL/SQL Away_? If not, why was this step added?
- The results include a couple of UDFs for which compilation and inlining actually produce worse performance than vanilla UDF interpretation with context switching. How can we detect, a priori, whether or not a query will benefit from UDF inlining?

### Further Reading

- Aggify: Lifting the Curse of Cursor Loops using Custom Aggregates (2020)
