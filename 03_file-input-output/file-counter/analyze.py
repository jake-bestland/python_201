# Use the `csv` module to read in and count the different file types.
import pathlib
import csv

desktop = pathlib.Path("/Users/jakebestland/Desktop")

desk_files = []

for filepath in desktop.iterdir():
    desk_files.append(filepath.suffix)

count = {x: desk_files.count(x) for x in desk_files}

with open("filecounts.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=[x for x in count.keys()])
    counts2 = list(reader)
print(counts2)





