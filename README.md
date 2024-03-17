This is a guide to tune Java for Minecraft. Every flag and tweak is individually benchmarked to test for regressions, and checked against Java defaults to avoid redundancy.

While these tweaks notably reduce some server and client stutters, expect only modest TPS gains + minimal FPS gains at best, and somewhat increased RAM + CPU usage. And they are no substitute for clearing laggy things out with mods like [Spark](https://spark.lucko.me/docs/guides/Finding-lag-spikes) or [Observable](https://github.com/tasgon/observable). 

Discord for questions and such: https://discord.gg/zeFSR9PnUw, also feel free to make an issue.

## Downloads for Spark & Observable:
Spark: [Spark's Website](https://spark.lucko.me/download) or [Modrinth](https://modrinth.com/mod/spark) or [CurseForge](https://www.curseforge.com/minecraft/mc-mods/spark)

Observable: [Modrinth](https://modrinth.com/mod/observable) or [CurseForge](https://www.curseforge.com/minecraft/mc-mods/observable)

<br />
<br />

TL:DR
======
### Client: 
| JREs:        | 
| ------------ | 
| Adoptium 17  | 
| GraalVM 17   |

| Garbage Collectors: |
| ------------------- | 
| G1GC                |
| Shenandoah          |

### Server: 
| JREs:          |
| -------------- |
| Adoptium |
| Clear Linux 17 |
| GraalVM 17     |

| Garbage Collectors: |
| ------------------- | 
| G1GC                |
| ZGC                 |

<br />

Don't forget to add memory arguments and if you are on Linux you can also use Large Pages. 

**<ins>DO NOT USE</ins> Large Pages on windows unless you understand the risks associated, more information in the [Large Pages](#large-pages) section**

Don't forget Performance Mods! [Performance Mods](#performance-mods)

<br />
<br />

Benchmarks
======

~~All flags are tested with Benchmark.py script. See the work-in-progress [Benchmarks.md](https://github.com/brucethemoose/Minecraft-Performance-Flags-Benchmarks/blob/main/Benchmarks.md).~~

Note: I do not test my flags anymore for reasons, though they still are very similar to @brucethemoose's

<br/>

Launchers
======
It is important to note that the launcher you use may influence the behavior of how you input your java arguments/flags. 

### Linux
When using Linux with Flathub's Prism Launcher your default permissions may prevent the launcher from accessing your entire custom Java directory which may cause the Java executable to fail to launch.

In order to fix this, you must use Flatseal, or you can manually change the permissions, so that Prism launcher can access the entire directory of where you put Java.

<br/>

Picking a Java Runtime
======
Java runtimes from Azul, Microsoft, Adoptium, Amazon and so on are basically identical. Some notable exceptions:

- **Oracle GraalVM** features a more aggressive Java compiler. This is what I personally run Minecraft with, see the GraalVM section below.

- **Intel's Clear Linux OpenJDK** uses the same code as any other OpenJDK (making it highly compatible), but the build process itself and the dependencies are [optimized for newer CPUs](https://www.phoronix.com/review/zen4-clear-linux/2). Grab it from Clear Linux's repos via `swupd`, from [Distrobox](https://github.com/89luca89/distrobox), or from [Docker](https://hub.docker.com/r/clearlinux/openjdk). Note that you must roll back to the Java 17 release, and that Java 18 [reverts some of the performance enhancements](https://github.com/clearlinux-pkgs/openjdk/commit/14202e83f919643031cfb7a6318b067310be90f1). 

- **Azul's Prime OpenJDK** is *very* fast since it hooks into llvm, but its currently incompatible with most mods and is linux-only. Get it from here: https://docs.azul.com/prime/prime-quick-start-tar

- **Red Hat Java 8** has the Shenandoah garbage collector. You can download it by going to [Adoptium Marketplace](https://adoptium.net/marketplace/), swapping java version to "8 - LTS", and downloading the Red Hat Build.

- **IBM's OpenJ9** is... *much* slower in Minecraft, and uses totally different flags than any other Java build, but it does consume less memory than OpenJDK-based runtimes. See [FAQ](#FAQ), the [Benchmarks folder](Benchmarks), and [this Gist for low memory consumption flags](https://gist.github.com/FluffyFoxUwU/69f8f156feefae3d826ad0d15c694002).

If you dont know what to pick, I recommend GraalVM 17 (see below) or the latest Adoptium Java 17 JRE: https://adoptium.net/

You can also go here for recommendations: https://whichjdk.com - Though it says to use Java 21, use the list below to ensure Minecraft runs correctly, this website is for general advice on JDKs, it is not made specifically for Minecraft
- **Minecraft 1.17 and above require Java 17 to run correctly**
- **Minecraft 1.16 mods may work with Java versions above 8 but the base game will run just fine**
- **Minecraft 1.15 and below require Java 8 to run correctly**

<br />

~~Couleur also maintains a good (but somewhat outdated) running list of JREs here: https://rentry.co/JREs~~ 
> Sadly, It got removed, here's a wayback machine link if you need it: https://web.archive.org/web/20231023145734/https://rentry.co/JREs
<br/>

Base Java Flags
======
These optimized flags run with any Java 11+ build. They work on both servers and clients:


```
-XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysActAsServerClassMachine -XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:NmethodSweepActivity=1 -XX:ReservedCodeCacheSize=400M -XX:NonNMethodCodeHeapSize=12M -XX:ProfiledCodeHeapSize=194M -XX:NonProfiledCodeHeapSize=194M -XX:-DontCompileHugeMethods -XX:MaxNodeLimit=240000 -XX:NodeLimitFudgeFactor=8000 -XX:+UseVectorCmov -XX:+PerfDisableSharedMem -XX:+UseFastUnorderedTimeStamps -XX:+UseCriticalJavaThreadPriority -XX:ThreadPriorityPolicy=1 -XX:AllocatePrefetchStyle=3
```

**You *must* add garbage collection flags to these java arguments.**  


<details>
    <summary>For example, if we were to use Java 21 with GraalVM's Java Arguments and G1GC, it would something look like this:</summary>

``
-Xms8G -Xmx8G -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysActAsServerClassMachine -XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:AllocatePrefetchStyle=3 -XX:NmethodSweepActivity=1 -XX:ReservedCodeCacheSize=400M -XX:NonNMethodCodeHeapSize=12M -XX:ProfiledCodeHeapSize=194M -XX:NonProfiledCodeHeapSize=194M -XX:-DontCompileHugeMethods -XX:+PerfDisableSharedMem -XX:+UseFastUnorderedTimeStamps -XX:+UseCriticalJavaThreadPriority -XX:+EagerJVMCI -XX:+UseG1GC -XX:MaxGCPauseMillis=37 -XX:+PerfDisableSharedMem -XX:G1HeapRegionSize=16M -XX:G1NewSizePercent=23 -XX:G1ReservePercent=20 -XX:SurvivorRatio=32 -XX:G1MixedGCCountTarget=3 -XX:G1HeapWastePercent=20 -XX:InitiatingHeapOccupancyPercent=10 -XX:G1RSetUpdatingPauseTimePercent=0 -XX:MaxTenuringThreshold=1 -XX:G1SATBBufferEnqueueingThresholdPercent=30 -XX:G1ConcMarkStepDurationMillis=5.0 -XX:G1ConcRefinementServiceIntervalMillis=150 -XX:GCTimeRatio=99
``

<b>DONT COPY THESE!</b>
<b>Please use the [TL:DR](#tl:dr) located above</b>


</details>

<br/>

Memory Allocation
======
Minimum and maximum (`-xms` and `-xmx`) memory should be set to the same value, as explained here: https://dzone.com/articles/benefits-of-setting-initial-and-maximum-memory-siz

One exception: if you are on a low-memory system, and Minecraft takes up almost all your RAM, set your minimum memory below your maximum memory to conserve as much as possible.

Sizes are set in megabytes (`-Xms4096M`) or gigabytes (`-Xmx8G`)

Allocating too much memory can break gc or just slow Minecraft down, even if you have plenty to spare. Allocating too little can also slow down or break the game. Keep a close eye on the Windows Task manager (or your DE's system monitor) as Minecraft is running, and allocate only as much as it needs (which is usually less than 8G). `sparkc gcmonitor` will tell you if your allocation is too high (the pauses will be too long) or too low (frequent GC with a low memory warning in the notification).

<br/>

Garbage Collection
======

**Garbage collection flags must be added to Minecraft servers and clients**, as the default "pauses" to stop and collect garbage manifest as stutters on the client and lag on servers. Use the `/sparkc gcmonitor` command in the [Spark](https://www.curseforge.com/minecraft/mc-mods/spark) mod to observe pauses in-game. *Any* old generation pauses are bad, and young generation G1GC collections should be infrequent, but short enough to be imperceptible.  

<br/>

### ZGC 

ZGC is great for high memory/high core count servers. It has no server throughput hit I can measure, and absolutely does not stutter. However, it requires more RAM and more cores than other garbage collectors. Enable it with
```
`-XX:+UseZGC -XX:AllocatePrefetchStyle=1 -XX:-ZProactive
```

Unfortunately, it has a significant client FPS hit on my (8-core/16 thread) laptop. See the "ZGC" benchmark in the benchmarks folder. Its not available in Java 8, and much less performant in Java 11 than in Java 17.

> Note: Allocate more RAM and more `ConcGCThreads` than you normally would for other GC, also note that ZGC does not like AllocatePrefetchStyle=3, hence setting it to 1 overrides the previous entry.


<br/>

### Shenandoah

Shenandoah performs well on clients, but kills server throughput in my tests. Enable it with 
```
-XX:+UseShenandoahGC -XX:ShenandoahGCMode=iu -XX:ShenandoahGuaranteedGCInterval=1000000 -XX:AllocatePrefetchStyle=1
```

See more tuning options [here](https://wiki.openjdk.org/display/shenandoah/Main). The "herustic" and "mode" options don't change much for me (except for "compact," which you should not use). 

> Note:  that Shenandoah is not in Java 8. Its also not in any Oracle Java builds! If you are a Java 8 user, you must use Red Hat OpenJDK to use Shenandoah. Like ZGC, Shenandoah does not like AllocatePrefetchStyle=3.

Download Links:
 - [Red Hat Developer](https://developers.redhat.com/products/openjdk/download)
 - [Adoptium Marketplace](https://adoptium.net/marketplace/)

<br/>

### Client G1GC

G1GC is the default garbage collector for all JREs. Aikar's [famous Minecraft server G1GC arguments](https://aikar.co/2018/07/02/tuning-the-jvm-g1gc-garbage-collector-flags-for-minecraft/) run great on clients, with two caveats: they effectively [clamp](https://www.oracle.com/technical-resources/articles/java/g1gc.html) the `MaxGCPauseMillis` parameter by setting `G1NewSizePercent` so high, producing long stutters on some clients, and they collect oldgen garbage too aggressively (as the client produces *far* less than a populated server). 

These are similar to the aikar flags, but with shorter, more frequent pauses, less aggressive G1 mixed collection and more aggressive background collection: 
```
-XX:+UseG1GC -XX:MaxGCPauseMillis=37 -XX:+PerfDisableSharedMem -XX:G1HeapRegionSize=16M -XX:G1NewSizePercent=23 -XX:G1ReservePercent=20 -XX:SurvivorRatio=32 -XX:G1MixedGCCountTarget=3 -XX:G1HeapWastePercent=20 -XX:InitiatingHeapOccupancyPercent=10 -XX:G1RSetUpdatingPauseTimePercent=0 -XX:MaxTenuringThreshold=1 -XX:G1SATBBufferEnqueueingThresholdPercent=30 -XX:G1ConcMarkStepDurationMillis=5.0 -XX:GCTimeRatio=99 -XX:G1ConcRefinementServiceIntervalMillis=150 -XX:G1ConcRSHotCardLimit=16
```

> NOTE: Java 21 depreciated the `G1ConcRefinementServiceIntervalMillis` flag and the `-XX:G1ConcRSHotCardLimit=16` flag, remove them when using Java 21 as they aren't needed

> Note: `G1NewSizePercent` and `MaxGCPauseMillis` can be used to tune the frequency/dureation of your young generation collections. `G1HeapWastePercent=18` should be removed if you are getting any old generation pauses on your setup. Alternatively, you can raise it and set `G1MixedGCCountTarget` to 2 or 1 to make mixed garbage collection even lazier (at the cost of higher memory usage). 

<br/>

### Server G1GC

Longer pauses are more acceptable on servers. These flags are very close to the aikar defaults:

```
-XX:+UseG1GC -XX:MaxGCPauseMillis=130 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=28 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=20 -XX:G1MixedGCCountTarget=3 -XX:InitiatingHeapOccupancyPercent=10 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=0 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1 -XX:G1SATBBufferEnqueueingThresholdPercent=30 -XX:G1ConcMarkStepDurationMillis=5 -XX:G1ConcRefinementServiceIntervalMillis=150 -XX:G1ConcRSHotCardLimit=16
```

> NOTE: Java 21 depreciated the `G1ConcRefinementServiceIntervalMillis` flag and the `-XX:G1ConcRSHotCardLimit=16` flag, remove them when using Java 21 as they aren't needed

<br/>

### Garbage Collection Threading

`-XX:ConcGCThreads=[Some Number]` controls the [*maximum* number](https://github.com/openjdk/jdk/blob/dd34a4c28da73c798e021c7473ac57ead56c9903/src/hotspot/share/gc/z/zHeuristics.cpp#L96-L104) of background threads the garbage collector is allowed to use, and defaults to `logical (hyperthreaded) cores / 4`. Recent versions of Java will [reduce the number of gc threads, if needed](https://wiki.openjdk.org/display/zgc/Main#Main-SettingConcurrentGCThreads).

In some cases (especially with ZGC or Shenandoh) you want to increase this thread cap past the default. I recommend `[number of real cores - 2]` on most CPUs, but you may need to play with this parameter. If its too low, garbage collection can't keep up with Minecraft, and the game will stutter and/or start eating gobs of RAM and crash. If its too high, it might slow the game down, especially if you are running Java 8. 

No other "threading" flags like `ParallelGCThreads` or `JVMCIThreads` are necessary, as they are enabled by default with good automatic settings in Java 8+.

<br/>

Large Pages
======
**NOTE: Large Pages requires admin privileges on Windows. This is a security risk, and you should skip this section if you aren't comfortable with that.**

Enabling large pages improves the performance of Minecraft servers and clients by reducing the load on your system. Here are some great tutorials for enabling it:

- Windows 10 Pro: https://www.chaoticafractals.com/manual/getting-started/enabling-large-page-support-windows
- Windows 10 Home: https://awesomeprojectsxyz.blogspot.com/2017/11/windows-10-home-how-to-enable-lock.html?m=1
- Tool mirrors for the W10 Home tutorial: https://gist.github.com/eyecatchup/0107bab3d92473cb8a3d3547848fc442
- Linux: https://kstefanj.github.io/2021/05/19/large-pages-and-java.html



On Windows, you **must** run java, and your launcher, as an administrator. That means checking the ["run as administrator" compatibility checkbox](https://support.sega.com/hc/en-us/articles/201556551-Compatibility-Mode-and-Running-as-Administrator-for-PC-Games) for `javaw.exe`, `java.exe` and `your launcher.exe`, otherwise Large Pages will silently fail. Add `-XX:+UseLargePages -XX:LargePageSizeInBytes=2m` to your arguments.  

On linux, you generally want to use `-XX:+UseTransparentHugePages`. To have the kernel automatically allocate memory instead (for a bigger performance boost), Red Hat has a good tutorial for RHEL-like linux distros, like Fedora, CentOS, or Oracle Linux: https://www.redhat.com/en/blog/optimizing-rhel-8-run-java-implementation-minecraft-server 

Check and see if large pages is working with the `-Xlog:gc+init` java argument in Java 17. 

In any Java version/platform, if large pages isn't working, you will get a warning in the log similar to this: 

`Java HotSpot(TM) 64-Bit Server VM warning: JVM cannot use large page memory because it does not have enough privilege to lock pages in memory.`

<br/>

GraalVM
======

GraalVM is a new Java VM from Oracle that can improve the performance of (modded and vanilla) Minecraft. While client FPS gains are modest, server-side workloads like chunk generation can get a 20%+ boost!

Download it from [graalvm.org](https://www.graalvm.org/downloads/) or [oracle.com](https://www.oracle.com/java/technologies/downloads/)

These releases are not Java installers, they are portable zips. You need to unzip and manually replace your launcher's version of Java, or use a Minecraft launcher that supports specifying your Java path. I recommend ATLauncher, Prism Launcher or GDLauncher. When specifying a java path, navigate to the "bin" folder in the GraalVM download and use "javaw.exe" or "java.exe". 

For servers, you need to replace the "java" command in your server start sh/bat file with the full path to graalvm java, in quotes.

Alternatively, you can install it system-wide by following Oracle's guide: https://www.graalvm.org/latest/docs/getting-started/

### GraalVM Java Arguments

Arguments for GraalVM Java 17+

```
-XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysActAsServerClassMachine -XX:+AlwaysPreTouch -XX:+DisableExplicitGC -XX:AllocatePrefetchStyle=3 -XX:NmethodSweepActivity=1 -XX:ReservedCodeCacheSize=400M -XX:NonNMethodCodeHeapSize=12M -XX:ProfiledCodeHeapSize=194M -XX:NonProfiledCodeHeapSize=194M -XX:-DontCompileHugeMethods -XX:+PerfDisableSharedMem -XX:+UseFastUnorderedTimeStamps -XX:+UseCriticalJavaThreadPriority -XX:+EagerJVMCI -Dgraal.TuneInlinerExploration=1
```

**You must use G1GC or ZGC with these arguments.** GraalVM currently doesn't work with Shenandoah.  

<br/>

### GraalVM Mod Compatibility

**GraalVM EE 22.3.0 fixed all known Minecraft bugs**

<details>
    <summary>If you run an older, Java 8-based version of GraalVM EE, there are some potential issues:</summary>

    - `VectorizeSIMD` turns entities invisible with shader mods like Optifine, Iris or Occulus... but only under certain conditions. This will be fixed in GraalVM EE 22.3.0. See: https://github.com/oracle/graal/issues/4849
    
    - GraalVM CE and EE both break constellation rendering in 1.16.5 Astral Sorcery. This is possibly related to the shader bug. See: https://github.com/HellFirePvP/AstralSorcery/issues/1963
    
    I have not observed any server-side bugs yet. 
    
    If you run into any other mod issues you can trace back to GraalVM, please create a Github issue or post in the Discord! Generally, you can work around them by disabling major `dgraal` optimization flags, or by finding the right function with `Dgraal.PrintCompilation=true`, and working around it with `-Dgraal.GraalCompileOnly=~...` once you find the miscompiled function.

</details>

<br/>

SpecialK
======
A "universal" Windows mod akin to [ReShade](https://reshade.me/), SpecialK has 2 major performance benefits:

- A "smart" frame limiter that reduces stutter, eliminates tearing, saves power, and saves CPU TDP to boost when needed. It even works in conjuction with VRR or Nvidia Reflex. 

- A OpenGL-to-DirectX11 wrapper called OpenGL-IK that eliminates Minecraft's windowed mode overhead, and enables other features (like auto-HDR or a resizable borderless window).

Download it here: https://wiki.special-k.info/en/SpecialK/Tools

Add your MC launcher, and check the "elevated service" checkbox. Then navigate to your java bin folder where your javaw.exe is, and create an empty file called `SpecialK.OpenGL32`. Launch your Minecraft launcher with the SpecialK launcher, and the launcher will then "inject" SpecialK into Minecraft.
![SpecialK](Tutorial_Images/specialk.PNG)

You can create a desktop shortcut to your Minecraft launcher through the SpecialK UI for even more convenience. 

Be sure to turn off VSync and the in-game Minecraft frame limiter.

One user has reported reduced FPS when running SpecialK. If this happens to you, please let me know through Discord or Github!

<br/>

Process Priority
======
After launching Minecraft, set Java to run at an "Above Normal" process priority in Windows with the Task Manager in the details tab:

![taskmanager](Tutorial_Images/taskmon.PNG)

Linux users can add  `sudo nice -n -10` to the beginning of the launch command, but note that nice levels below 0 (with the "max" being -20) require running Minecraft as `sudo`. Alternatively, use the `renice` command after launching Minecraft to avoid this security risk.

<br/>

Performance Mods
======

This is a **fantastic** repo for finding performance mods: https://github.com/TheUsefulLists/UsefulMods

Instead of Optifine, I would recommend more compatible alternatives like [Sodium](https://modrinth.com/mod/sodium) + [Iris](https://modrinth.com/mod/iris) for Fabric/Quilt and [Embeddium](https://modrinth.com/mod/embeddium) + [Oculus](https://modrinth.com/mod/oculus) for Forge/NeoForge.

<br/>

Java 8
======

I recommend using Java 17 or, failing that, Java 11 unless 8 is absolutely necessary. But if it is, these flags will work with OpenJDK8, along with Shenandoh GC (for Red Hat OpenJDK on clients) or G1GC (for everything else):

```
-XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysActAsServerClassMachine -XX:+ParallelRefProcEnabled -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:+PerfDisableSharedMem -XX:+AggressiveOpts -XX:+UseFastAccessorMethods -XX:MaxInlineLevel=15 -XX:MaxVectorSize=32 -XX:+UseCompressedOops -XX:ThreadPriorityPolicy=1 -XX:+UseDynamicNumberOfGCThreads -XX:NmethodSweepActivity=1 -XX:ReservedCodeCacheSize=350M -XX:-DontCompileHugeMethods -XX:MaxNodeLimit=240000 -XX:NodeLimitFudgeFactor=8000 -XX:+UseFPUForSpilling
```

x86 Java 8 users can add these additional arguments:

```
-XX:+UseXMMForArrayCopy
```

You can also get Java 8 versions of GraalVM EE from the [21.X section on the Oracle site](https://www.oracle.com/downloads/graalvm-downloads.html), and use these arguments:

```
-XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+AlwaysActAsServerClassMachine -XX:+ParallelRefProcEnabled -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:+AggressiveOpts -XX:+UseFastAccessorMethods -XX:AllocatePrefetchStyle=1 -XX:ThreadPriorityPolicy=1 -XX:+UseDynamicNumberOfGCThreads -XX:NmethodSweepActivity=1 -XX:ReservedCodeCacheSize=350M -XX:-DontCompileHugeMethods -XX:MaxNodeLimit=240000 -XX:NodeLimitFudgeFactor=8000 -XX:+UseFPUForSpilling -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true
```

Be sure to set `-Dgraal.VectorizeSIMD` to `false` if you run shaders.

<br/>

Other Performance Tips
======

- Run your Minecraft servers on Clear Linux! It's by far the most optimized linux distribution out-of-the-box, and it has some other nice features (like a stateless config system). It also runs clients on AMD/Intel GPUs quite well: https://web.archive.org/web/20220916090057/https://docs.01.org/clearlinux/latest/tutorials/multi-boot/dual-boot-win.html

- Oracle Linux is also a good choice for servers, since its reasonably well optimized out-of-the-box and has Graalvm EE available via the package manager. For clients, Arch-based distros like CachyOS or EndeavorOS are excellent, as they have wide support for most hardware.

- Make sure the Minecraft client is using your discrete GPU! Check the F3 tab, and force Minecraft to use it in the "**Windows Graphics Settings**", *not* the AMD/Nvidia control panel (as they don't seem to work anymore).

- Minecraft client linux users should check out https://github.com/Admicos/minecraft-wayland 

- Close everything in the background, including Discord, game launchers and your browser! Minecraft is resource intensive, and does not like other apps generating CPU interrupts or eating disk I/O, RAM and so on.  

- Server Owners can check this out, [YouHaveTrouble/minecraft-optimization](https://github.com/YouHaveTrouble/minecraft-optimization).

<br/>

FAQ
======

- Java versions above 17 have some mod incompatibilities. They reportedly work with most modpacks, but I'm not sure if there are any performance benefits outside of incubator flags (`--add-modules=jdk.incubator.vector`) which (I believe) are only supported on Minecraft Servers with explicit work like [Pufferfish](https://docs.pufferfish.host/optimization/how-to-apply-aikars-flags).).

- Java tweaks improve server performance and client stuttering, but they don't boost average client FPS much (if at all). For that, running correct/up-to-date graphics drivers and performance mods is far more important: https://github.com/TheUsefulLists/UsefulMods

- This guide assumes you have a little spare RAM when running Minecraft. If your setup is RAM constrained, try removing the following arguments in particular: 
```
-XX:NmethodSweepActivity=1 -XX:ReservedCodeCacheSize=400M -XX:NonNMethodCodeHeapSize=12M -XX:ProfiledCodeHeapSize=194M -XX:NonProfiledCodeHeapSize=194M
```
, and try the server G1GC arguments.

- IBM's OpenJ9 does indeed save RAM, as its reputation would suggest, but is over 30% slower at server chunkgen in my tests. If there are any flags that make it competitive with OpenJDK, please let me know on Discord or here: https://github.com/brucethemoose/Minecraft-Performance-Flags-Benchmarks/issues/9

<br/>

Flag Explanations
======
- Aikar G1GC flags are explained here: https://aikar.co/2018/07/02/tuning-the-jvm-g1gc-garbage-collector-flags-for-minecraft/
- `-XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions` simply unlock more flags to be used. These can be listed with the `-XX:+PrintFlagsFinal` and `-XX:+JVMCIPrintProperties` flags, see [Flag Dumps](Flag_Dumps)
- `-XX:G1MixedGCCountTarget=3`: This is how many oldgen gc blocks to target in "mixed" gc. These mixed collections are much slower, and the Minecraft client doesn't generate oldgen very quickly, so we can lower this value to 3, 2, or even 1 for shorter GC pauses.
- ~~`-XX:+UseNUMA` enables optimizations for multisocket systems, if applicable. Not sure if this applies to MCM CPUs like Ryzen or Epyc, but its auto disabled if not applicable.~~ Thanks to @draeath for explaining why we shouldn't do this as the BIOS may not expose NUMA domains correctly
- `-XX:-DontCompileHugeMethods` *Allows* huge methods to be compiled. Modded Minecraft has some of these, and we don't care about higher background compiler CPU usage.
- `-XX:MaxNodeLimit=240000 -XX:NodeLimitFudgeFactor=8000` Enable optimization of larger methods. See: https://bugs.java.com/bugdatabase/view_bug.do?bug_id=8058148
- `-XX:ReservedCodeCacheSize=400M -XX:NonNMethodCodeHeapSize=12M -XX:ProfiledCodeHeapSize=194M -XX:NonProfiledCodeHeapSize=194M` reserves more space for compiled code. All sections must "add up" to `ReservedCodeCacheSize`. I have observed modded Minecraft run into the default 250 megabyte limit with `XX:+PrintCodeCache`, but even if its not filled, the larger size makes eviction of compiled code less aggressive. 
- `-XX:NmethodSweepActivity=1` (default 10) keeps "cold" code in the cache for a longer time. There is no risk of "filling up" the code cache either, as cold code is more aggressively removed as it fills up. 
- ~~`-XX:+UseStringDeduplication`~~ This is a popular option, but not used here, as it's benching slower. Maybe its useful on low memory systems?  
- `-XX:+UseFastUnorderedTimeStamps` Avoid system calls for getting the time. The impact of this will vary per system, but we aren't really concerned with logging timestamp accuracy. 
- `-XX:+UseCriticalJavaThreadPriority` *Nothing* should preempt the Minecraft threads. GC and Compiler threads can wait. 
- `-XX:ThreadPriorityPolicy=1` Use a wider range of thread priorities. Requires sudo on linux to work. Some JDKs (like Graal) enable this by default, but some don't.
- `-XX:G1SATBBufferEnqueueingThresholdPercent=30 -XX:G1ConcMarkStepDurationMillis=5 -XX:G1ConcRefinementServiceIntervalMillis=150`: Optimizes G1GC's concurrent collection threads, still being tested: https://research.spec.org/icpe_proceedings/2014/p111.pdf
- `-XX:G1RSetUpdatingPauseTimePercent=0`: We want *all* this work to be done in the G1GC concurrent threads, not the pauses. 
- `-XX:G1HeapWastePercent=18` Don't bother collecting from old gen until its above this percent. This avoids triggering slower "mixed" young generation GCs, which is fine since Minecraft (with sufficient memory) doesn't fill the old gen that fast. Idea from: https://www.reddit.com/r/Minecraft/comments/k9zb7m/tuning_jvm_gc_for_singleplayer/
- `-XX:GCTimeRatio=99` As a goal, 1% of CPU time should be spent on garbage collection. Default is 12, which seems way too low. The default for Java 8 was 99.
- `-XX:AllocatePrefetchStyle=3` Generate one prefetch instruction per cache line. More aggressive prefetching is generally useful on newer CPUs with large caches. It seems to break ZGC. See: https://github.com/openjdk/jdk/blob/bd90c4cfa63ba2de26f7482ed5d1704f9be9629f/src/hotspot/share/opto/macro.cpp#L1806
- `-Dgraal.LoopRotation=true` A non default optimization, will probably be default soon. 
- `-Dgraal.TuneInlinerExploration=1` Spend more time making inlining decisions. For Minecraft, we want the C2 compiler to be as slow and aggressive as possible. 
- Most other `-Dgraal` arguments are enabled by default, and are either there as a sanity check, for debugging or as a failsafe (if, for instance, someone unknowingly disables JVCMI with some other flag). 
- Many Java 8 flags (such as `-XX:MaxInlineLevel=15 -XX:MaxVectorSize=32`) are just copied from the Java 17 defaults. Others (like `+AggressiveOpts`) are only non-default in some older Java 8 builds. 

<br/>

Flags Under Consideration
======
- More aggressive inlining, via `-Dgraal.BaseTargetSpending=160` (default 120) in Graal and some other flags in OpenJDK. CPUs with larger caches might benefit from this.
- OpenJDK flags which are disabled by default: `-XX:+AlignVector -XX:+OptoBundling -XX:+OptimizeFill -XX:+AlwaysCompileLoopMethods -XX:+EnableVectorAggressiveReboxing -XX:+EnableVectorSupport -XX:+OptoScheduling -XX:+UseCharacterCompareIntrinsics -XX:+UseCopySignIntrinsic -XX:+UseVectorStubs`
- ~~`-Dgraal.LSRAOptimization=true`~~ seems to hurt performance 
- `-Dgraal.OptWriteMotion=true` and `graal.WriteableCodeCache=true`, which *do not* seem stable, but may be more stable in GraalVM 22.3.0 
- Extreme `G1HeapWastePercent` values.

<br/>
 
Sources
======
- Updated Aikar flags from this repo: https://github.com/etil2jz/etil-minecraft-flags
- Reddit post from a Forge dev: https://www.reddit.com/r/feedthebeast/comments/5jhuk9/modded_mc_and_memory_usage_a_history_with_a/
- Red Hat's optimization guide: https://www.redhat.com/en/blog/optimizing-rhel-8-run-java-implementation-minecraft-server
- GraalVM release notes: https://www.graalvm.org/release-notes/
- Oracle's Java 17 Documentation: https://docs.oracle.com/en/java/javase/17/docs/specs/man/java.html
- VM Options explorer: https://chriswhocodes.com/
- Java itself, via the `-XX:+PrintFlagsFinal` and the `-XX:+JVMCIPrintProperties` flags to dump flag descriptions/defaults. 
- OpenJDK source: https://github.com/openjdk/jdk/
- Testing from @keyboard.tn in Discord.
- https://research.spec.org/icpe_proceedings/2014/p111.pdf
- https://www.diva-portal.org/smash/get/diva2:1466940/FULLTEXT01.pdf
- https://malloc.se/blog/zgc-jdk17
- https://docs.oracle.com/javase/8/embedded/develop-apps-platforms/codecache.htm
