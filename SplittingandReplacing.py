#!/usr/bin/env python3

import re 

result = re.split(r"[.?!]", "One sentence. Another one? And the last one!")

print(result)

# using sub: substitution

result2 = re.sub(r"[\w.%+-]+@[\w.-]+", "[email-replaced]", "Received an email for lucian20sardanha23323@gmail.com")
print(result2)
 # 'backslashNumber' indicates the group> \3 \2 \1
result3 = re.sub(r"([\w .-]*), ([\w .-]*), ([0-9]*)$", r"\3 \2 \1", "Lovelace, Ada, 333" )
print(result3) #

result4= re.split(r"the|a", "One sentence. Another one? And the last one!")

print(result4) #['One sentence. Ano', 'r one? And ', ' l', 'st one!']
