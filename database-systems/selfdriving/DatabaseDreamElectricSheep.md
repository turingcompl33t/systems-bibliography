## Make Your Database System Dream of Electric Sheep: Towards Self Driving Operation (2021)

Andrew Pavlo, Matthew Butrovich, Lin Ma, Prashanth Menon, Wan Shen Lim, Dana Van Aken, and William Zhang.

Available [here](http://vldb.org/pvldb/vol14/p3211-pavlo.pdf).

### Big Idea

Building a self-driving database management system requires that we consider the requirements of autonomous components in the design and implementation of the rest of the system. Make the self-driving nature of the system a first-order concern.

### Summary

The authors present their ideas regarding the design of a self-driving database management system. The contributions of the paper are:
- A taxonomy of self-driving database systems
- A high-level description of the self-driving architecture of the NoisePage system
- An itemization of design principles that enable self-driving operation

### Commentary

The design principles for self-driving operation compose the majority of this paper. With these principles, the authors help us answer the question "how might we make our database dream of electric sheep?" or "what are aspects of the system that we need to consider, outside of the self-driving architecture itself, to enable self-driving operation?"

A quick rundown of the principles that stand out to me:
- Maintain a workload history with queries, transactions, and various metadata about each
- Maintain an accurate estimation of current hardware capabilities to ensure that metrics are accurate
- Make configuration knows amenable to automatic tuning (e.g. explicitly mark those that are untunable[like file paths], expose an acceptable range of values for each knob)
- Do not introduce dependencies between actions deployed by self-driving operation
- Maintain a log of each action deployment to track outcomes over time
- Do not require downtime or a restart of the system to deploy actions

### Questions

- What is the overall overhead associated with self-driving operation? For instance, the authors describe the importance of maintaining a workload history (for the workload forecasting component of the system); what is the overhead of maintaining this workload history? Obviously there are some intelligent things that can be done to lessen the overhead (e.g. compression techniques, sampling, aggregation) but at the end of the day, how much are we actually paying for self-driving operation? Are we willing to pay this much?

### Further Reading

- Query-Based Workload Forecasting for Self-Driving Database Management Systems (2018)
- MB2: Decomposed Behavior Modeling for Self-Driving Database Management Systems (2021)
- Self-Driving Database Management Systems (2017)
- External vs. Internal: An Essay on Machine Learning Agents for Autonomous Database Management Systems (2019)
- Automatic Database Management System Tuning Through Large-scale Machine Learning (2017)
