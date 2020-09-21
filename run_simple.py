#!/usr/bin/python
from subprocess import Popen, PIPE, STDOUT
command = ['cat']
p = Popen(command, stdout=PIPE, stdin=PIPE,stderr=PIPE)
cmds="""Hello World
"""
stdout_data = p.communicate(input=cmds)
print(stdout_data)
