## MonetDB/X100: Hyper-Pipelining Query Execution (2005)

Peter Boncz, Marcin Zukowski, and Niels Nes

Available [here](https://15721.courses.cs.cmu.edu/spring2018/papers/18-execution/boncz-cidr2005.pdf).

### Summary

This paper describes a new backend implementation for the MonetDB database system - X100. X100 differentiates itself from the "standard" MonetDB query execution backend by virtue of the fact that it adds native support for vectorized execution. This departs from the standard backend in that it no longer fully materializes intermediate results and instead materializes vectors of tuples in an effort to improve locality and thereby reduce the influence of the memory bottleneck.

### Commentary

I was hoping that this paper would have more details describing the implementation of the execution engine in MonetDB, but it is far more concerned with changes to the storage model and the query processing engine in general, rather than the specifics of the MIL/MAL virtual machine. Indeed, it might even be the case that this paper (published in 2005) is too outdated to offer any interesting details on the implementation of the MAL VM.

### Questions

- Based on the sentiments expressed in papers about MonetDB that follow this one, it seems that X100 did not "pan out" in the way the authors of this paper claimed that it would. Is this the case, and if so, what happened to it? Why does MonetDB today stick to the "traditional" model in which it adopts full materialization of binary tables?

### Further Reading

- Monet: A Next-Generation DBMS Kernel for Query Intensive Applications (2002)
- MIL Primitives for Querying a Fragmented World (1999)
