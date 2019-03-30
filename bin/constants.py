########################
# Constants declaration
########################

# YOU SHOULD MODIFY THIS FILE
# USE 'constants_perso' to declare your modifications

# the tag for replacement
tag = '€'


# 1. list of LaTeX environnment whose content will be discard

# Ex. \begin{equation} ... \end{equation} will be replace by a tag
# Ex. \begin{itemize} ... \end{itemize} is not there and the content will be kept

list_env_discard = ['equation',
					'equation*',
					'align',
					'align*',
					'lstlisting'
					]

# Add you personnal environnment in 'constants_perso.py'


# 2. list of LaTeX command with argument who will be totally will be discard

# Ex. \usepackage[option]{class} will be replace by a tag
# Ex. \emph{my text} is not there and the content will be kept

list_cmd_arg_discard = ['usepackage',
						'documentclass',
						'begin',
						'end',
						'includegraphics',
						'label',
						'ref',
						'cite'
						]

# Add you personnal commands in 'constants_perso.py'
