## Towards Responsible AI in the Era of ChatGPT: A Reference Architecture for Designing Foundation-Model Based AI Systems (2023)

Qinghua Lu, Liming Zhu, Xiwei Xu, Zhenchang Xing, Jon Whittle

Available [here](todo).

### Big Idea

Foundation models will fundamentally change the relevant architecture for machine learning systems. Employ a reference architecture for systems that utilize foundation models to ensure that AI components are utilized responsibly and in a way that maximizes the quality of the user experience.

### Summary

The authors define a foundation model as:

> massive AI models that are pre-trained on vast amounts of broad data and can be adapted to perform a wide variety of tasks

Foundation models offer unique challenges in that they are black boxes. The implicit argument here is that we have existing methods that are capable of illuminating aspects of non-foundation models, but that these techniques cannot be extended to foundation models. Furthermore, foundation models provide so much functionality that they will likely absorb the functionality provided by suites of today's models, implying a "moving boundary."

The authors describe the development of AI system architectures:

- Currently, architectures consist of many AI components (models) and many non-AI components.
- Next, architectures will consist of some AI components, a single foundation model serving as a "connector", and many non-AI components.
- In the future, architectures will consist of a foundation model that absorbs all AI components and most non-AI components. These foundation models may be monolithic or implemented as a chain.

One of the large design considerations when working with foundation models is the source of the data on which it is pre-trained. The authors stress the tradeoff between efficient training via specialized organizations and privacy issues.

The foundation model reference architecture proposes a three-tiered approach that includes the system layer, the supply-chain layer, and the operations layer.

### Commentary

The authors claim that future architectures will consist of foundation models that absorb most non-AI software components. Is this predicated on the fact that the model is so large that it can implement an arbitrarily complex function that implements any software task? If so, how is this model specified?

### Questions

N/A

### Further Reading

- On the Opportunities and Risks of Foundation Models (2021)
- Palm-E: An Embodied Multimodal Language Model (2023)