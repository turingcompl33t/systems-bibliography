## Tuplex: Data Science in Python at Native Code Speed (2021)

Leonhard Spiegelberg, Rahul Yesantharao, Malte Schwarzkopf, and Tim Kraska.

Available [here](https://tuplex.cs.brown.edu/).

### Summary

The authors present Tuplex, a new framework for distributed analytics comparable to Spark or the Dask Python framework. In Tuplex, user's implement data analytics pipelines via a Python API that is similar to that provided by PySpark (both of which are , apparently, inspired by LINQ from Microsoft). Tuplex achieves improved performance on analytics pipelines by compiling Python UDFs to native code with LLVM. The authors of the Tuplex framework are able to achieve native compilation of Python code (where others have failed) by leveraging a novel _dual-mode execution model_ in which up to three (3) code paths are generated for each UDF: an optimized common-case path, a less-optimized general case path, and a fallback path that invokes the Python interpreter. Specialization of the UDF for the common case makes native compilation of the Python UDF tractable, ensures that the majority of the data is processed via this fast path, while maintaining the invariant that the semantics of the original Python code are preserved.

### Commentary

A high-level overview of the Tuplex system:

- A sample of the input data is analyzed and the "common case" is determined; the profile of the common case includes things like data types for columns in the input data (which are inferred by Tuplex) and which inputs constitute exceptional cases (e.g. is a NULL value in this column the common case or the exceptional case?)
- The Python AST for each UDF is specialized for this common case by adding type annotations and removing expensive checks for conditions that are not expected to occur in the common case
- The specialized Python AST is compiled to native code with LLVM
- The "classifier" code that determines whether an input row fits the common case or not is compiled to native code with LLVM
- The pipeline is executed; if an exception occurs in the native code for the common case, the row is deferred for later processing under the general case; failures in the general case are similarly deferred to processing on the Python interpreter

The dual-mode execution strategy is interesting, and indeed this is the primary contribution that the authors of this paper highlight. However, of perhaps equal importance are the optimizations that they are able to apply as a result of the various levels of representation for the UDFs they consider. Because Tuplex has full knowledge of the UDFs in a pipeline, it can perform high-level optimizations that would otherwise be precluded by black-box UDFs. For instance, Tuplex can determine that a UDF functions as a filter and push this down in the overall plan to mimic typical predicate-pushdown. Furthermore, they apply some optimizations at the level of the Python AST such as converting dictionaries with string keys into tuples to avoid an additional layer of indirection. Finally, they remove certain checks (branches) during code generation based on the profile they compute during the sample analysis phase - sort of a simple form of profile-guided optimization that results from the fact that they are optimizing for the common case.

### Questions

- One of the primary limitations of Tuplex is the fact that it assumes UDFs are stateless and do not have side effects. Is this realistic? Is it possible to overcome this limitation considering rows in Tuplex may be processed up to three times?
- Why are HyPer's compiled queries able to out-perform those produced by Tuplex so readily? What accounts for this distinction?

### Further Reading

- DBToaster: A SQL Compiler for High-Performance Delta Processing (2009)
- An Architecture for Compiling UDF-Centric Workflows (2015)
- Flare: Optimizing Apache Spark with Native Compilation for Scale-Up Architectures and Medium-Size Data (2018)
- Building Efficient Query Engines in a High-Level Language (2014)
- How to Architect a Query Compiler (2016)
- How to Architect a Query Compiler, Revisited (2018)
- Vectorwise: A Vectorized Analytical DBMS (2012)
