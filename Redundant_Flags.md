These flags (among others) are enabled by default on Adoptium and GraalVM Java 17 CE/EE.

```-XX:+UseStringDeduplication -XX:+UseAES -XX:+UseAESIntrinsics -XX:AllocatePrefetchStyle=1 -XX:+UseLoopPredicate -XX:+RangeCheckElimination -XX:+EliminateLocks -XX:+DoEscapeAnalysis -XX:+UseCodeCacheFlushing -XX:+UseFastJNIAccessors -XX:+OptimizeStringConcat -XX:+UseCompressedOops -XX:+UseThreadPriorities -XX:+OmitStackTraceInFastThrow -XX:+UseInlineCaches  -XX:+RewriteBytecodes -XX:+RewriteFrequentPairs -XX:+UseFPUForSpilling -XX:+UseNewLongLShift -XX:+UseXMMForArrayCopy -XX:+UseXmmI2D -XX:+UseXmmI2F -XX:+UseXmmLoadAndClearUpper -XX:+UseXmmRegToRegMoveAll -XX:+UseNewLongLShift```


Hence they are removed from the Java 17 Graal flags, but I will leave them in the "general" Java flags, as not all Java distributions enable them.

Many of the `dgraal` options are redundant as well, but these are left in for ease of testing, in case one of the compiler options breaks a mod. 
