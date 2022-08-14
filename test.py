
import datetime,os,csv,pprint
csvpath = os.path.normpath(os.path.join(os.getcwd(),  "Benchmarks", "presentmon.csv"))
frametimes = []
with open(csvpath, "r") as f:
    csv_reader = csv.DictReader(f, delimiter = ',')
    #print(csv_reader)
    for line in csv_reader:
        if line['msBetweenPresents'] is not None:
            frametimes.append(float(line['msBetweenPresents']))
pprint.pprint(frametimes)