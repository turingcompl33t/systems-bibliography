## Re-using Deep Neural Network Models through Model Re-engineering (2023)

Binhang Qi et al.

Available [here](todo).

### Big Idea

Apply model re-engineering to trained deep neural networks in order to produce new models that retain performance while drastically reducing the number of weights required to implement the model.

### Summary

The authors propose model re-engineering as a means of reusing neural networks while reducing the overhead of reuse and minimizing defect inheritance.

The authors achieve model re-engineering via a search-based approach that locates neurons of interest that pertain to the target problem. This approach is distinct from neuron-coverage based approaches in that it is directly informed by the target objective. 

The general workflow for model re-engineering is:

- Apply the re-engineering search procedure to a trained model, producing a new model
- Fine-tune the re-engineered model on the target problem

In the evaluation, on average, the re-engineering approach reduces the number of weights by 90%.

### Commentary

N/A

### Questions

N/A

### Further Reading

- Model Reuse Attacks on Deep Learning Systems (2018)
- Decomposing Convolutional Neural Networks into Reusable and Replaceable Modules (2022)
