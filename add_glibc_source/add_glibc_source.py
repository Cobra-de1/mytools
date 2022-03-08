import gdb
import os

def add_all_folder(path):
	gdb.execute('dir ' + path)
	dir = os.listdir(path)
	for i in dir:
		subfolder = path + i + '/'
		if os.path.isdir(subfolder):
			add_all_folder(subfolder)

add_all_folder('~/Install/glibc/')
#add_all_folder('/home/cobra/Install/system_glibc_source/glibc-2.31/')

