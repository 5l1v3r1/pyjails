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


bandeau="""         . .
       .. . *.
- -_ _-__-0oOo
 _-_ -__ -||||)
    ______||||______
~~~~~~~~~~`""'
Welcome to the P&B's bar.
Our customers are exigent, they want good beer. But in this bar, good beers are only for people who knows python.

There some known payload when you're doing a pyjail... Just drink your Goose IPA and go further !


Type every python code you want, to execute it juste leave an empty line. You can also use the exit() function to leave the bar
Show me what you got !


"""

sanitize=re.compile(r'(?:import|locals|exec|eval|join|format|replace|translate|try|except|with|content|frame|back|os|sys|open|builtins)').sub
trusted_builtins="open EOFError OSError Exception False True dir".split()

alphabet = ' \n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ(),.:+-=_0123456789[]"\'/'
orig=None

t1 = ''.join(chr(code) for code in xrange(256))
t2 = []
for i in t1:
    if i in alphabet:
        t2.append(i)
    else:
        t2.append(' ')
trans_table = string.maketrans(t1, ''.join(t2))

def clear_builtins():
    global orig
    orig = __builtins__.__dict__.copy()
    __builtins__.__dict__.clear()
    for i in trusted_builtins:
        __builtins__.__dict__[i] = orig[i]

def restore_builtins():
    global orig
    for k, v in orig.iteritems():
        __builtins__.__dict__[k] = v

def verify_flag(flag):
    true_flag=open("flag.txt","r").read()[:-1]
    if true_flag==flag:
        print("Well done, you managed to get the flag !\nLet's have a better beer !\n\nNext time you'll come, you'll have access to this new beer with this flag as passord to the user pybeer4")
    else:
        print("That's not the flag... Improve your python skills instead of trying to fuzz this chall!")

class beer:
    '''
    Just a beer, because I like it
    '''

    def __init__(self,empty=False,name="beautiful Maximator", flag="There is no flag"):
        self._empty=empty
        self._what_the_flag=flag
        self._name=name

    def _get_name(self):
        return self._name
    
    def _is_empty(self):
        if self._empty:
            return True
        else:
            return False

    def _set_empty(self,val):
        if val not in [True,False]:
            print("That's not how it's supposed to be used !")
            exit()
        else:
            self._empty=val

    def drink(self):
        if not(self._is_empty()):
            print("You drink your whole %s in one time ! You was that thirsty ?" % self._get_name())
            self._set_empty(True)
        else:
            print("What are you trying to do ? There is no more %s in your glass" % self._get_name())

    def fill(self):
        if self._is_empty():
            print("You pourred some %s in your glass..." % self._get_name())
            self._set_empty(False)
        else:
            print("Your glass is already filled with %s. Do you really want to waste it ?" % self._get_name())


gooseIPA=beer(name="Goose IPA", flag="There is not flag here")

del sys,string,re,orig, alphabet, beer
def main():
    print(bandeau)
    def sandbox():
        
        def exec_code(context):
            try:
                print("executing : "+code)
                exec(code,context)
            except Exception as e:
                print(e)

        exec_code({"gooseIPA":gooseIPA,"verify_flag":verify_flag})


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
        clear_builtins()
        sandbox()
        restore_builtins()


if __name__=='__main__':
    main()


