OpenJDK17:
- ```-XX:ThreadPriorityPolicy=1```


GraalVM 22:
- ```-XX:JVMCIThreads=8 -XX:JVMCIHostThreads=8```


Both:
- ```-XX:AllocatePrefetchStyle-3 -XX:+AlignVector -XX:+UseFastStosb -XX:+RelaxAccessControlCheck -XX:+OptoScheduling -XX:+OptoBundling -XX:+OptimizeFill -XX:+AlwaysCompileLoopMethods -XX:+AlwaysActAsServerClassMachine```
- Various G1GC changes
- Most of the current option, non-gc related flags