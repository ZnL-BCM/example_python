# Example python package
### Last updated: 1/20/2021

**NOTE**: this package is currently **IN PROGRESS**.

This is an example python package that you can download and directly modify as you wish to make a functional python package.

Current status: **in progress**

To use it, do the following:
```
# The base module with a command
import helloworld
print(helloworld.__version__)   # This displays the version number
helloworld.hello()   # This prints a statement “hello world”
helloworld.hello_input("foo")   # This prints another statement that accepts a custom input string

# Importing and calling commands from sub-modules
import helloworld.plot as hplt
import helloworld.monty as mty
hplt.hello_plot()   # This shows an example scatter plot and is dependent on numpy and matplotlib.pyplot
mty.printmenu()   # This prints an example dataframe and is dependent on pandas
```

## Next steps

Next, we will build the following utilities: 
* Add setup.py to allow installation
* Add functions that allow args and kwargs inputs
* Reorganize files for published package format

## Usage

As the license states, since I made this by referring to multiple free online sources, it is of my best interest to not claim copyright. You are welcomed to use this repo in any way you wish. 

## Contact

Please contact Zian Liu (zian.liu@bcm.edu) if you have any questions.
