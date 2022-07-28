OpenJDK17:
```-XX:ThreadPriorityPolicy=1```


GraalVM 22:
```-XX:JVMCIThreads=8 -XX:JVMCIHostThreads=8```
See here for more: https://chriswhocodes.com/graalvm_ee_only_jdk17_options.html


Both:
```-XX:AllocatePrefetchStyle-3 -XX:+AlignVector -XX:+UseFastStosb -XX:+RelaxAccessControlCheck -XX:+OptoScheduling -XX:+OptoBundling -XX:+OptimizeFill -XX:+AlwaysCompileLoopMethods -XX:+AlwaysActAsServerClassMachine -XX:+ AllowParallelDefineClass```
