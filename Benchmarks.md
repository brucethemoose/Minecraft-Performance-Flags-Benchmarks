`Benchmarks.py` is a script that will automatically benchmark Minecraft server instances. Currently, it will:

- Take configurations to benchmark multiple minecraft instance with specific java distributions/flags.

- Time server startup and chunk generation time, averaging them over multiple runs.

- Save GC, tps, and resource usage data if the Spark mod is present.

- Generate fake players to load the server if the Carpet (currently Fabric-only) mod is present.

- Forceload chunks on the server.

- Dump all the data as a json.

Benchmarks are configured at the top of the `Benchmarks.py` file, which requires some very basic knowledge about Python formatting and strings. 

Some work-in-progress features:

- Stressing the server without generating chunks, via carpet/forceloading. 

- Loading an existing, played-in world instead of a freshly generated one.

- Starting a Minecraft client with PolyMC, connecting it to a server instance, and collecting frametime data with Intel Presentmon (and hopefully a linux equivalent).

- Print hardware and system info.

- Optional concurrent benchmark execution, as long as the results are consistent.
 
 - More detailed performance metric collection.

Please, contribute more benchmarks if you got em. 
