## Spark SQL: Relational Data Processing in Spark (2015)

Michael Armbrust, Reynold S. Xin, Cheng Lian, Yin Huai, Davies Liu, Joseph K. Bradley, Xiangrui Meng, Tomer Kaftan, Michael J. Franklin, Ali Ghodsi, and Matei Zaharia

Available [here](https://people.csail.mit.edu/matei/papers/2015/sigmod_spark_sql.pdf).

### Summary

The authors present Spark SQL, a major addition to the Spark data analytics framework. Spark SQL introduces two major components to Spark:
- A _DataFrame_ API, similar to the dataframe API provided by programming languages (e.g. R) and analytics libraries (e.g. Pandas for Python). The DataFrame API is exposed to Spark programmers as a collection of library functions and types in each of the three major programming languages supported for Spark development (Scala, Python, and Java).
- The _Catalyst_ query optimizer, an extensible optimizer that enables transformation of query plans (especially those produced by use of the new relational DataFrame API) into semantically-equivalent plans that execute more efficiently.

### Commentary

This paper explores a topic that is near and dear to my heart, coming from research on user-defined functions in a relational database setting: the gap between declarative and imperative computation (both in how we express it, and how we execute it). Spark already has a high-level, functional API (e.g. operations like `map` and `filter`), but the introduction of Spark SQL takes this one step further.

The ideas in this paper reinforce something that seems to be at the heart of many of these papers - high-level, declarative code is critical for performance. It is this manner of expressing our intent that is most amenable to automatic optimization and efficient distributed computation (?).

Similarly, the authors note a limitation of the implementation of Spark SQL that they describe in this paper: that user-defined functions passed to Spark via the traditional RDD API (e.g. as Scala closures) are an impediment to optimization. These UDFs are treated as black boxes, the Spark is unable to do anything to optimize their execution. However, it seems like since this paper was published, this problem may have been addressed by the _Flare_ Spark module that natively compiles Spark jobs, and also supports native compilation of UDFs (assuming they adopt the LMS library in their implementation).

I found the description of the architecture of the Catalyst optimizer extremely compelling. In brief:
- The query plan is represented within the optimizer as a tree
- Optimizations are transformations from one tree to another tree; we search for subtrees matching a specific pattern and replace them with semantically-equivalent subtrees that are more efficient

This is a **beautiful** abstraction. I plan to look more closely at how the Catalyst optimizer has evolved since this paper was published and whether this idea has scaled.

Finally, it is worth noting the code generation technique that is introduced in this paper. As part of the Catalyst optimizer, the optimizer may choose to generate Java bytecode for certain portions of the query plan. This is implemented in a similar manner as the optimization passes - a transformation step from one subtree to another. The implementation relies on Scala "quasiquotes" to perform code generation. These quasiquotes are compiled (by the Scala compiler) from Scala source (within a quoted string) to the Scala AST that implements this source, at the time of compilation of the program itself. This is insanely cool that this is _part of the Scala language_ itself. Yet another reason Scala is a language worth taking a closer look at. The authors note in the related works section that the approach used in LegoBase wherein code generation is implemented via generative programming with the Lighweight Modular Staging library is an alternative to the use of quasiquotes.

### Questions

- How has the approach to extensible optimization pioneered by Catalyst fared since this paper was published? Is Catalyst able to implement optimizations that would otherwise be performed on a different intermediate representation? Are there certain optimization patterns that it fails to capture?

### Further Reading

- The Cascades Framework for Query Optimization (1995)
- Building Efficient Query Engines in a High-Level Language (2014)
- Quasiquotes for Scala, A Technical Report (2013)
