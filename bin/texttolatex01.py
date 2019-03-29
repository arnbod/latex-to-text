#!/usr/bin/env python3

# Convert a text file + a dicttionnary file to a LaTeX file
# Usage : 'python3 texttolatex.py toto.txt'
# or 'python3 texttolatex.py toto.txt toto.dic'
# or 'python3 texttolatex.py toto.txt toto.dic new_toto.tex'
# Output : create a file toto.tex (or new_toto.tex)

import argparse
import re
import sys
import os
import yaml
from constants import *

#--------------------------------------------------
#--------------------------------------------------
# Arguments 

parser = argparse.ArgumentParser(description='Conversion a text file to a LaTeX gluing back commands and maths.')
parser.add_argument('inputfile', help='input text filename')
parser.add_argument('outputfile', nargs='?', help='output LaTeX filename')
parser.add_argument('dicfile', nargs='?', help='input dictionnary filename')
options = parser.parse_args()

#print(options.inputfile)
#print(options.outputfile)


txt_file = options.inputfile
output_file = options.outputfile
dictionnary_file = options.dicfile

# Get argument : a tex file
file_name, file_extension = os.path.splitext(txt_file) 


# Output file name 
if output_file:
    tex_file = output_file    # Name given by user
else:
    tex_file = file_name+'.tex' # If no name add a .tex extension


# Dictionnary file name 
if dictionnary_file:
    dic_file = dictionnary_file    # Name given by user
else:
    dic_file = file_name+'.dic' # If no name add a .dic extension



# Read file object to string
fic_txt = open(txt_file, 'r', encoding='utf-8')
text_all = fic_txt.read()
fic_txt.close()
# print(text_all)


# Read dictionnary
fic_dic = open(dic_file, 'r', encoding='utf-8')
dictionnary = yaml.load(fic_dic)
fic_dic.close()

# count = len(dictionnary)  # Nb of replacements
# print(dictionnary)

text_new = text_all

for i,val in dictionnary.items():
    tag_str = tag+str(i)+tag
    val = val.replace('\\','\\\\')    # double \\ for correct write
    # val = re.escape(val)
    text_new = re.sub(tag_str,val,text_new, flags=re.MULTILINE|re.DOTALL)


with open(tex_file, 'w', encoding='utf-8') as fic_tex:
    fic_tex.write(text_new)


