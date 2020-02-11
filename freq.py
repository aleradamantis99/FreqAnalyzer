#!/usr/bin/python3.7

import re, sys
from unicodedata import normalize
import matplotlib.pylab as plt
from json import dump

def show_data(d, top=None):
    normalize_values(d)
    print_dict_sorted(d)
    plot_dict(d)

def normalize_values(d, total = None):
    if total is None:
        total = sum(d.values())
    d.update((x, (y/total)*100) for x, y in d.items())

def print_dict_sorted(d):
    print (sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))

def plot_dict(d, sort_by_key=False):
    #lists = sorted(d.items()) # sorted by key, return a list of tuples
    lists = sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    x, y = zip(*(lists[:50])) # unpack a list of pairs into two tuples

    plt.bar(x, y)
    plt.show()

filename = "text.txt"
if len(sys.argv) > 1:
    filename = sys.argv[1]

letter_freq = {}
bin_freq = {}
trio_freq = {}
try:
    with open(filename) as f:
        for l in f:
            l = l.split()
            
            for w in l:
                for i, c in enumerate(w):
                    if c in letter_freq:
                        letter_freq[c] += 1
                    else:
                        letter_freq[c] = 1
                    if i+1 < len(w):
                        pair = c+w[i+1]
                        
                        if pair in bin_freq:
                            bin_freq[pair] += 1
                        else:
                            bin_freq[pair] = 1
                        if i+2 < len(w):
                            tri = pair+w[i+2]
                            if tri in trio_freq:
                                trio_freq[tri] += 1
                            else:
                                trio_freq[tri] = 1
except IOError as e:
    print ("Error with file {}: {}".format(filename, e.strerror))

show_data(letter_freq)
print()
show_data(dict((x, y) for x, y in bin_freq.items() if x[0] == 'e'))
show_data(bin_freq)
show_data(trio_freq)
