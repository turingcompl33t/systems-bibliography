## Compiling PL/SQL Away (2019)

Christian Duta, Denis Hirn, and Torsten Grust

Available [here](https://db.inf.uni-tuebingen.de/staticfiles/publications/compiling-PLSQL-away.pdf).

### Summary

The authors present a framework to compile arbitrary PL/SQL functions (they focus on the PL/pgSQL dialect) to equivalent SQL expressions that may then be inlined into a calling query. The work may be regarded as an improvement upon the Froid framework in several respects:
- The framework adds support for imperative iteration constructs (`WHILE` and `FOR`) for which Froid lacks support
- The framework is implemented as a standalone UDF compiler and is not integrated into a DBMS in the same way that Froid is, enabling the framework to be used more easily with arbitrary database systems, even those without native support for UDF execution

The authors present preliminary results for an experimental evaluation of their framework which show that inlining completely removes the context-switching overhead observed in the original queries. Furthermore, they find that the performance improvement exceeds that which would be realized if context-switching overhead were the only area of improvement for the approach, implying that inlining the UDF has additional benefits (e.g. opening up the UDF to the optimizer) beyond just eliding this overhead.

### Terminology

- Iterative Common Table Expressions: This is a shorthand for recursive CTEs that implement proper tail recursion. Because the CTE is tail recursive, only the final stack (frame) is required to continue to evaluate it, meaning that all preceding stack frames can be discarded (or reused) as recursion unfolds. The `WITH ITERATE` syntax was originally propsed by Neumann, and the authors of this paper adopt this terminology and implement the feature in Postgres. NoisePage implements this as `WITH ITERATIVE`.

### Commentary

The authors describe PL/SQL as "the in-database scripting language." I am not sure why this comparison never occurred to me before, but I really like it! PL/SQL really is just a special-purpose scripting language with some unfortunate syntax. It really does resemble most other scripting languages like Python. I like this analogy because it implies that we might be able to apply some of the techniques that the programming language and compiler/interpreter community have developed over many years of researach to PL/SQL and get performance benefits.

The authors describe the impedance mismatch between declarative SQL and imperative PL/SQL programs in much the same way as the authors of the Froid paper, and they go so far as to say that the distincton is "fundamental" which I interpret as "irreducible" - it is not an implementation shortcoming, but rather a fundamental property of the two styles. However, they make the caveat here that this applies to _interpreted_ query engines and may not necessarily hold true for compiled query engines that generate imperative code that implements the query plan tree. This is the category in which my research with NoisePage falls. 

The compilation process from PL/SQL to SQL expression consists of four (4) intermediate forms:
- SSA: Transforms the input PL/SQL function to SSA form; only `GOTO` is used for control flow
- ANF: Derive administrative normal form from the SSA form; expresses iteration in terms of (perhaps mutually-) tail-recursive calls
- Flatten mutual recursion to a single tail-recursive UDF
- Perform the final translation to SQL by turning tail-recursion into recursive common table expressions (`WITH RECURSIVE`)

The authors note that PL/SQL code is subject to the same optimizations as any imperative programming language. Furthermore, they already perform the translation from PL/SQL to SSA form, on which compiler optimizations are well-studied. Is there potential here to perform standard compiler optimizations? What if we took the "custom SSA" form down to LLVM IR SSA and turned LLVM loose on it, and only then lowered to ANF form?

Lowering from PL/SQL to SSA should follow the well-known algorithm for this relatively well. Furthermore, it appears there is also a well-known algorithm for translation from SSA form to ANF form. By its definition, ANF leaves us in a good position to express the original logic as a SQL query because it trades the `GOTO`-based control flow of SSA for mutual recursion and is purely expression-based. This multi-step lowering process is beautiful.

The authors admit that dynamic SQL will likely always be out of reach of the compilation + inlining approach to UDF evalution. This might be the area in which direct compilation yields the most potential for benefit.

### Questions

N/A

### Further Reading

- Orthogonal Optimization of Subqueries and Aggregation (2001)
- SQL and Operator-Centric Data Analytics in Relational Main-Memory Databases (2017)
