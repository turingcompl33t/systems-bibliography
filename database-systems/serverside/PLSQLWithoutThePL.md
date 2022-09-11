## PL/SQL Without the PL (2020)

Denis Hirn and Torsten Grust

Available [here](https://db.inf.uni-tuebingen.de/staticfiles/publications/plsql-without-the-pl.pdf). Video coverage available [here](https://www.youtube.com/watch?v=-PHQMDpl8_Y).

### Summary

The authors present a demonstration of the the source-to-source compilation technique originally presented in _Compiling PL/SQL Away_. Compilation translates user-defined functions expressed in PL/pgSQL to equivalent SQL expressions. The input PL/pgSQL program may contain arbitrary control flow constructs (e.g. `if/else`, `while`, and `for`). The authors demonstrate the compilation process via an interactive compilation interface - the Godbolt Compiler Explorer.

### Commentary

I am not entirely convinced of the utility of the web UI for the Apfel compiler from a developer point of view, but it definitely helps people like me who want to know more about how the system works to explore the transformations involved.

### Questions

- What is the current status of this project? Are Torsten and Denis still working to add new features, or have they largely declared success?

### Further Reading

- Compiling PL/SQL Away (2019)
