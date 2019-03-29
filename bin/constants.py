########################
# Constants declaration
########################


# the tag for replacement
tag = '€'


# 1. list of LaTeX environnment whose content will be discard

# Ex. \begin{equation} ... \end{equation} will be replace by a tag
# Ex. \begin{itemize} ... \end{itemize} is not there and the content will be kept

# DO NOT MODIFY 
list_env_discard = ['equation',
					'equation*',
					'align',
					'align*',
					'lstlisting'
					]

# Add you personnal environnment their
list_env_discard_perso = []

# 2. list of LaTeX command with argument who will be totally will be discard

# Ex. \usepackage[option]{class} will be replace by a tag
# Ex. \emph{my text} is not there and the content will be kept

list_cmd_arg_discard = ['usepackage',
						'documentclass',
						'begin',
						'end',
						'includegraphics'
						]

list_cmd_arg_discard_perso = ['ci','mybox','index']
