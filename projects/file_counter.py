# Add the code for the file counter script that you wrote in the course.
import pathlib
import csv

desktop = pathlib.Path("/Users/jakebestland/Desktop")

desk_files = []

for filepath in desktop.iterdir():
    desk_files.append(filepath.suffix)

count = {x: desk_files.count(x) for x in desk_files}
print(count)

# data = f"{count[""]}, {count[".py"]}, {count[".png"]}, {count[".txt"]}, {count[".csv"]}"
# file_out = open("filecounts.csv", "a")
# file_out.write(f"{data}")
# file_out.write("\n")
# file_out.close()

# file_in = open("output.txt", "r")
# contents = file_in.read()
# print(contents)
# file_in.close()

with open("filecounts.csv", "a") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=count)
    writer.writeheader()
    writer.writerow(count)
    
    # countwriter = csv.writer(csvfile)
    # data = [count[""], count[".py"], count[".png"], count[".txt"], count[".csv"]]
    # countwriter.writerow(data)

# # file_out = open("filecounts.csv", "a")
# # file_out.write(str(count))
# with open("filecounts.csv", "a") as csvfile:
#     countwriter = csvfile.writer(count)
#     data = [count[""], count[".py"], count[".png"], count[".txt"], count[".csv"]]
#     countwriter.writerow(data)