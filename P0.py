import sys


def main():

    args = sys.argv

    # given command
    command = " ".join(args[1:])

    # open the log file to update
    logfile = open("aggiestack-log.txt", "a")

    if args[1] == "aggiestack":
        # takes care of the config comamnds
        if args[2] == "config":
            if args[3] == "--hardware":
                status = readHardwareFile()
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "-images":
                status = readImagesFile()
                logfile.write(command + "     " + status +"\n")
            elif args[3] == "--flavors":
                status = readFlavorsFile()
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

def error(command, logfile):
    logfile.write(command + "     FAILURE" +"\n")
    print("Not a valid command \n", file=sys.stderr)
    helpMessage()
    return 

def helpMessage():
    print("Below are the only valid commands for this program:")
    print("aggiestack config --hardware <file name>\naggiestack config –images <file name>\n"\
    "aggiestack config --flavors <file name>'\naggiestack show hardware\n"\
    "aggiestack show images\naggiestack show flavors\naggiestack show all\n")

# Reads the configuration file describing
# the hardware hosting the cloud
def readHardwareFile():
    status = False
    return status

# Reads the configuration file listing
# images available in the storage server
def readImagesFile():
    status = False
    return status

# Reads the configuration file listing the
# flavor for instances available for the
# users.
def readFlavorsFile():
    status = False
    return status

# Output is the information about the
# hardware hosting the cloud 
def showHardware():
    status = False
    return status

# Output the list of images available for the
# user to choose when creating virtual machines
def showImages():
    status = False
    return status

# Output the list of flavors available for the
# user to choose when creating virtual machines
def showFlavors():
    status = False
    return status

# Output has “show” for hardware, images,flavors
def showAll():
    status = False
    return status

if __name__ == "__main__":
    main()