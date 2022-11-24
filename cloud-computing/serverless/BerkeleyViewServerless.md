## Cloud Programming Simplified: A Berkeley View on Serverless Computing (2019)

Eric Jonas, Johann Schleier-Smith, Vikram Sreekanti, Chia-Che Tsai, Anurag Khandelwal, Qifan Pu, Vaishaal Shankar, Joao Carreira, Karl Krauth, Neeraja Yadwadkar, Joseph E. Gonzalez, Raluca Ada Popa, Ion Stoica, and David A. Patterson.

Available [here](https://arxiv.org/abs/1902.03383).

### Big Idea

Serverless is the cloud-computing sub-paradigm of the future, but advances need to be made across several domains related to the technology in order to realize this dream.

### Summary

The authors summarizes the following three (3) distinguishing features of serverless computing:

1. Decoupled computation and storage
2. Executing code without managing resource allocation
3. Paying in proportion to the resources used instead of for resources allocated

The authors summarize many attractive features of serverless computing throughout the paper. Some of these include:
- Higher resource utilization potential for cloud providers
- Lower barrier to entry for cloud users
- Cost savings for cloud users
- New opportunities for optimization of a new cloud abstraction

The authors describe several limitations of current serverless implementations:
- Inadequate storage for fine-grained operations 
- Lack of fine-grained coordination (e.g. among functions)
- Poor performance for standard communication patterns
- (Un)predictable performance (harder to provide performance guarantees)

The authors describe features that should be developed for serverless computing to enable it to become the new abstraction of choice:
- Add a way to express data dependencies among function instances. This might be accomplished via manual description by users, by profiling performed by the cloud provider, or by exposing the internal computation graph from popular distributed computing frameworks (e.g. expose the underlying graph from Spark RDD)
- Design an ephemeral storage solution for sharing data among cloud functions within a single application invocation. An example might be a high-performance distributed memory service.
- Design a durable storage solution for sharing data among cloud function application invocations.
- Design a distributed coordination service for efficiently sending messages between cloud functions.
- Minimize the startup time for individual function instances. This might be achieved by reducing the 1) function runtime startup time, 2) the programming library startup time, or 3) the application-specific startup time.
- Take advantage of high level programming abstractions to increase performance. This might be achieved through hardware-software codesign or through use of domain-specific architectures.

### Commentary

The authors make the following analogy, which I love:

> serverful computing is like programming in low-level assembly language whereas serverless computing is like programming in a higher-level language such as Python.

The analogy runs through on so many levels. With serverful computing, users must handle low-level steps like resource acquisition (register allocation) and release. Serverless computing abstracts these steps away.

The authors claim that _decoupled computation and storage_ is a distinguishing characteristic of serverless computing, but this is not limited to serverless applications. Indeed, any application I build, regardless of the cloud resources on which it is built, would demonstrate decoupling of these two types of resources. Furthermore, I would add another item to the list of distinguishing features: a finer-grained unit of accounting, relative to serverful offerings.

The authors compare backend-as-a-service offerings like S3 to domain-specific, highly-optimized implementations of serverless computing. Cloud functions are then the general-purpose instantiation of serverless.

### Questions

- How difficult would it be to extract the internal computation graph from a distributed compute framework and expose this to a cloud function framework?
- Is there a unified way to express a computation graph for this purpose? i.e. a product-agnostic method that could allow portability between the distributed computation framework and the cloud function runtimes? What would the nature of this "language" be?
- What performance improvements can we expect from capitalizing on this style of optimization?

### Further Reading

- A New Golden Age for Computer Architecture (2019)
- Pocket: Elastic Ephemeral Storage for Serverless Analytics (2018)
- The RAMCloud Storage System (2015)
- FaRM: Fast Remote Memory (2014)
- Autoscaling Tiered Cloud Storage in Anna (2019)
