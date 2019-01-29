#!/usr/bin/python2
# -*- encoding:utf-8 -*-

#Secure Python Sandbox

import re
import os
import sys
import time
import string
from sys import stdout
sys.stderr=stdout

sanitize=re.compile(r'(?:import|locals|exec|eval|join|format|replace|translate|try|except|with|content|frame|back|os|sys|\[|\])').sub
trusted_builtins="EOFError OSError Exception False True dir".split()

orig = __builtins__.__dict__
fakeBuiltins={}
for i in trusted_builtins:
    fakeBuiltins[i] = orig[i]

alphabet = ' \n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ(),.:=_+[]'

t1 = ''.join(chr(code) for code in xrange(256))
t2 = []
for i in t1:
    if i in alphabet:
        t2.append(i)
    else:
        t2.append(' ')
trans_table = string.maketrans(t1, ''.join(t2))

del sys,string,re,orig, alphabet

def main():

    def sandbox():
        
        def exec_code(context):
            try:
                print("executing : "+code)
                exec(code,context)
            except Exception as e:
                print(e)

        exec_code({"__builtins__":fakeBuiltins})


    boucle=True
    while boucle:
        code=[]
        while True:
            try:
                entree=raw_input("> ")
                if entree=='':
                    break
                if entree=='exit()':
                    boucle=False
                    break

                code.append(entree)

            except EOFError:
                break

        code=sanitize("---LOLNOP---","\n".join(code).translate(trans_table))
        sandbox()


if __name__=='__main__':
    main()


