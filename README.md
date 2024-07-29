
Latex to text (help to translation)
===================================

Let's translate
---------------

Do you need to translate your work in LaTeX into a foreign language? Don't have the time or skills to do it? Why not let a computer do it for you?

Machine translation has made huge progress and the text produced is quite good.

Issue with maths
----------------

However automatic translators don't like mathematics and LaTeX file. We provide here a tool to hide mathematics to the machine so that you can translate any scientific text from one language to another.


It works!
---------

These tools have been used to translate the book *Python au lycée* to *Python in high school*, more than 200 pages, in 15 workdays. See [GitHub Exo7](https://github.com/exo7math).



Requirements
------------

* Your original LaTeX file,

* a Python3 installation and all the Python files you will find in the `bin/` directory, 

* and a translator like [DeepL Translator](https://www.deepl.com/translator) or [Google Translate](https://translate.google.com/).


Operations
----------

* Use `python3 latextotext.py toto.tex` to transform a LaTeX file to a text file `toto.txt`. You will get an additional dictionary `toto.dic`.

* Don't panic if you see lots of tags `€1234€`, they replace maths and LaTeX commands!  

* Use automatic translation on the text file, I recommend [DeepL Translator](https://www.deepl.com/translator), save the file in your target langage as `new_toto.txt`.

* Recover your LaTeX file with `python3 texttolatex.py new_toto.txt toto.dic`, you will get a
file `new_toto.tex` in your target langage with your original maths.

* You certainly need to check and correct the translation.


Example
-------

1. Start from a file `maths.tex` written in French:
```
	...
	Soient $f$ et $g$ deux fonctions continues de $\mathbf{R}$ vers $\mathbf{C}$.
	...
```


2. Execute `python3 latextotext.py maths.tex`.

3. You will get a file `maths.txt`:
```
	...
	Soient €0€ et €1€ deux fonctions continues de €2€ vers €3€.
	...
```

4. And a file `maths.dic`:
```
	0: $f$
	1: $g$
	2: $\mathbf{R}$
	3: $\mathbf{C}$
```

5. Translate the file `maths.txt` to English using DeepL and name the translation `new_math.txt`:
```
	...
	Let be €0€ and €1€ two continuous functions from €2€ to €3€.
	...
```

6. Execute `python3 texttolatex.py new_maths.txt maths.dic` to get a file `new_maths.tex`:
```
	...
	Let be $f$ and $g$ two continuous functions from $\mathbf{R}$ to $\mathbf{C}$.
	...
```

7. Adjust the translation by hand:
```
	...
	Let $f$ and $g$ be two continuous functions from $\mathbf{R}$ to $\mathbf{C}$.
	...
```

Advice if you use ChatGPT for translation
-----------------------------------------

* The size limit for a message to ChatGPT-4o seems around 6500-8500 characters. Above the limit, ChatGPT-4o usually hallucinates or freezes. Below the limit, ChatGPT-4o can still occasionally hallucinate, replacing a tag with another tag: you should check your translated pdf carefully!

* You may need to repeat the instructions to ChatGPT in every message, since ChatGPT's memory seems around 8000 characters.

* You may manage to use ChatGPT to translate LaTeX files without this software. Yet, this software can save characters, thus reduce ChatGPT usage. This can save you time and be more ecological (since ChatGPT consumes a fair amount of energy).

* You can adapt and use the prompt below.

````
Translate from French to English extracts from my article about mathematics.
Do not replace the patterns €number€. They are tags standing for LaTeX code.
When punctuation seems missing after a tag, it's probably part of what the tag stands for.
So, DO NOT add missing punctuation after a tag.
Your output will be encapsulated in blockquote markdown (```like this```).
Consider using the following dictionary, in the format "{original:correct translation}", updated from your previous mistranslations.
{
partie:subset
Abélien:Abelian
application:map
noté:denoted by
}
##
```
Text to translate.
```
````

