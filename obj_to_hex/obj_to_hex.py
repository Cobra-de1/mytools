#!/usr/bin/python

import subprocess
import sys

if len(sys.argv) < 2:
	print('Usage: python ' + sys.argv[0] + ' <filename>')
	exit(0)

subprocess = subprocess.Popen('objdump -d ' + sys.argv[1], shell=True, stdout=subprocess.PIPE)

output = subprocess.stdout.read().decode('utf-8')

print(output)

lines = output.strip().split('\n')

hexdump = ''
flag = False
for line in lines:
	if '<_start>' in line:
		flag = True
	elif flag:
		hexdump += line[line.find('\t'):line.find('\t', line.find('\t') + 1)].strip('\t')

print('\\x' + '\\x'.join([x for x in hexdump.split(' ') if x]))
