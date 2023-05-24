## Generating Test Databases for Database Backed Applications (2023)

Cong Yan, Suman Nath, and Shan Lu.

Available [here](todo).

### Big Idea

Propose a tool that increases branch coverage in tests for database-backed applications by automatically generating test databases.

### Summary

The authors begin with the observation that application code often contains logic that implements a conditional branch on the basis of persistent database state. As a result, to cover branches effectively, developers must set up the persistent state preconditions accordingly (i.e. populate the database to reflect their conditions).

This study introduces a method to automatically synthesize databases for test purposes that increase branch coverage. This is difficult for two reasons:

- The generated databases must be semantically valid. The validity checks are often distributed throughout application code - not centralized as constraints within the schema itself
- Generating test databases, which may be large, must be efficient

The authors generate test databases by mutating seed databases that are input by the developer (assumed to be valid). They then utilize static analysis to resolve validity checking logic from the application itself and utilize this to ensure that the generated databases are in fact valid.

Furthermore, the authors filter out databases that do not improve branch coverage by performing further static analysis that locates the database-dependent branches in the application source. Databases that do not improve coverage are discarded. 

The solution proposed by the authors increases database-dependent branch coverage by an average of 14% across tested applications.

### Commentary

The authors suggest that another approach to this problem would be to utilize symbolic execution and constraint solving to synthesize all reachable database states based on the application source code. However, they claim this is intractable because of the complexity of modern applications. This is an extremely interesting idea.

Is there an engineering mechanism that would allow us to remove the database-dependent branches entirely?

### Questions

- The authors extract semantic constraints for databases based on the assumption that "validation callbacks" are used to verify the integrity of the database after each operation that takes place. Can we extend this approach to work with arbitrary application logic?

### Further Reading

- BigTest: A Symbolic Execution Based Systematic Test Generation Tool for Apache Spark (2020)