## Pollux: Co-adaptive Cluster Scheduling for Goodput-optimized Deep Learning (2021)

Aurik Quia et al.

Available [here](https://www.usenix.org/system/files/osdi21-qiao.pdf).

### Big Idea

TODO

### Summary

Deep learning training needs to balance two metrics that are often in tension:

- System throughput, the number of examples processed per wall-clock time
- Statistical efficiency, the amount of training progress made per example 

Pollux performs adaptive scheduling of deep learning jobs by controlling several paramters:

- number of GPUS
- co-location of workers
- per-GPU batch size
- gradient accumulation
- learning rate scaling

### Commentary

TODO

### Questions

- How does Pollux model context switching costs when migrating deep learning jobs to new resources?

### Further Reading

TODO 
