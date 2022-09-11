## Apache Spark as a Compiler: Joining a Billion Rows per Second on a Laptop (2016)

Sameer Agarwal, Davies Liu, and Reynold Xin.

Available [here](https://databricks.com/blog/2016/05/23/apache-spark-as-a-compiler-joining-a-billion-rows-per-second-on-a-laptop.html).

### Big Idea

General purpose code for query evaluation is slow, so generate query-specific code at runtime and take advantage of runtime information to improve performance.

### Summary

The authors present the high-level ideas behind the Tungsten 2.0 engine in Apache Spark. Most importantly, the engine adds support for runtime code generation in which certain operators are compiled to JVM bytecode prior to evaluation to elide many of the overheads associated with the general iterator-style execution model. They observe speedups across a wide variety of operations as a result of this update to the engine.

### Commentary

This is just a blog post so there isn't a ton of content to dive into here. The important takeaways are that Tungsten generates JVM bytecode for certain operators to improve performance by:
- Removing virtual function calls
- Increasing the "volume" of intermediate results that can be kept in registers rather than residing on the stack (or spilling to memory?)
- Allowing for a greater degree of loop unrolling and automatic SIMD vectorization (although as far as I can tell auto-vectorization is still in its infancy...)

Like the Impala paper, this paper also does a nice job of motivating the code generation approach. They show the implementation of an operator in the iterator model and then demonstrate a Java function that accomplishes the same thing, without any of the indirection and generality overhead imposed by the former approach. This is also similar to what is done in the _How to Architect a Query Compiler, Revisited_ paper.

### Questions

- Spark generates Java bytecode rather than targeting LLVM IR like so many other systems. How does the degree of optimizations provided out-of-the-box compare for these two infrastructures (the JVM vs LLVM)?

### Further Reading

- Spark SQL: Relational Data Processing in Spark (2015)
