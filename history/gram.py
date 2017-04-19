import nltk
from nltk import ngrams

from nltk.tokenize import sent_tokenize,word_tokenize
example_text="Hello there, how are you doing today? The weather is great and python is awesome. The sky is pinkish-blue. You should not eat cardboard."
et="this is a foo bar sentences and i want to ngramize it this is a this is a a this is"
print(sent_tokenize(example_text))
print(word_tokenize(et))
tokens=word_tokenize(et)
bgs = nltk.bigrams(tokens)
n=3

sixgrams = ngrams(et.split(), n)
fdist = nltk.FreqDist(sixgrams)
for k,v in fdist.items():
    print (k,v)
