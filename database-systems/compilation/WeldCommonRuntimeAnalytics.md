## Weld: A Common Runtime for High Performance Data Analytics (2017)

Shoumik Palkar, James J. Thomas, Anil Shanbhag, Deepak Narayanan, Holger Pirk, Malte Schwarzkopf, Saman Amarasinghe, and Matei Zaharia.

Available [here](https://cs.stanford.edu/~matei/papers/2017/cidr_weld.pdf)

### Big Idea

A common intermediate representation and associated runtime that enables optimization across function calls from different data-processing libraries.

### Summary

The authors present _Weld_, a common intermediate representation and runtime for high performance data analysis. In Weld, data processing libraries utilize the Weld API (at the time of writing, available in Python and Scala) to generate Weld IR instead of performing the computation directly. Weld then constructs a DAG of these IR fragments and evaluates them lazily (only when required). The common intermediate representation between different libraries allows Weld to optimize parts of the workflow that would otherwise be impossible to optimize, namely data movement between operations.

### Commentary

The authors define data-intensive as: workflows that perform little computation per byte. This is in contrast to a compute intensive operation that is likely compute-bound. In a data-intensive application, the bottleneck is (likely) data movement. This is where Weld comes in because it can optimize the data movement _between_ calls into distinct libraries, which would otherwise be impossible.

The authors claim that, as applications continue to use a greater number of distinct libraries, "one size will have to fit all" in terms of the runtime for the application. They argue that data movement becomes a fundamental bottleneck in such systems, and that a common runtime is required to achieve near bare-metal speeds.

How would one integrate a DBMS with Weld? It appears that for a code generation engine like NoisePage, this would be relatively straightforward: we simply generate Weld intermediate representation instead of LLVM IR, and then use the Weld runtime to execute the query. The question then becomes, however, how difficult would it be to map a TPL program to Weld IR? This is likely not what we would do because it would mean going from a declarative query, to a query plan tree, to an imperative bytecode program, back "up" to the high-level, declarative Weld IR... As it stands, I think it would be difficult to map TPL to Weld's explicitly parallel IR.

### Questions

- How would you integrate a cost-based optimizer for the Weld intermediate representation? This is one of the proposals made by the authors at the end of the paper, but the mechanism for doing this seems unclear to me because of the requirement of evaluating cost across distinct libraries.
- Where is the sweet spot for an intermediate representation for data analytics? Weld adopts a relatively minimal intermediate representation that makes certain optimizations possible that would otherwise be unattainable. However, its low-level nature likely leaves some performance on the table because it lacks certain high-level knowledge that is only available in a domain-specific context. It seems like what we need is, in addition to the IR and runtime, an interface by which domain-specific knowledge of program structure can be injected into Weld. That, or multiple intermediate representations...

### Further Reading

- Spark SQL: Relational Data Processing in Spark (2015)
- Building Efficient Query Engines in a High-Level Language (2014)
- Optimizing Data Structures in High-Level Programs (2013)
- Apache Spark: A Unified Engine for Big Data Processing (2016)
