import os

for filename in os.listdir(os.getcwd()):
    sourceFile = open(filename, "r")
    content = sourceFile.read()
    sourceFile.close()
    outFile = open("output.docx", "a")
    outFile.write("----------------------------" + str(filename) + "----------------------\n\n")
    outFile.write(content)
    outFile.write("\n\n-------------------------------EOF-------------------------------\n\n")
    outFile.close()

    
    


