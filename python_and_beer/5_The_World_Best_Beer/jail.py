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

Woaw, you know things about objects structure in python!
Now I let you the menu so you can choose the beer you want. You can see some beer that you're not allowed to drink, so I'll check if you have the right to drink each beer you ask for.

Type every python code you want, to execute it juste leave an empty line. You can also use the exit() function to leave the bar
Show me what you got !


"""
sanitize=re.compile(r'(?:import|locals|exec|eval|join|format|replace|translate|try|except|with|content|frame|back|sys|dict|base|subclasses|open|builtins|class|__|raw|input)').sub
trusted_builtins="raw_input open EOFError OSError Exception False True dir".split()

alphabet = ' \n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ(),.:=_'
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
    __builtins__.__dict__["Beer"]=Beer

def restore_builtins():
    global orig
    for k, v in orig.iteritems():
        __builtins__.__dict__[k] = v

def verify_flag(flag):
    true_flag=open("flag.txt","r").read()[:-1]
    if true_flag==flag:
        print("Well done, you managed to get the flag !\nNow that you tasted the World Best Beer, I have nothing to teach you.\n\nHope you enjoyed the challenges (and the beers?)!")
    else:
        print("That's not the flag... Improve your python skills instead of trying to fuzz this chall!")

    
class Beer:
    '''
    Just a beer, because I like it
    '''

    def __init__(self,empty=False,name="beautiful Maximator", flag="There is no more default flag"):
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


your_beer=Beer(name="Tank 7", flag="It's not the default flag. Look further.")


class menu:
    '''
    The beers menu. So you can choose one of it
    '''
    global your_beer

    def __init__(self):
        self.allowed=["Kronenbourg","Grimbergen","Tank 7","Goose IPA"]
        self.beers={"Kronenbourg":"kronenbourg.txt","Grimbergen":"grimbergen.txt","Tank 7":"tank7.txt","Goose IPA":"gooseIPA.txt","Westvleteren XII":"westvleterenXII.txt"}

    def _is_allowed_beer(self,b):
        if b in self.allowed:
            return True
        else:
            return False

    def choose_beer(self):
        global your_beer
        print("Here are the list of beers that we have :")
        print("\n".join(self.beers.keys()))
        choose=raw_input("Which one do you want to drink ?\n- ")
        if choose not in self.beers.keys():
            print("That's not a beer on our menu, sorry.")
        else:
            print("Wait a bit, I'll check if you are allowed to drink it.")
            if self._is_allowed_beer(choose):
                print("You're allowed, nice!")
                beer_infos=open("beers/"+self.beers[choose],'r').read().split("\n")
                your_beer=Beer(name=beer_infos[0],flag=beer_infos[1])
                print("You're beer will be changed at next execution !")
            else:
                print("Well... You're not allowed.")





del sys,string,re,orig, alphabet
def main():
    print(bandeau)
    def sandbox():
        
        def exec_code(context):
            try:
                print("executing : "+code)
                exec(code,context)
            except Exception as e:
                print(e)

        exec_code({"your_beer":your_beer,"verify_flag":verify_flag,"menu":menu()})


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


