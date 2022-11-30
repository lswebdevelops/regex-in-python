#!/usr/bin/env python3

import re 
#result = re.search(r"[a-zA-Z]{5}", "a ghost")
#print(result)
#print(result[0])

result2 = re.findall(r"[\w]{5,10}", "a scary ghost appeared")
print(result2)

result3 = re.findall(r"[\w]{,10}", "a scary ghost appeared")
print(result3)
result5 = re.findall(r"[\w]{5,}", "a scary ghost appeared")
print(result5)
result4 = re.findall(r"[\w]{5}", "a scary ghost appeared")
print(result4)

def long_words(text):
  pattern = r"[\w]{7,9}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

