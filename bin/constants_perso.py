#################################################
# Constants declaration - personal configuration
#################################################


# Need to modify the tag? It's there:
# tag = '€'


# 1. list of personal LaTeX environments whose content will be discarded

# Ex. \begin{equation} ... \end{equation} will be replaced by a tag
# Ex. \begin{itemize} ... \end{itemize} is not there and the content will be kept

list_env_discard_perso = []    # like ['equation','align*']



# 2. list of personal LaTeX commands with arguments which will be totally discarded

# Ex. \usepackage[option]{class} will be replaced by a tag
# Ex. \emph{my text} is not there and the content will be kept

list_cmd_arg_discard_perso = ['ci','mybox']
