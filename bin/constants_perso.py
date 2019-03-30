#################################################
# Constants declaration - personnal configuration
#################################################


# Need to modify the tag? It's there:
# tag = '€'


# 1. list of personnal LaTeX environnment whose content will be discard

# Ex. \begin{equation} ... \end{equation} will be replace by a tag
# Ex. \begin{itemize} ... \end{itemize} is not there and the content will be kept

list_env_discard_perso = []    # like ['equation','align*']



# 2. list of personnal LaTeX command with argument who will be totally will be discard

# Ex. \usepackage[option]{class} will be replace by a tag
# Ex. \emph{my text} is not there and the content will be kept

list_cmd_arg_discard_perso = ['ci','mybox']
