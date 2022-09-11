## Magpie: Python at Speed and Scale using Cloud Backends

Alekh Jindal, K. Venkatesh Emani, Maureen Daum, Olga Poppe, Brandon Haynes, Anna Pavlenko, Ayushi Gupta, Karthik Ramachandra, Carlo Curino, Adnreas Mueller, Wantao Wu, and Hiren Patel.

Available [here](http://cidrdb.org/cidr2021/papers/cidr2021_paper08.pdf).

### Big Idea

The cloud data analytics ecosystem is too complex. Simplify it by introducing a middleware that provides a common interface and optimization opportunities.

### Summary

The authors introduce Magpie, a middleware for "unified" data analytics in the cloud. Magpie works by introducing a standard API for anlytical operations, modeled on the Pandas dataframe API, and mapping operations expressed in this API to various cloud backends. Magpie intelligently determines the backend that is most appropriate for a given operation (or set of operations?) with a decision tree classifier.

### Commentary

The authors identify four key enablers for bridging the gap between Python analytics and cloud workloads:
- An ongoing effort to standardize the Python APIs for data
- Many dataframe operations can be mapped to relational algebra expressions
- A shift from _polystores_ to _polyengines_ that all operate on a common set of data stored in a data lake
- Emergence of a common data format in Apache Arrow (for in-memory analytics? transfer?)

Users (data scientists) interact with Magpie through a Python module. The module then provides a dataframe interface that appears identical to Pandas.

### Questions

N/A

### Further Reading

- DBridge: Translating Imperative Code to SQL (2017)
- Extracting Equivalent SQL from Imperative Code in Database Applications (2016)
- Froid: Optimization of Imperative Programs in a Relational Database (2017)
