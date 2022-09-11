## Hyrise Re-engineered: An Extensible Database System for Research in Relational In-Memory Data Management (2019)

Markus Dreseler, Jan Kossmann, Martin Boissier, Stefan Klauck, Matthias Uflacker, and Hasso Plattner.

Available [here](https://openproceedings.org/2019/conf/edbt/EDBT19_paper_152.pdf).

### Big Idea

Prioritize developer productivity and extensibility for a research database system.

### Summary

The authors present the architecture of the database management system _Hyrise_, an open-source research system designed for HTAP workloads. In addition to the system architecture, they describe some of the lower-level, practical steps they have taken to ensure that working in the system is productive, even for developers that are new to the project.

### Commentary

I read this paper because it seems like the authors may be in a situation that is similar to what we experience with the NoisePage project. Like us, the authors are building a research system in which multiple orthogonal lines of research effort are concurrently active. I know that this is something that we struggle with in NoisePage, so I was curious as to the steps this team has taken to ease some of this pain.

The first important observation the authors make is that the growing complexity of a codebase with multiple ongoing research projects quickly becomes an impediment to future research. As new features are added, the system as a whole becomes more difficult to understand, increasing the barrier to entry for new developers. I know that I felt completely overwhelmed when I first started working on NoisePage because there is so much going on in the system. After gaining some more experience with the code this feeling went away, but the issue is the time that is wasted (in some sense) trying to construct a sufficiently-accurate mental model of the system such that one can contribute meaningful work. Our goal is to reduce the duration of this period.

Hyrise implements an interesting design wherein many of the novel features that come out of research work may be selectively enabled and disabled. This allows developers to test the impact of their own new additions in isolation, without losing the results in the "noise" of an overly-complex system with too many state-of-the-art features.

One thing the authors of Hyrise prioritize is the ability to run benchmarks. They endeavor to make it extremely simple to run integrated benchmarks by preparing them as standalone binaries that:
- Load the benchmark data
- Run the benchmark
- Dump the results to a file

This is an awesome feature to have. I know from experience that benchmarking, when not made a priority, can be a painful process. Furthermore, when it is not standardized in this way, it might lead to issues of inconsistent benchmark results as different developers may perform the benchmark differently. This is definitely a feature worth investing more time into.

A small observation that the authors make is that the use of `std::shared_ptr` and its reference counting behavior is OK in most scenarios, and that only when they observe the reference counting becoming a bottleneck do they look for lower-overhead approaches to memory management. I found this interesting because `std::shared_ptr` is one of the few "banned types" in NoisePage, and I wonder if this is a result of superstition or we actually observed that it was a bottleneck.

Hyrise exposes 3 distinct interfaces to the system:
- Custom CLI
- Postgres wire protocol
- C++ API

The first two are unsurprising. However, the third, a well-defined C++ API, would be a major improvement to NoisePage. Currently, it seems like we have test and benchmarks that "jump in" to the system at arbitrary locations, limited only by the access control of various components. 

The Hyrise execution engine follows a relatively-standard procedure:
- AST
- Logical Query Plan
- Physical Query Plan
- Evaluation

The authors describe how they take steps to ensure that every intermediate representation of the query is easily-inspectable. In my experience, this is absolutely crucial to efficient development of new features. Furthermore, I believe this was one of the primary goals of the LLVM intermediate representation (i.e. why it has a textual representation in the first place).

Hyrise distinguishes between the database system core and _plugins_ that add additional functionality but are external to the core. Plugins are implemented as dynamic libraries that can be loaded and unloaded at runtime with the help of a new system component - the Plugin Manager. I love this idea, and I wonder how much of the DBMS core can be pushed out to plugins. This seems like it would make development of orthogonal components within the context of the same system much simpler.

### Questions

N/A

### Further Reading

- Self-Driving Database Management Systems (2017)
- Query Compilation in PostgreSQL by Specialization of the DBMS Source Code (2017)
