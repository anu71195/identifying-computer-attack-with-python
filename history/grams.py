import nltk
from nltk import ngrams
import math
sentence = 'this is a foo bar sentences and i want to ngramize it this is a this is a a this is'
n = 3
sixgrams = ngrams(sentence.split(), n)
i=0;
data=[];
count=[];
for grams in sixgrams:
 	i=i+1
 	print (grams);
 	if grams in data:
 		count[data.index(grams)]=count[data.index(grams)]+1;
 	else:
 		count.append(1);
 		data.append(grams);

print(i)
fdist = nltk.FreqDist(sixgrams)
print("\n\n")
for k,v in fdist:
    print (k,v)
    print("here")

print("\n\n")
print(fdist)
print(data)
print(count)

for i in range(len(data)):
	print(data[i],end=" ")
	print(count[i])
	data[i]
print("\n")
itera=math.ceil(len(data)*3/10)
print(itera)

for i in range(itera):
	print(data[i])


