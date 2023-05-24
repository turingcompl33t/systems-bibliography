## A Framework for Designing Foundation Model Based Systems (2023)

Qinghua Lu , Liming Zhu, Xiwei Xu, Zhenchang Xing, Jon Whittle

Available [here](todo).

### Big Idea

### Summary

The authors propose a taxonomy with three categories:

- Foundation model pre-training and fine-tuning
- Architecture and design of foundation model based systems
- Responsible AI by design

In the pre-training and fine-tuning category, a major design decision is the manner in which a domain-specific foundation model is achieved. The authors distinguish between a sequential approach in which general foundation models are subsequently pre-training on domain data, and a parallel approach in which the model is trained on both general and domain-specific data at the same time.

Fine-tuning for foundation models can be accomplished in a number of ways, including in-context learning, parameter fine-tuning, and knowledge distillation.

The authors propose several distinct roles that foundation models can play within an AI system: connector, coordinator, converter, and facilitator.

### Commentary

In April 2023, a large number of influential AI researchers signed a petition to halt progress on building foundation models larger than GPT-4. This is a really interesting event that I didn't know about. I wonder if it is a first in the history of AI research, of if similar moratoriums have been proposed in the past.

Foundation models are analogous to the cloud computing revolution:

- With standard AI models, organizations design, build, and train their own models. This imposes a high up-front cost in the time and effort required to curate training data and train the model itself.
- In contrast, with foundation models, organizations can pay only for what they use by way of the foundation model API. We can effectively outsource the model development to another organization. 
- "AI-as-a-service"

The authors describe the use of a "vector database" as a means of incorporating internal knowledge with an existing foundation model. I am not familiar with this technology. 

### Questions

N/A

### Further Reading

- Llama: Open and Efficient Foundation Language Models
- Palm-E: An embodied multimodal language model
