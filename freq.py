#!/usr/bin/python3.7

import re
filename = "hola.txt"
pat = re.compile(r'[^a-zA-Z ]+')
letter_freq = {}
bin_freq = {}

with open(filename) as f:
    for l in f:
      l = re.sub(pat, '', l).lower().split()
      for w in l:
        for i, c in enumerate(w):
          letter_freq[c] += 1
          if i+1<w.len():
            bin_freq[c+w[i+1]] += 1
