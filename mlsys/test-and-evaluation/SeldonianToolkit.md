## Seldonian Toolkit: Building Software with Safe and Fair Machine Learning (2023)

Austin Hoag, James E. Kostas, Bruno Castro da Silva, Philip S. Thomas, and Yuriy Brun.

Available [here](todo).

### Big Idea

Provide a means for developers to express certain model constraints in an ergonomic way and subsequently automatically train a model that meets these constraints.

### Summary

The key observation of this paper is that there is a disconnect between users of ML systems, software engineers, and data scientists. This disconnect leads to failures of these systems in the real world.

The authors propose the seldonian toolkit as a response to this problem. The toolkit provides practitioners with a method to specify requirements and subsequently evaluate seldonian models with respect to these requirements.

The tool provides a GUI that assists in the process of developing requirements for seldonian models. Users utilize the tool to input, for instance, fairness constraints in terms of the mathematical properties that are required to achieve them. 

The seldonian engine is the core of the toolkit. This is a library that accepts the constraints specified in the GUI, a model, and a dataset on which to train it. Internally, it trains this model to satisfy the given constraints. It provides probabilistic guarantees that, in the event it returns a model, the model satisfies the constraints.

The seldonian experiments library is a support library that allows developers to compare the models produced by the seldonian engine with a "standard" baseline. This allows them to evaluate the tradeoffs of achieving their fairness constraints.

### Commentary

The toolkit proposed in this paper takes an approach that is similar to MLTE - that of "bridging the gap" between ML development and system integration. However, it seems significantly more limited in scope - deeper but less broad. That said, in order to make MLTE "competitive" with approaches like this one, we need to provide a similar level of depth in our implementation.

### Questions

N/A

### Further Reading

- Preventing Undesirable Behavior of Intelligent Machines (2019)