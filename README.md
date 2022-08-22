Benchmarks
------

Flags are tested with Benchmark.py script. See [Benchmarks.md](https://github.com/brucethemoose/Minecraft-Performance-Flags-Benchmarks/blob/main/Benchmarks.md).

Discord: https://discord.gg/zeFSR9PnUw

GraalVM EE has a consistent 20% chunkgen speedup over OpenJDK 17, see the `Benchmarks` folder. But testing is in progress, more results are coming soon(TM).

Base Java Flags
------
These optimized flags, when added to garbage collection flags, will work with any Java 17+ build: 

```-server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -Dsun.rmi.dgc.server.gcInterval=2147483646 -Djdk.nio.maxCachedBufferSize=262144 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+UseStringDeduplication  -XX:+UseFastUnorderedTimeStamps -XX:+UseCriticalCompilerThreadPriority -XX:+UseCriticalJavaThreadPriority```

They are applicable to both servers and clients. Barring some *minor* differences in default flags, all Java distributions perform almost identically, with 2 major exceptions I am aware of: Oracle's GraalVM (which has a custom C2 compiler), and Intel's (linux-only, highly optimized binary) Clear Linux OpenJDK, which you can get through [distrobox](https://github.com/89luca89/distrobox).


Memory Allocation
------
Minimum and maximum (`-xms` and `-xmx`) values should generally be set to the same value, as explained here: https://dzone.com/articles/benefits-of-setting-initial-and-maximum-memory-siz

Allocating too much memory can make GC pauses much more severe, or overflow out of your physical RAM. Allocating too little can slow the game down. Less than 8GB is usually sufficient, but experiment with your mod loadout, and give Minecraft only as much as it needs.


Garbage Collection
------

Garbage Collection tuning is critical for both Minecraft servers and clients, as the "pauses" to stop and collect garbage manifest as stutters on the client and lag on servers. To minimize them, you have a few options. 

- **Multicore Collection**: More parallel collection can be done on all garbage collectors with `-XX:ConcGCThreads=[Some Number]`. I set it to `[number of physical cores - 1]`, but this may or may not work on your system. 

- **ZGC**: If you have RAM and cores to spare, and regular OpenJDK, use ZGC. On an 8-core test laptop, it has *no* throughput hit over G1GC, and absolutely no pausing/stutters on the server or client. `-XX:+UseZGC -XX:ZAllocationSpikeTolerance=4` enables it, and doubles the "spike tolerance" to handle more rapid in-game changes. Allocate more `Xmx` and more `ConcGCThreads` than you normally would, but set your `-Xms` value lower than `-Xmx`, as otherwise Java sometimes spits out warnings. 

- **G1GC on clients**: G1GC is fine for GraalVM users (Who have [no other option](https://github.com/oracle/graal/issues/2149)), and regular OpenJDK users on resource constrained computers. [Aikar's famous arguments](https://aikar.co/2018/07/02/tuning-the-jvm-g1gc-garbage-collector-flags-for-minecraft/) work well, but have a major issue: they effectively [disable](https://www.oracle.com/technical-resources/articles/java/g1gc.html) the `MaxGCPauseMillis` parameter. Without the "newsize" parameters, we end up with: `-XX:MaxGCPauseMillis=17 -XX:GCPauseIntervalMillis=21 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=23 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=3 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1` "MaxGCPauseMillis" is our pause target (with a 1 frame lag at 60FPS being ~17ms), and GCPauseIntervalMillis has to be higher than that.

- **G1GC on servers**: Longer pauses are not so catastrophic on servers, and do increase throughput:  `-XX:MaxGCPauseMillis=100 -XX:GCPauseIntervalMillis=2 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=23 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=3 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1`  (with 100ms being 2 ticks) 

- **Shenandoh**: All combinations of Shenandoh tested so far have a significant performance penalty. However, if you are a Java 8 user who can't run Graal EE 21 for some reason, Red Hat builds Java 8 with Shenandoah: https://access.redhat.com/products/openjdk

Large Pages
------

Enabling large pages improves the performance of Minecraft servers and clients. Chaotica Fractals has a great explanation, and a tutorial for enabling it in Windows: https://www.chaoticafractals.com/manual/getting-started/enabling-large-page-support-windows

Another windows/linux tutorial here: https://kstefanj.github.io/2021/05/19/large-pages-and-java.html

On Windows, you **must** run java, and your launcher, as an administrator. That means checking the ["run as administrator" compatibility checkbox](https://support.sega.com/hc/en-us/articles/201556551-Compatibility-Mode-and-Running-as-Administrator-for-PC-Games) for `javaw.exe`, `java.exe` and `your launcher.exe`, otherwise Large Pages will silently fail. Add `-XX:+UseLargePages -XX:LargePageSizeInBytes=2m` to your arguments.  

On linux, you generally want to use `-XX:+UseTransparentHugePages`. But if you want to manually allocate some server memory for Minecraft, Red Hat has a good tutorial for RHEL-like linux distros, like Fedora, CentOS, or Oracle Linux: https://www.redhat.com/en/blog/optimizing-rhel-8-run-java-implementation-minecraft-server 


GraalVM Enterprise Edition
------

GraalVM is a new high performance Java VM from Oracle that can improve the performance of (modded) Minecraft.

Unfortunately, only GraalVM Enterprise Edition comes with the full set of optimizations, and downloading it requires making a free Oracle account.

Register and download it here: https://www.oracle.com/downloads/graalvm-downloads.html

Grab the newest "Oracle GraalVM Enterprise Edition Core" release available for Java 17+ from the "Archives" section. Unzip it, and put the unzipped folder somewhere safe.

Again, you *must* use 22.1.0, not 22.2.0.

These releases are not Java installers. You need to manually replace your launcher's version of Java, or use a Minecraft launcher that supports specifying your Java path. I recommend PolyMC, ATLauncher, or GDLauncher. When specifying a java path, navigate to the "bin" folder in the GraalVM download and use "javaw.exe" or "java.exe"

For servers, you need to replace the "java" command in your server start sh/bat file with the full path to graalvm java, in quotes.

If you don't feel comfortable making an Oracle account, grab the latest [GraalVM CE release](https://github.com/graalvm/graalvm-ce-builds/releases) and use the flags from above ^. But Oracle does not check the information you put into the registration page, and GraalVM CE lacks most of the EE optimizations.

GraalVM Java Arguments
------

These work for servers and clients, on any operating system and ARM/x86 hardware. They do not include the `xms` or `xmx` memory flags.

Client arguments for GraalVM EE 22+ for Java 17+ (or Java 11):

``` -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+UseG1GC -XX:+AlwaysPreTouch -Dlibgraal.AlwaysPreTouch=true -XX:+ParallelRefProcEnabled -Dlibgraal.ParallelRefProcEnabled=true -XX:+ExplicitGCInvokesConcurrent -Dlibgraal.ExplicitGCInvokesConcurrent=true -XX:MaxGCPauseMillis=17 -Dlibgraal.MaxGCPauseMillis=17 -Dlibgraal.GCPauseIntervalMillis=20 -XX:GCPauseIntervalMillis=20 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=25 -Dlibgraal.G1ReservePercent=25 -XX:G1HeapWastePercent=5 -Dlibgraal.G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -Dlibgraal.G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -Dlibgraal.InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=2 -Dlibgraal.G1RSetUpdatingPauseTimePercent=2 -XX:SurvivorRatio=32 -Dlibgraal.SurvivorRatio=32 -Dsun.rmi.dgc.server.gcInterval=2147483646 -Djdk.nio.maxCachedBufferSize=262144 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -XX:AllocatePrefetchStyle=3  -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+UseStringDeduplication  -XX:+UseFastUnorderedTimeStamps -XX:+UseCriticalCompilerThreadPriority -XX:+UseCriticalJavaThreadPriority -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true```

Raise `-XX:MaxGCPauseMillis=17 -Dlibgraal.MaxGCPauseMillis=17` And remove `-Dlibgraal.GCPauseIntervalMillis=20 -XX:GCPauseIntervalMillis=20` on servers.

Many of the `Dgraal` arguments are redundant/default, and there for easy testing. Again, you must use G1GC when running GraalVM CE or EE. 


Mod Compatibility
------
- GraalVM 22.2.0 has issues with Minecraft, particularly with the `UsePriorityInlining` flag enabled. Please use 22.1.0 until 22.3.0 is out see: https://github.com/oracle/graal/issues/4776

- Some flags, including `VectorizeSIMD`, turn villagers and some passive mobs invisible when running shaders through Iris or Occulus... but only after some time. If this happens to you, disable `VectorizeSIMD`. If that doesn't work, please try disabling other flags and create or add to a Github issue! See: https://github.com/oracle/graal/issues/4775

- GraalVM CE and EE both break constellation rendering in Astral Sorcery, unless JVCMI is disabled. See: https://github.com/HellFirePvP/AstralSorcery/issues/1963

If you run into any issues, please create a Github issue or post in the Discord!


Java 8
------
Java 8 is not being tested thoroughly. But these flags + g1gc flags should work in OpenJDK 8 builds:

```-server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+UseStringDeduplication -XX:+UseFastUnorderedTimeStamps -XX:+UseAES -XX:+UseAESIntrinsics -XX:AllocatePrefetchStyle=1 -XX:+UseLoopPredicate -XX:+RangeCheckElimination -XX:+EliminateLocks -XX:+DoEscapeAnalysis -XX:+UseCodeCacheFlushing -XX:+UseFastJNIAccessors -XX:+OptimizeStringConcat -XX:+UseCompressedOops -XX:+UseThreadPriorities -XX:+OmitStackTraceInFastThrow -XX:ThreadPriorityPolicy=1 -XX:+UseInlineCaches -XX:+RewriteBytecodes -XX:+RewriteFrequentPairs -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseFPUForSpilling -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.CompilerConfiguration=community -Dgraal.SpeculativeGuardMovement=true```

x86 Java 8 users (aka most Java 8 users) can add these additional arguments:

```-XX:+UseNewLongLShift -XX:+UseXMMForArrayCopy -XX:+UseXmmI2D -XX:+UseXmmI2F -XX:+UseXmmLoadAndClearUpper -XX:+UseXmmRegToRegMoveAll -XX:+UseNewLongLShift```

While these flags work with GraalVM EE 21.X:

```-server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch  -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:+UseStringDeduplication -XX:+UseFastUnorderedTimeStamps -XX:AllocatePrefetchStyle=1 -XX:+UseLoopPredicate -XX:+RangeCheckElimination -XX:+EliminateLocks -XX:+DoEscapeAnalysis -XX:+UseCodeCacheFlushing -XX:+UseFastJNIAccessors -XX:+OptimizeStringConcat -XX:+UseCompressedOops -XX:+UseThreadPriorities -XX:+OmitStackTraceInFastThrow -XX:ThreadPriorityPolicy=1 -XX:+UseInlineCaches -XX:+RewriteBytecodes -XX:+RewriteFrequentPairs -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseFPUForSpilling -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true```

Mod Compatibility
------
- GraalVM 22.2.0 has issues with Minecraft, particularly with the `UsePriorityInlining` flag enabled. Please use 22.1.0 for now, see: https://github.com/oracle/graal/issues/4776

- Some flags, including `VectorizeSIMD`, turn villagers and some passive mobs invisible when running shaders through Iris or Occulus... but only under certain unknown conditions. Disable this, otherwise you may have to roll back to OpenJDK, see https://github.com/oracle/graal/issues/4775

- GraalVM CE and EE both break constellation rendering in Astral Sorcery, unless JVCMI is disabled. See: https://github.com/HellFirePvP/AstralSorcery/issues/1963

If you run into any issues, please create a Github issue!

SpecialK
------
A Windows program called SpecialK has 2 major performance benefits to Minecraft:

- A frame limiter that's even better than RTSS, eliminating the need for Vsync (especially on setups without access to Sodium's adaptive vsync.

- A OpenGL-to-DirectX wrapper called OpenGL-IK that eliminates Minecraft's windowed moded overhead, and enables other features (like SpecialK's HDR injection).

Download it here: https://wiki.special-k.info/en/SpecialK/Tools

Enable the service. Then navigate to your java bin folder, and create an emtpy file called `SpecialK.OpenGL32` 

Other Performance Notes
------

- Some users report improved performance from running Minecraft at a high priority, via the task manager on Windows or `sudo nice -n -18 java...` on linux. The `Benchmark.py` script does this automatically.

- Minecraft linux users should check out https://github.com/Admicos/minecraft-wayland


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
- https://research.spec.org/icpe_proceedings/2014/p111.pdf
- https://www.diva-portal.org/smash/get/diva2:1466940/FULLTEXT01.pdf