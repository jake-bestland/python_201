# Add the code for the file counter script that you wrote in the course.
from pathlib import Path
import csv
from datetime import date


desktop = Path("/Users/jakebestland/Desktop")

desk_files = []

for filepath in desktop.iterdir():
    desk_files.append(filepath.suffix)

count = {x: desk_files.count(x) for x in desk_files}
today = date.today()
count['updated on'] = today.strftime("%m/%d/%Y")
print(count)


csvfile_path = Path("/Users/jakebestland/Desktop/filecounts.csv")

with open(csvfile_path.joinpath(), "a") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=count)
    writer.writeheader()
    writer.writerow(count)

# with open(csvfile_path.joinpath(), "a") as csvfile:
#     countwriter = csv.writer(csvfile)
#     data = [count[".py"], count[""], count[".png"], count[".txt"], count[".csv"]]
#     countwriter.writerow(data)

with csvfile_path.open() as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=[x for x in count.keys()])
    counts2 = list(reader)
print(counts2[-1])
