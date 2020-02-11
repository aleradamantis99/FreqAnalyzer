#!/usr/bin/python3.7

import re, sys
from unicodedata import normalize

filename = sys.argv[1]
pat = re.compile(r'[^a-zA-Z ñÑáéíóúüÁÉÍÓÚÜ]+')
with open(filename) as f:
        for l in f:
            l = re.sub(pat, '', l).lower()
            if not l:
                continue
            #Source: https://es.stackoverflow.com/questions/135707/c%C3%B3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l
            l = re.sub(
                    r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                    normalize( "NFD", l), 0, re.I
                )

            # -> NFC
            l = normalize( 'NFC', l)
            print(l)
