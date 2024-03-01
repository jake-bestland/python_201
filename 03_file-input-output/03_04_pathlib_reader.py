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
print(count)

file_path = Path("/Users/jakebestland/Desktop/filecounts.csv")

with file_path.open() as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["PY", "Folder", "PNG", "TXT", "CSV"])
    counts2 = list(reader)
print(counts2)
print(counts2[-1])


# with open(file_path.joinpath(), "a") as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=count)
#     writer.writeheader()
#     writer.writerow(count)