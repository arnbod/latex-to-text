#!/usr/bin/env python3

# Convert a LaTeX file to txt file
# Usage : 'python3 latextotext.py toto.tex'
# Output : create a file toto.txt and a file toto.dic


# Author: Arnaud Bodin. Thanks to Kroum Tzanev
# Idea from Mr.Sh4nnon https://codereview.stackexchange.com/questions/209049
# Licence CC-BY-SA 4.0

import argparse
import re
import sys
import os
import yaml
from constants import *    # Definition of the tag symbol and special commands/environments
from constants_perso import *  # Personal customization

#--------------------------------------------------
#--------------------------------------------------

# Arguments 
parser = argparse.ArgumentParser(description='Conversion a LaTex file to a text file keeping apart commands and maths.')
parser.add_argument('inputfile', help='input LaTeX filename')
parser.add_argument('outputfile', nargs='?', help='output text filename')
parser.add_argument('dicfile', nargs='?', help='output dictionary filename')
options = parser.parse_args()

tex_file = options.inputfile
output_file = options.outputfile
dictionary_file = options.dicfile


# Get argument: a tex file
file_name, file_extension = os.path.splitext(tex_file) 


# Output file name 
if output_file:
    txt_file = output_file    # Name given by user
else:
    txt_file = file_name+'.txt' # If no name add a .txt extension


# Dictionary file name 
if dictionary_file:
    dic_file = dictionary_file    # Name given by user
else:
    dic_file = file_name+'.dic' # If no name add a .dic extension


# Read file object to string
fic_tex = open(tex_file, 'r', encoding='utf-8')
text_all = fic_tex.read()
fic_tex.close()

# Real stuff starts there!
# Replacement function pass as the replacement pattern in re.sub()

count = 0           # counter for tags
dictionary = {}    # memorize tag: key=nb -> value=replacement

def func_repl(m):
    """ Function called by sub as replacement pattern given by output
    Input: the pattern to be replaced
    Ouput: the new pattern
    Action: also update the dictionary of tags/replacement
    and increment the counter
    https://stackoverflow.com/questions/33962371"""
    global count
    dictionary[count] = m.group(0)  # Add old string found to the dic
    tag_str = tag+str(count)+tag     # tag = '€' is defined in 'constants.py'
    count += 1   
    return tag_str                   # New string for pattern replacement


# Now we replace case by case math and commands with tags
text_new = text_all

# Done first, to prevent accidentally replacing commented Latex code later
# Replace %LINE but not \%
text_new = re.sub(r'(?<!\\)%.*',func_repl,text_new)

# Replace LaTeX newlines with optional argument, e.g. r'\\[-0.2cm]'
text_new = re.sub(r'\\\\\[.*\]',func_repl,text_new)
# Done here to avoid a bug below when replacing r'\[ ... \]'


### PART 1 - Replacement of maths ###

# $$ ... $$
text_new = re.sub(r'\$\$(.+?)\$\$',func_repl,text_new, flags=re.MULTILINE|re.DOTALL)
# $ ... $
text_new = re.sub(r'\$(.+?)\$',func_repl,text_new, flags=re.MULTILINE|re.DOTALL)
# \( ... \)
text_new = re.sub(r'\\\((.+?)\\\)',func_repl,text_new, flags=re.MULTILINE|re.DOTALL)
# \[ ... \]
text_new = re.sub(r'\\\[(.+?)\\\]',func_repl,text_new, flags=re.MULTILINE|re.DOTALL)


### PART 2 - Discard contents of some environments ###

for env in list_env_discard + list_env_discard_perso:
    # escape *, e.g. replace r'align*' by r'align\*'
    env = re.sub(r'\*', r'\*', env)
    str_env = r'\\begin\{' + env + r'\}(.+?)\\end\{' + env + r'\}'
    text_new = re.sub(str_env,func_repl,text_new, flags=re.MULTILINE|re.DOTALL)


### PART 3 - Replace \begin{env} and \end{env} but not its contents

text_new = re.sub(r'\\begin\{(.+?)\}',func_repl,text_new, flags=re.MULTILINE|re.DOTALL)
text_new = re.sub(r'\\end\{(.+?)\}',func_repl,text_new, flags=re.MULTILINE|re.DOTALL)


### PART 4 - Replacement of LaTeX commands with their argument ###

for cmd in list_cmd_arg_discard + list_cmd_arg_discard_perso:
    # Without opt arg, ex. \cmd{arg}
    str_env = r'\\' + cmd + r'\{(.+?)\}'
    text_new = re.sub(str_env,func_repl,text_new, flags=re.MULTILINE|re.DOTALL)
    # With opt arg, ex. \cmd[opt]{arg}
    str_env = r'\\' + cmd + r'\[(.*?)\]\{(.+?)\}'
    text_new = re.sub(str_env,func_repl,text_new, flags=re.MULTILINE|re.DOTALL)


### PART 5 - Replacement of LaTeX remaining commands (but not their argument) ###

text_new = re.sub(r'\\[a-zA-Z]+',func_repl,text_new, flags=re.MULTILINE|re.DOTALL)


### PART 6 - Save space on tags and whitespace

# replace at least n consecutive whitespace characters with a tag (and leave one whitespace character unchanged)
n = 1 + len(tag + str(count) + tag)
text_new = re.sub(r'\s{' + str(n) + r',}(?=\s)',func_repl,text_new, flags=re.MULTILINE|re.DOTALL)

# replace consecutive tags with one tag (even if separated by whitespace)
regexp_tag = tag + r'\d+' + tag
regexp = regexp_tag + r'(\s*' + regexp_tag + r')+'
text_new = re.sub(regexp,func_repl,text_new)


# Output: text file
with open(txt_file, 'w', encoding='utf-8') as fic_txt:
    fic_txt.write(text_new)

# Output: dictionary file
with open(dic_file, 'w', encoding='utf-8') as fic_dic:
    yaml.dump(dictionary,fic_dic, default_flow_style=False,allow_unicode=True)
