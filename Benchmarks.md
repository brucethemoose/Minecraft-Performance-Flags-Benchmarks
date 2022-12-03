

`Benchmarks.py` is a script that will automatically benchmark Minecraft server and client instances. It can benchmark multiple configurations consecutively, and average runs together for more consistent data, and do all that unattended*. 

# Setup

Clone or download this repo with the "download as zip" button on GitHub. 

Install a recent version of Python (preferably Python 3.10), and run this command in this folder: `python -m pip install -r requirements.txt`

Client benchmarks require Prism Launcher (preferrably the portable release) and Intel Presentmon. 
https://github.com/GameTechDev/PresentMon/releases

**NOTE: My own benchmarking is on pause, and this script/guide may need more updating for the switch from PolyMC to Prism Launcher**

Currently, client benchmarking only works on Windows. Server benching is tested on Windows and Linux, but it should work on other platforms like OSX.

# Server Benchmarking Setup

- Create or clone server instances you want to test. Make sure it starts up and generates chunks without any issues.

- Disable `sync-chunk-writes` in your server.properties file. 

- Open the Benchmark.py file in a text editor, ideally one that will check Python syntax like VSCode. 

- Benchmarks are configured as a list of Python dicts with this format:

```
    {
        "Name": "Server benchmark name", 
        "Command": Full java command to launch the server, except for forge/fabric arguments,
        "Path": full path to the server, 
        "Iterations": # of iterations to run and average together
    },
```

- The "Name" is just a descriptive nickname for that particular benchmark that will show up in the log. The "Command" is the *full* java command to launch the Minecraft server. However, forge/fabic jars will be automatically detected and added to the script command, so all that's really required for forge/fabric tests is your java command/path + your launch arguments. "Path" is the full path your the server folder. "Iterations" is the number of iterations to run the benchmark.

- If you want to assemble common paths, arguments and such with python strings, there is scratch space at the top of the Python file with filled-in examples of how that might be done. Remember that python does not like `\` in paths! 

- Be sure to look at the `#Server benchmarking options` section, as it contains important parameters you probably need to tweak (such as timeouts for really slow modpacks, or forceload/carpet commands to tweak how much you load the server) 

- You can start Bechmark.py via command line, or with the included .bat file. Note that scripts should be run as an administrator on Windows or sudo on linux, otherwise some features (like large pages on Windows or raising the process priority on linux) may not work.

# Server Benchmark Progression and Results. 

- After starting Benchmark.py, the script will back up the server's world so it can be restored later. If the script errored out on a previous run and detects an already backed up world, it will restore the backup first.

- The script with then start the first iteration of the first benchmark, timing how long it takes to start.

- If the "Carpet" fabric mod is installed (which I recommend), it will spawn the specified number of "Fake" players to generate a more realistic load on the server. 

- A specific area will be chunkloaded via the vanilla `forceload` command. If you are testing a world with a big base or some other laggy area, try to center the forceload command on it!

- Chunks will then be generated with the specified command, and timed. This chunkgen time is the primary performance metric of the benchmark at the moment. 

- If the "spark" mod is installed (which I *highly* recommend), Garbage collection and resource usage statistics will be recorded. 

- The server is then killed, and the world backup is restored. 

- At the end of each benchmark iteration, data will be written to a json file in the "Benchmarks" folder.

- Then the script moves onto the next iteration, the next benchmark, and so on until it's done. 

- At the end of each benchmark, iteration results will be averaged together and written to the json file.  

- "CRASH", "STOPPED", or "TIMEOUT" will show up in your chunkgen/startup times if something went wrong with your server. If that's the case, you should make sure the server-start command in that partiular entry looks right, and try starting the server with that command manually. 


# Client Benchmarking

**WIP, the client benchmark is transitioning from PolyMC to Prism Launcher!**

Client benchmarking is tricky and finicky. You have been warned!

- First, open the Prism options and disable it from automatically opening log windows when instances start.

- Set up your Prism instance(s) you want to benchmark. Set the appropriate Java flags, install the mods you want, and so on. 

- Now launch that Prism instance, and create or load exactly one world you want to test. Delete all other worlds. 

- The actual "benchmark" consists of the player character running forward in a straight line, jumping and holding the attack button down, so position your player accordingly. Place them near a populated base if one exists, and make sure they have room to run in a straight line for some time. Consider enabling creative mode so the test character can break blocks in their way more easily. Start them off looking slightly "down" so they can break blocks blocking their path, and try to align them with a cardinal direction so their movement is more deterministic. 

- Once your instance is configured, close it. If you want to run similar instances with, say, different mods or different Java parameters, clone that instance so that all tested instances have the exact same world. 

- Look up the **folder name** of your instance in Windows explorer (not the instance name in the Prism UI). 

- Now open Benchmark.py. Client benchmarks are also stored as a list of Python dicts, formatted like this: 

```
    {
        "Name": "Client Benchmark Name", 
        "PrismInstance": "Name (not full path) of your Prism instance folder",
        "Iterations": # of iterations to run and average together
    },
```
- "Name" is a descriptive nickname for the benchmark, "PrismInstance" is the Prism instance folder you just looked up, and "Iterations" is the number of iterations to run the bench. 

- You also need to configure the path to your Prism .exe file, and the path to your instances folder if your Prism installation isn't portable. 

- Now close (not minimize) *all* other active windows, except the explorer window to start the script. Open apps can interfere with the machine vision used to automate the benchmark. 

# Client Benchmark Progression and Results

- Like the server benchmark, your world will be backed up and restored after each iteration. 

- The script then starts your Prism instance, and clicks through and loads the first singleplayer world it finds. This step is *very* finicky and delicate. For instance, while it has some tolerance for modded startscreens, sometimes the script can't find the "Singleplayer" button to click. Sometimes background windows will "occlude" fullscreen Minecraft, even if they have been minimized. And sometimes the auto clicking just doesn't work for unknown reasons, but restarting your PC seems to fix it.

- After loading your world, the player character idles for some time to let Java "warm up." 

- Then, the player will start constantly moving forward, jumping, and attacking. At this very moment, Intel Presentation Monitor starts recording frametime data. Do not move your mouse during this phase. 

- Spark info is collected at the end (if that mod is present), the client is killed, and the process continues for other iterations/benchmarks. 

- Average FPS and the average of the top 1% and 5% slowest frames (which is arguably more important than average FPS, since this data represents stutters and laggy areas) is written to a json file. 



# Benchmarking Tips.

- Disable boosting on Windows to make runs more consistent: https://www.reddit.com/r/ZephyrusG14/comments/gho535/important_update_to_properly_disable_boosting/

- Disable power-saving features like auto screen off or sleeping. 

- The client benchmark works better with starts near existing bases. Be sure to clone instances you actually play with, just in case!

- Run many iterations of each benchmark, especially if there's a lot of variation between runs on your setup.

- Test your servers/instances before benching them! The benchmark hides output in the command line.



#### Work-in-Progress Features:

- Better Client benchmark error handling 

- Print hardware and system info.

- More options to stress the server/client. I am open to suggestions!

- OSX support?

- Client linux support? 

- Replace the `pexpect` module with log scanning.
