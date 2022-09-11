## Goods: Organizing Google's Datasets (2016)

Alon Halevy, Flip Korn, Natalya F. Not, Christopher Olston, Neoklis Polyzotis, Sudip Roy, Steven Euijong Whang.

Available [here](https://research.google/pubs/pub45390/).

### Big Idea

Perform post-hoc indexing of datasets within an enterprise setting to improve developer productivity through dataset discoverability.

### Summary

The critical distinction between Goods and other EDM systems is that it is intended to operate in a post-hoc manner - users generate datasets without regard for the indexing process, and after the fact Goods allows other users to find this dataset efficiently.

A critical feature of Goods is that it provides a unified view of datasets across the enterprise - it is storage system agnostic.

Goods also provides provenance tracking. This allows users to visualize the lineage of a particular dataset in terms of upstream and downstream datasets.

The challenges the authors faced when building Goods include:
- The large number of datasets (billions)
- The size of datasets (GBs to TBs)
- The diversity of storage systems and storage formats

Challenge: It is infeasible to index metadata for all datasets at Google when the number of such datasets exceeds 26 billion
- Solution: prioritize datasets and visit these first

Challenge: Dataset aliasing occurs when a particular "logical" dataset is present in multiple physical locations e.g. a Bigtable table with column families, backed by GFS.
- Solution: Goods deals with each of these aliasing issues on a class-basis - e.g. they have a solution for BigTable, a solution for Dremel, etc.

Goods provides dataset clustering. This groups several "physical" datasets into a single "logical" dataset for more efficient search by consumers and more efficient metadata collection by Goods.

The Goods catalog is implemented on top of BigTable.

### Commentary

I love this quotation from the first paragraph:

> by allowing engineers and data scientists to consume and generate datasets in an unfettered manner, enterprises promote fast development cycles, experimentation and ultimately innovation

The fact that Google was able to solve this problem on the scale that they did makes me hopeful for the future prospects in my organization. It is unlikely that our scale will come close to what Google had to contend with here.

There is a great idea introduced in passing in this paper - that of a dataset TTL. Presumably, we can tag a dataset with a TTL as a final step of its production. This allows a tool like Goods to know whether a dataset that it comes across is a transient dataset produced as a side-effect of a larger pipeline, or is a persistent dataset that is worth indexing.

Another critical component mentioned in passing is the presence of log files. The Goods system relies on logs to perform much of the work that it does to add value e.g. provenance information. Without logs, Goods would not be possible. Therefore, in an organization, we must be vigilant about writing useful, consistent logs.

### Questions

- What are examples of enterprises data management (EDM) tools that might be used in place of Goods? Might this just be a centralized metadata database where all data sources are centrally indexed?
- How is the process of datasets prioritization performed? What methods are used to optimize this process?

### Further Reading

- Bigtable: A distributed storage system for structured data