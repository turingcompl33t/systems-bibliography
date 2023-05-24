## Guidance in Applied Machine Learning through Software Engineering Techniques

Lars Reimann and Gunter Kniesel-Wunsche

Available [here](todo).

### Big Idea

Propose a unified ecosystem of tools and specifications to apply software engineering principles to machine learning workflows and automate best practices.

### Summary

The authors contend that better guidance is required to help developers make use of machine learning.

The authors superimpose common software engineering tasks over a typical machine learning workflow. At each step, they specify the desirable guidance that should be available. 

The authors identify that the machine learning workflow is supported by:

- high level APIs
- dynamic languages
- dynamic development environments

For high level APIs, the authors identify the following criticisms:

- Hidden and inconsistent constraints in API documentation
- Lack of constraint checking and helpful error messages
- No checking of ML best practices
- No static checking

The authors criticize the use of Python for machine learning workflows because it makes static checking difficult. 

For ML IDEs, the authors identify the following criticisms:

- No support for data engineering
- No support for introspection
- No experiment management

As an antidote to these criticisms, the authors propose the Simple ML project. The project is based on a unified IDE, machine learning APIs, and a domain-specific language. The project addresses both low-level concerns (e.g. static typing) as well as machine learning best practices.

### Commentary

The authors state that the power and flexibility of Python is not necessary for most machine learning workflows. This is how they justify the reduction in flexibility that comes with their approach. It is an interesting point - for which use-cases is this true, and where is it false?

### Questions

- Is better guidance the answer, in the long run? Or are technologies like AutoML going to make this type of work obsolete?

### Further Reading

- Simple-ML: Towards a Framework for Semantic Data Analytics Workflows (2019)
