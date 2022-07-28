These flags are enabled by default on Adoptium and Oracle Java 17, and should probably be removed:

```-XX:+UseStringDeduplication -XX:+UseAES -XX:+UseAESIntrinsics -XX:AllocatePrefetchStyle=1 -XX:+UseLoopPredicate -XX:+RangeCheckElimination -XX:+EliminateLocks -XX:+DoEscapeAnalysis -XX:+UseCodeCacheFlushing -XX:+UseFastJNIAccessors -XX:+OptimizeStringConcat -XX:+UseCompressedOops -XX:+UseThreadPriorities -XX:+OmitStackTraceInFastThrow -XX:+UseInlineCaches  -XX:+RewriteBytecodes -XX:+RewriteFrequentPairs -XX:+UseFPUForSpilling```

But in some cases, it may be useful to explicitly enable the flag in case something else tries to disable it?
