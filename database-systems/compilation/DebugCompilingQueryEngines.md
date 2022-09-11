## On Another Level: How to Debug Compiling Query Engines (2020)

Timo Kersten and Thomas Neumann.

Available [here](http://www.db.in.tum.de/~kersten/codegen_debugger.pdf).

### Big Idea

Combine a standard program debugger with a time-travel debugger and a custom extension to efficiently implement a multi-level debugger for compiling query engines.

### Summary

The authors present a way to "hack together" a multi-level debugger for compiling query engines. The approach utilizes a standard interactive debugger (e.g. `gdb`) combined with a time-travel debugger (e.g. Mozilla's RR debugger) in two distinct debugging sessions. The approach proceeds (roughly) as follows:
- Run code generation, recording a trace for the time travel debugger
- Attach the standard debugger to the code produced by the code generation system (this might be native code, but in the case of the paper they use Umbra IR, a modified version of LLVM IR)
- Locate an offending line in the generated code, note the instruction pointer
- Use the custom extension for the time travel debugger to place a breakpoint in the code generation source at the location where the offending line (in the generated code) is produced; this is the "secret sauce" of this technique
- Use the time travel feature to re-run code generation up to the point where the breakpoint is hit; we now have the full context of the code generator (in the time travel debugging session) at the point the offending line of generated code is produced

### Commentary

I use the term "hack together" in the above summary because the mutli-level debugger implementation presented in this paper really makes use of existing tools, albeit in an intelligent way. This is not to say this paper is not informative or the technique is not useful. Indeed, the fact that anyone (myself included) can replicate this technique in our own code generation system is a major advantage of this approach to the problem.

The approach in this paper is very similar to the approach to multi-level profiling explored in the _Profiling Dataflow Systems on Multiple Abstraction Levels_ paper - perhaps unsurprising because it comes from the same group. Furthermore, the root problem is the same: the multi-stage nature of the code generation engine implies that the link between source locations in each stage is lost, if not manually preserved. This is what tailored profiling fixes in the _Dataflow Systems_ paper, and what the two concurrent debugging sessions achieve in this paper - a way to "link" the stages of the code generator together. 

The authors note that the LB2 team from _How to Architect a Query Compiler, Revisited_ get an elegant solution to this same problem "for free" with their approach to query compilation. I need to revisit this paper to determine precisely how their approach to code generation gets you debuggability; the best I can remember is that it relies heavily on Lightweight Modular Staging to perform code generation, and I'm not quite sure how this helps the debugging experience (over a traditional code generator).

### Questions

- What would be the engineering effort involved in adding first-class debugging support to the TPL virtual machine?

### Further Reading

- Making Compiling Query Engines Practical (2019)
- Umbra: A Disk-Based System with In-Memory Performance (2020)
