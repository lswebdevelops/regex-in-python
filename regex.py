#!/usr/bin/env python3
#  for now it is just working on the python terminal, not as a script
import re
def redo_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
            return name
    return "{} {}".format(result[2], result[1])
print(redo_name("Sardanha, Luciano F."))
