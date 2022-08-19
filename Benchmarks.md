

`Benchmarks.py` is a script that will automatically benchmark Minecraft server and client instances! It can benchmark multiple configurations consecutively, and average runs together for more consistent data.

#Setup

Install a recent version of Python (preferably Python 3.10), and install the requirements by opening a terminal in this directory, and running `python -m pip install -r requirements.txt`. 

Server benchmarking works on both Windows and Linux, and you don't need anything beyond the python modules and your Java server. But you should configure java to run as an administrator on Windows, if possible. 

Client benchmarks require PolyMC and Intel Presentmon:
- https://github.com/GameTechDev/PresentMon/releases
- https://github.com/PolyMC/PolyMC

# Server Benchmarking

First, make sure your server instance has started and generated its initial chunks, at the very least. I recommend disabling `sync-chunk-writes` in your server.properties file, and testing on an SSD if you have one. 

Arguments for launching your server benchmark (such as java args, paths and such) can be assembled at the top of the Benchmarks.py file. Forge/Fabric installations will automatically be detected, but vanilla servers and servers with other modding APIs will need to have their `.jar` file manually specified. 

Benchmark parameters are stored as a Python dict. Benchmark.py has an example of how it should be formatted. Be sure to look at the `#Server benchmarking options` section, as it contains important parameters you probably need to tweak (such as timeouts for really slow modpacks, or forceload/carpet commands to tweak how much you load the server) 

You can start the script either via command line, or with the included .bat file. Note that scripts should be run as an administrator on Windows or sudo on linux, as otherwise it will fail to change the process priority, and some features (like large pages on Windows) may not work. In theory it should still run without elevated privledges, but your results could be less consistent. 

The script itself starts the server (timing how long it takes to start up), and then forceloads a large area to generate a sustained load. If you have the Fabric "Carpet" mod installed, it will also populate the server with fake players and send them running out of spawn.

If you have other suggestions for loading the server, particularly Forge or Vanilla servers, please let me know!

If Forge or Fabric are installed, the script then pregenerates chunks on the loaded server with the specified pregeneration command, and times how long it takes. At the end, if the "Spark" mod is installed, garbage collection and resource usage metrics are also collected

The benchmark saves your current world at the start of each iteration, and restores it to its original state at end of each iteration for consistency. If the benchmark crashes, your world backup will be in the "_world_backup" folder, and will automatically be restored if you run "Benchmark.py" again. Hence the benchmark will accept, and benefits from, heavily played-in worlds, but you may need to adjust your chunk pregeneration and forceloading parameters. 

# Client Benchmarking

Client benchmarking relies on PolyMC as your Minecraft instance launcher. Create insances and position your character where you want them to start for the benchmark, and clone instances if you want to test for differences between, say, java parameters or mod loadouts. You should only have 1 "world" in each instance you want to test.

Its important to configure the instance before you run it! Place your charachter somewhere they can run in a straight line for awhile, and disable graphics settings like vsync or fps caps. 

The "PolyInstance" parameter in your benchmark script should point to the name of your instance folder, *not* the full path or the name in the PolyMC window. 

Like the server benchmark, your world will be backed up and restored after each iteration, and everything should be run as an admin on Windows if possible. 

The script will start up PolyMC automatically, click and load the first singleplayer world it finds, and wait for the world to "warm up." Then it will move your character forward, while jumping and attacking, for the specified amount of time, and collect even more performance data with Spark if that mod is installed. 

# Benchmark Data

Raw data from the benchmarks is progressively written to .json files in the `Benchmarks` folder.

On the server, you should primarily be looking at chunk generation times and garbage collection info. On the client, the 1% and 5% metrics represent the slowest 1% and 5% of your frametimes, which represents "spikes" and how sluggish the game feels during its worst stutters. 

In server benchmarks, "CRASH", "STOPPED", or "TIMEOUT" will show up in your chunkgen/startup times if something went wrong with your server. If that's the case, you should make sure the server-start command in that partiular entry looks right, and try starting the server with that command manually. 

# Benchmarking Tips.

- Disable boosting on Windows to make runs more consistent: https://www.reddit.com/r/ZephyrusG14/comments/gho535/important_update_to_properly_disable_boosting/

- Disable power-saving features like auto screen off or sleeping. 

- The client benchmark runs better with Creative worlds.

- It also works better with starts near existing bases. But be sure to clone your instances you actually play with, just in case!

- Run several iterations of each benchmark, especially if theres a lot of variation between runs.

- Test your servers/instances before benching them! The Benchmark hides output in the command line.

Some work-in-progress features:

- Better Client benchmark error handling 

- Print hardware and system info.

- More options to stress the server/client.

- Better server OSX support. I just need a tester. 

- Client linux support (via mangohud), if requested. 