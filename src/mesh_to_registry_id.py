import sys
import os
from collections import defaultdict

infile = sys.argv[1]

current_mesh_id = ""
for line in os.popen("zcat " + infile + " | awk 'substr($0, 0, 16) == \"  <DescriptorUI>\" || substr($0, 0, 20) == \"    <RegistryNumber>\"' | sed 's/<DescriptorUI>/\\n/g'"):
    line = line.strip()
    if "DescriptorUI" in line:
        current_mesh_id = line.split("<")[0]
        continue
    if "RegistryNumber" in line:
        print(current_mesh_id + "\t" + line.split(">")[1].split("<")[0])

