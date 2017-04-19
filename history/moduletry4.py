import os;
import nltk
import math;
from nltk import ngrams
featurelist=[];
os.system("rm -rf output")
for i in [3,5,7]:			#getting data form all the files iteratively about the features and putting them in the featurelist
	filename=str(i)+"grams_features.txt";
	fr=open(filename,"r");
	text=fr.read();
	text=text.split("\n")
	for j in range(2):
		text.pop(-1)			#removing the last empty value
	fr.close()
	featurelist.append(text)
print(len(featurelist))
cwd0=os.getcwd();				#getting the current directory(home directory)
for sub0,fold0,file0 in os.walk(cwd0):	#getting the data about the contents in the current folder
	if len(fold0)>0:
		break;
#print(fold0)
os.system("mkdir output")
fold0.sort();					#sorting the folders in ascending order
cwd1=cwd0+"/"+fold0[0];
os.chdir(cwd1)	
for sub1,fold1,file1 in os.walk(cwd1):	#getting the data about the contents in the current folder
	if len(fold1)>0:
		break;
fold1.sort()				#sorting the folders in ascending order
out_dir=cwd0+"/output"		#creating output folder in the main folder
os.chdir(out_dir)
os.system("mkdir Attack_Data_Master")	#creating attack data master folder in output folder
for folder in fold1:		#recursing over all the folders in attack
	if '8' in folder  or '9' in folder or '10' in folder:	#recursing over 30%of the folders in it
		out_dir=cwd0+"/output/Attack_Data_Master"
		os.chdir(out_dir)
		print(folder)

		making="mkdir "+folders#creating all the attack folder iteratively
		os.system(making)
		cwd2=cwd1+"/"+folder
		os.chdir(cwd2);
		print(cwd2)
		for sub2,fold2,file2 in os.walk(cwd2):#rgetting the data over all the files
			if len(file2)>0:
				break;
			pass;
		for files in file2:				#recursing over all the files
			fr=open(files,"r")
			text=fr.read()
			fr.close();
			for i in [3,5,7]:			#recursing all the files over 3,5and 7 grams
				featureindex=math.floor(i/2)-1	#normalizing index with respect to i
				count=[0 for x in range(len(featurelist[featureindex])) ]
				single_grams=ngrams(text.split(),i)
				for grams in single_grams:		#recursing over the ngrams generated and counting them
					string=grams[0]+" ";
					for j in range(1,i):
						string=string+grams[j]+" ";
					if string in featurelist[featureindex]:
						#print("true")
						ind=featurelist[featureindex].index(string);
						count[ind]=count[ind]+1;
					#else:
					#	print("false")
				filename=str(i)+"gramsfrequency_"+files		
				print(filename)
				out_dir=cwd0+"/output/Attack_Data_Master/"+folder;
				os.chdir(out_dir)						
				fw=open(filename,"a")					##########################################################afterwards change it to append##################################################
				for frequency in range(len(count)):		#writing the feature and frequenycy of it in the files
					fw.write(featurelist[featureindex][frequency])
					fw.write("----->")
					fw.write("Frequency of F")
					fw.write(frequency)
					fw.write("----->")
					fw.write(str(count[frequency]))
					fw.write("\n")
				os.chdir(cwd2)

cwd1=cwd0+"/"+fold0[2];
out_dir=cwd0+"/output"
os.chdir(out_dir)
os.system("mkdir Validation_Data_Master")#making validation data master folder in output folder
print(cwd1)
os.chdir(cwd1)
for sub1,fold1,files1 in os.walk(cwd1):	#collecting data from validation data master folder
	pass;
print(files1)
#print(files1)
#print(fold1)
for files in files1:		#recursing over all the files in validation data master
	#print(files)
	if files==".DS_Store":
		continue;
	fr=open(files,"r")
	text=fr.read();
	fr.close();
	for i in [3,5,7]:			#recursing over the 3,5,7 grams in the files in validatoin data master
		featureindex=math.floor(i/2)-1
		count=[0 for x in range(len(featurelist[featureindex])) ]
		single_grams=ngrams(text.split(),i);
		for grams in single_grams:		
			string=grams[0]+" ";
			for j in range(1,i):
				string=string+grams[j]+" ";
			if string in featurelist[featureindex]:
				ind=featurelist[featureindex].index(string);
				count[ind]=count[ind]+1;				#counting the frequency of features
		filename=str(i)+"gramsfrequency_"+files
		print(filename)
		out_dir=cwd0+"/output/Validation_Data_Master"
		os.chdir(out_dir)						
		fw=open(filename,"a")					##########################################################afterwards change it to append##################################################
		for frequency in range(len(count)):			#writing the features and frequency of it in the files
			fw.write(featurelist[featureindex][frequency])
			fw.write("----->")
			fw.write("Frequency of F")
			fw.write(frequency)
			fw.write("----->")
			fw.write(str(count[frequency]))
			fw.write("\n")
		os.chdir(cwd1)

		
		