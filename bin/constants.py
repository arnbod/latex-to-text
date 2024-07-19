########################
# Constants declaration
########################

# YOU SHOULD NOT MODIFY THIS FILE
# USE 'constants_perso' to declare your modifications

# the tag for replacement
tag = '€'


# 1. list of LaTeX environments whose content will be discarded

# Ex. \begin{equation} ... \end{equation} will be replaced by a tag
# Ex. \begin{itemize} ... \end{itemize} is not there and the content will be kept

list_env_discard = ['equation',
					'equation*',
					'align',
					'align*',
					'multline',
					'multline*',
					'lstlisting'
					]

# Add your personal environment in 'constants_perso.py'


# 2. list of LaTeX commands with arguments which will be totally discarded

# Ex. \usepackage[option]{class} will be replaced by a tag
# Ex. \emph{my text} is not there and the content will be kept

list_cmd_arg_discard = ['usepackage',
						'documentclass',
						'begin',
						'end',
						'includegraphics',
						'label',
						'ref',
						'eqref',
						'cite'
						]

# Add your personal commands in 'constants_perso.py'
