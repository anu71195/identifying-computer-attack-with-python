import os;
import nltk
import math;
from nltk import ngrams
featurelist=[];
os.system("rm -rf output")

for i in [3,5,7]:			#getting data form all the files iteratively about the features and putting them in the featurelist
	filename=str(i)+"grams_features.txt";
	print("collecting data from",filename,"...",end="")
	fr=open(filename,"r");
	text=fr.read();
	text=text.split("\n")
	for j in range(2):
		text.pop(-1)			#removing the last empty value
	fr.close()
	featurelist.append(text)
	print("done")
#print(len(featurelist))
counter=0;
cwd0=os.getcwd();				#getting the current directory(home directory)
print("collecting data from",cwd0,"...",end="")
for sub0,fold0,file0 in os.walk(cwd0):	#getting the data about the contents in the current folder
	if len(fold0)>0:
		break;
print("done");
#print(fold0)
os.system("mkdir output")
print("sorting the contents in",cwd0,"...",end="")
fold0.sort();					#sorting the folders in ascending order
print("done")
cwd1=cwd0+"/"+fold0[0];
os.chdir(cwd1)
print("	collecting data from",cwd1,"...",end="")	
for sub1,fold1,file1 in os.walk(cwd1):	#getting the data about the contents in the current folder
	if len(fold1)>0:
		break;
print("done")
print("	sorting the contents in",cwd1,"...",end="")
fold1.sort()				#sorting the folders in ascending order
print("done")
out_dir=cwd0+"/output"		#creating output folder in the main folder
os.chdir(out_dir)
os.system("mkdir Attack_Data_Master")	#creating attack data master folder in output folder
for folder in fold1:		#recursing over all the folders in attack
	if '8' in folder  or '9' in folder or '10' in folder:	#recursing over 30%of the folders in it
		out_dir=cwd0+"/output/Attack_Data_Master"
		os.chdir(out_dir)
#		print(folder)
		print("	creating",folder,"...",end="")
		making="mkdir "+folder #creating all the attack folder iteratively
		os.system(making)
		print("done")
		cwd2=cwd1+"/"+folder
		os.chdir(cwd2);
		#print(cwd2)
		print("collecting data about the files from",cwd2,"...",end="")
		for sub2,fold2,file2 in os.walk(cwd2):#rgetting the data over all the files
			if len(file2)>0:
				break;
			pass;
		print("done")
		counter=0;
		sizeoffiles=len(file2)
		for files in file2:				#iterating over all the files
			fr=open(files,"r")
			text=fr.read()
			fr.close();
			for i in [3,5,7]:			#iterating all the files over 3,5and 7 grams
				featureindex=math.floor(i/2)-1	#normalizing index with respect to i
				count=[0 for x in range(len(featurelist[featureindex])) ]
				print("	",counter+1,"/",sizeoffiles,"	getting",i,"grams for",files,"...",end="")
				single_grams=ngrams(text.split(),i)
				print("done    ",end="\r")
				#print(counter+1,"/",sizeoffiles,end="\r");
				print("	",counter+1,"/",sizeoffiles,"	counting the",i,"gram features in",files,"...",end="")
				for grams in single_grams:		#iterating over the ngrams generated and counting them
					string=grams[0]+" ";
					for j in range(1,i):
						string=string+grams[j]+" ";
					if string in featurelist[featureindex]:
						#print("true")
						ind=featurelist[featureindex].index(string);
						count[ind]=count[ind]+1;
					#else:
					#	print("false")
				print("done    ",end="\r")

				#print(counter+1,"/",sizeoffiles,end="\r");
				filename=str(i)+"gramsfrequency_"+files		
				#print(filename)
				print("	",counter+1,"/",sizeoffiles,"	printing the data in",filename,"...",end="")
				out_dir=cwd0+"/output/Attack_Data_Master/"+folder;
				os.chdir(out_dir)						
				fw=open(filename,"a")					##########################################################afterwards change it to append##################################################
				for frequency in range(len(count)):		#writing the feature and frequenycy of it in the files
					fw.write(featurelist[featureindex][frequency])
					fw.write("----->")
					fw.write("Frequency of F")
					fw.write(str(frequency))
					fw.write("----->")
					fw.write(str(count[frequency]))
					fw.write("\n")
				os.chdir(cwd2)
				print("done  ",end="\r")
				#print(counter+1,"/",sizeoffiles,end="\r");				
			counter=counter+1;

cwd1=cwd0+"/"+fold0[2];
out_dir=cwd0+"/output"
os.chdir(out_dir)
os.system("mkdir Validation_Data_Master")#making validation data master folder in output folder
#print(cwd1)
os.chdir(cwd1)
print("collecting data about files in",cwd1,"...",end="")
for sub1,fold1,files1 in os.walk(cwd1):	#collecting data from validation data master folder
	pass;
print("done")
#print(files1)
#print(files1)
#print(fold1)	
counter=0;
for files in files1:		#recursing over all the files in validation data master
	#print(files)
	if files==".DS_Store":
		continue;
	fr=open(files,"r")
	text=fr.read();
	fr.close();

	sizeoffiles=len(files1)
	for i in [3,5,7]:			#recursing over the 3,5,7 grams in the files in validatoin data master
		featureindex=math.floor(i/2)-1
		count=[0 for x in range(len(featurelist[featureindex])) ]
		print("	",counter+1,"/",sizeoffiles,"	getting",i,"grams for",files,"...",end="")
		single_grams=ngrams(text.split(),i);
		print("done    ",end="\r")
		#print(counter+1,"/",sizeoffiles,end="\r");
		print("	",counter+1,"/",sizeoffiles,"	counting the",i,"gram features in",files,"...",end="")
		for grams in single_grams:		
			string=grams[0]+" ";
			for j in range(1,i):
				string=string+grams[j]+" ";
			if string in featurelist[featureindex]:
				ind=featurelist[featureindex].index(string);
				count[ind]=count[ind]+1;				#counting the frequency of features
		print("done    ",end="\r")
		#print(counter+1,"/",sizeoffiles,end="\r");
		filename=str(i)+"gramsfrequency_"+files
		#print(filename)
		print("	",counter+1,"/",sizeoffiles,"	printing the data in",filename,"...",end="")
		out_dir=cwd0+"/output/Validation_Data_Master"
		os.chdir(out_dir)						
		fw=open(filename,"a")					##########################################################afterwards change it to append##################################################
		for frequency in range(len(count)):			#writing the features and frequency of it in the files
			fw.write(featurelist[featureindex][frequency])
			fw.write("----->")
			fw.write("Frequency of F")
			fw.write(str(frequency))
			fw.write("----->")
			fw.write(str(count[frequency]))
			fw.write("\n")
		os.chdir(cwd1)
		print("done  ",end="\r")
		#print(counter+1,"/",sizeoffiles,end="\r");	
	counter=counter+1;

		
		
