import pyfiglet
import sys
import os
import platform
import time
import requests

class ComputerSys:

    def __int__(self):
        print("Initialize...")

    ascii_banner = pyfiglet.figlet_format("COMPUTER SYSINFO")
    print(ascii_banner)

    time.sleep(3)



    def chooseModul(self):
        print("""
        [1].OperatingSys
        [2].OperatingDirectory
        [3].NowDirectory
        [4].DirectoryInFolder
        [5].WindowsVersion
        [6].CodeWorkingOperatingSys
        [7].PythonDirectorySetup
        [8].PythonVersionNumber
        [9].ProcessingInfo
        [10].ProcessingArchitecture
        [11].help
        [12].Show Options
        [13].Exit
        """)
        while True:
            choose = int(input("Choose Option ==>>"))


            if choose == 1:
                computers.operatingSys()
                continue

            if choose == 2:
                computers.operatingDirectory()
                continue

            if choose == 3:
                computers.nowDirectory()
                continue

            if choose == 4:
                computers.directoryInFolder()
                continue

            if choose == 5:
                computers.windowsVersion()
                continue

            if choose == 6:
                computers.codeWorkingOperatingSys()
                continue

            if choose == 7:
                computers.pythonDirectorySetup()
                continue

            if choose == 8:
                computers.pythonVersionNumber()
                continue

            if choose == 9:
                computers.processingInfo()
                continue

            if choose == 10:
                computers.processingArch()
                continue

            if choose == 11:
                print("Usage ==>> 1")
                continue

            if choose == 12:
                print("""
                [1].OperatingSys
                [2].OperatingDirectory
                [3].NowDirectory
                [4].DirectoryInFolder
                [5].WindowsVersion
                [6].CodeWorkingOperatingSys
                [7].PythonDirectorySetup
                [8].PythonVersionNumber
                [9].ProcessingInfo
                [10].ProcessingArchitecture
                [11].help
                [12].Show Options
                [13].Exit
                """)

            if choose == 13:
                break

            elif choose > 13:
                print("enter a value 1-13!")
                continue




    def operatingSys(self):
        #this function learning operating System name
        os_name = os.name
        print("Operating System ==>> {}".format(os_name))
        #print(type(os_name))

        if os_name == 'nt':
            print("Windows-based operating system family")

        elif os_name == 'posix':
            print("Unix-based operating system family")

        else:
            print("Default!!!")




    def operatingDirectory(self):
        #It shows us what the index separator of the operating system our code is running on.
        os_sep = os.sep
        print("Operating Directory Seperator ==>> {}".format(os_sep))


    def nowDirectory(self):
        # this function tells you the directory you are in
        os_getwd = os.getcwd()
        print("Operating Directory Now ==> {}".format(os_getwd))

        return os_getwd


    def directoryInFolder(self):
        #this function allows us to list files and folder in a directory
        present_directory = os.getcwd()

        for fl in os.listdir(present_directory):
            print("Directory in Folder ==>> {}".format(fl))
            #print(type(fl))



    def windowsVersion(self):
        #This function only works onwindows
        windows_vers = sys.getwindowsversion()
        print("Windows Version ==>> {}".format(windows_vers))



    def codeWorkingOperatingSys(self):
        #this function tells us about the operating system our code is running on
        print("Our code is running Operating System ==>> {}".format(sys.platform))



    def pythonDirectorySetup(self):
        """
        this function Shows which directory Python is installed in
        print("Which setup python show ==>> {}".format(sys.prefix))
        """

        try:
            print("Which setup python show ==>> {}".format(sys.prefix))
        except FileNotFoundError:
            print("You do not have python on your computer\n")
            print("Select to Download(Y/N)")

            while True:
                chose = input("(Y/N)")

                if chose == "Y":
                    want = requests.get('https://www.python.org/')
                    time.sleep(2)
                    print(want)

                if chose =="N":
                    break

                else:
                    print("Wrong Choose")
                    continue





    def pythonVersionNumber(self):
        #this function Returns the major version number and minor version number of Python
        #print("Python Version showing major and minor ==>> {}".format(sys.winver))

        try:
            print("Python Version showing major and minor ==>> {}".format(sys.winver))
        except FileNotFoundError:
            print("You do not have python on your computer\n")
            print("Select to Download(Y/N)")

            while True:
                chose = input("(Y/N)")

                if chose == "Y":
                    want = requests.get('https://www.python.org/')
                    time.sleep(2)
                    print(want)

                if chose == "N":
                    break

                else:
                    print("Wrong Choose")
                    continue



    def processingInfo(self):
        #this function Python program to display platform processor
        print("Platform Processor ==>> {}".format(platform.processor()))




    def processingArch(self):
        #this function Python program to display platform architecture
        print("Platform Architecture ==>> {}".format(platform.architecture()))



computers = ComputerSys()

ComputerSys.ascii_banner

computers.chooseModul()
