Benchmarks
------

Flags are tested with the Benchmark.py script. See [Benchmarks.md](https://github.com/brucethemoose/Minecraft-Performance-Flags-Benchmarks/blob/main/Benchmarks.md).

GraalVM EE has a consistent 20% chunkgen speedup over OpenJDK 17, see the `Benchmarks` folder.

Minecraft Java Edition Flags
------
These optimized flags will work with any Java 17+ build: 

```-server -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+UseStringDeduplication -XX:+UseFastUnorderedTimeStamps -XX:AllocatePrefetchStyle=3 -XX:+OmitStackTraceInFastThrow -XX:+TrustFinalNonStaticFields -XX:ThreadPriorityPolicy=1 -XX:InlineSmallCode=1000 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.CompilerConfiguration=community -Dgraal.SpeculativeGuardMovement=true```

This subset works with Java 8:

```-server -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+UseStringDeduplication -XX:+UseFastUnorderedTimeStamps -XX:+UseAES -XX:+UseAESIntrinsics -XX:AllocatePrefetchStyle=1 -XX:+UseLoopPredicate -XX:+RangeCheckElimination -XX:+EliminateLocks -XX:+DoEscapeAnalysis -XX:+UseCodeCacheFlushing -XX:+UseFastJNIAccessors -XX:+OptimizeStringConcat -XX:+UseCompressedOops -XX:+UseThreadPriorities -XX:+OmitStackTraceInFastThrow -XX:+TrustFinalNonStaticFields -XX:ThreadPriorityPolicy=1 -XX:+UseInlineCaches -XX:+RewriteBytecodes -XX:+RewriteFrequentPairs -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseFPUForSpilling -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.CompilerConfiguration=community -Dgraal.SpeculativeGuardMovement=true```

x86 Java 8 users (aka most Java 8 users) can add these additional arguments:

```-XX:+UseNewLongLShift -XX:+UseXMMForArrayCopy -XX:+UseXmmI2D -XX:+UseXmmI2F -XX:+UseXmmLoadAndClearUpper -XX:+UseXmmRegToRegMoveAll -XX:+UseNewLongLShift```

These flags are applicable to both servers and clients. Most Java distributions are similar, except for a few extra optimizations in GraalVM CE, which you can [download here](https://github.com/graalvm/graalvm-ce-builds/releases).

But even more performance can be gained with the tweaks below:

GraalVM Enterprise Edition
------

GraalVM is a new high performance Java VM from Oracle that can improve the performance of (modded) Minecraft.

Unfortunately, only GraalVM Enterprise Edition comes with the full set of optimizations, and downloading it requires making a free Oracle account.

Register and download it here: https://www.oracle.com/downloads/graalvm-downloads.html

Grab the newest "Oracle GraalVM Enterprise Edition Core" release available for Java 17+ from the "Archives" section, or grab the latest GraalVM 21.X Java 8 for running old versions of Minecraft that explicitly require Java 8. Unzip it, and put the unzipped folder somewhere safe.

Again, you *must* use 22.1.0, not 22.2.0.

These releases are *not* Java installers. You need to manually replace your launcher's version of Java, or use a Minecraft launcher that supports specifying your Java path. I recommend ATlauncher, PolyMC, or GDLauncher. When specifying a java path, navigate to the "bin" folder in the GraalVM download and use "javaw.exe" or "java.exe"

For servers, you need to replace the "java" command in your server start sh/bat file with the full path to graalvm java, in quotes.

If you don't feel comfortable making an Oracle account, grab the latest [GraalVM CE release](https://github.com/graalvm/graalvm-ce-builds/releases) and use the flags from above ^. But Oracle does not check the information you put into the registration page, and GraalVM CE lacks most of the EE optimizations.

Large Pages
------

Enabling large pages can further improve the performance of Minecraft servers and clients, but requires launching Minecraft as an administrator. Chaotica Fractals has a great explanation, and a tutorial for enabling it in Windows: https://www.chaoticafractals.com/manual/getting-started/enabling-large-page-support-windows

You **must** run java [as an administrator](https://support.sega.com/hc/en-us/articles/201556551-Compatibility-Mode-and-Running-as-Administrator-for-PC-Games) on Windows, otherwise Large Pages will silently not work. 

Red Hat has a good tutorial for RHEL-like linux distros, like Fedora, CentOS, or Oracle Linux. Note that some linux users may have to change the value of`LargePageSizeInBytes`: https://www.redhat.com/en/blog/optimizing-rhel-8-run-java-implementation-minecraft-server

To skip this tweak, remove `-XX:+UseLargePages -XX:LargePageSizeInBytes=2m` from the end of the arguments below. 

GraalVM Java Arguments
------

These work for servers and clients, on any operating system and ARM/x86 hardware. They do not include the `xms` or `xmx` memory flags.

Arguments for GraalVM EE 22+ for Java 17+ (or Java 11):

```-server -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:+UseFastUnorderedTimeStamps -XX:AllocatePrefetchStyle=3 -XX:+TrustFinalNonStaticFields -XX:ThreadPriorityPolicy=1 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true -Dlibgraal.ExplicitGCInvokesConcurrent=true -Dlibgraal.AlwaysPreTouch=true -Dlibgraal.ParallelRefProcEnabled=true -XX:+UseLargePages -XX:LargePageSizeInBytes=2m```

Some experimental flags, but most of these are unstable under certain conditions:

```-Dlibgraal.WriteableCodeCache=true -Dgraal.VectorPolynomialIntrinsics=true -Dgraal.SIMDVectorizationSingletons=true -Dgraal.SIMDVectorizationDirectLoadStore=true -Dgraal.OptWriteMotion=true -Dgraal.LSRAOptimization=true -XX:JVMCIThreads=8```


Arguments for GraalVM EE 21 for Java 8 (only recommended for packs that absolutely require Java 8):

```-server -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1  -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:+UseStringDeduplication -XX:+UseFastUnorderedTimeStamps -XX:+UseAES -XX:+UseAESIntrinsics -XX:AllocatePrefetchStyle=1 -XX:+UseLoopPredicate -XX:+RangeCheckElimination -XX:+EliminateLocks -XX:+DoEscapeAnalysis -XX:+UseCodeCacheFlushing -XX:+UseFastJNIAccessors -XX:+OptimizeStringConcat -XX:+UseCompressedOops -XX:+UseThreadPriorities -XX:+OmitStackTraceInFastThrow -XX:+TrustFinalNonStaticFields -XX:ThreadPriorityPolicy=1 -XX:+UseInlineCaches -XX:+RewriteBytecodes -XX:+RewriteFrequentPairs -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseFPUForSpilling -XX:+UseXMMForArrayCopy -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -XX:+UseLargePages -XX:LargePageSizeInBytes=2m```

Memory Allocation
------
The minimum and maximum (`-xms` and `-xmx`) values should be set to the same value, as explained here: https://dzone.com/articles/benefits-of-setting-initial-and-maximum-memory-siz

Among other things, allocating too much memory can make GC pauses much more severe, while allocating too little can slow the game down. Give Minecraft only as much memory as your setup needs.   

Alternative Garbage Collection
------
- In OpenJDK, replacing the G1GC flags with `-XX:+UseZGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ZAllocationSpikeTolerance=5` has almost no performance hit compared to g1gc, at the cost of higher memory usage. More specific zgc flags are still being tested.

- All combinations of Shenandoh tested so far have a significant performance penalty. However, if you are a Java 8 user who can't run Graal EE 21 for some reason, Red Hat builds Java 8 with Shenandoah https://access.redhat.com/products/openjdk

- Ony G1GC works well with GraalVM. ZGC will disable JVMCI and most of Graal EE's performance optimizations. 

Mod Compatibility
------
- GraalVM 22.2.0 has issues with Minecraft, particularly with the `UsePriorityInlining` flag enabled. Please use 22.1.0 for now, see: https://github.com/oracle/graal/issues/4776

- `VectorizeSIMD` turns villagers and some passive mobs invisible when running shaders through Iris or Occulus... but only under certain unknown conditions. Disable this flag if you experience this, see https://github.com/oracle/graal/issues/4775

- GraalVM CE and EE both break constellation rendering in Astral Sorcery, unless JVCMI is disabled. See: https://github.com/HellFirePvP/AstralSorcery/issues/1963

I know of no other Graal mod incompatibilities, and I run 1.18.2 Forge/Fabric modpacks. If you run into any issues, please create a Github issue!


Performance Notes
------

- A Windows program called SpecialK can mitigate the impact of Minecraft's windowed mode and janky frame limiter. After installing it, create an empty `SpecialK.OpenGL32` file in you Java bin directory.

- Some users report improved performance from running Minecraft at a high priority, via the task manager on Windows or `nice -n -19 java...` on linux. The `Benchmark.py` script does this automatically.

- Minecraft linux users should check out https://github.com/Admicos/minecraft-wayland

- G1GC parameters like `MaxGCPauseMillis` and `G1HeapRegionSize` need more testing, given how divergent recommendations are. On clients, you can try decreasing `MaxGCPauseMillis` and increasing `XX:G1ReservePercent` (which allocates more memory to GC), but your mileage may vary.

- Many OpenJDK8 Flags are redundant/default in some distributions/versions. In addition, many of the `dgraal` flags are reduntant for testing ease of access.




Sources
------
- Updated Aikar flags from this repo: https://github.com/etil2jz/etil-minecraft-flags
- Reddit post from a Forge dev: https://www.reddit.com/r/feedthebeast/comments/5jhuk9/modded_mc_and_memory_usage_a_history_with_a/
- Red Hat's optimization guide: https://www.redhat.com/en/blog/optimizing-rhel-8-run-java-implementation-minecraft-server
- GraalVM release notes: https://www.graalvm.org/release-notes/
- Oracle's Java 17 Documentation: https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html
- VM Options explorer: https://chriswhocodes.com/
- Java itself, via the `-XX:+PrintFlagsFinal` and the `-XX:+JVMCIPrintProperties` flags to dump flag descriptions/defaults. 
- Testing from @keyboard.tn in Discord.
