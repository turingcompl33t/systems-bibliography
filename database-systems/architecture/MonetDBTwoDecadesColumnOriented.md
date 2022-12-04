## MonetDB: Two Decades of Research in Column-Oriented Database Architectures (2012)

Stratos Idreos, Fabian Groffen, Niels Nes, Stefan Manegold, Sjoerd Mullender, and Martin Kersten

Available [here](https://stratos.seas.harvard.edu/publications/monetdb-two-decades-research-column-oriented-database-architectures).

### Summary

This paper presents an overview of the innovations in the MonetDB database system. As the name suggests, the system has been under active development for over two decades, and accordingly has produced a significant number of interesting innovations. Areas of innovation include:

- Physical Storage Model: MonetDB famously adopts a radical storage model in which all schemas are mapped to binary tables that consist of two columns (called binary association tables, or BATs).
- Execution Engine: The MonetDB execution engine consists of a bytecode virtual machine. The bytecode executed by the virtual machine is MonetDB Assembly Language, or MAL.
- System Architecture: The MonetDB architecture consists of three distinct components that are (relatively) independent: frontend, backend, and kernel. The frontend translates the input query to MAL, the backend implements the MAL virtual machine, and the kernel implements the backing operations for the MAL VM.

### Commentary

Naturally, the aspect of this paper that most interests me is the implementation of the execution engine. The design of the MAL virtual machine used in MonetDB is interesting / novel for several reasons. First, MAL is a relatively low-level intermediate representation. As the name implies, it really is essentially a virtual assembly language. It does have support for database-specific operations (e.g. it includes instructions for transaction management) but it also seems to decompose certain operations into finer-grained instructions than I have come to expect to see from other database-specific DSLs (case in point: TPL). 

As a result of the low-level nature of MAL, the optimizations that are applied to the intermediate representation of the query are themselves low-level. Many of the optimizations listed in the optimizer pipeline in the MonetDB documentation are similar to those one would find available in LLVM (e.g. constant propagation, dead code elimination, etc.) I am left wondering if they are able to perform higher-level optimizations (e.g. loop fusion) and if so, how?

One final interesting aspect of the execution engine is that the majority of the optimizations that are typically applied by the query optimizer prior to execution of the query are pushed down the stack into the MAL virtual machine and are applied during query execution. This appears to be a double edged sword. First, it seems like it might be more difficult to recover high-level semantics of the query once the query is decomposed to low-level MAL, making some optimizations impossible to apply. On the flip side, because the optimizations are applied during execution and MonetDB always fully-materializes intermediate results, there is no guessing or estimation going on - the cardinality of intermediate result sets is always known at the time the optimization is applied.

### Questions

- MonetDB uses a single intermediate representation in its execution engine, which is implemented as a bytecode virtual machine. Would it benefit from the additional of further intermediate representations (in the spirit of _How to Architect a Query Compiler_)?

### Further Reading

- Database Architecture Optimized for the New Bottleneck: Memory Access (1999)
- [MonetDB/X100: Hyper-Pipelining Query Execution (2005)](../execution/MonetDBX100.md)
