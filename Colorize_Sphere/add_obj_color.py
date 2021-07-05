import os, sys
import math
import random

def generate_random_color():
    return [random.random(), random.random(), random.random()]
    

if __name__ == "__main__":
    # change current working directory
    os.chdir(sys.path[0])
    # open obj file
    with open("105.obj", 'r') as in_file, open("105_color.obj", 'w') as out_file:
        for line in in_file:
            data = line.split()
            if data[0] == "v":
                color = generate_random_color()
                data.extend(color)
            for item in data:
                out_file.write("%s " % item)
            out_file.write("\n")