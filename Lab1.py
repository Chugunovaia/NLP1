import nltk
from nltk.tokenize import word_tokenize
from nltk import sent_tokenize
nltk.download('punkt_tab')

f = open(r'text.txt')
text = f.read()

word_text=word_tokenize(text)
words=list(t for t in word_text )
print (words)

import pymorphy3
m = pymorphy3.MorphAnalyzer()

from itertools import pairwise


for first, second in pairwise(words):
    f=m.parse(first) [0]
    s=m.parse(second) [0]
    
    if f.tag.POS not in ('NOUN', 'ADJF'):
        continue
    else: 
        
        if (f.tag.POS =='NOUN'  and s.tag.POS =='ADJF' ) or (f.tag.POS =='ADJF'  and s.tag.POS =='NOUN' ):
            if (f.tag.gender == s.tag.gender or f.tag.gender=='neut' or s.tag.gender=='neut') and f.tag.number == s.tag.number and f.tag.case == s.tag.case:
                print (f.normal_form,  s.normal_form)
             
