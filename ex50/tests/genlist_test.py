import sys 
import os

cwd = os.getcwd()

sys.path.append(cwd)

from generate_list import printIt


for count in range(0, 1000):
    printIt()