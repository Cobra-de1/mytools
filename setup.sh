#!/bin/sh

echo "source /home/cobra/Install/mytools/add_glibc_source/add_glibc_source.py" >> ~/.gdbinit
chmod 777 ./libc/libc /obj_to_hex/obj_to_hex
cp ./libc/libc /usr/bin/
cp ./obj_to_hex/obj_to_hex /usr/bin/

