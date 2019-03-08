#!/bin/bash

end=$1

printf '' > input1.dat
for ((i=1;i<=$end ; i++))
do 
printf '\x47' >> input1.dat
done




./hexdump ./input1.dat
