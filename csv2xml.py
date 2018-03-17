#creates the XML tags
def openbracket(str):
    return "<"+str+">"

def closebracket(str):
    return "</"+str+"> \n"

def splitArray(str):
    if("|" in str):
        arr = str.split("| ")
        return arr
    else:
        return str

def main():

    #get the name of the file we want to read
    filename = input("Enter the path to the CSV file you want to convert \n")
    entitiyname = input("What will your entries be called? enter 'd' for default")

    if(entitiyname == "d"):
        entitiyname = "object"

    #create the new xml file
    newfilename = filename[0: len(filename)-4] + ".xml"
    newfile = open(newfilename, "w")
    newfile.write(openbracket(entitiyname + "s"))
    newfile.write("\n")

    #open CSV file and iterate over lines
    with open(filename, "r") as file:
        linect = 0
        for line in file:
            #take in first line which includes the attributes
            if(linect < 1):
                headers = line.strip()
                headers_arr = headers.split(', ')
            else:
                #for every data line, write the corresponding entry into it
                data = line.strip()
                data_arr = data.split(", ")

                newfile.write(openbracket(entitiyname) + "\n")

                for element in headers_arr:
                    writeme = splitArray(data_arr[headers_arr.index(element)])
                    if(writeme == data_arr[headers_arr.index(element)]):
                        newfile.write(openbracket(element))
                        newfile.write(writeme)
                        newfile.write(closebracket(element))
                    else:
                        for el in writeme:
                            newfile.write(openbracket(element))
                            newfile.write(el)
                            newfile.write(closebracket(element))                

                newfile.write(closebracket(entitiyname))

            linect += 1

    newfile.write(closebracket(entitiyname + "s"))
    newfile.close()


main()
