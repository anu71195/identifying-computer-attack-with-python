import os
import math
import nltk
from nltk import ngrams
os.system("rm hydra_ftp_training.txt & rm hydra_ssh_training.txt & rm java_meterpreter_training.txt & rm meterpreter_training.txt & rm webshell_training.txt")
os.system("rm Training_Data_Master.txt & rm Validation_Data_Master.txt & rm adduser_training.txt & rm adduser_test.txt & rm hydra_ftp_test.txt ");
os.system("rm hydra_ssh_test.txt & rm java_meterpreter_test.txt & rm meterpreter_test.txt & rm webshell_test.txt")
os.system("rm 3* & rm 5* & rm 7* ")

cwd0=os.getcwd();#main directory
print("working directory is",cwd0,end="\r");
for sub0,folders0,files0 in os.walk(cwd0):
	if len(folders0)>0 :
		break;
#print(folders0);
folders0.sort();

path=cwd0+"/"+folders0[0];#attack data master
os.chdir(path);
cwd1=os.getcwd();
print("working directory is",cwd1,end="\r");
for sub1,folders1,files1 in os.walk(cwd1):
	if len(folders1)>0:
		break;
folders1.sort();
#print(folders1);
#print('\n')
for i in range(0,60):##add user files range
#	if i%10==1 or i%10==8 or i%10==9:##sorted one has 10 in second position
#		continue;
	print(folders1[i]);
	path=cwd1+"/"+folders1[i];
	os.chdir(path);
	cwd2=os.getcwd();
	print(cwd2);
	for sub2,folders2,files2 in os.walk(cwd2):#files all folder
			print(files2,end="\r");
	for data in range(0,len(files2)):#data in those files reading and writing those files
		print(files2[data],end="\r")
		print(len(files2),end="\r")
		fr=open(files2[data],"r")
		text=fr.read();
		fr.close();
		#print(text);
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
		fw.write("\n\n")  #remove if don't want the files appended to treated differently
		fw.close();
	print("\n");
print("\n\n")
for i in range(1,3):
	path=cwd0+"/"+folders0[i];#training data master and validation data master
	os.chdir(path)
	cwd1=os.getcwd();
	#print(cwd1);
	for sub1,folders1,files1 in os.walk(cwd1):#recursing over files in training data and validation data master
		files1.sort();
		print(files1,end="\r");
		print(len(files1),end="\r")
	for data in range(0,len(files1)):#reading and writing those files
		print(files1[data],end="\r");
		print(len(files1),end="\r");
		if files1[data]==".DS_Store":
			continue;
		fr=open(files1[data],"r");
		text=fr.read();
		fr.close;
		#print(text);
		if i==1:
			location=cwd0+"/Training_Data_Master.txt";
		elif i==2:
			location=cwd0+"/Validation_Data_Master.txt";
		fw=open(location,"a");
		fw.write(text);
		fw.write("\n\n");
		fw.close();
	print("\n\n");

#here creating the training and test files is finished

#changing to main directory
os.chdir(cwd0);
#print(os.getcwd())
#all_data=[];#intializing empty all_data 
#all_count=[]#intializing empty all count
#making training array which lists all the files

training=["adduser_training.txt","hydra_ftp_training.txt","hydra_ssh_training.txt","java_meterpreter_training.txt","meterpreter_training.txt","webshell_training.txt","Training_Data_Master.txt"]
for n in [3,5,7]:
	fname=str(n)+"grams_featurefile.txt"#name of feature file
	featurefile=open(fname,"a")
	print("working for",n,"grams...")
#	single_data=[]
#	single_count=[]
	for t in training:
		filename=str(n)+"gramsfor"+t
		fw=open(filename,"a")
		print("		file",t,"...")
		fr=open(t,"r")
		text=fr.read();
		fr.close;
		data=[]
		count=[]
		all_grams=ngrams(text.split(),n)
		for grams in all_grams:
			if grams in data:			#increasing count
				ind=data.index(grams);
				count[ind]=count[ind]+1;	
			else:					##adding the data
				data.append(grams)
				count.append(1)
				#for i in range(n):
				#	fw.write(grams[i]);
				#	fw.write(" ")
				#fw.write("\n")
		p_data=[]
		for i in range(len(data)):			#list consisting of count and data
			temp=[count[i]]+[data[i]]
			p_data.append(temp)					#data to be printed in the file
		p_data.sort(reverse=True)
		#print(p_data)
		for j in range(len(p_data)):
			fw.write(str(p_data[j][0]));
			fw.write(" ")
			for i in range(n):
				fw.write(p_data[j][1][i]);
				fw.write(" ")
			fw.write("\n")
		#print(p_data)
		fw.close();
		filename2="30percentwithout_count_of"+filename
		filename="30percentof"+filename
		#print(filename)
		fw=open(filename,"a")
		fw2=open(filename2,"a")
		#print(len(p_data))
		for j in range(math.ceil((len(p_data))*0.3)):
			fw.write(str(p_data[j][0]));
			fw.write(" ")
			for i in range(n):
				fw.write(p_data[j][1][i]);
				fw2.write(p_data[j][1][i]);
				featurefile.write(p_data[j][1][i]);
				featurefile.write(" ")
				fw2.write(" ")
				fw.write(" ")
			fw.write("\n")
			featurefile.write("\n")
			fw2.write("\n")
		#print(p_data)
		fw.close();
	#	single_data.append(data)
	#	single_count.append(count)

	#all_data.append(single_data);
	#all_count.append(single_count);	
featurefile.close();
#print(all_count);
#print(len(all_data))
features=[]

for n in [3,5,7]:
	temp=[]
	fname=str(n)+"grams_featurefile.txt"
	filename=str(n)+"grams_features.txt";
	fr=open(fname,"r")
	fw=open(filename,"a");
	text=fr.read();
	text=text.split("\n")
	for i in range (len(text)):
		text[i]=text[i].split();
		for j in range(n):
			if i==len(text)-1:
				continue;
			text[i][j]=int(text[i][j]);
		if text[i] in temp:
			continue;
		temp.append(text[i])	
		for k in range(n):
			if i==len(text)-1:
				continue;
			fw.write(str(text[i][k]))
			#print(text[i][k]);
			fw.write(" ")
		fw.write("\n")
	features.append(temp);
	fr.close();
	fw.close();
print(features)
print(len(features))
print(len(features[0]),len(features[1]),len(features[2]))
