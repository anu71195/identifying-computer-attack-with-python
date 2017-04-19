import nltk
import time
from time import time
from nltk import ngrams
timestamp=time();
a=[1,2,3,4,5,6,7,8,1,2]
single_grams=ngrams(a,3)
adata=[]
point_int={}
count=[]
index_count=0;
for grams in single_grams:
			try:
				if point_int[grams]>=0:
					passing=point_int[grams];
			except:
				passing=-1;
			if passing>=0:	
				ind=passing;
				count[ind]=count[ind]+1;	
			else:					
				data.append(grams)
				count.append(1)
				point_int[grams]=index_count;
				index_count=index_count+1;
print(point_int)
print(count)
print(time()-timestamp)
print(data)
#print(data)
##print(count)
#print(point_int)
#a={}
#a["4"]=4
##try:
#	print(a["4"])
#except:
#	pass