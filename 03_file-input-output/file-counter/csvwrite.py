# Write the file counts to a `.csv` file.

import pathlib
import csv

desktop = pathlib.Path("/Users/jakebestland/Desktop")

desk_files = []

for filepath in desktop.iterdir():
    desk_files.append(filepath.suffix)

count = {x: desk_files.count(x) for x in desk_files}

with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[".py"], count[""], count[".png"], count[".txt"], count[".csv"]]
    countwriter.writerow(data)