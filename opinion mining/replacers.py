#!/usr/bin/env python

#!/usr/bin/env python

#!/usr/bin/env python

import re
import enchant
from nltk.metrics import edit_distance
replacement_patterns = [
        (r'won\'t', 'will not'),
        (r'can\'t', 'cannot'),
        (r'i\'m', 'i am'),
        (r'ain\'t', 'is not'),
        (r'(\w+)\'ll', '\g<1> will'),
        (r'(\w+)n\'t', '\g<1> not'),
        (r'(\w+)\'ve', '\g<1> have'),
        (r'(\w+t)\'s', '\g<1> is'),
        (r'(\w+)\'re', '\g<1> are'),
        (r'(\w+)\'d', '\g<1> would'),
        (r'(\w+)\'d', '\g<1> would')
        ]
class RegexpReplacer(object):
    def __init__(self, patterns=replacement_patterns):
                self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replace(self, line):
                s = line

                for (pattern, repl) in self.patterns:
                        (s, count) = re.subn(pattern, repl, s)

                return s
class SpellingReplacer(object):
    def __init__(self, dict_name='en', max_dist=2):
        self.spell_dict = enchant.Dict(dict_name)
        self.max_dist = 2
    def replace(self,word):
        if self.spell_dict.check(word):
            return word
        suggestions = self.spell_dict.suggest(word)
        if suggestions and edit_distance(word, suggestions[0]) <=self.max_dist:
            return suggestions[0]
        else:
            return word
        