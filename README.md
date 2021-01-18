# Example python package
### Last updated: 1/17/2021

**NOTE**: this package is currently *INCOMPLETE* and not usable.

This is an example python package that you can download and directly modify as you wish to make a functional python package.

Current status: **incomplete**

The goal is to build something that can do the following:
```
# The base module with a command
import helloworld
print(helloworld.__version__)   # This displays the version number
helloworld.hello()   # This prints a statement “hello world”

# Importing and calling commands from sub-modules
import helloworld.plot as hplt
import helloworld.monty as mty
hplt.hello(figsize=[10, 5])   # This shows an example scatter plot and is dependent on matplotlib.pyplot
mty.printmenu()   # This prints a list of strings in a numpy array and is dependent on numpy
```

As the license states, since I made this by referring to multiple free online sources, it is of my best interest to not claim copyright. You are welcomed to use this repo in any way you wish without acknowledging me.

## Contact

Please contact Zian Liu (zian.liu@bcm.edu) if you have any questions.
