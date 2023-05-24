## Safe-DS: A Domain-Specific Language to Make Data Science Safe (2023)

Lars Reimann, Gunter Kniesel-Wunsche

Available [here](todo).

### Big Idea

Design a domain-specific language that supports static checking of data science pipelines to improve developer productivity. Allow extension of the DSL through an expressive stub language. Support both textual and graphical views of the same underlying pipeline abstraction.

### Summary

The authors define a data science pipeline as consisting of the following steps:

- Data loading
- Data preparation
- Model training
- Hyperparameter optimization

Pipelines in Safe-DS lack branching functionality e.g. loops and conditionals. The authors claim this makes development easier and static type checking simpler to implement because of the "linear" data flow.

The authors identify the following type errors that are not caught by current Python linters:

- range restrictions
- broken dataset access
- broken order

The authors implement a stub language that supports integration between Safe-DS and Python. Users develop a stub for a call to a particular Python function and this allows the corresponding function to be invoked in a pipeline.

Safe-DS provides both textual and graphical views of the same underlying abstraction. The authors claim that this allows more productive development.

### Commentary

The analysis in this paper relies on the idea that DS pipelines written in Python directly are easy to misuse. I wonder if this statement is correct in the era of interactive notebooks where we can verify the correctness of an implementation interactively before running the complete invocation (e.g. with large data volumes)? 

Data sampling might be utilized to prototype portions of a pipeline before running it on the complete data volume. The types of errors that might not be caught by this approach (e.g. runtime exceptions caused by malformed data) might also fail to be caught by the static approach in Safe-DS because they are dynamic aspects. However, if the type system of Safe-DS is expressive enough to encode e.g. nullable-values, this might be safe enough.

The _range restrictions_ type error seems like a good candidate for a refinement type in Python.

I really love the core idea for this paper, and the confluence of data science, compilers, and programming languages. However, while this seems like an excellent academic solution to the problem, I worry that adoption in practice may be unlikely because of the divergence from existing workflows. It makes me wonder if a more practical approach would be to embed the DSL directly in Python and expose it this way instead of authoring a standalone compiler.

### Questions

- What is the benefit of this approach to data science efficiency over the current model in which data science code is iterated-into-existence with the help of interactive notebooks and data subsets?
- What subset of the functionality of Safe-DS could be achieved by a Python embedded DSL?

### Further Reading

- Achieving Guidance in Applied Machine Learning through Software Engineering Techniques (2020)
- API Design for Machine Learning Software: Experiences from the scikit-learn Project (2013)
- A Preliminary Survey on Domain-Specific Languages for Machine Learning in Big Data (2016)
- How do Data Science Workers Collaborate? Roles, Workflows, and Tools (2020)