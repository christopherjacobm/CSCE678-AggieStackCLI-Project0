import sys
import os.path
import pickle
from collections import OrderedDict


def main():
    # command line arguments
    args = sys.argv

    # given command
    command = " ".join(args[1:])

    # open the log file if exists already, otherwise create one
    logfile = "aggiestack-log.txt"
    if fileExists(logfile):
        logfile = open(logfile, "a")
    else:
        logfile = open(logfile, "w")

    # command length should be atleast 4
    if (len(args) < 4):
        error(command, logfile)
        sys.exit(0)

    if args[1] == "aggiestack":
        # takes care of the config comamnds
        if args[2] == "config":
            if args[3] == "--hardware" and args[4]:
                status = readHardwareFile(args[4])
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "-images" and args[4]:
                status = readImagesFile(args[4])
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "--flavors" and args[4]:
                status = readFlavorsFile(args[4])
                logfile.write(command + "     " + status +"\n")
            else:
                error(command, logfile)

        # takes care of the show commands
        elif args[2] == "show":
            if args[3] == "hardware":
                status = showHardware()
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "images":
                status = showImages()
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "flavors":
                status = showFlavors()
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "all":
                status = showAll()
                logfile.write(command + "     " + status +"\n")
            else:
                error(command, logfile)
        else:
            error(command, logfile)
    else:
        error(command, logfile)

# print error
def error(command, logfile):
    logfile.write(command + "     FAILURE" +"\n")
    print("Not a valid command \n", file=sys.stderr)
    helpMessage()
    return 

# print help message
def helpMessage():
    print("Below are the only valid commands for this program:")
    print("aggiestack config --hardware <file name>\naggiestack config –images <file name>\n"\
    "aggiestack config --flavors <file name>'\naggiestack show hardware\n"\
    "aggiestack show images\naggiestack show flavors\naggiestack show all\n")

# Reads the configuration file describing
# the hardware hosting the cloud
def readHardwareFile(fileName):
    status = "FAILURE"

    # dictionary that stores all the machines
    hardwareList = {}

    #dictionary that stores the machine configuration
    machineConfig = {}

    fileExist= fileExists(fileName)
    
    if fileExist:
        f = open(fileName, "r")
        machines = f.readlines()

        harwareConfigurationFile = "hardwareConfiguration.dct"

        if fileExists(harwareConfigurationFile) and fileNotEmpty(harwareConfigurationFile):
            with open(harwareConfigurationFile, "rb") as f:
                hardwareList = pickle.load(f)

        for m in machines[1:]:
            machine = m.split()
            machineConfig["ip"] = machine[1]
            machineConfig["mem"] = machine[2]
            machineConfig["num-disks"] = machine[3]
            machineConfig["num-vcpus"] = machine[4]
            hardwareList[machine[0]] = machineConfig

        # print(hardwareList)
        # hardwareList = OrderedDict(sorted(hardwareList.items(), key=lambda x: x[0]))

        with open("hardwareConfiguration.dct", "wb") as f:
            pickle.dump(hardwareList, f)

        status = "SUCCESS"

    else:
        print("Given file does not exit")

    return status

# Reads the configuration file listing
# images available in the storage server
def readImagesFile(fileName):
    status = "FAILURE"
    
    fileExist= fileExists(fileName)
    
    if fileExist:
        f = open(fileName, "r")

    return status

# Reads the configuration file listing the
# flavor for instances available for the
# users.
def readFlavorsFile(fileName):
    status = "FAILURE"

    fileExist= fileExists(fileName)
    
    if fileExist:
        f = open(fileName, "r")

    return status
    

# Output is the information about the
# hardware hosting the cloud 
def showHardware():
    status = "SUCCESS"

    # hardwareConfig = {}

    if fileExists("hardwareConfiguration.dct") and fileNotEmpty("hardwareConfiguration.dct"):
        with open("hardwareConfiguration.dct", "rb") as f:
            hardwareConfig = pickle.load(f)
 
        hardwareConfigDict = OrderedDict(sorted(hardwareConfig.items(), key=lambda x: x[0]))
        # printMachineHardwareDict(hardwareConfigDict)
    
        printMachineHardwareDict(hardwareConfigDict)

    else:
        print("No hardware information available")
    return status

# Output the list of images available for the
# user to choose when creating virtual machines
def showImages():
    status = "FAILURE"
    return status

# Output the list of flavors available for the
# user to choose when creating virtual machines
def showFlavors():
    status = "FAILURE"
    return status

# Output has “show” for hardware, images,flavors
def showAll():
    status = "FAILURE"
    return status

# check if the given file exits 
def fileExists(fileName):
    # get the current working directory
    cwd = os.getcwd()
    filePath = cwd + "/" + fileName

    if os.path.isfile(filePath):
        return True
    else:
        return False

# print the hardware config info
def printMachineHardwareDict(dict):
    for machine, configuration in dict.items():
        print('%s : %s' % (machine, configuration))

def fileNotEmpty(fileName):
    cwd = os.getcwd()

    if (os.path.getsize(cwd + "/" + fileName) > 0):
        return True
    else:
        return False

if __name__ == "__main__":
    main()