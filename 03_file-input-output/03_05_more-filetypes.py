# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

from pathlib import Path
import csv

desktop = Path("/Users/jakebestland/Desktop")

desk_files = []

for filepath in desktop.iterdir():
    desk_files.append(filepath.suffix)

count = {x: desk_files.count(x) for x in desk_files}
#print(count)

file_path = Path("/Users/jakebestland/Desktop/filecounts.csv")

#### this will write the suffix for each item on a row above each count ####
### Therefore do not need to choose which files need to be recorded ###
with open(file_path.joinpath(), "a") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=count)
    writer.writeheader()
    writer.writerow(count)


# ## added ".html" and ".jpg" to filecounter ##
# with open(file_path.joinpath(), "a") as csvfile:
#     countwriter = csv.writer(csvfile)
#     data = [count[".py"], count[""], count[".png"], count[".txt"], count[".csv"], count[".html"], count[".jpg"]]
#     countwriter.writerow(data)

## added html and jpg
with file_path.open() as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["PY", "Folder", "PNG", "TXT", "CSV", "HTML", "JPG"])
    counts2 = list(reader)
#print(counts2)
print(counts2[-1])
