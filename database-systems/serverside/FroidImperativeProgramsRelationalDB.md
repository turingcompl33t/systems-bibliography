## Froid: Optimization of Imperative Programs in a Relational Database (2018)

Karthik Ramachandra, Kwanghyun Park, K. Venkatesh Emani, Alan Halverson, Cesar Galindo-Legaria, and Conor Cunningham

Available [here](https://www.vldb.org/pvldb/vol11/p432-ramachandra.pdf).

### Summary

The authors present the Froid framework which improves the performance of UDF execution in the Microsoft SQL Server database system by transforming UDFs into equivalent relational algebraic expressions and inlining the result into the calling query, thereby eliding "distinct" execution of the UDF altogether.

In addition to their approach to UDF transformation (might this be considered a form of compilation?), the authors also introduce several optimizations that may be applied on the transformed query that imitate the application of traditional compiler optimizations like dead code elimination.

An experimental evaluation shows that Froid achieves significant reductions in query execution time, memory consumption, and IO operations relative to the existing execution strategy in SQL Server, with relatively low additional compilation and optimization time overhead.

### Terminology

- Scalar User-Defined Function: A UDF that returns a single scalar value
- Table-Valued Function: A UDF that returns a set of rows

### Commentary

Why procedural extensions? The authors of this paper offer the following reasons:
1. Code reuse among queries
2. Some computations are more amenable to expression in an imperative form
3. Improving readability and maintainability by allowing users to mix simple SQL queries with the complex logic encapsulated in the UDF

The authors claim that the fundamental issue that leads to the poor execution performance of UDFs in database systems is the "impedance mismatch" between the two programming paradigms - declarative SQL and imperative UDFs.

The high-level flow of the transformation applied by Froid is as follows:
- Partition the input UDF into "regions" - analogous to basic blocks e.g. sequential regions, conditional regions (if/else), and loop regions (while loops)
- Compute an equivalent relational expression for each region in the UDF body
- Combine the expressions for each region into a single relational expression using the `APPLY` operator (`LATERAL JOIN`?) - it is important to note here that all of the transformations are applied on the query AST rather than directly at the SQL language layer!

The authors faced the choice of making UDF-inlining a cost-based decision - one that was applied during query optimization rather than during binding. They utlimately decided to apply inlining during binding (always) because they observed that it was almost always more efficient than the alternative execution strategy. However, this is definitely an interesting line of research, and one that we might want to look into more closely once we have an evaluation of direct UDF compilation.

One aspect of Froid that appears not to be addressed in subsequent literature (?) is its extensibility. The authors describe how Froid is designed to be extensible to other programming languages and imperative constructs within those languages. It appears that they distinguish between the syntax of the language in which the UDF is expressed and the more abstract imperative constructs this syntax encodes. For instance, T-SQL and Python have different syntax for conditional expressions, but the semantics of the conditional remain the same once we get beyond the parsing layer.

One big question / confusion I am left with is in the discussion of integration of Froid with Hekaton. The authors say that Hekaton natively-compiles queries / UDFs. Does this imply that Hekaton is using the standard query compilation approach that we all known and love (i.e. from Neumann) or that they have implemented a distinct system in Hekaton to natively compile UDFs? If the latter is the case, then my research may be in trouble... The next thing to read will be the Hekaton paper.

### Questions

- The authors claim that procedural extensions to SQL are "widely used." How widely used are these procedural extensions? Does this differ across settings / use cases?
- The "traditional" approach to UDF execution in SQL server is particularly ill-suited to the execution of UDFs that include embedded SQL queries because this implies (at least) two context switches between the relational engine and the scalar engine. How common are these types of UDFs?

### Further Reading

- Optimizing Database-Backed Applications with Query Synthesis (2013)
- Hekaton: SQL Server's Memory-Optimized OLTP Engine (2013)
- DBridge: Translating Imperative Code to SQL (2017)
- Orthogonal Optimization of Subqueries and Aggregation (2001)
