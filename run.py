#!/usr/bin/python
import sys
from subprocess import Popen, PIPE, STDOUT




def run_command(command):
    print('Running command ' + command)
    #command = ['cat']
    p = Popen(command, stdout=PIPE, stdin=PIPE,stderr=PIPE)
    #cmds="""Hello World
    #"""
    #stdout_data = p.communicate(input=cmds)
    stdout_data = p.communicate()
    print(stdout_data)

def main(args):
    for arg in args:
        print('arg ' + arg)
        out = run_command(arg)
        print(out)

main(sys.argv[1:])
