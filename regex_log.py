#!/usr/bin/env python3

import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[0])
print(result[1])
# create a function to be used in case we don't have numbers between ()
#for that we are using PID

log1 = "July 31 07:51:48 mycomputer bad_process[34567]: ERROR Performing package upgrade"
log2 = "July 31 07:51:48 mycomputer bad_process[letters]: ERROR Performing package upgrade"
def extract_pid(log_line):
    regex = r"\[(\d+)]"
    result  = re.search(regex, log_line)
    if result is None:
        return "None"
    return result[1]
print(extract_pid(log1))
print(extract_pid(log2))



