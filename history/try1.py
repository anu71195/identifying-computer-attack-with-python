import os
os.system("rm hydra_ftp_training.txt & rm hydra_ssh_training.txt & rm java_meterpreter_training.txt & rm meterpreter_training.txt & rm webshell_training.txt")
os.system("rm Training_Data_Master.txt & rm Validation_Data_Master.txt & rm adduser_training.txt & rm adduser_test.txt & rm hydra_ftp_test.txt ");
os.system("rm hydra_ssh_test.txt & rm java_meterpreter_test.txt & rm meterpreter_test.txt & rm webshell_test.txt")
cwd0=os.getcwd();#main directory
print(cwd0);
for sub0,folders0,files0 in os.walk(cwd0):
	if len(folders0)>0 :
		break;
#print(folders0);
print("\n\n");
folders0.sort();

path=cwd0+"/"+folders0[0];#attack data master
os.chdir(path);
print("\n")
cwd1=os.getcwd();
print(cwd1);
for sub1,folders1,files1 in os.walk(cwd1):
	if len(folders1)>0:
		break;
folders1.sort();
print(folders1);
print('\n')
for i in range(0,60):##add user files range
#	if i%10==1 or i%10==8 or i%10==9:##sorted one has 10 in second position
#		continue;
	print(folders1[i]);
	path=cwd1+"/"+folders1[i];
	os.chdir(path);
	cwd2=os.getcwd();
	print(cwd2);
	for sub2,folders2,files2 in os.walk(cwd2):#files all folder
			print(files2);
	for data in range(0,len(files2)):#data in those files reading and writing those files
		print(files2[data])
		print(len(files2))
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
	print(cwd1);
	for sub1,folders1,files1 in os.walk(cwd1):#recursing over files in training data and validation data master
		files1.sort();
		print(files1);
		print(len(files1))
	for data in range(0,len(files1)):#reading and writing those files
		print(files1[data]);
		print(len(files1));
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

