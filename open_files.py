import glob
import os
import shutil

curr_dir = os.path.realpath(os.curdir)
print(curr_dir)
print((os.path.realpath("d.toml")))
path, file = os.path.split(os.path.realpath("d.toml"))
print("path = ", path)
print("file = ", file)

-95
