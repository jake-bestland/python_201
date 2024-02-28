# Add the code for the file counter script that you wrote in the course.
import pathlib

desktop = pathlib.Path("/Users/jakebestland/Desktop")

desk_files = []

for filepath in desktop.iterdir():
    desk_files.append(filepath.suffix)

desk_dict = {x: desk_files.count(x) for x in desk_files}
print(desk_dict)