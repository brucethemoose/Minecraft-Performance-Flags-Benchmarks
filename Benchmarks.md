

`Benchmarks.py` is a script that will automatically benchmark Minecraft server instances. It's currently being reworld to support client frametime benching. 

The script is tested against Python 3.10, and you can install the requirements with the `pip install -r requirements.txt` command. It works on Linux and Windows, and right now it can:

- Take configurations to benchmark multiple minecraft server instances with specific java distributions/flags.

- Time server startup and chunk generation time, averaging them over multiple runs.

- Save Garbage Collection Info, tps, and resource usage data if the Spark mod is present.

- Generate fake players and send them running from spawn to load the server if the "Carpet" mod is present.

- Forceload chunks on the server.


Benchmarks are configured at the top of the `Benchmarks.py` file, which requires some very basic knowledge about Python formatting and strings. And they are written to the `Benchmarks` folder as a .json file.

Some work-in-progress features:

- Stressing the server more without generating chunks, via carpet/forceloading and premade worlds

- Client fps/frametime benchmarks with PolyMC.

- Print hardware and system info.
