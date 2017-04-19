import os
import time
import math
import nltk
from time import time
from nltk import ngrams
os.system("rm hydra_ftp_training.txt & rm hydra_ssh_training.txt & rm java_meterpreter_training.txt & rm meterpreter_training.txt & rm webshell_training.txt")
os.system("rm Training_Data_Master.txt & rm Validation_Data_Master.txt & rm adduser_training.txt & rm adduser_test.txt & rm hydra_ftp_test.txt ");
os.system("rm hydra_ssh_test.txt & rm java_meterpreter_test.txt & rm meterpreter_test.txt & rm webshell_test.txt")
os.system("rm -rf output")
os.system("rm featurefile.txt");
os.system("rm 3* & rm 5* & rm 7* & rm 1* & rm 2* & rm 4* & rm 6* & rm 8* & rm 9* & rm 0*")
os.system("clear")
print("\n\n","running...\n\n")
all_net_grams=[3,5,7]#array of all grams say all_net_grams=[3,5,7]
timestamp=time();
cwd0=os.getcwd();#main directory
for sub0,folders0,files0 in os.walk(cwd0):
	if len(folders0)>0 :
		break;
folders0.sort();
path=cwd0+"/"+folders0[0];#attack data master
os.chdir(path);
cwd1=os.getcwd();
for sub1,folders1,files1 in os.walk(cwd1):
	if len(folders1)>0:
		break;
folders1.sort();
for i in range(0,60):##add user files range
	path=cwd1+"/"+folders1[i];
	os.chdir(path);
	cwd2=os.getcwd();
	for sub2,folders2,files2 in os.walk(cwd2):#files all folder
			pass;
	for data in range(0,len(files2)):#data in those files reading and writing those files
		fr=open(files2[data],"r")
		text=fr.read();
		fr.close();
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
		fw=open(location,"a");
		fw.write(text);
		fw.write("\n\n")   
		fw.close();
for i in range(1,3):
	path=cwd0+"/"+folders0[i];#training data master and validation data master
	os.chdir(path)
	cwd1=os.getcwd();
	for sub1,folders1,files1 in os.walk(cwd1):#recursing over files in training data and validation data master
		pass;
	files1.sort();
	for data in range(0,len(files1)):#reading and writing those files
		if files1[data]==".DS_Store":
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
training=["adduser_training.txt","hydra_ftp_training.txt","hydra_ssh_training.txt","java_meterpreter_training.txt","meterpreter_training.txt","webshell_training.txt","Training_Data_Master.txt"]
for n in all_net_grams:
	fname=str(n)+"grams_featurefile.txt"#name of feature file
	featurefile=open(fname,"a")
	for t in training:
		filename=str(n)+"gramsfor"+t
		fw=open(filename,"a")
		fr=open(t,"r")
		text=fr.read();
		fr.close;
		data=[]
		count=[]
		all_grams=ngrams(text.split(),n)
		data=[]
		point_int={}
		count=[]
		index_count=0;
		for grams in all_grams:
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
		p_data=[]
		for i in range(len(data)):			#list consisting of count and data
			temp=[count[i]]+[data[i]]
			p_data.append(temp)					#data to be printed in the file
		p_data.sort(reverse=True)
		for j in range(len(p_data)):
			temp7=str(p_data[j][0])+" "
			fw.write(temp7)
			for i in range(n):
				temp7=p_data[j][1][i]+" "
				fw.write(temp7)
			fw.write("\n")
		fw.close();
		for j in range(math.ceil((len(p_data))*0.3)):#listing all the ngram features
			for i in range(n):
				temp7=p_data[j][1][i]+" "
				featurefile.write(temp7)
			featurefile.write("\n")
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
	temp=[]
	fname=str(n)+"grams_featurefile.txt"
	filename=str(n)+"grams_features.txt";
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
			fw.write(temp7)
		fw.write("\n")
	features.append(temp);
	fr.close();
	fw.close();
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
tempdictionary={}
dictionaryarray=[];
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
						ind=mydictionary[string];
						count[ind]=count[ind]+1;		#couting
				filename=str(all_net_grams[i])+"gramsfrequency_"
				out_dir=cwd0+"/output/Attack_Data_Master/";
				os.chdir(out_dir)						
				fw=open(filename,"a")					##########################################################afterwards change it to append##################################################
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
print("\n\ntime taken = ",time()-timestamp,"\n")

print("running...\n\n")
fw=[]
for i in range(len(all_net_grams)):
	filename=str(all_net_grams[i])+"gramsfrequency"
	fwi=open(filename,"a")
	fw.append(fwi)

for files in files1:		#recursing over all the files in validation data master
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
		for frequency in range(len(count)):			#writing the features and frequency of it in the files
			temp7=str(count[frequency])+","
			fw[i].write(temp7)
		temp7=filetype+"\n\n"
		fw[i].write(temp7)
for t in range(len(all_net_grams)):
	temp="mv "+str(all_net_grams[t])+"gramsfrequency "+cwd0+"/output/Validation_Data_Master";
	os.system(temp)
cwd1=cwd0+"/"+fold0[1];
os.chdir(cwd1)
for sub1,fold1,files1 in os.walk(cwd1):	#collecting data from Training data master folder
	pass;
filetype=attack_type(fold0[1]);

print("time taken = ",time()-timestamp)
print("running...\n\n",end="")
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
	for i in range(len(all_net_grams)):			#recursing over the 3,5,7 grams in the files in validatoin data master
		mydictionary={};
		thisfeatures=featurelist[i];
		count_features=0
		mydictionary=dictionaryarray[i]
		count=[0 for x in range(len(featurelist[i])) ]
		single_grams=ngrams(text.split(),all_net_grams[i]);
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
print("\n")
print("total time taken = ",time()-timestamp)

