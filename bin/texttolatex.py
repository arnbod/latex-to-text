#!/usr/bin/env python3

# Convert a text file + a dictionary file to a LaTeX file
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
from constants_perso import *  # Personal customization

#--------------------------------------------------
#--------------------------------------------------

# Arguments 
parser = argparse.ArgumentParser(description='Conversion a text file to a LaTeX gluing back commands and maths.')
parser.add_argument('inputfile', help='input text filename')
parser.add_argument('dicfile', nargs='?', help='input dictionary filename')
parser.add_argument('outputfile', nargs='?', help='output LaTeX filename')
options = parser.parse_args()

txt_file = options.inputfile
output_file = options.outputfile
dictionary_file = options.dicfile


# Get argument: a txt file
file_name, file_extension = os.path.splitext(txt_file) 


# Dictionary file name 
if dictionary_file:
    dic_file = dictionary_file    # Name given by user
else:
    dic_file = file_name+'.dic' # If no name add a .dic extension


# Output file name 
if output_file:
    tex_file = output_file    # Name given by user
else:
    tex_file = file_name+'.tex' # If no name add a .tex extension

# Read file object to string
fic_txt = open(txt_file, 'r', encoding='utf-8')
text_all = fic_txt.read()
fic_txt.close()


# Read dictionary
fic_dic = open(dic_file, 'r', encoding='utf-8')
dictionary = yaml.load(fic_dic, Loader=yaml.BaseLoader)
fic_dic.close()


# Replacements start now
text_new = text_all

# Iterate replacing until nothing remains to be replaced
# (to deal with nested replacements)
keep_replacing = True
k = 0
while keep_replacing:
    keep_replacing = False
    for i,val in dictionary.items():
        tag_str = tag+str(i)+tag
        val = val.replace('\\','\\\\')    # double \\ for correct write
        # val = re.escape(val)
        (text_new, number_of_subs_made) = re.subn(tag_str,val,text_new, flags=re.MULTILINE|re.DOTALL)
        if number_of_subs_made > 0:
            keep_replacing = True
    k += 1
# print(f'{k} iteration(s) done.')

# Write the result
with open(tex_file, 'w', encoding='utf-8') as fic_tex:
    fic_tex.write(text_new)


