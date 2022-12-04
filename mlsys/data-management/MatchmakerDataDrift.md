## Matchmaker: Data Drift Mitigation in Machine Learning for Large-Scale Systems (2022)

Ankur Mallick, Kevin Hsieh, Behnaz Arzani, and Gauri Joshi.

Available [here](https://proceedings.mlsys.org/paper/2022/hash/1c383cd30b7c298ab50293adfecb7b18-Abstract.html).

### Big Idea

Data drift leads to performance degradations in ML systems that power datacenter applications. Dynamically select the model that serves a particular request at runtime based on how the distribution of its training batch matches the distribution from which the incoming sample is pulled.

### Summary

Novelty of Matchmaker:
- Limited overhead at runtime
- Adapts to data drift without waiting for a new batch of ground truth labels
- Addresses both types of data drift (virtual and real)

The key technique in Matchmaker is to select the model that was trained on the batch of data that is more similar to the current, incoming example. The model that performs inference is dynamically determined for each incoming inference request.

The mechanism used to select a batch at test time is a combination of two factors: 
- A random forest model. The model is trained on all available examples (at train time) with _T_ leaf nodes representing the _T_ batches of training data. At inference time, the incoming example is processed through this random forest to select the batch that has the closest _spatial nearness_ to the incoming example. This is used to compute the _covariate shift_ score.
- The _concept drift_ score is computed merely as a decreasing order of accuracy on the most recent batch across all models.

The two scores are combined, and the model that corresponds to the batch with the highest score is selected for inference.

The key characteristic of this model selection procedure is that it is fast and can therefore scale to the low inference latency that is required in a production setting in a datacenter.

### Commentary

This paper is not about managing data drift issues for ML applications that run _in the datacenter_, rather it is about addressing issues that arise in ML applications that run _as part of the datacenter_. This is more interesting - using ML to optimize the datacenter. I need to look into these types of use cases more.

The sample applications for this paper are cool:
- A network incident response reporter that routes incident reports to the correct team
- A system that predicts the resource utilization of a VM based on the characteristics of the request that will generate it (how? what are the features?)

The authors state that the solution to data drift must satisfy three properties:
- Scalability: it must scale to operate at the level of applications that matter to a datacenter
- Adaptability: it must adapt to drifts even before new ground truth labels are present
- Flexibility: it must be able to work across different types of models and "drifts"

It is amazing that they are able to claim the "scalability" of this approach - it appears that no engineering has gone into this to make it scalable! They claim scalability merely on the basis of the algorithmic complexity of the approach - inference latency does not depend on number of training examples, batch size, number of features, etc. In the back, they just use the `RandomForestClassifier` from `sklearn` combined with some additional math written in Python to combine the scores.

### Questions

N/A

### Further Reading

- FirePlace: Placing Firecracker Virtual Machines with Hindsight Imitation (2020)
- Continuous Training for Production {ML} in the Tensorflow Extended ({TFX}) platform (2019)