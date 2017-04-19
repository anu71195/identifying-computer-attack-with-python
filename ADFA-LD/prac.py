import nltk
from nltk import ngrams
listing=[1,2,3,4,5,6,7,8]
featurelist=[]

single_grams=ngrams(listing,3)
temp=[]
for grams in single_grams:
	temp.append(grams)
featurelist.append(temp)

single_grams=ngrams(listing,5)
temp=[]
for grams in single_grams:
	temp.append(grams)
featurelist.append(temp)

single_grams=ngrams(listing,7)
temp=[]
for grams in single_grams:
	temp.append(grams)
featurelist.append(temp)

#print(featurelist)
test=[1,2,3,4,2,3,5,1,3,2,4,5,1,2,4,5,1]
single_grams=ngrams(test,3)
temp=[]
for grams in single_grams:
	temp.append(str(grams))
#print(temp)
mydictionary={}
counter=0;
for j in featurelist[0]:
	mydictionary[str(j)]=counter
	counter=counter+1;
#print(mydictionary)
print(featurelist[0])
count=[0 for x in range(len(featurelist[0])) ]
#print(len(mydictionary))
#print(len(count))
print(mydictionary)
print(mydictionary['(5, 6, 7)'])
for grams in temp:
	print(grams)
	try:
		if mydictionary[grams]>=0:
			flag=1;
	except:
			flag=0;
	if flag==1:
		ind=mydictionary[grams];
		print("ind is",ind)
		count[ind]=count[ind]+1;

print(count)

#if string in featurelist[featureindex]:				
#	ind=featurelist[featureindex].index(string);
#	count[ind]=count[ind]+1;
