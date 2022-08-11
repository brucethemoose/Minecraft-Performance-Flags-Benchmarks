
import datetime,os
print(os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Benchmarks/", r"benchmark-"+str(datetime.datetime.now())[:-7].replace(" ", "_").replace(":","-") + r".json"))) #Benchmark log path