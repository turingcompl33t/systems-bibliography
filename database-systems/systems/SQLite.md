## System Design: SQLite

Per usual, the primary component of interest in this system for our purposes is the execution engine. I was initially surprised to learn that despite its reputation as a small, simple database implementation (indeed, it is _the_ embedded database system), SQLite's execution engine does not utilize the traditional (read: simple) iterator model. Instead, it compiles query plans to bytecode programs and interprets these programs on a virtual machine.

Compared to the internal virtual machines used by other systems, the SQLite virtual machine appears to implement a refreshingly simple design:
- The `sqlite3_prepare_v2()` function implements the high-level interface to the engine; it translates an input SQL query to a bytecode program (or "prepared statement" in SQLite parlance)
- The `sqlite3_step()` function is the interface to run interpretation; the function returns whenever a result row is returned by the byetcode program

Each of the opcodes in the SQLite engine accepts up to 5 operands that are stored in registers. It is never explicitly stated, but it appears that the SQLite engine implements a virtual register set, something akin to the LLVM intermediate representation, that abstracts over the physical register set of the machine on which the VM runs.

My big takeaway from this document is the manner in which the SQLite engine implements subqueries in their bytecode engine. Importantly, they need the ability lazily yield result rows from subprograms. This is implemented by coroutines within the bytecode engine. This is an awesome idea, and importantly it appears to be one way in which we might do something similar in the NoisePage execution engine when handling both CTEs and subqueries.

**Questions**

- Although this document describes the high-level design of the bytecode engine, I am still left wondering how the authors of the SQLite engine arrived at their final design. It appears parsimonious and elegant, but how did they decide on the precise set of operations that they now support? Do they ever add or remove operations? What motivates these decisions?

### References

- [The SQLite Bytecode Engine](https://www.sqlite.org/opcode.html)
