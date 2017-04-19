import os;
import nltk
import math;
from nltk import ngrams
featurelist=[];
for i in [3,5,7]:
	filename=str(i)+"grams_features.txt";
	fr=open(filename,"r");
	text=fr.read();
	text=text.split("\n")
	for j in range(2):
		text.pop(-1)
	fr.close()
	#print(text)
	featurelist.append(text)
print(featurelist)

#print(featurelist)
print(len(featurelist))
cwd0=os.getcwd();
for sub0,fold0,file0 in os.walk(cwd0):
	if len(fold0)>0:
		break;
fold0.sort();
cwd1=cwd0+"/"+fold0[0];
os.chdir(cwd1)
for sub1,fold1,file1 in os.walk(cwd1):
	if len(fold1)>0:
		break;
fold1.sort()
for folder in fold1:
	if '8' in folder  or '9' in folder or '10' in folder:
		cwd2=cwd1+"/"+folder
		os.chdir(cwd2);
		for sub2,fold2,file2 in os.walk(cwd2):
			pass;
		for files in file2:				#recursing over all the files
		#	print(files)
			fr=open(files,"r")
			text=fr.read()
			fr.close();
			for i in [3,5,7]:
				featureindex=math.floor(i/2)-1
				count=[0 for x in range(len(featurelist[featureindex])) ]
				single_grams=ngrams(text.split(),i)
				for grams in single_grams:
		#			print(grams);
					string=grams[0]+" ";
					for j in range(1,i):
						string=string+grams[j]+" ";
					if string in featurelist[featureindex]:
						print("true")
						ind=featurelist[featureindex].index(string);
						count[ind]=count[ind]+1;
					else:
						print("false")
				filename=str(i)+"gramsfrequency_"+files
				print(filename)
				os.chdir(cwd0)
				fw=open(filename,"w")
				for frequency in range(len(count)):
					#for k in range(i):
					fw.write(featurelist[featureindex][frequency])
					fw.write("----->")
					fw.write(str(count[frequency]))
					fw.write("\n")
				os.chdir(cwd2)

		
		