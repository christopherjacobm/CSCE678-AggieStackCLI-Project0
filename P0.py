import sys


def main():

    args = sys.argv

    # given command
    command = " ".join(args[1:])

    # open the log file to update
    logfile = open("aggiestack-log.txt", "a")

    if args[1] == "aggiestack":
        if args[2] == "config":
            print()
    
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

def showHardware():
    status = False
    return status

def showImages():
    status = False
    return status

def showFlavors()
    status = False
    return

def showAll():
    status = False
    return status

if __name__ == "__main__":
    main()