# gromacsplotter

GROMACS natively produces xvg output files for use with xmgrace.
I don't like that too much, so this is a quick and incomplete way
to plot those output files with matplotlib.

## Install

Download or clone the files, change to the gromacsplotter's top level directory
and type
```
$ python setup.py install
```
You might need root access for that, or you can use the `--user` option to install only
for your account.

## Command Line Script

Since this is about quickly plotting the xvg output, a command line script is provided.
After install, it should be in your PATH, so that you can use
```
$ gromacsplotter <name-of-xvg-file>
```
to create a plot.
There are currently no options or arguments implemented. It will plot all the columns
found in the file against the first column, and will try to read the axis labels and
title from the xvg file.