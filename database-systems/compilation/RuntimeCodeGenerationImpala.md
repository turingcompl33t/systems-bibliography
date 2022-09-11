## Runtime Code Generation in Cloudera Impala (2014)

Skye Wanderman-Milne and Nong Li.

Available [here](http://sites.computer.org/debull/A14mar/p31.pdf).

### Big Idea

The generality of the code used to evaluate operators degrades performance (for several reasons) so generate query-specific code at runtime to improve performance.

### Summary

The authors present the architecture of runtime code generation in Cloudera Impala, an open-source massively parallel processing (MPP) database that runs on Hadoop. Impala utilizes the LLVM compiler infrastructure to generate query-specific code for certain operators. This query-specific code is able to take advantage of additional information that is only available at runtime (because now the query is known) to reduce many of the overheads associated with the general iterator execution model.

### Commentary

The architecture for runtime code generation in Impala does not contain many surprises. This is perhaps unsurprising considering the paper was published back in 2014, only 3 years after _Efficiently Compiling Efficient Query Plans for Modern Hardware_, and is an open source project.

One thing I think this paper does better than most other papers on runtime code generation is motivate the use of code generation to solve performance problems. They provide a concrete example of iterator-model code and show how it can be improved once query-specific information is added to the equation.

The authors identify the primary advantages of runtime code generation as:
- Removing conditionals: conditionals that are dependent on some property of the query that is known at code generation time can be elided entirely; loops may be unrolled for a similar reason (the number of iterations is known)
- Removing loads: query-invariant data can be reduced to constant values which elides loads from memory e.g. the offset within a tuple of a particular attribute is known, so this value no longer needs to be looked up in a table at runtime
- Inlining virtual function calls: The operator tree for a query plan is often implemented via a class hierarchy that utilizes virtual function calls; because the type of each operator is known at code generation time, these expensive virtual calls can be fully inlined

### Questions

- How does the UDF support in Impala relate to my work on PL/pgSQL compilation? Ultimately, will people care that they can get fast UDFs in PL/SQL when they might be able to go elsewhere and get compiled UDFs in e.g. Python?

### Further Reading

- LLVM: An Infrastructure for Multi-Stage Optimization (2002)
