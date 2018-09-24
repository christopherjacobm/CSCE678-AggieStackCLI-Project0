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
                status = readInputFile(args[4], "hardwareConfiguration.dct")
                if status == "SUCCESS":
                    status = updateCurrentHardware()
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "-images" and args[4]:
                status = readInputFile(args[4], "imageConfiguration.dct")
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "--flavors" and args[4]:
                status = readInputFile(args[4], "flavorConfiguration.dct")
                logfile.write(command + "     " + status +"\n")
            else:
                error(command, logfile)

        # takes care of the show commands
        elif args[2] == "show":
            if args[3] == "hardware":
                status = showContent("hardwareConfiguration.dct")
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "images":
                status = showContent("imageConfiguration.dct")
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "flavors":
                status = showContent("flavorConfiguration.dct")
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "all":
                status = showAll()
                logfile.write(command + "     " + status +"\n")
            else:
                error(command, logfile)
				
		# takes care of the admin commands
        elif args[2] == "admin":
            if args[3] == "show":
                if args[4] == "hardware":
                    status = showContent("currentHardwareConfiguration.dct")
                    logfile.write(command + "     " + status +"\n")
                else:
                    error(command, logfile)
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
    "aggiestack show images\naggiestack show flavors\naggiestack show all\n"\
	"aggiestack admin show hardware\n")

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

"""
Reads the given file and 
save the content into a file
"""
def readInputFile(fileToRead, savedFile):
    status = "FAILURE"

    # a dictionary to store all the configurations
    contentList = {}

    # a dictionary to store only one instance's config
    config = {}

    # chekc if the file exists
    fileExist= fileExists(fileToRead)
    
    if fileExist:

        hardware = ["ip", "mem", "num-disks", "num-vcpus"]
        image = ["path"]
        flavor = ["num-disks", "num-vcpus"]

        if (savedFile == "hardwareConfiguration.dct"):
            listToLoop = hardware
        elif (savedFile == "imageConfiguration.dct"):
            listToLoop = image
        else:
            listToLoop = flavor

        # open the input file to read
        f = open(fileToRead, "r")
        lines = f.readlines()

        if fileExists(savedFile) and fileNotEmpty(savedFile):
            with open(savedFile, "rb") as f:
                contentList = pickle.load(f)

        # save the file data
        for line in lines[1:]:
            tokens = line.split()
            
            for i, val in enumerate(listToLoop):
                config[val] = tokens[i+1]
            
            contentList[tokens[0]] = config
            config = {}
            

        with open(savedFile, "wb") as f:
            pickle.dump(contentList, f)

        status = "SUCCESS"

    else:
        print("Given file does not exist")

    return status


"""
showContent method - sub-method
Used in various methods
"""
def showContent(fileToRead):
    status = "SUCCESS"

    if fileExists(fileToRead) and fileNotEmpty(fileToRead):
        with open(fileToRead, "rb") as f:
            config = pickle.load(f)
 
        configDict = OrderedDict(sorted(config.items(), key=lambda x: x[0]))
    
        printMachineHardwareDict(configDict)

    else:
        print("No information available")
    return status
	

"""
showAll - Used in show -all
Giving the statistics of all the resources
"""
def showAll():
    status = "SUCCESS"

    print("Hardware Info: \n")
    showContent("hardwareConfiguration.dct")
    print("Image Info: \n")
    showContent("imageConfiguration.dct")
    print("Flavor Info: \n")
    showContent("flavorConfiguration.dct")

    return status
	
	
"""
updateCurrentHardware - Updates currentHardwareConfiguration.dct whenever hardwareConfiguration.dct is updated 
TODO: handle all cases when vCPUs can be allocated, as some entries should not be overwritten
"""	
def updateCurrentHardware():
    status = "FAILURE"
    hardwareFile = "hardwareConfiguration.dct"
    currHardwareFile = "currentHardwareConfiguration.dct"
    columns = ["mem", "num-disks", "num-vcpus"]
	
	# a dictionary to store all the configurations
    currHardwareDict = {}
	
    if fileExists(hardwareFile) and fileNotEmpty(hardwareFile):
        with open(hardwareFile, "rb") as f:
            hardwareDict = pickle.load(f)

		# copy data from one dictionary to the other
        for machineName, machineInfo in hardwareDict.items():
            config = {}
            for val in columns:
                config[val] = machineInfo[val] 
	
            currHardwareDict[machineName] = config
		
		# save to currHardwareDict
        with open(currHardwareFile, "wb") as f:
            pickle.dump(currHardwareDict, f)
			
        status = "SUCCESS"
    else:
        print("No information available")
    return status

if __name__ == "__main__":
    main()