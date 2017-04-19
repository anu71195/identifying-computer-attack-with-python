import os
import time
import math
import nltk
from time import time
from nltk import ngrams

print("deleting all the unnecessary files...")
os.system("rm hydra_ftp_training.txt & rm hydra_ssh_training.txt & rm java_meterpreter_training.txt & rm meterpreter_training.txt & rm webshell_training.txt")
os.system("rm Training_Data_Master.txt & rm Validation_Data_Master.txt & rm adduser_training.txt & rm adduser_test.txt & rm hydra_ftp_test.txt ");
os.system("rm hydra_ssh_test.txt & rm java_meterpreter_test.txt & rm meterpreter_test.txt & rm webshell_test.txt")
os.system("rm -rf output")
os.system("rm featurefile.txt");
os.system("rm 3* & rm 5* & rm 7* & rm 1* & rm 2* & rm 4* & rm 6* & rm 8* & rm 9*")
all_net_grams=[3]#array of all grams say all_net_grams=[3,5,7]
timestamp=time();
cwd0=os.getcwd();#main directory
print("current working directory is",cwd0);
print("collecting data from",cwd0,"...",end="")
for sub0,folders0,files0 in os.walk(cwd0):
	if len(folders0)>0 :
		break;
print("done")
print("sorting the folders in",cwd0,"...",end="");
folders0.sort();
print("done")
path=cwd0+"/"+folders0[0];#attack data master
os.chdir(path);
cwd1=os.getcwd();
print("current working directory is",cwd1);
print("collecting data from",cwd1,"...",end="");
for sub1,folders1,files1 in os.walk(cwd1):
	if len(folders1)>0:
		break;
print("done");
print("sorting the folders in",cwd1,"...",end="");
folders1.sort();
print("done");
for i in range(0,60):##add user files range
	path=cwd1+"/"+folders1[i];
	os.chdir(path);
	cwd2=os.getcwd();
	print("		current woring directory is",cwd2,end="\r");
	print("		collecting data from",cwd2,end="\r");
	for sub2,folders2,files2 in os.walk(cwd2):#files all folder
			pass;
	for data in range(0,len(files2)):#data in those files reading and writing those files
		print("			working on",files2[data],"...",end="")
		fr=open(files2[data],"r")
		text=fr.read();
		fr.close();
		print("done",end="\r");
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
		print("			printing data in",location,"...",end="")
		fw=open(location,"a");
		#temp7=text+"\n\n"
		fw.write(text);
		fw.write("\n\n")   
		#fw.write(temp7)
		fw.close();
		print("done",end="\r");
	print("		data from",cwd2,"collected",end="\r")
print("	data from",cwd1,"collected")
for i in range(1,3):
	path=cwd0+"/"+folders0[i];#training data master and validation data master
	os.chdir(path)
	cwd1=os.getcwd();
	print("		current working directory is",cwd1);
	print("		collecting data from",cwd1);
	for sub1,folders1,files1 in os.walk(cwd1):#recursing over files in training data and validation data master
		pass;
	print("		data from",cwd1,"collected")
	print("		sorting files from",cwd1,"...",end="")
	files1.sort();
	print("done	")
	for data in range(0,len(files1)):#reading and writing those files
		print("			working on",files1[data],"...",end="");
		if files1[data]==".DS_Store":
			continue;
		fr=open(files1[data],"r");
		text=fr.read();
		fr.close;
		print("done",end="\r")

		if i==1:
			location=cwd0+"/Training_Data_Master.txt";
		elif i==2:
			location=cwd0+"/Validation_Data_Master.txt";
		print("			printing data in",location,"...",end="");
		fw=open(location,"a");
		#temp7=text+"\n\n"
		fw.write(text);
		fw.write("\n\n");
		#fw.write(temp7)
		fw.close();
		print("done",end="\r")
print("data from",cwd0,"collected")

#here creating the training and test files is finished

#changing to main directory
os.chdir(cwd0);
print("current working directory is",cwd0)
#making training array which lists all the files

training=["adduser_training.txt","hydra_ftp_training.txt","hydra_ssh_training.txt","java_meterpreter_training.txt","meterpreter_training.txt","webshell_training.txt","Training_Data_Master.txt"]
for n in all_net_grams:
	fname=str(n)+"grams_featurefile.txt"#name of feature file
	featurefile=open(fname,"a")
	print("working for",n,"grams")
	countert_training=0
	for t in training:
		length_of_trianing=len(training)
		print("	",countert_training+1,"/",length_of_trianing)
		countert_training=countert_training+1;
		filename=str(n)+"gramsfor"+t
		fw=open(filename,"a")
		print("		working on file",t,"...",end="")
		fr=open(t,"r")
		text=fr.read();
		fr.close;
		print("done")
		data=[]
		count=[]
		print("		finding",n,"grams for",t,"...",end="")
		all_grams=ngrams(text.split(),n)
		print("done")
		
		print("		counting the frequency of",n,"grams in",t,"...",end="")
		s_counter=0;
		data=[]
		point_int={}
		count=[]
		index_count=0;

		for grams in all_grams:
			print(s_counter,end="\r")
			s_counter=s_counter+1;
			try:
				if point_int[grams]>=0:
					passing=point_int[grams];
			except:
				passing=-1;
			if passing>=0:					#increasing count
				ind=passing;
				count[ind]=count[ind]+1;	
			else:						#adding the data
				data.append(grams)
				count.append(1)
				point_int[grams]=index_count;
				index_count=index_count+1;
		print("\n")
		print("		frequency of",n,"grams in",t,"counted",)
		print("		creating list consisting of count and data together...",end="");
		p_data=[]
		for i in range(len(data)):			#list consisting of count and data
			temp=[count[i]]+[data[i]]
			p_data.append(temp)					#data to be printed in the file
		print("done")
		print("		sorting the created list...",end="")
		p_data.sort(reverse=True)
		print("done")
		print("		printing the data in",filename,"...",end="")
		for j in range(len(p_data)):
			temp7=str(p_data[j][0])+" "
			#fw.write(str(p_data[j][0]));
			#fw.write(" ")
			fw.write(temp7)
			for i in range(n):
				temp7=p_data[j][1][i]+" "
				#fw.write(p_data[j][1][i]);
				#fw.write(" ")
				fw.write(temp7)
			fw.write("\n")
		print("done")
		fw.close();
		filename2="30percentwithout_count_of"+filename
		filename="30percentof"+filename
		fw=open(filename,"a")
		fw2=open(filename2,"a")
		print("		storing 30% of",n,"gram features in",filename,"and",filename2,"...",end="");
		for j in range(math.ceil((len(p_data))*0.3)):#listing all the ngram features
			temp7=str(p_data[j][0])+" "
			#fw.write(str(p_data[j][0]));
			#fw.write(" ")
			fw.write(temp7)
			for i in range(n):
				temp7=p_data[j][1][i]+" "
				#fw.write(p_data[j][1][i]);
				#fw2.write(p_data[j][1][i]);
				#featurefile.write(p_data[j][1][i]);
				fw.write(temp7)
				fw2.write(temp7)
				featurefile.write(temp7)
				#featurefile.write(" ")
				#fw2.write(" ")
				#fw.write(" ")
			#temp7="\n"
			#fw.write("\n")
			#featurefile.write("\n")
			#fw2.write("\n")
			fw.write("\n")
			fw2.write("\n")
			featurefile.write("\n")
		print("done")
		fw.close();
	print("done for",n,"grams")
featurefile.close();
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


features=[]

for n in all_net_grams:	#creating all the unique n gram features 
	print("working for all unique",n,"gram features...")
	temp=[]
	fname=str(n)+"grams_featurefile.txt"
	filename=str(n)+"grams_features.txt";
	print("	reading from file",fname,"...",end="")
	fr=open(fname,"r")
	fw=open(filename,"a");
	text=fr.read();
	print("done")
	text=text.split("\n")
	print("	printing all unique",n,"gram features in",filename,"...",end="")
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
			if mydictionary[ind]==1:		#seeing dublicates
				flag=1
		except:
			flag=0;
		if flag>0:
			continue;
		mydictionary[ind]=1			#no dublicates then add
		temp.append(text[i])

		for k in range(n):
			if i==len(text)-1:
				continue;
			temp7=str(text[i][k])+" "
			#fw.write(str(text[i][k]))
			#fw.write(" ")
			fw.write(temp7)
		fw.write("\n")
	features.append(temp);
	fr.close();
	fw.close();
	print("done")
	print("done")
featurelist=[];
for i in all_net_grams:			#getting data form all the files iteratively about the features and putting them in the featurelist
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
tempdictionary={}
dictionaryarray=[];
for i in range(len(all_net_grams)):
	featureindex=i;
	tempdictionary={}
	thisfeatures=featurelist[featureindex];
	count_features=0;
	for every_feature in thisfeatures:
		tempdictionary[every_feature]=count_features;
		count_features=count_features+1;
	dictionaryarray.append(tempdictionary)
counter=0;
cwd0=os.getcwd();				#getting the current directory(home directory)
print("collecting data from",cwd0,"...",end="")
for sub0,fold0,file0 in os.walk(cwd0):	#getting the data about the contents in the current folder
	if len(fold0)>0:
		break;
print("done");
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
	filetype=attack_type(folder);
	if '8' in folder  or '9' in folder or '10' in folder:	#recursing over 30%of the folders in it
		out_dir=cwd0+"/output/Attack_Data_Master"
		cwd2=cwd1+"/"+folder
		os.chdir(cwd2);
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
			for i in range(len(all_net_grams)):			#iterating all the files over 3,5and 7 grams
				featureindex=i;
				mydictionary={};
				thisfeatures=featurelist[featureindex];
				count_features=0
				mydictionary=dictionaryarray[featureindex];
				#for every_feature in thisfeatures:			##creating dictionary giving out indices for the grams
				#	mydictionary[every_feature]=count_features;
				#	count_features=count_features+1

				count=[0 for x in range(len(featurelist[featureindex])) ]
				print("	",counter+1,"/",sizeoffiles,"	getting",all_net_grams[i],"grams for",files,"...",end="")
				single_grams=ngrams(text.split(),all_net_grams[i])
				print("done    ",end="\r")
				print("	",counter+1,"/",sizeoffiles,"	counting the",all_net_grams[i],"gram features in",files,"...",end="")
				for grams in single_grams:		#iterating over the ngrams generated and counting them
					string=grams[0]+" ";
					for j in range(1,all_net_grams[i]):
						string=string+grams[j]+" ";

					try:						
						if mydictionary[string]>=0:			#present in mydictionary that is , it is a feature
							flag=1;
					except:
							flag=0;						#fearture not present
					if flag==1:
						#print(string,ind)
						ind=mydictionary[string];
						#print(string,ind)
						count[ind]=count[ind]+1;		#couting
				print("done    ",end="\r")
				filename=str(all_net_grams[i])+"gramsfrequency_"
				print("	",counter+1,"/",sizeoffiles,"	printing the data in",filename,"...",end="")
				out_dir=cwd0+"/output/Attack_Data_Master/";
				os.chdir(out_dir)						
				fw=open(filename,"a")					##########################################################afterwards change it to append##################################################
				for frequency in range(len(count)):		#writing the feature and frequenycy of it in the files
					temp7=str(count[frequency])+","
					fw.write(temp7)
					#fw.write(",")
				temp=filetype+"\n\n"
				#fw.write(filetype)
				#fw.write("\n\n")
				fw.write(temp)
				os.chdir(cwd2)
				print("done  ",end="\r")
			counter=counter+1;

cwd1=cwd0+"/"+fold0[2];
out_dir=cwd0+"/output"
os.chdir(out_dir)
os.system("mkdir Validation_Data_Master")#making validation data master folder in output folder
os.chdir(cwd1)
print("collecting data about files in",cwd1,"...",end="")
for sub1,fold1,files1 in os.walk(cwd1):	#collecting data from validation data master folder
	pass;
print("done")
filetype=attack_type(fold0[2]);
print("\n")
print("time taken = ",time()-timestamp)

#for i in range(len(all_net_grams)):
#	featureindex=i;
#	tempdictionary={}
#	thisfeatures=featurelist[featureindex];
#	count_features=0;
#	for every_feature in thisfeatures:
#		tempdictionary[every_feature]=count_features;
#		count_features=count_features+1;
#	dictionaryarray.append(tempdictionary)
#print(dictionaryarray)
counter=0;
filesdata=[[] for i in range(len(all_net_grams))]
#filetypeff=[[] for i in range(len(all_net_grams))]
sizeoffiles=len(files1)
for files in files1:		#recursing over all the files in validation data master
	if files==".DS_Store":
		continue;
	fr=open(files,"r")
	text=fr.read();
	fr.close();

	print("file",counter+1,"/",sizeoffiles,end="\r")
	for i in range(len(all_net_grams)):			#recursing over the 3,5,7 grams in the files in validatoin data master
		featureindex=i;
		mydictionary={};
		thisfeatures=featurelist[featureindex];
		count_features=0
		mydictionary=dictionaryarray[featureindex]
#		for every_feature in thisfeatures:			##creating dictionary giving out indices for the grams
#			mydictionary[every_feature]=count_features;
#			count_features=count_features+1
		count=[0 for x in range(len(featurelist[featureindex])) ]
		#print("	",counter+1,"/",sizeoffiles,"	getting",all_net_grams[i],"grams for",files,"...",end="")
		single_grams=ngrams(text.split(),all_net_grams[i]);
		#print("done    ",end="\r")
		#print("	",counter+1,"/",sizeoffiles,"	counting the",all_net_grams[i],"gram features in",files,"...",end="")
		for grams in single_grams:		
			string=grams[0]+" ";
			for j in range(1,all_net_grams[i]):
				string=string+grams[j]+" ";

			try:						
				if mydictionary[string]>=0:			#present in mydictionary that is , it is a feature
					flag=1;
			except:
				flag=0;						#fearture not present
			if flag==1:
				ind=mydictionary[string];
				count[ind]=count[ind]+1;		#couting
#
		#print("done    ",end="\r")
#		filesdata[i].append(count);
#		filetypeff[i].append(filetype);
		filename=str(all_net_grams[i])+"gramsfrequency"
		#print("	",counter+1,"/",sizeoffiles,"	printing the data in",filename,"...",end="")
		out_dir=cwd0+"/output/Validation_Data_Master"
		os.chdir(out_dir)						
		fw=open(filename,"a")				##########################################################afterwards change it to append##################################################
		for frequency in range(len(count)):			#writing the features and frequency of it in the files
			temp7=str(count[frequency])+","
			fw.write(temp7)
			#fw.write(",")
		temp7=filetype+"\n\n"
		#fw.write(filetype)
		#fw.write("\n\n")
		fw.write(temp7)
		os.chdir(cwd1)
		#print("done  ",end="\r")
	counter=counter+1;

 
print("\n")
print("time taken = ",time()-timestamp)

#print(os.getcwd())
