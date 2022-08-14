from difflib import restore
import os,time,shutil,glob,datetime,json,platform,signal,statistics,pprint,subprocess,csv,atexit
import pexpect 
import psutil  
from pexpect import popen_spawn





#----------------------------String Scratch Space----------------------------
#Create your strings to construct the benchmark here!


#Minecraft Paths

atm7 = r"C:/Games/atm7"

vev = r"C:/Games/mcservers/vevserver"

minfabric = r"C:/Games/mcservers/MinimalFabric"

minfabricpoly = r"C:/Games/PolyMC-Windows-Portable-1.4.0/instances/1.18.2"

#Java Paths

graalpath = r"F:/JDKs/graalvm-ee-java17-22.2.0/bin/java.exe"

jdkpath = r"F:/JDKs//OpenJDK17U-jre_x64_windows_hotspot_17.0.4_8/jdk-17.0.4+8-jre/bin/java.exe"

j9path = r"F:/JDKs/ibmopenj9/bin/java.exe"

gbackpath = r"F:/JDKs/graalvm-ee-java17-windows-amd64-22.1.0/graalvm-ee-java17-22.1.0/bin/java.exe"

#Java Flags
#(Should start with a space, so they can be "added" together with the + sign)

#GC
aikar = r''' -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1'''

#aikartweaks = r''' -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=20 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=32M -XX:G1ReservePercent=45 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1 -XX:+ExplicitGCInvokesConcurrent'''

aikarmegatweak = r''' -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=8 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=35 -XX:G1MaxNewSizePercent=45 -XX:G1HeapRegionSize=32M -XX:G1ReservePercent=38 -XX:G1HeapWastePercent=4 -XX:G1MixedGCCountTarget=1 -XX:InitiatingHeapOccupancyPercent=1 -XX:G1MixedGCLiveThresholdPercent=45 -XX:G1RSetUpdatingPauseTimePercent=4 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1 -XX:+ExplicitGCInvokesConcurrent -XX:GCPauseIntervalMillis=9 -XX:G1RSetUpdatingPauseTimePercent=10 -XX:G1ConcRSHotCardLimit=8 -XX:G1ConcRefinementServiceIntervalMillis=75'''

aikarlesstweak = r''' -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=16 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=38 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=2 -XX:InitiatingHeapOccupancyPercent=1 -XX:G1MixedGCLiveThresholdPercent=70 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1 -XX:+ExplicitGCInvokesConcurrent -XX:GCPauseIntervalMillis=17 -XX:G1RSetUpdatingPauseTimePercent=12 -XX:G1ConcRSHotCardLimit=8 -XX:G1ConcRefinementServiceIntervalMillis=150'''

shen1 = r''' -XX:+UseShenandoahGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ShenandoahGCMode=satb -XX:ShenandoahGCHeuristics=adaptive'''

shen2 = r''' -XX:+UseShenandoahGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ShenandoahGCMode=satb -XX:ShenandoahGCHeuristics=static'''

shen3 = r''' -XX:+UseShenandoahGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ShenandoahGCMode=satb -XX:ShenandoahGCHeuristics=compact'''

shen4 = r''' -XX:+UseShenandoahGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ShenandoahGCMode=iu -XX:ShenandoahGCHeuristics=adaptive'''

shen5 = r''' -XX:+UseShenandoahGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ShenandoahGCMode=iu -XX:ShenandoahGCHeuristics=static'''

shen6 = r''' -XX:+UseShenandoahGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ShenandoahGCMode=iu -XX:ShenandoahGCHeuristics=compact'''

z1 = r''' -XX:+UseZGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent'''

z2 = r''' -XX:+UseZGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ZAllocationSpikeTolerance=5'''

#flags
minimalgraal = r''' -server'''

somegraal = r''' -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+PerfDisableSharedMem -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:+UseNUMA -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true -Dlibgraal.ExplicitGCInvokesConcurrent=true -Dlibgraal.AlwaysPreTouch=true -Dlibgraal.ParallelRefProcEnabled=true'''

moregraal = r''' -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+PerfDisableSharedMem -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:+UseNUMA -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true -Dlibgraal.ExplicitGCInvokesConcurrent=true -Dlibgraal.AlwaysPreTouch=true -Dlibgraal.ParallelRefProcEnabled=true -XX:AllocatePrefetchStyle=3 -XX:-DontCompileHugeMethods -XX:ThreadPriorityPolicy=1'''

graal = r''' -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:+UseFastUnorderedTimeStamps -XX:AllocatePrefetchStyle=3 -XX:+TrustFinalNonStaticFields -XX:ThreadPriorityPolicy=1 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true -Dlibgraal.ExplicitGCInvokesConcurrent=true -Dlibgraal.AlwaysPreTouch=true -Dlibgraal.ParallelRefProcEnabled=true'''

ojdk = r''' -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+PerfDisableSharedMem -XX:+UseStringDeduplication -XX:+UseFastUnorderedTimeStamps -XX:AllocatePrefetchStyle=1 -XX:+OmitStackTraceInFastThrow -XX:+TrustFinalNonStaticFields -XX:ThreadPriorityPolicy=1 -XX:InlineSmallCode=1000 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.CompilerConfiguration=community -Dgraal.SpeculativeGuardMovement=true'''

experimental = r''' -XX:+EnableVectorAggressiveReboxing -XX:+EnableVectorReboxing -XX:+EnableVectorSupport -XX:+ExplicitGCInvokesConcurrent -XX:+OptimizeFill -XX:+OptoBundling -XX:+OptoScheduling -XX:+UseCharacterCompareIntrinsics -XX:+UseCopySignIntrinsic -XX:+UseCriticalCompilerThreadPriority -XX:+UseCriticalJavaThreadPriority -XX:+UseOptoBiasInlining -XX:+UseVectorStubs'''

lpages = r''' -XX:+UseLargePages -XX:LargePageSizeInBytes=2m'''

memory = r''' -Xms6G -Xmx6G'''

zmemory =r''' -Xms3G -Xmx9G'''

lightmemory = r''' -Xms4G -Xmx4G'''


#-----------------------Benchmark Data--------------------------
benchname = r"Test Client Benchmark"   #Name for the whole benchmark run

blist = [
#Note that Forge/Fabric packs only need "java + arguments" for their launch command, as their jars are automatically found
#Formatting for the benchmark data
#Benchmark name, Bechmark command (java + flags),server root directory, polymc instance name (only needed for client benchmarking), # of iterations to run this benchmark
  {
    "Name": "VeV", 
    "Command": gbackpath + moregraal + lightmemory + aikar + lpages,
    "Path": vev, 
    "PolyInstance": "Valhelsia- Enhanced Vanilla - 1.18",
    "Iterations":  3
  },
  {
    "Name": "Almost Vanilla", 
    "Command": gbackpath + moregraal + lightmemory + aikar + lpages,
    "Path": minfabric, 
    "PolyInstance": "1.18.2",
    "Iterations":  3
  }

]

#----------------------Other Options--------------------------

nogui = True     #Whether to run the dedicated server GUI or not
carpet = 60 #number of simulated players if the "Carpet" fabric mod is present
fabric_chunkgen_command = r"chunky start"                 #Chunk generation command to use in fabric packs
fabric_chunkgen_expect =  r"[Chunky] Task finished for"   #String to look for when chunk generation is finished
forge_chunkgen_command = r"forge generate 0 0 0 3000"     #Chunk generation command to use in forge packs
forge_chunkgen_expect =  r"Finished generating"           ##String to look for when chunk generation is finished
startuptimeout= 350 #Number of seconds to wait before considering the server to be dead/stuck
chunkgentimeout = 600 #Number of seconds to wait for chunk generation before considering the server to be dead/stuck 
totaltimeout = 1200 #Number of seconds the whole server can run before timing out. 
forceload_cmd= r"forceload add -100 -100 100 100" #Command to forceload a rectangle. Can also be some other server console command. 
debug = False #Print stages of when the server starts/runs

#Client benchmarking options (WIP NOT DONE YET)
client = True #Try to connect to the minecraft server with the specified PolyMC instance, if there is one
polypath = r"C:/Games/PolyMC-Windows-Portable-1.4.0/polymc.exe" #Full path to polymc executable file
presentmonpath = r"presentmon.exe"  #full path to Intel presentmon
clientstartdelay = 46   #Time to wait after starting the server before starting the client. Time this so the client doesn't try to connect before the server is up.




#-------------------------Code----------------------------
#You shouldn't have to configure anything below this line!

benchlog = os.path.normpath(os.path.join(os.getcwd(), "Benchmarks/", str(datetime.datetime.now())[:-7].replace(" ", "_").replace(":","-") + "_" + benchname.replace(" ", "_") + r".json")) #Benchmark log path
csvpath = os.path.normpath(os.path.join(os.getcwd(),  "Benchmarks", "presentmon.csv"))

def benchmark(i): #"i is the benchmark index"
  iter = 1
  blist[i]["Startup_Times"] = []
  blist[i]["Chunkgen_Times"] = []

  #Init
  bclient = client and (blist[i]["PolyInstance"] != "")
  spark = False
  hascarpet = False
  g1gc = False
  chunkgen_command = ""
  chunkgen_expect = ""
  os.chdir(blist[i]["Path"])
  plat = "Linux"
  if "Windows" in platform.system():
    plat = "Windows"
  ngui = ""
  if nogui:
    ngui = " nogui"

  #return world to pre-benchmark state
  def restore_world():
    if os.path.isdir("world") and os.path.isdir("_world_backup"):
      shutil.rmtree("world")
      os.rename("_world_backup", "world")
  atexit.register(restore_world)
  #Backup existing world for determinism
  restore_world()
  if os.path.isdir("world"):
    shutil.copytree("world", "_world_backup")




  #Start building the Minecraft command
  if plat == "Linux":
    command = "nice -n -18 " + blist[i]["Command"]
  else:
    command = blist[i]["Command"]

  #Try to find Fabric
  d = glob.glob("*.jar")
  for f in d:
    if "fabric-" in os.path.basename(f):
      if debug: print("Found Fabric: " + f)
      chunkgen_command = fabric_chunkgen_command
      chunkgen_expect = fabric_chunkgen_expect
      command = command + " -jar " + os.path.basename(f)
  
  #Try to find Forge
  d = glob.glob(r"libraries/net/minecraftforge/forge/*/win_args.txt")
  if len(d) == 1:
    if debug: print("Found Forge" + d[0])
    chunkgen_command = forge_chunkgen_command
    chunkgen_expect = forge_chunkgen_expect
    if plat == "Linux":
      command = command + " @" + os.path.normpath(os.path.join(os.path.dirnamme(d[0]), r"unix_args.txt")) + ngui + r' "$@"'
    else:
      command = command + " @" + os.path.normpath(d[0]) + r" %*"
      if nogui:
        command = command + " --nogui"
    

  #Try to find Spark and/or Carpet mods
  if os.path.isdir("mods"):
    mods = glob.glob("mods/*.jar")
    spark = any('spark' in s for s in mods) #Check for Spark mod
    if spark:
      blist[i]["Average_TPS_Values"] = []   #initialize lists
      blist[i]["GC_Stop_MS"] = []
      blist[i]["GC_Stops"] = []
      blist[i]["Oldgen_GCs"] = []
      blist[i]["Memory_Usage"] = []
      blist[i]["CPU_Usage"] = []
    hascarpet =  any('fabric-carpet' in s for s in mods)
    if hascarpet:
      blist[i]["Player_Spawn_Times"] = []
    if bclient:
      blist[i]["Average_FPS"] = []
      blist[i][r"1%_Frametime_ms"] = []
      blist[i][r"5%_Frametime_ms"] = []
    
  else: 
    if debug: print("No mods folder found")

  #Helper function for crash notification
  def qw(s):
    print("Startup error, please check the server log: " + s)
    blist[i]["Startup_Times"].append(s)
    blist[i]["Chunkgen_Times"].append(s)

  #bench minecraft for # of iterations  
  for n in range(1, blist[i]["Iterations"] + 1):
    #Clear the existing world if there is one
    if os.path.isdir("world"):
        shutil.rmtree("world")

    #Delete chunky config if found, as it stores jobs there
    if os.path.isfile(r"config/chunky.json"):
      if debug: print("Removing chunky config")
      os.remove(r"config/chunky.json")

    #Start Minecraft
    print("Running '" + blist[i]["Name"] + "' iteration " + str(n))
    if debug:print(command)
    start = time.time()
    try:
      mcserver = pexpect.popen_spawn.PopenSpawn(command, timeout=totaltimeout, maxread=20000000)   #Start Minecraft server
    except Exception as e:
      print("Error running the command:")
      print(command)
      raise e
    if debug: print("Starting server: " + command)
    time.sleep(0.01)
    if plat == "Windows":
      try:
        for proc in psutil.process_iter(['pid', 'name']):   #Set to high process priority in windows, for greater consistency when run in the background
          if "java" in str(proc.name):
            if debug: print("Setting Priority")
            proc.nice(psutil.HIGH_PRIORITY_CLASS)
      except:
        print("Failed to set process priority, please run this benchmark as an admin!")
    crash = False
    if bclient:
      time.sleep(clientstartdelay)
      for proc in psutil.process_iter(['pid', 'name']):   #Check for an existing javaw process
        if "javaw" in str(proc.name):
          raise Exception("Please kill all existing 'javaw' processes")
      try:  
        clientprocess = subprocess.Popen([polypath, "--launch", blist[i]["PolyInstance"], "--server", "0.0.0.0:25565"], creationflags=subprocess.HIGH_PRIORITY_CLASS) #launch the client
      except Exception as e:
        print("Error starting client:")
        raise e
    index = mcserver.expect_exact(pattern_list=[r'''! For help, type "help"''', 'Minecraft Crash Report', pexpect.EOF, pexpect.TIMEOUT], timeout=startuptimeout)  #wait until the server is started
    if index == 0:
      if debug: print("Server started")
    elif index == 1:
      mcserver.sendline('stop')
      time.sleep(0.01)
      mcserver.kill(signal.SIGTERM)
      qw("CRASH")
      crash = True
    elif index == 2:
      qw("STOPPED")
      crash = True
    elif index == 3:
      mcserver.sendline('stop')
      mcserver.kill(signal.SIGTERM)
      qw("TIMEOUT")
      crash = True
    if not crash:
      blist[i]["Startup_Times"].append(round(time.time() - start , 2))
      if bclient:
        mcserver.expect_exact(pattern_list=[r'''joined the game'''])  #Wait for the client to joim
      time.sleep(8)    #Let the server "settle", or let the client join
      if bclient:
        try: 
          subprocess.run([presentmonpath, "-terminate_existing"])
        except:
          pass
        if os.path.isfile(csvpath):
          os.remove(csvpath)
        pmonprocess = subprocess.Popen([presentmonpath, "-process_name", "javaw.exe", "-output_file", csvpath, "-terminate_on_proc_exit"])
      if hascarpet:
        if debug: print("Spawning players")
        start = time.time()
        for x in range(1, carpet + 1):
          mcserver.sendline("player " + str(x) + " spawn")
          mcserver.expect_exact(str(x) + " joined the game")
          mcserver.sendline("player " + str(x) + " look 30 " + str(int(round(360 * x / carpet))))
          mcserver.sendline("player " + str(x) + " jump continuous")
          mcserver.sendline("player " + str(x) + " move forward")
          mcserver.sendline("player " + str(x) + " sprint")
          mcserver.sendline("player " + str(x) + " attack continuous")
        blist[i]["Player_Spawn_Times"].append(round(time.time() - start , 3))
      mcserver.sendline(forceload_cmd) 
      time.sleep(1)    #Let it settle some more
      if debug: print("Generating chunks...")
      start = time.time()
      mcserver.sendline(chunkgen_command)   #Generate chunks
      index = mcserver.expect_exact(pattern_list=[chunkgen_expect, 'Minecraft Crash Report', pexpect.EOF, pexpect.TIMEOUT], timeout=chunkgentimeout)
      if bclient:
        pmonprocess.terminate()
        clientprocess.terminate()  #close presentmon and kill the minecraft client
        for proc in psutil.process_iter(['pid', 'name']):   #Make sure the java client is really dead
          if "javaw" in str(proc.name):
            if debug: print("Killing client")
            proc.kill()
      if index == 0:
        if debug: print("Chunks finished. Stopping server...")
        blist[i]["Chunkgen_Times"].append(round(time.time() - start, 2))
        if spark:
          mcserver.sendline("spark health --memory")
          mcserver.expect_exact("TPS from last 5")
          mcserver.sendline("spark gc")
          mcserver.expect_exact("Garbage Collector statistics")
          time.sleep(0.5) #make sure log is flushed to disk
          with open("logs/latest.log", "r") as f:     #Get spark info from the log
            lines=f.readlines()
            iter = 0
            for l in lines:
              if "TPS from last 5" in l:
                blist[i]["Average_TPS_Values"].append(float(lines[iter+1].split(",")[-1][1:-1].split("*")[-1])) #TPS
              if "Memory usage:" in l:
                blist[i]["Memory_Usage"].append(float(lines[iter+1].split("GB")[0].strip())) #Memory
              if "CPU usage" in l:
                blist[i]["CPU_Usage"].append(float(lines[iter+2].split(",")[-1].split(r"%")[0].strip())) #CPU
              if ("G1 Young Generation" in l) or ("ZGC Pauses collector:" in l) or ("Shenandoah Pauses collector" in l):
                blist[i]["GC_Stop_MS"].append(float(lines[iter+1].split("ms avg")[0].strip()))
                blist[i]["GC_Stops"].append(int(lines[iter+1].split("ms avg,")[-1].split("total")[0].strip()))   #GC Stop-the-world info
              if ("G1 Old Generation" in l):
                g1gc = True
                blist[i]["Oldgen_GCs"].append(int(lines[iter+1].split("collections")[0].strip()))    #G1GC Old Gen collections 
              iter = iter + 1
      elif index == 1:
        blist[i]["Chunkgen_Times"].append("CRASH")
      elif index == 2:
        blist[i]["Chunkgen_Times"].append("STOPPED")
      elif index == 3:
        blist[i]["Chunkgen_Times"].append("TIMEOUT")
      mcserver.kill(signal.SIGTERM)
      if bclient:
        frametimes = []
        with open(csvpath, "r") as f:
          csv_reader = csv.DictReader(f, delimiter = ',')
          for line in csv_reader:
            if line['msBetweenPresents'] is not None:
              frametimes.append(float(line['msBetweenPresents']))
        blist[i]["Average_FPS"].append(round(1000 / statistics.mean(frametimes),2))
        blist[i][r"1%_Frametime_ms"].append(round(statistics.mean(sorted(frametimes)[round(len(frametimes) * 0.99 - 1):]), 2))
        blist[i][r"5%_Frametime_ms"].append(round(statistics.mean(sorted(frametimes)[round(len(frametimes) * 0.95 - 1):]), 2))


      if debug: pprint.pprint(blist[i])
  #End of iteration loop
  if blist[i]["Iterations"] >= 2:
    def safemean(l):  #average lists while ignoring strings in them
      l = [x for x in l if not isinstance(x, str)]
      if len(l) > 1:
        return round(statistics.mean(l), 2)
      elif len(l) == 1:
        return l[0]
      else:
        return "-"
    def safevar(l):  #pvariance lists while ignoring strings in them
      l = [x for x in l if not isinstance(x, str)]
      if len(l) > 1:
        return round(statistics.pvariance(l), 2)
      else:
        return "-"

    blist[i]["Average_Chunkgen_Time"] = safemean(blist[i]["Chunkgen_Times"])
    blist[i]["Average_Startup_Time"] = safemean(blist[i]["Startup_Times"])
    blist[i]["PVariance_Chunkgen_Time"] = safevar(blist[i]["Chunkgen_Times"])
    blist[i]["Pvariance_Startup_Time"] = safevar(blist[i]["Startup_Times"])
    if spark:
      blist[i]["Average_TPS"] = safemean(blist[i]["Average_TPS_Values"])
      blist[i]["PVariance_TPS"] = safevar(blist[i]["Average_TPS_Values"])
      blist[i]["Average_GC_Stop_MS"] = safemean(blist[i]["GC_Stop_MS"])
      blist[i]["PVariance_GC_Stop_MS"] = safevar(blist[i]["GC_Stop_MS"])
      blist[i]["Average_GC_Stops"] = safemean(blist[i]["GC_Stops"])
      blist[i]["Average_Memory_Usage_GB"] = safemean(blist[i]["Memory_Usage"])
      blist[i]["Average_CPU_Usage"] = safemean(blist[i]["CPU_Usage"])
      if g1gc:
        if len(blist[i]["Oldgen_GCs"]) > 1:
          blist[i]["Average_Oldgen_GCs"] = safemean(blist[i]["Oldgen_GCs"])
    if carpet:
      blist[i]["Average_Spawn_Time"] = safemean(blist[i]["Player_Spawn_Times"])
      blist[i]["Player_Spawn_Variance"] = safevar(blist[i]["Player_Spawn_Times"])
    if client:
      blist[i]["Net_Average_FPS"] = safemean(blist[i]["Average_FPS"])
      blist[i]["Average_FPS_Variance"] = safevar(blist[i]["Average_FPS"])
      blist[i][r"Average_1%_Frametime_ms"] = safemean(blist[i][r"1%_Frametime_ms"])
      blist[i][r"PVariance_1%_Frametime_ms"] = safevar(blist[i][r"1%_Frametime_ms"])
      blist[i][r"Average_5%_Frametime_ms"] = safemean(blist[i][r"5%_Frametime_ms"])
      blist[i][r"PVariance_5%_Frametime_ms"] = safevar(blist[i][r"5%_Frametime_ms"])
  #os.remove(benchlog)
  with open(benchlog, "w") as f:
    json.dump(blist[0:i+1], f, indent=4)  #Write current data to the benchmark log
  


#-------------------------------Main thread---------------------------------------------

iter = 0
for bench in blist:
  benchmark(iter)
  iter = iter + 1
  print("Bench completed.")
print("All benches completed.")

#Do stuff with the data in blist here.
