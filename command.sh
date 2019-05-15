if wget  -q -O -  "`  echo $1 ` " | grep -q 'cat.JPG'; then
        echo 'yeaaaaaah'
fi
echo
