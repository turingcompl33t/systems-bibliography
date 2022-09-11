## Orthogonal Optimization of Subqueries and Aggregation (2001)

Cesar Galindo-Legaria and Milind Joshi.

Available [here](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.563.8492&rep=rep1&type=pdf).

### Big Idea

Use a set of small, independent optimization primitives to achieve flexible coverage of the strategies typically employed to optimize subquery evaluation and aggregations.

### Summary

The authors present a set of optimization strategies for subquery and aggregation evaluation. Instead of proposing distinct, "specific" optimizations tailored for each pattern, the authors present a number of small, independent optimization techniques that achieve many of the same ends while providing better coverage of the optimization search space.

### Commentary

The primary focus of this paper is on the optimization of correlated subqueries, typically by removing the subquery and translating it into a `JOIN`, thereby "flattening" the query. This has direct ramifications for work on UDF optimization because the flattening process they describe (especially as they get into the details of the `APPLY` operator and its usage) appears applicable to the types of queries that are produced by the Froid framework.

The authors describe how some of the overhead that is elided by subquery optimization comes in the form of removing context switch overhead between scalar and relational processing systems. This paper is twenty years old at the time of this writing, yet they already realized this fundamental issue that leads to the poor performance of UDFs!

### Questions

N/A

### Further Reading

- The Cascades Framework for Query Optimization (1995)
- The Volcano Optimizer Generator: Extensibility and Efficient Search (1993)
