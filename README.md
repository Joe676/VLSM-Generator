# VLSM Generator

This small program calculates ipv4 subnets given a base net address and subnet requirements such as number of subnets and their sizes.

# How to use

Make sure you have [python](https://www.python.org/downloads/) installed on your computer. Download the vlsm.py file and launch it either by double-clicking or through the terminal:  
`python vlsm.py`
Afterwards the program will prompt you for a base network. make sure to provide it in the prefix notation (for example 192.168.0.0/16).
Then provide the program with number of subnets and size of each of them **in descending order**.

# Output
The output is formated like so:

```
subnet #: address of the subnet
mask: subnet mask in decimal and prefix notation
broadcast: broadcast address of the subnet
size: max number of hosts that this subnet is suitable for
first usable: first host address in this subnet
last usable: last host address in this subnet
```
