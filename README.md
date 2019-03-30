
Latex to text (help to translation)
===================================


* Use 'python3 latextotext.py toto.tex' to get transform a LaTeX file to a text file 'toto.txt'. You will get an additionnal dictionnary 'toto.dic'.

* Don't panic if you see lots of tags '€1234€', they replace maths and LaTeX commands!  

* Use automatic translation on the text file, for instance use [DeepL Translator]( https://www.deepl.com/translator), save the file in your target langage as 'new_toto.txt'

* Recover your LaTeX file with 'python3 texttolatex.py new_toto.txt toto.dic', you will get a
file 'new_toto.tex' in your target langage with your original maths.

