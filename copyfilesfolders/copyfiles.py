#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

# move into the working directory
os.chdir("/home/student/scripts/Python/mycode/copyfilesfolders/")

# copy the fileA to fileB
shutil.copy("srcdir/srcfile01.txt", "dstdir/srcfile_backup01.txt")

# copy the entire directoryA to directoryB
shutil.copytree("srcdir/", "dstdir_backup/")

