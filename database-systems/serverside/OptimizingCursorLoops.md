## Optimizing Cursor Loops in Relational Databases (2020)

Surabhi Gupta, Sanket Purandare, and Karthik Ramachandra.

Available [here](https://arxiv.org/pdf/2004.05378.pdf).

### Summary

The authors describe a framework (_Aggify_) that transforms cursor loops to equivalent SQL queries via the systematic construction of a custom aggregate that implements the logic of the cursor loop. The input cursor loop may be expressed in any imperative form, such as procedural extensions to SQL (UDFs) or in application source code (e.g. Java over JDBC). The resulting queries avoid many of the overheads inherent in the evaluation of cursor loops. Experimental results show improvements in runtime performance, resource consumption, and data movement.

### Terminology

- Cursor Loop: Any explicit loop construct over the result rows of a query. This is in contrast to a set-oriented operation over the results of a query (an aggregate is an example of such a set-oriented operation).

### Commentary

The declarative / imperative impedance mismatch rears its ugly head again in this paper, this time in the guise of set-oriented operations versus row-by-row operations. We are fighting the same war here as we are in the _Froid_ and _Apfel_ papers, just perhaps on a different front.

The _Aggify_ framework is distinct from _Froid_. However, the two complement one another well. On its own, _Froid_ does not support iteration constructs like cursor loops or `FOR`-loops. _Aggify_ can be used to allow _Froid_ to optimize UDFs with loops in the following way:
- Run _Aggify_ on the UDF with an embedded loop to rewrite the loop with a custom aggregate
- Run _Froid_ on the resulting loop-less UDF and inline the resulting query into the calling query

The combination of _Aggify_ and _Froid_ appears to overcome the primary distinguishing factor of _Apfel_ over _Froid_ - namely that _Froid_ does not support iteration constructs.

Despite the fact that I typically group _Apfel_ and _Froid_ together in my discussion of techniques for overcoming UDF performance bottlenecks, they really are two distinct systems - distinct approaches that imply different performance characteristics. For instance, in this paper, the authors claim that _Apfel_ may sometimes perform worse than the combination of _Froid_ + _Aggify_ because of its liberal use of recursive common table expressions and the limited optimizations that exist for these (relative to what?). Naturally, _Aggify_ avoids the creation of recursive CTEs by taking an entirely different approach to implementing iteration. A couple of interesting questions arise here:
- Which is the more efficient way to transform explicit iteration constructs? Recursive common table expressions, or custom aggregates?
- Does the choice depend on the nature of the iteration? What properties are important?
- Can we devise a system that captures the benefits of both approaches?

Near the end of this paper the authors call out a general trend of attempting to improve the performance of in-database computation with concepts from the programming language community. This is an important observation to make, and corroborates the thinking that I see coming out of the _Apfel_ group as well.

### Questions

See above.

### Further Reading

- Optimizing Database Applications with Query Synthesis (2013)
- [Compiling PL/SQL Away (2019)](CompilingPLSQLAway.md)
- Extracting Equivalent SQL from Imperative Code in Database Applications (2016)
- Cobra: A Framework for Cost-Based Rewriting of Database Applications (2018)
- SQLoop: High-Performance Iterative Processing in Data Management (2018)
- [Orthogonal Optimization of Subqueries and Aggregation (2001)](../optimization/OrthogonalOptimizationSubqueries.md)
- Iterative Query Processing Based on Unified Optimization Techniques (2019)
- Translating Imperative Code to MapReduce (2014)
- Froid: Optimization of Imperative Programs in a Relational Database (2017)
