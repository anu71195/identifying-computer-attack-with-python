import os;
import nltk
from nltk import ngrams
fr1=open("3grams_features.txt","r")
fr2=open("5grams_features.txt","r")
fr3=open("7grams_features.txt","r")
text1=fr1.read();
text2=fr2.read();
text3=fr3.read();
text1=text1.split("\n")
text2=text2.split("\n")
text3=text3.split("\n")
text1.pop(-1)
text1.pop(-1)
text2.pop(-1)
text2.pop(-1)
text3.pop(-1)
text3.pop(-1)
fr1.close()
fr2.close()
fr3.close()
count1=[0 for i in range(len(text1))]
#print(text2)
#print(len(text1),len(text2),len(text3))
cwd0=os.getcwd();
#print(cwd0)
for sub0,fold0,file0 in os.walk(cwd0):
	if len(fold0)>0:
		break;
#print(fold0)
fold0.sort();
cwd1=cwd0+"/"+fold0[0];
#print(cwd1)
os.chdir(cwd1)
for sub1,fold1,file1 in os.walk(cwd1):
	if len(fold1)>0:
		break;
fold1.sort()

for folder in fold1:
	if '8' in folder  or '9' in folder or '10' in folder:
		#print(folder);
		cwd2=cwd1+"/"+folder
		os.chdir(cwd2);
		#print(os.getcwd())
		for sub2,fold2,file2 in os.walk(cwd2):
			pass;
		#print(file2)
		for files in file2:
			#print(files)
			fr=open(files,"r")
			text=fr.read()
			#print(text)
			fr.close();
			all_grams=ngrams(text.split(),3)
			#print(text1)
			for grams in all_grams:
				#print(grams[0])
				str=grams[0]+" "+grams[1]+" "+grams[2]+" "
				#print(str)
				if str in text1:
					#print("true")
					ind=text1.index(str);
					count1[ind]=count1[ind]+1;
				#else:
					#print("false")
			

print(count1)
cwd1=cwd0+"/"+fold0[2];
print(cwd1)
os.chdir(cwd1)

