import os,time,shutil,glob,datetime,json,platform,signal,statistics,pprint,subprocess,csv,atexit
import psutil  
import pexpect
from pexpect import popen_spawn






#----------------------------String Scratch Space----------------------------
#Write your strings to construct server benchmarks here!
#Use / or \\ instead of \ for paths

#Minecraft Server Paths

vevserver = r"C:/Games/mcservers/vevserver"

minfabric = r"C:/Games/mcservers/MinimalFabric"

#Java Paths

graalpath = r"F:/JDKs/graalvm-ee-java17-windows-amd64-22.1.0/graalvm-ee-java17-22.1.0/bin/java.exe"

jdkpath = r"F:/JDKs//OpenJDK17U-jre_x64_windows_hotspot_17.0.4_8/jdk-17.0.4+8-jre/bin/java.exe"

j9path = r"F:/JDKs/ibmopenj9/bin/java.exe"

#Java Flags (for servers)
#(Should start with a space, so they can be "added" together with the + sign)
#Client flags must be set in PolyMC instances!

#GC
aikar = r''' -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1'''

aikartesttweak = r''' -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=16 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=16M -XX:G1ReservePercent=38 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=2 -XX:InitiatingHeapOccupancyPercent=1 -XX:G1MixedGCLiveThresholdPercent=70 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:MaxTenuringThreshold=1 -XX:+ExplicitGCInvokesConcurrent -XX:GCPauseIntervalMillis=17 -XX:G1RSetUpdatingPauseTimePercent=12 -XX:G1ConcRSHotCardLimit=8 -XX:G1ConcRefinementServiceIntervalMillis=150'''

shen1 = r''' -XX:+UseShenandoahGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ShenandoahGCMode=satb -XX:ShenandoahGCHeuristics=adaptive'''

shen4 = r''' -XX:+UseShenandoahGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ShenandoahGCMode=iu -XX:ShenandoahGCHeuristics=adaptive'''

z1 = r''' -XX:+UseZGC -XX:+AlwaysPreTouch -XX:+ParallelRefProcEnabled -XX:+ExplicitGCInvokesConcurrent -XX:ZAllocationSpikeTolerance=3'''

conc = r'''  -XX:ConcGCThreads=7'''

lessconc = r''' -XX:ConcGCThreads=4'''

moreconc = r'''  -XX:ConcGCThreads=12'''

#Non gc flags
minimal = r''' -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions'''

moregraal = r''' -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+PerfDisableSharedMem -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:+UseNUMA -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true -Dlibgraal.ExplicitGCInvokesConcurrent=true -Dlibgraal.AlwaysPreTouch=true -Dlibgraal.ParallelRefProcEnabled=true -XX:AllocatePrefetchStyle=3 -XX:-DontCompileHugeMethods -XX:ThreadPriorityPolicy=1'''

evenmoregraal = r''' -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:+UseFastUnorderedTimeStamps -XX:AllocatePrefetchStyle=3 -XX:+TrustFinalNonStaticFields -XX:ThreadPriorityPolicy=1 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true -Dlibgraal.ExplicitGCInvokesConcurrent=true -Dlibgraal.AlwaysPreTouch=true -Dlibgraal.ParallelRefProcEnabled=true'''

ojdk = r''' -server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+PerfDisableSharedMem -XX:+UseStringDeduplication -XX:+UseFastUnorderedTimeStamps -XX:AllocatePrefetchStyle=1 -XX:+OmitStackTraceInFastThrow -XX:+TrustFinalNonStaticFields -XX:ThreadPriorityPolicy=1 -XX:InlineSmallCode=1000 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.CompilerConfiguration=community -Dgraal.SpeculativeGuardMovement=true'''

experimental = r''' -XX:+EnableVectorAggressiveReboxing -XX:+EnableVectorReboxing -XX:+EnableVectorSupport -XX:+ExplicitGCInvokesConcurrent -XX:+OptimizeFill -XX:+OptoBundling -XX:+OptoScheduling -XX:+UseCharacterCompareIntrinsics -XX:+UseCopySignIntrinsic -XX:+UseCriticalCompilerThreadPriority -XX:+UseCriticalJavaThreadPriority -XX:+UseOptoBiasInlining -XX:+UseVectorStubs'''

lpages = r''' -XX:+UseLargePages -XX:LargePageSizeInBytes=2m'''

memory = r''' -Xms8G -Xmx8G'''

zmemory =r''' -Xms3G -Xmx9G'''

lightmemory = r''' -Xms4G -Xmx4G'''


oldgraal = r'''-server -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=50 -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -XX:ThreadPriorityPolicy=1 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -Djdk.nio.maxCachedBufferSize=262144 -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true -Dlibgraal.ExplicitGCInvokesConcurrent=true -Dlibgraal.AlwaysPreTouch=true -Dlibgraal.ParallelRefProcEnabled=true -XX:+UseLargePages -XX:LargePageSizeInBytes=2m'''

newgraal = r'''-server -XX:+UnlockExperimentalVMOptions -XX:+UnlockDiagnosticVMOptions -XX:+UseG1GC -XX:+AlwaysPreTouch -Dlibgraal.AlwaysPreTouch=true -XX:+ParallelRefProcEnabled -Dlibgraal.ParallelRefProcEnabled=true -XX:+ExplicitGCInvokesConcurrent -Dlibgraal.ExplicitGCInvokesConcurrent=true -XX:MaxGCPauseMillis=20 -Dlibgraal.MaxGCPauseMillis=20 -Dlibgraal.GCPauseIntervalMillis=21 -XX:GCPauseIntervalMillis=21 -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -Dlibgraal.MaximumYoungGenerationSizePercent=40 -XX:G1HeapRegionSize=32M -XX:G1ReservePercent=20 -Dlibgraal.G1ReservePercent=20 -XX:G1HeapWastePercent=5 -Dlibgraal.G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -Dlibgraal.G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -Dlibgraal.InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -Dlibgraal.G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -Dlibgraal.SurvivorRatio=32 -Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+UseNUMA -XX:-DontCompileHugeMethods -XX:+UseVectorCmov -XX:AllocatePrefetchStyle=3 -Djdk.nio.maxCachedBufferSize=262144 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -XX:+UseStringDeduplication -XX:ThreadPriorityPolicy=1 -XX:+EnableJVMCIProduct -XX:+EnableJVMCI -XX:+UseJVMCICompiler -XX:+EagerJVMCI -Dgraal.TuneInlinerExploration=1 -Dgraal.CompilerConfiguration=enterprise -Dgraal.UsePriorityInlining=true -Dgraal.Vectorization=true -Dgraal.OptDuplication=true -Dgraal.DetectInvertedLoopsAsCounted=true -Dgraal.LoopInversion=true -Dgraal.VectorizeHashes=true -Dgraal.EnterprisePartialUnroll=true -Dgraal.VectorizeSIMD=true -Dgraal.StripMineNonCountedLoops=true -Dgraal.SpeculativeGuardMovement=true -Dgraal.InfeasiblePathCorrelation=true -Dgraal.LoopRotation=true -XX:+UseLargePages -XX:LargePageSizeInBytes=2m'''

#-----------------------Benchmark Data--------------------------
benchname = r"Old vs New GraalVM 22 Flags"   #Name for the whole benchmark run

blist = [
#Note that Forge/Fabric server packs only need "java + arguments" for their launch command, as their jars are automatically found
#Formatting for the benchmark data:
#Server: benchmark name, bnechmark command (java + flags), server root directory, # of iterations to run this benchmark
#Client: benchmark name, PolyMC instance folder (note: must be the actual folder name, not the name on the polymc instance!),  # of iterations to run this benchmark
  
  {
    "Name": "VeV OldFlags",
    "PolyInstance": "oldgraal",
    "Iterations": 4
  },
  {
    "Name": "VeV NewFlags",
    "PolyInstance": "newgraal",
    "Iterations": 4
  },
  {
    "Name": "VEV Server OldFlags", 
    "Command": graalpath + oldgraal + memory + moreconc,
    "Path": vevserver, 
    "Iterations": 4
  },
  {
    "Name": "VEV Server NewFlags", 
    "Command": graalpath + newgraal + memory + moreconc,
    "Path": vevserver, 
    "Iterations": 4
  },
]

#----------------------Other Options--------------------------

#Server benchmarking options
nogui = True     #Whether to run the dedicated server GUI or not
carpet = 67 #number of simulated players if the "Carpet" fabric mod is present
fabric_chunkgen_command = r"chunky start"                 #Chunk generation command to use in fabric packs
fabric_chunkgen_expect =  r"[Chunky] Task finished for"   #String to look for when chunk generation is finished
forge_chunkgen_command = r"forge generate 0 0 0 3000"     #Chunk generation command to use in forge packs
forge_chunkgen_expect =  r"Finished generating"           ##String to look for when chunk generation is finished
startuptimeout= 350 #Number of seconds to wait before considering the server to be dead/stuck
chunkgentimeout = 600 #Number of seconds to wait for chunk generation before considering the server to be dead/stuck 
totaltimeout = 1200 #Number of seconds the whole server can run before timing out. 
forceload_cmd= r"forceload add -120 -120 120 120" #Command to forceload a rectangle. Can also be some other server console command. 

#Client benchmarking options
polypath = r"C:/Games/PolyMC-Windows-Portable-1.4.0/polymc.exe" #Full path to polymc executable file
polyinstances = r"" #Full path to polymc instance folder. Normally in %appdata%/roaming/polymc on windows, but you can leave this blank if using polyMC portable. 
presentmonpath = r"presentmon.exe"  #full path to Intel presentmon executable file
warmup = 45    #Seconds to wait after hitting the "singleplayer" button before starting the benchmark. Give enough time for the world to load!
benchtime = 100 #Seconds to run the benchmark
focusclick = True #Click before searching for buttons, only really necessary for fullscreen Minecraft




#-------------------------Code----------------------------
#You shouldn't have to configure anything below this line!

debug = False
loadedstring = r"mob_effects.png" #String to look for in a log when a client is finished loading
benchlog = os.path.normpath(os.path.join(os.getcwd(), "Benchmarks/", str(datetime.datetime.now())[:-7].replace(" ", "_").replace(":","-") + "_" + benchname.replace(" ", "_") + r".json")) #Benchmark log path
csvpath = os.path.normpath(os.path.join(os.getcwd(),  "Benchmarks", "presentmon.csv"))
cvpath = os.path.abspath("CV_Images")

def benchmark(i): #"i is the benchmark index"
  iter = 1

  #Init
  spark = False
  hascarpet = False
  g1gc = False
  chunkgen_command = ""
  chunkgen_expect = ""
  
  plat = "Linux"
  if "Windows" in platform.system():
    plat = "Windows"
  ngui = ""
  if nogui:
    ngui = " nogui"
  if "PolyInstance" in blist[i] and ("Command" in blist[i] or "Path" in blist[i]):
    raise Exception("Each benchmark instance should ether have a command and path entry, or a polymc instance entry, not both")
  
  #Function to wait for a given line to appear in a log file. 
  def waitforlogline(lfile, key, delay = 1, timeout = 1800):
    t = time.time()
    with open(lfile, "r") as t:
      while True:
        for line in t.readlines():
          if "key" in line:
            return
        time.sleep(delay)
        if time.time() - t > timeout:
          raise Exception("Cannon find " + key + " in log!")
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

  if "PolyInstance" in blist[i]:
    #---Client branch---
    
    from guibot.guibot import GuiBot 
    from guibot.controller import PyAutoGUIController
    from guibot.config import GlobalConfig
    from guibot.finder import TemplateFinder
    import pydirectinput
    import pyautogui
    #Only import client modules in client branch.

    if plat != "Windows":
      raise Exception("Benchmarking is only supported on Windows!")
    polyfolder = os.path.normpath(os.path.join(os.path.dirname(polypath), "instances", blist[i]["PolyInstance"]))
    if not os.path.isdir(polyfolder):
      polyfolder = os.path.join(polyinstances, blist[i]["PolyInstance"])
      if not os.path.isdir(polyfolder):
        raise Exception("Either your PolyMC instance path or your selected instance is incorrect: " + polyfolder)
    print(os.path.join(polyfolder, "*minecraft"))
    polyfolder = (glob.glob(os.path.join(polyfolder, "minecraft")) + glob.glob(os.path.join(polyfolder, ".minecraft")))[0]
    if not os.path.isdir(polyfolder):
      print(polyfolder)
      raise Exception("PolyMC instance not valid!")
    plog = os.path.join(polyfolder, "logs", "latest.log")
    try:
      worldfolder = glob.glob(os.path.join(polyfolder, "saves", "*"))[0]
    except:
      raise Exception("Please create a world in this instance before running the benchmark!")
    worldbackup = os.path.join(polyfolder, "world_backup")

    os.chdir(polyfolder)
    
    #initialize lists
    blist[i]["Average_FPS"] = []
    blist[i][r"1%_Frametime_ms"] = []
    blist[i][r"5%_Frametime_ms"] = []
        #Try to find Spark and/or Carpet mods
    if os.path.isdir("mods"):
      mods = glob.glob("mods/*.jar")
      spark = any('spark' in s for s in mods) #Check for Spark mod
      if spark:                         
        blist[i]["GC_Stop_MS"] = []
        blist[i]["GC_Stops"] = []
        blist[i]["Oldgen_GCs"] = []
        blist[i]["Memory_Usage"] = []
        blist[i]["CPU_Usage"] = []

    def restore_world():
      if os.path.isdir(worldfolder) and os.path.isdir(worldbackup):
        try: 
          shutil.rmtree(worldfolder)
        except:
          time.sleep(7)   #Give the old server some time to close
          shutil.rmtree(worldfolder)
        os.rename(worldbackup, worldfolder)
    atexit.register(restore_world)
    restore_world() #restore backup in case it wasnt restored on exit before

    for n in range(1, blist[i]["Iterations"] + 1):  #Run benchmark for # of iterations
      try:
        #Backup existing world to restore later
        if os.path.isdir(worldfolder) and not os.path.isdir(worldbackup):
          shutil.copytree(worldfolder, worldbackup)
        for proc in psutil.process_iter(['name']):   #Check for an existing javaw process
          if "javaw" in str(proc.name):
            raise Exception("Please kill all existing 'javaw' processes")
        try:  
          clientprocess = subprocess.Popen([polypath, "--launch", blist[i]["PolyInstance"]], creationflags=subprocess.HIGH_PRIORITY_CLASS, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) #launch the client
        except Exception as e:
          print("Error starting client:")
          raise e

        #Wait for client to start up
        time.sleep(10)
        waitforlogline(plog, loadedstring, delay = 1, timeout = 1800)
        time.sleep(4)
        GlobalConfig.smooth_mouse_drag = False
        GlobalConfig.delay_after_drag = 0
        ctl = PyAutoGUIController()
        gfinder = TemplateFinder()
        guibot = GuiBot(ctl,gfinder)
        guibot.add_path(cvpath)
        _timeout = time.time() + 80
        if focusclick:
          pydirectinput.mouseDown(button='left')
          pydirectinput.mouseUp(button='left')
        #Try to find matches PNGs in CV_Images and click on them:
        def ClickPlay():
          while True:
            time.sleep(0.3)
            if guibot.exists("Play1"):
              guibot.click("Play1")
              break
            elif guibot.exists("Play2"):
              guibot.click("Play2")
              break
            elif guibot.exists("Play3"):
              guibot.click("Play3")
              break
            elif guibot.exists("Play4"):
              guibot.click("Play4")
              break
            else:
              if time.time() > _timeout:
                raise Exception("Cannot find 'Play' Button to click! This may be a machine vision issue if the start screen is modded.")
        def ClickVersion():
          while True:
            time.sleep(0.5)
            if guibot.exists("Version1"):
              guibot.click("Version1")
              ClickPlay()
              break
            elif guibot.exists("Version2"):
              guibot.click("Version2")
              ClickPlay()
              break
            elif guibot.exists("Version3"):
              guibot.click("Version3")
              ClickPlay()
              break
            elif guibot.exists("Version4"):
              guibot.click("Version4")
              ClickPlay()
              break
            else:
              if time.time() > _timeout:
                raise Exception("Cannot find world to click! Please create a world before running the script. This may be a machine vision issue if the start screen is modded.")
        while True:
          time.sleep(1)
          if guibot.exists("Singleplayer1"):
            guibot.click("Singleplayer1")
            ClickVersion()
            break
          elif guibot.exists("Singleplayer2"):
            guibot.click("Singleplayer2")
            ClickVersion()
            break
          elif guibot.exists("Singleplayer3"):
            guibot.click("Singleplayer3")
            ClickVersion()
            break
          elif guibot.exists("Singleplayer4"):
            guibot.click("Singleplayer4")
            ClickVersion()
            break
          else:
            if time.time() > _timeout:
              raise Exception("Cannot find 'Singleplayer' button to click! This may be a machine vision issue if the start screen is modded.")
        #Client control here
        time.sleep(warmup)
        
        #pyautogui.keyDown('w')
        #pyautogui.keyDown('space')
        #pyautogui.mouseDown(button='left')
        #pyautogui.move(0, 30, 1)
        pydirectinput.keyDown('space')
        pydirectinput.keyDown('w')
        pydirectinput.move(0, 30)  
        pydirectinput.mouseDown(button='left')


        if os.path.isfile(csvpath):
          os.remove(csvpath)
        pmonprocess = subprocess.Popen([presentmonpath, "-process_name", "javaw.exe", "-output_file", csvpath, "-terminate_on_proc_exit"])
        time.sleep(benchtime)

        #Bench period here

        try: 
          subprocess.run([presentmonpath, "-terminate_existing"])
        except:
          pass
        pmonprocess.terminate()
        #pyautogui.keyUp('w')
        #pyautogui.keyUp('space')
        #pyautogui.mouseUp(button='left')
        pydirectinput.keyUp('w')
        pydirectinput.keyUp('space')
        pydirectinput.mouseUp(button='left')
        if spark:
          pydirectinput.press(r"/")
          pydirectinput.typewrite("sparkc health --memory")
          pydirectinput.press(r"enter")
          pydirectinput.press(r"/")
          pydirectinput.typewrite("sparkc gc")
          pydirectinput.press(r"enter")
          time.sleep(0.3) #make sure log is written to disk
          with open(plog, "r") as f:     #Get spark info from the log
            lines=f.readlines()
            iter = 0
            for l in lines: 
              if "Memory usage:" in l:
                blist[i]["Memory_Usage"].append(float(lines[iter].split(r"Memory usage:\n")[-1].split("GB")[0].strip())) #Memory
              if "CPU usage" in l:
                blist[i]["CPU_Usage"].append(float(lines[iter].split(r"(process)\n\n>")[0].split(",")[-1].split(r"%")[0].strip())) #CPU
              if ("G1 Young Generation" in l) or ("ZGC Pauses collector:" in l) or ("Shenandoah Pauses collector" in l):
                blist[i]["GC_Stop_MS"].append(float(lines[iter].split("ms avg")[0].split(r"\n")[-1].strip()))
                blist[i]["GC_Stops"].append(int(lines[iter].split("ms avg,")[1].split("total")[0].strip()))   #GC Stop-the-world info
              if ("G1 Old Generation" in l):
                g1gc = True
                blist[i]["Oldgen_GCs"].append(int(lines[iter].split(r"G1 Old Generation collector:\n")[-1].split("collections")[0].strip()))    #G1GC Old Gen collections 
              iter = iter + 1


        clientprocess.terminate()  #close presentmon and kill the minecraft client
        time.sleep(1)
        try:
          for proc in psutil.process_iter(['name']):   #Make sure the java client is really dead, as it likes to hang
            if "javaw" in str(proc.name):
              if debug: print("Killing client")
              proc.kill()
        except:
          print("Failed to run psutil loop to kill Minecraft")
        
        frametimes = []
        with open(csvpath, "r") as f:
          csv_reader = csv.DictReader(f, delimiter = ',')
          for line in csv_reader:
            if line['msBetweenPresents'] is not None:
              frametimes.append(float(line['msBetweenPresents']))
        blist[i]["Average_FPS"].append(round(1000 / statistics.mean(frametimes),2)) #Average FPS
        blist[i][r"1%_Frametime_ms"].append(round(statistics.mean(sorted(frametimes)[round(len(frametimes) * 0.99 - 1):]), 2))  #Slowest 1% of frametimes average
        blist[i][r"5%_Frametime_ms"].append(round(statistics.mean(sorted(frametimes)[round(len(frametimes) * 0.95 - 1):]), 2))  #Slowest 5% of frametimes average

        #End of iteration loop
      except Exception as e: #Clean up
        try: 
          subprocess.run([presentmonpath, "-terminate_existing"])
        except:pass
        try:
          clientprocess.terminate()  #close presentmon and kill the minecraft client
          pmonprocess.terminate()
          time.sleep(1)
        except:pass
        try:
          for proc in psutil.process_iter(['name']):   #Make sure the java client is really dead, as it likes to hang
            if "javaw" in str(proc.name):
              if debug: print("Killing client")
              proc.kill()
        except:pass
        restore_world()
        print("Error in client benchmark iteration!")
        pprint.pprint(repr(e))


    try: 
      if blist[i]["Iterations"] >= 2:
        blist[i]["Net_Average_FPS"] = safemean(blist[i]["Average_FPS"])
        blist[i]["Average_FPS_Variance"] = safevar(blist[i]["Average_FPS"])
        blist[i][r"Average_1%_Frametime_ms"] = safemean(blist[i][r"1%_Frametime_ms"])
        blist[i][r"PVariance_1%_Frametime_ms"] = safevar(blist[i][r"1%_Frametime_ms"])
        blist[i][r"Average_5%_Frametime_ms"] = safemean(blist[i][r"5%_Frametime_ms"])
        blist[i][r"PVariance_5%_Frametime_ms"] = safevar(blist[i][r"5%_Frametime_ms"])
        if spark:
          blist[i]["Average_GC_Stop_MS"] = safemean(blist[i]["GC_Stop_MS"])
          blist[i]["PVariance_GC_Stop_MS"] = safevar(blist[i]["GC_Stop_MS"])
          blist[i]["Average_GC_Stops"] = safemean(blist[i]["GC_Stops"])
          blist[i]["Average_Memory_Usage_GB"] = safemean(blist[i]["Memory_Usage"])
          blist[i]["Average_CPU_Usage"] = safemean(blist[i]["CPU_Usage"])
          if g1gc:
            if len(blist[i]["Oldgen_GCs"]) > 1:
              blist[i]["Average_Oldgen_GCs"] = safemean(blist[i]["Oldgen_GCs"])
    except Exception as e:
      print("Error saving client benchmark data!")
      pprint.pprint(repr(e))
        


  
    #---end of client branch---

  elif "Command" in blist[i] and "Path" in blist[i]:
    blist[i]["Startup_Times"] = []
    blist[i]["Chunkgen_Times"] = []
    #---Server branch---
    os.chdir(blist[i]["Path"])
    #return world to pre-benchmark state
    def restore_world():
      if os.path.isdir("world") and os.path.isdir("_world_backup"):
        try:
          shutil.rmtree("world")
        except:
          time.sleep(7) #The old server is stull up, give it some time to close
          shutil.rmtree("world")
        os.rename("_world_backup", "world")
    atexit.register(restore_world)
    restore_world() #restore backup in case it wasnt restored on exit before

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
        if nogui:
          command = command + ngui
    
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
      
    else: 
      if debug: print("No mods folder found")

    #Helper function for crash notification
    def qw(s):
      print("Startup error, please check the server log: " + s)
      blist[i]["Startup_Times"].append(s)
      blist[i]["Chunkgen_Times"].append(s)

    #bench minecraft for # of iterations  
    for n in range(1, blist[i]["Iterations"] + 1):
      #Backup existing world to restore later
      if os.path.isdir("world") and not os.path.isdir("_world_backup"):
        shutil.copytree("world", "_world_backup")
      try:
        #Delete chunky config if found, as it stores jobs there
        if os.path.isfile(r"config/chunky.json"):
          if debug: print("Removing chunky config")
          os.remove(r"config/chunky.json")

        #Start Minecraft
        print("Running '" + blist[i]["Name"] + "' iteration " + str(n))
        if debug:print(command)
        start = time.time()
        try:
          
          mcserver = popen_spawn.PopenSpawn(command, timeout=totaltimeout, maxread=20000000)   #Start Minecraft server
        except Exception as e:
          print("Error running the command:")
          print(command)
          raise e
        if debug: print("Starting server: " + command)
        time.sleep(0.01)
        if plat == "Windows":
          try:
            for proc in psutil.process_iter(['name']):   #Set to high process priority in windows, for greater consistency when run in the background
              if "java" in str(proc.name):
                if debug: print("Setting Priority")
                proc.nice(psutil.HIGH_PRIORITY_CLASS)
          except:
            print("Failed to set process priority, please run this benchmark as an admin!")
        crash = False
        index = mcserver.expect_exact(pattern_list=[r'''! For help, type "help"''', 'Minecraft Crash Report', pexpect.EOF, pexpect.TIMEOUT], timeout=startuptimeout)  #wait until the server is started
        if index == 0:
          if debug: print("Server started")
        elif index == 1:
          mcserver.sendline('stop')
          time.sleep(0.01)
          mcserver.kill(signal.SIGTERM)
          qw("CRASH")
          print(command)
          crash = True
        elif index == 2:
          qw("STOPPED")
          print(command)
          crash = True
        elif index == 3:
          mcserver.sendline('stop')
          mcserver.kill(signal.SIGTERM)
          qw("TIMEOUT")
          print(command)
          crash = True
        if not crash:
          blist[i]["Startup_Times"].append(round(time.time() - start , 2))
          time.sleep(6)    #Let the server "settle"
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
        if debug: pprint.pprint(blist[i])
      except Exception as e:
        print("Error in iteration!")
        pprint.pprint(repr(e))
        try:
          mcserver.kill(signal.SIGTERM)
          time.sleep(2)
        except:pass
      try:
        restore_world() #Restore the world backup
      except:
        try:
          mcserver.kill(signal.SIGTERM)
        except:pass
        time.sleep(5)
        restore_world() #Sometimes shutil fails if the server is still up, so try again. 

    #End of iteration loop
    try: #Dont let funky data kill the benchmark
      if blist[i]["Iterations"] >= 2:
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
    except Exception as e:
      print("Error saving benchmark data!")
      pprint.pprint(repr(e))

    #---End of server bench branch---
  
  with open(benchlog, "w") as f:
    json.dump(blist[0:i+1], f, indent=4)  #Write current data to the benchmark log
  
  #End of benchmark


#-------------------------------Main thread---------------------------------------------

iter = 0
for bench in blist:
  benchmark(iter)
  iter = iter + 1
  print("Bench completed.")
print("All benches completed.")

#Do stuff with the data in blist here.
