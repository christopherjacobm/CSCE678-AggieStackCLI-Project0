# Project P0 
# CSCE 678 - Distributed Systems and Cloud Computing
This projects implements AggieStack CLI (the CLI for an OpenStack, a free and open source Software Platform for cloud computing.)
The project has been implemented in Python 3.

The project is divided into two parts:

### 1. **AggieStack CLI** - Part I : reads from the command line and generates output. 

The commands implemented are:
- aggiestack config --hardware <file name>
- aggiestack config -images <file name>
- aggiestack config --flavors <file name>
- aggiestack show hardware
- aggiestack show images
- aggiestack show flavors
- aggiestack show all

A Log file is mantained to show the status of each command - SUCCESS or FAILURE

### 2. **AggieStack CLI** - Part II: capability to represent instances.

The commands implemented are:
- aggiestack admin show hardware
- aggiestack admin can_host <machine name> <flavor>

### Instructions for running
- The project runs on Python3. Please install Python3 in order to run the program.
- cd folder_name
- git clone https://github.tamu.edu/sgill12/678-18-c.git
- cd 678-18-c
- Files: configurations.txt files - image-config.txt, hdwr-config.txt and flavor-config.txt need to be present in the folder structure, 
as these are the input files for the script.

- python3 P0.py aggiestack config --hardware hdwr-config.txt
- python3 P0.py aggiestack config -images image-config.txt
- python3 P0.py aggiestack config -flavors flavor-config.txt

(These commands will create the corresponding .dct files, needed to run the rest of the commands)

Now, can simply run the above written commands by using *python3 P0.py* infront of it.
Example:

python3 P0.py aggiestack show flavors

### Team Members
-- Bhavesh Munot (227002818)
-- Sukhdeep Gill (326007739)
-- Christopher Mureekan (227001713)
-- Krit Gupta (927001565)


