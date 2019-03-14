#python gadgets.py --test -length $1 /lib/x86_64-linux-gnu/libc-2.24.so
#python gadgets.py --test -length $1 /bin/ls
#python gadgets.py --test -length $1 hexdump
python kengadgets.py --test -length $1 hexdump
