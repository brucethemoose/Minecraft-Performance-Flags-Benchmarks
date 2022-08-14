

`Benchmarks.py` is a script that will automatically benchmark Minecraft server instances. It's a WIP, and client benching in particular isn't quite done yet. Currently, it will:

- Take configurations to benchmark multiple minecraft instance with specific java distributions/flags.

- Time server startup and chunk generation time, averaging them over multiple runs.

- Save GC, tps, and resource usage data if the Spark mod is present.

- Generate fake players and send them running from spawn to load the server if the "Carpet" mod is present.

- Forceload chunks on the server.


Benchmarks are configured at the top of the `Benchmarks.py` file, which requires some very basic knowledge about Python formatting and strings. And they are written to the `Benchmarks` folder as a .json file.

Some work-in-progress features:

- Stressing the server more without generating chunks, via carpet/forceloading and premade worlds

- Starting a Minecraft client with PolyMC, connecting it to a server instance, and collecting frametime data with Intel Presentmon (and hopefully a linux equivalent).

- Print hardware and system info.
