# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

from pathlib import Path
import csv

desktop = Path("/Users/jakebestland/Desktop")

desk_files = []
for filepath in desktop.iterdir():
    desk_files.append(filepath.suffix)

count = {x: desk_files.count(x) for x in desk_files}

csvfile_path = Path("/Users/jakebestland/Desktop/filecounts.csv")

### This will print a header row with suffix of each file, followed by the values on new row ###
with open(csvfile_path.joinpath(), "a") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=count)
    writer.writeheader()
    writer.writerow(count)

### This will just print the count
# with open(csvfile_path.joinpath(), "a") as csvfile:
#     countwriter = csv.writer(csvfile)
#     data = [count[".py"], count[""], count[".png"], count[".txt"], count[".csv"]]
#     countwriter.writerow(data)


with csvfile_path.open() as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=[x for x in count.keys()])
    counts2 = list(reader)
#print(counts2) #prints all
print(counts2[-1]) #prints most recent