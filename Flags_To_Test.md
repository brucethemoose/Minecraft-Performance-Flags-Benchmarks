OpenJDK17:

```-XX:ThreadPriorityPolicy=1````


GraalVM 22:
```-XX:JVMCIThreads=8 -XX:JVMCIHostThreads=8```


Both:
```-XX:AllocatePrefetchStyle-3 -XX:+AlignVector```
