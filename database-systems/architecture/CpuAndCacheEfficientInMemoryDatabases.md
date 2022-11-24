## CPU and Cache Efficient Management of Memory-Resident Databases (2013)

Holger Pirk, Florian Funke, Martin Grund, Thomas Neumann, Ulf Leser, Stefan Manegold, Alfons Kemper, and Martin Kersten.

Available [here](https://15721.courses.cs.cmu.edu/spring2020/papers/14-compilation/pirk-icde2013.pdf).

### Big Idea

Combine the partially-decomposed storage model (PDSM) with JIT query compilation to achieve greater performance through increases CPU and cache efficiency.

### Summary

The authors present a technique for achieving a closer-to-optimal mix of CPU and cache efficiency in database systems. They combine the existing JIT compilation infrastructure of the HyPer DBMS with the partially-decomposed storage model (PDSM). In this storage model, each table in the database is subject to physical partitioning such that subsets of the table's attributes are stored in row-oriented fashion (the subset may be of cardinality 1, which would make this look just like a true decomposition storage model). To fully take advantage of this combination of JIT and PDSM, the authors present a "programmable cost model" that builds on the _Generic Cost Model_ proposed in prior work. This cost model is used to (dynamically?) optimize the physical layout of the table as more knowledge of the workload is gained.

### Commentary

This paper is not focused on compilation, but rather the intersection of compilation and storage technologies. This is an area that I do not have much experience in, so it was a pleasant surprise to stumble upon this paper.

The primary contributions of this paper are:
- The design and implementation of a PDSM storage component for a JIT-based system
- A cost model for memory-resident PDSM systems that allows for dynamic optimization of the physical layout of partitions
- An experimental evaluation

The authors claim that the focus of query compilation systems (up to this point) has been on flexibility and extensibility rather than performance. This is an interesting claim - isn't the whole point of a query compilation system for performance? 

The most compelling idea in this paper is the extension to the _Generic Cost Model_ that the authors propose as a means of computing better cost estimates for different storage models. In the original _Generic Cost Model_, the queries themselves are examined for the attributes of each relation that they access, and this is used as input to the model. In the proposed extension, the access patterns of the queries are provided as input to the model, rather than the queries themselves. Further, construction of the cost model for a query is analogous to code generation for the query. As the operator tree is scanned, each operator in the tree emits an access pattern (in the form of an access pattern algebra instruction) into the overall "cost model program". 

The authors use the term _Programmable Cost Model_ to describe this approach, and I find this really compelling. I wonder if this is applicable in situations other than physical data layout optimization.

### Questions

- This paper is focused on the partially-decomposed storage model, which is most interesting in hybrid OLTP/OLAP scenarios. Is this still an area of interest in the academic community? I know Andy was on the HTAP train for quite some time, but he seems to be cooling on this, and I wonder what the future holds.

### Further Reading

- Database Architecture Optimized for the New Bottleneck: Memory Access (1999)
- Volcano - An Extensible and Parallel Query Evaluation System (1994)
- One Size Fits All, Again! The Architecture of the Hybrid OLTP and OLAP Database Management System HyPer (2011)
- Generic Database Cost Models for Hierarchical Memory Systems (2002)
- A Common Database Approach fr OLTP and OLAP Using an In-Memory Column Database (2009)
- Vectorization vs Compilation in Query Execution (2011)
