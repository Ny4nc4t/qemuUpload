#chr() {
#  [ ${1} -lt 256 ] || return 1
#  printf \\$(printf '%03o' $1)
#}
chr() {
  testing=$(printf '\%o' '68' )
}


hhr () {
  [ ${1} -lt 256 ] 
  number=\\$(($1/64*100+$1%64/8*10+$1%8))
}
chr 68 
printf $(printf '\%o' '68' )
echo $testing
