import argparse
import sys

# declare the parser
parser = argparse.ArgumentParser()

parser.add_argument("arg1", help="first argument", choices=["aggiestack"])
parser.add_argument("arg2", help="second argument", choices=["show", "config"])


group = parser.add_mutually_exclusive_group()
group.add_argument("--hardware", help="configuration file")
group.add_argument("--flavors", help="configuration file")
group.add_argument("--images", help="configuration file")


# Reads the configuration file describing
# the hardware hosting the cloud
def describeHardware(fileName):
    #read the given file
    status = False
    return status

# Reads the configuration file listing
# images available in the storage server.
def listImages(fileName):
    # process the file
    status = False
    return status

# Reads the configuration file listing the
# flavor for instances available for the
# users. A flavor specifies a virtual
# machine configuration: the amount of
# ram, number of disks, and number of
# vcpus.
def vmConfiguration(fileName):
    # read the file
    status = False

    return status
    
args = parser.parse_args()


if args.hardware:
    status = describeHardware(args.hardware)
if args.images:
    status = listImages(args.images)
if args.flavors:
    status = vmConfiguration(args.flavors)

# the complete command 
command = ' '.join(sys.argv[1:])

# update the logfile
f =  open("aggiestack-log.txt", "a")
f.write(command + " " + str(status) + "\n")
f.close()













