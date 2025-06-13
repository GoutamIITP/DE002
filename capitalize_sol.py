# capitalize: Task to make the first letter of every words as capital letter

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    capitalized_words = []
    
    for word in words:
        if word:
            capitalized_word = word[0].upper() + word[1:]
        else:
            capitalized_word = ''
        capitalized_words.append(capitalized_word)

    return ' '.join(capitalized_words)

 