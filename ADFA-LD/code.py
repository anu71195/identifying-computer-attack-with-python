import os
import time
import math
import nltk
from time import time
from nltk import ngrams
# Remove previous run files
os.system("rm hydra_ftp_training.txt & rm hydra_ssh_training.txt & rm java_meterpreter_training.txt & rm meterpreter_training.txt & rm webshell_training.txt")
os.system("rm Training_Data_Master.txt & rm Validation_Data_Master.txt & rm adduser_training.txt & rm adduser_test.txt & rm hydra_ftp_test.txt ");
os.system("rm hydra_ssh_test.txt & rm java_meterpreter_test.txt & rm meterpreter_test.txt & rm webshell_test.txt")
os.system("rm -rf output")
os.system("rm featurefile.txt");
os.system("rm 3* & rm 5* & rm 7* & rm 1* & rm 2* & rm 4* & rm 6* & rm 8* & rm 9* & rm 0*")
os.system("clear")
all_net_grams= input().split(' ');#[3,5,7]#array of all grams say all_net_grams=[3,5,7]
os.system("clear")
for i in range(len(all_net_grams)):
	all_net_grams[i]=int(all_net_grams[i])
print("input given is:-",all_net_grams)
print("\n\n","Generating Featurelist from Attack Data Master ...",end="")

timestamp=time();
cwd0=os.getcwd();#main directory

################################ GETTING FOLDER LIST ################################################ 
for sub0,folders0,files0 in os.walk(cwd0):
	if len(folders0)>0 :
		break;
folders0.sort(); # Sort filenames to loop

path=cwd0+"/"+folders0[0];#attack data master
os.chdir(path);
cwd1=os.getcwd();
for sub1,folders1,files1 in os.walk(cwd1):
	if len(folders1)>0:
		break;
folders1.sort(); 

################################ CONCATENATION ################################################ 

for i in range(len(folders1)):
	path=cwd1+"/"+folders1[i];
	os.chdir(path);
	cwd2=os.getcwd();
	for sub2,folders2,files2 in os.walk(cwd2):#files all folder
			pass;
	for data in range(0,len(files2)):#data in those files reading and writing those files
		
		if i<10:
			if i%10==1 or i%10==8 or i%10==9:
				location=cwd0+"/adduser_test.txt"
			else :
				location=cwd0+"/adduser_training.txt";
		elif i<20:
			if i%10==1 or i%10==8 or i%10==9:
				location=cwd0+"/hydra_ftp_test.txt"
			else :
				location=cwd0+"/hydra_ftp_training.txt";
		elif i<30:
			if i%10==1 or i%10==8 or i%10==9:
				location=cwd0+"/hydra_ssh_test.txt"
			else :
				location=cwd0+"/hydra_ssh_training.txt";
		elif i<40:
			if i%10==1 or i%10==8 or i%10==9:
				location=cwd0+"/java_meterpreter_test.txt"
			else :
				location=cwd0+"/java_meterpreter_training.txt";
		elif i<50:
			if i%10==1 or i%10==8 or i%10==9:
				location=cwd0+"/meterpreter_test.txt"
			else :
				location=cwd0+"/meterpreter_training.txt";
		else:
			if i%10==1 or i%10==8 or i%10==9:
				location=cwd0+"/webshell_test.txt"
			else :
				location=cwd0+"/webshell_training.txt";
		
		fr=open(files2[data],"r")
		text=fr.read(); # Read contents of each file into text
		fr.close();
		
		fw=open(location,"a");
		fw.write(text); #append the file as a row to the file 
		fw.write("\n\n")   
		fw.close();

# Concatenating files in folder Training_Data_Master.
for i in range(1,2):
	path=cwd0+"/"+folders0[i];#training data master and validation data master
	os.chdir(path)
	cwd1=os.getcwd();
	for sub1,folders1,files1 in os.walk(cwd1):#recursing over files in training data and validation data master
		pass; #extract filenames at depth 1 into variable files1
	files1.sort();
	for data in range(0,len(files1)):#reading and writing those files
		if files1[data]==".DS_Store": #Skip error files generated in the directory
			continue;
		fr=open(files1[data],"r");
		text=fr.read();
		fr.close;
		if i==1:
			location=cwd0+"/Training_Data_Master.txt";
		elif i==2:
			location=cwd0+"/Validation_Data_Master.txt";
		fw=open(location,"a");
		fw.write(text);
		fw.write("\n\n");
		fw.close();

os.chdir(cwd0);

################################ FINDING NGRAMS OF EACH CONCATENATED FILE ################################################ 
training=["adduser_training.txt","hydra_ftp_training.txt","hydra_ssh_training.txt","java_meterpreter_training.txt","meterpreter_training.txt","webshell_training.txt","Training_Data_Master.txt"]
for n in all_net_grams:
	fname=str(n)+"grams_featurefile.txt"#name of feature file
	# Create new/Appende file called Xgrams_featurefile
	featurefile=open(fname,"a")

	#print("Number of ngrams : ");
	for training_file in training:
		filename=str(n)+"gramsfor"+training_file
		fw=open(filename,"a")
		fr=open(training_file,"r")
		text=fr.read();
		fr.close;
		data=[]
		count=[]
		# Generate ngrams of each concatenated file.
		all_grams=ngrams(text.split(),n)

		data=[]
		point_int={}
		count=[]
		# index_count = NUMBER OF UNIQUE FEATURES
		# count = FREQUENCY OF FEATURES.
		# point_int is a dictionary of size index_count
		index_count=0;
		for curr_ngram in all_grams:
			try:
				if point_int[curr_ngram]>=0:
					passing=point_int[curr_ngram];
			except:
				passing=-1;
			# IF the ngram is already in the dictionary, just increment its count.
			if passing>=0:					#increasing count
				ind=passing;
				count[ind]=count[ind]+1;	
			else:						#adding the data
				data.append(curr_ngram)
				count.append(1)
				point_int[curr_ngram]=index_count;
				index_count=index_count+1;
		
# Sort the features ordered by their frequency count
		p_data=[]
		for i in range(len(data)):			#list consisting of count and data
			temp=[count[i]]+[data[i]]
			p_data.append(temp)					#data to be printed in the file
		
### TIME CONSUMING  - Will run 7 times i.e. for each concatenated training file.
## SIZE OF p_data = 
		#print(training_file,len(p_data));
		p_data.sort(reverse=True)

		for j in range(len(p_data)):
			temp7=str(p_data[j][0])+" "  	#Count of the Feature
			fw.write(temp7)
			
			# ' '.join(map(str,x)) will also work
			for i in range(n):
				temp7=p_data[j][1][i]+" " 	#Feature is a tuple
				fw.write(temp7)
			fw.write("\n")
		fw.close();

# 30 percent of the above
		for j in range(math.ceil((len(p_data))*0.3)):#listing all the ngram features
			for i in range(n):
				temp7=p_data[j][1][i]+" "
				featurefile.write(temp7)
			featurefile.write("\n")

featurefile.close();

#determine attack type
def attack_type(foldfile):
	if "Adduser" in foldfile:
		return "Adduser";
	elif "Hydra" in foldfile:
		if "FTP" in foldfile:
			return "Hydra_FTP";
		elif "SSH" in foldfile:
			return "Hydra_SSH"
	elif "Meterpreter" in foldfile:
		if "Java" in foldfile:
			return "Java_Meterpreter";
		else :
			return "Meterpreter";
	elif "WS" in foldfile or "Web" in foldfile:
		return "Web_Shell"
	else:
		return "normal"


################################ KEEP UNIQUE FEATURES (MERGE DUPLICATES)################################################ 

features=[]
for n in all_net_grams:	#creating all the unique n gram features 
	temp=[]
	fname=str(n)+"grams_featurefile.txt"  # TOP 30% NOT UNIQUE
	filename=str(n)+"grams_features.txt"; # LIST OF UNIQUE FEATURES
	fr=open(fname,"r")
	fw=open(filename,"a");
	text=fr.read();
	text=text.split("\n")
	mydictionary={};
	for i in range (len(text)):				
		text[i]=text[i].split();
		for j in range(n):
			if i==len(text)-1:
				continue;
			text[i][j]=int(text[i][j]);

		flag=0;
		ind=str(text[i])
		try:
			if mydictionary[ind]==1:		#seeing duplicates
				flag=1
		except:
			flag=0;
		if flag>0:
			continue;
		mydictionary[ind]=1			# if no duplicates then add
		temp.append(text[i])
		for k in range(n):
			if i==len(text)-1:
				continue;
			temp7=str(text[i][k])+" "
			fw.write(temp7)
		fw.write("\n")
	features.append(temp);
	fr.close();
	fw.close();

################################ CREATE ARRAY OF FEATURES FROM THE TOP30% UNIQUE FEATURES STORED IN FILE ################################################ 
featurelist=[];
for i in all_net_grams:			#getting data form all the files iteratively about the features and putting them in the featurelist
	filename=str(i)+"grams_features.txt";
	#print("collecting data from",filename,"...",end="")
	fr=open(filename,"r");
	text=fr.read();
	text=text.split("\n")
	for j in range(2):
		text.pop(-1)			#removing the last empty value
	fr.close()
	featurelist.append(text)

################################ Create Dictionary of feature count ################################################ 
tempdictionary={}
dictionaryarray=[]; # Contains set of 3 arrays.
for i in range(len(all_net_grams)):
	tempdictionary={}
	thisfeatures=featurelist[i];
	count_features=0;
	for every_feature in thisfeatures:
		tempdictionary[every_feature]=count_features;
		count_features=count_features+1;
	dictionaryarray.append(tempdictionary)

counter=0;
cwd0=os.getcwd();				#getting the current directory(home directory)
for sub0,fold0,file0 in os.walk(cwd0):	#getting the data about the contents in the current folder
	if len(fold0)>0:
		break;
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
os.system("mkdir Attack_Data_Master & mkdir Validation_Data_Master & mkdir Training_Data_Master")	#creating attack data master folder in output folder

################################ Writing Feature Counts for Attack Data Master  ##############################################
for folder in fold1:		#recursing over all the folders in attack
		filetype=attack_type(folder);
	#if '8' in folder  or '9' in folder or '10' in folder:	#recursing over 30%of the folders in it
		out_dir=cwd0+"/output/Attack_Data_Master"
		cwd2=cwd1+"/"+folder
		os.chdir(cwd2);
		for sub2,fold2,file2 in os.walk(cwd2):#rgetting the data over all the files
			if len(file2)>0:
				break;
			pass;
		sizeoffiles=len(file2)
		for files in file2:				#iterating over all the files
			fr=open(files,"r")
			text=fr.read()
			for i in range(len(all_net_grams)):			#iterating all the files over 3,5and 7 grams
				mydictionary={};
				thisfeatures=featurelist[i];
				count_features=0
				mydictionary=dictionaryarray[i];
				count=[0 for x in range(len(featurelist[i])) ]
				single_grams=ngrams(text.split(),all_net_grams[i])
				for curr_ngram in single_grams:		#iterating over the ngrams generated and counting them
					string=curr_ngram[0]+" ";
					for j in range(1,all_net_grams[i]):
						string=string+curr_ngram[j]+" ";
					try:						
						if mydictionary[string]>=0:			#present in mydictionary that is , it is a feature
							flag=1;
					except:
							flag=0;						#fearture not present
					if flag==1:
						ind=mydictionary[string];
						count[ind]=count[ind]+1;		#couting
				filename=str(all_net_grams[i])+"gramsfrequency_"
				out_dir=cwd0+"/output/Attack_Data_Master/";
				os.chdir(out_dir)						
				fw=open(filename,"a")					

				for frequency in range(len(count)):		#writing the feature and frequenycy of it in the files
					temp7=str(count[frequency])+","
					fw.write(temp7)
				temp=filetype+"\n\n"
				fw.write(temp)
				os.chdir(cwd2)

cwd1=cwd0+"/"+fold0[2];
os.chdir(cwd1)
for sub1,fold1,files1 in os.walk(cwd1):	#collecting data from validation data master folder
	pass;
filetype=attack_type(fold0[2]);
print("done")
print("time taken until now= ",time()-timestamp,"\n")

################################ Writing Feature Counts for Validation Data Master  ##############################################
print("Writing Feature Counts for Validation Data Master...",end="")
fw=[]
for i in range(len(all_net_grams)):
	filename=str(all_net_grams[i])+"gramsfrequency"
	fwi=open(filename,"a")
	fw.append(fwi)

for files in files1:		
	#if files==".DS_Store":
	#	continue;
	fr=open(files,"r")
	text=fr.read();
	for i in range(len(all_net_grams)):			#recursing over the 3,5,7 grams in the files in validatoin data master
		mydictionary={};
		thisfeatures=featurelist[i];
		count_features=0
		mydictionary=dictionaryarray[i]
		count=[0 for x in range(len(featurelist[i])) ]
		single_grams=ngrams(text.split(),all_net_grams[i]);
		for curr_ngram in single_grams:		
			string=curr_ngram[0]+" ";
			for j in range(1,all_net_grams[i]):
				string=string+curr_ngram[j]+" ";
			try:						
				if mydictionary[string]>=0:			#present in mydictionary that is , it is a feature
					flag=1;
			except:
				flag=0;						#fearture not present
			if flag==1:
				ind=mydictionary[string];
				count[ind]=count[ind]+1;		#couting
		for frequency in range(len(count)):			#writing the features and frequency of it in the files
			temp7=str(count[frequency])+","
			fw[i].write(temp7)
		temp7=filetype+"\n\n"
		fw[i].write(temp7)

################################ MOVE FILES INTO OUTPUT FOLDER ################################################ 
for t in range(len(all_net_grams)):
	temp="mv "+str(all_net_grams[t])+"gramsfrequency "+cwd0+"/output/Validation_Data_Master";
	os.system(temp)
cwd1=cwd0+"/"+fold0[1];
os.chdir(cwd1)
for sub1,fold1,files1 in os.walk(cwd1):	#collecting data from Training data master folder
	pass;
filetype=attack_type(fold0[1]);
print("done")
print("time taken until now= ",time()-timestamp)

################################ Writing Feature Counts for Training Data Master... ################################################ 
print("\nWriting Feature Counts for Training Data Master...",end=" ")
fw=[]
for i in range(len(all_net_grams)):
	filename=str(all_net_grams[i])+"gramsfrequency"
	fwi=open(filename,"a")
	fw.append(fwi)

sizeoffiles=len(files1)
for files in files1:		#recursing over all the files in validation data master
	#if files==".DS_Store":
	#	continue;
	fr=open(files,"r")
	text=fr.read();
	for i in range(len(all_net_grams)):			#recursing over the 3,5,7 gramss in the files in validatoin data master
		mydictionary={};
		thisfeatures=featurelist[i];
		count_features=0
		mydictionary=dictionaryarray[i]
		count=[0 for x in range(len(featurelist[i])) ]
		single_grams=ngrams(text.split(),all_net_grams[i]);
		for curr_ngram in single_grams:		
			string=curr_ngram[0]+" ";
			for j in range(1,all_net_grams[i]):
				string=string+curr_ngram[j]+" ";
			try:						
				if mydictionary[string]>=0:			#present in mydictionary that is , it is a feature
					flag=1;
			except:
				flag=0;						#fearture not present
			if flag==1:
				ind=mydictionary[string];
				count[ind]=count[ind]+1;		#couting
		for frequency in range(len(count)):			#writing the features and frequency of it in the files
			temp7=str(count[frequency])+","
			fw[i].write(temp7)
		temp7=filetype+"\n\n"
		fw[i].write(temp7)
		#os.chdir(cwd1)
for t in range(len(all_net_grams)):
	temp="mv "+str(all_net_grams[t])+"gramsfrequency "+cwd0+"/output/Training_Data_Master";
	os.system(temp)
print("done")
print("total time taken = ",time()-timestamp,"\n\n")
for i in range(len(featurelist)):
	print("features in",all_net_grams[i],"grams: ",len(featurelist[i]))
os.chdir(cwd0)
os.system("rm hydra_ftp_training.txt & rm hydra_ssh_training.txt & rm java_meterpreter_training.txt & rm meterpreter_training.txt & rm webshell_training.txt")
os.system("rm Training_Data_Master.txt & rm adduser_training.txt & rm adduser_test.txt & rm hydra_ftp_test.txt ");
os.system("rm hydra_ssh_test.txt & rm java_meterpreter_test.txt & rm meterpreter_test.txt & rm webshell_test.txt")
os.system("rm *featurefile.txt & rm *training.txt & rm *gramsforTraining_Data_Master.txt")

			################################ STEPS ################################################ 
################################ GETTING FOLDER LIST ################################################ 

################################ CONCATENATION ################################################ 

################################ FINDING NGRAMS OF EACH CONCATENATED FILE ################################################ 

################################ KEEP UNIQUE FEATURES (MERGE DUPLICATES)################################################ 

################################ CREATE ARRAY OF FEATURES FROM THE TOP30% UNIQUE FEATURES STORED IN FILE ################################################ 

################################ Create Dictionary of feature count ################################################ 

################################ Writing Feature Counts for Attack Data Master  ##############################################

################################ Writing Feature Counts for Validation Data Master  ##############################################

################################ Writing Feature Counts for Training Data Master  ##############################################
