# to read the file
fileName = input("Enter file name: ")
try :
    openFile = open(fileName)
except:
    print('Cannot open the file ',fileName ,'please try again')
    quit()

for line in openFile :
    line = line.upper()
    line = line.rstrip()
    print(line)