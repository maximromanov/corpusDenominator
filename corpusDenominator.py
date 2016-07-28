import os, re

# Define parameters here

separator = "\t" # you can change the separator here ("\t" for TAB, "," for COMMA, etc.)
schemeFile = "conversionList.txt" # you can change the file name of the scheme
key = "RE" # use "RE" for regular expressions, "PLAIN" for simple find/replace

# Folder variables

folderOld = "./textsOld/" # folder for texts in old orthography
folderNew = "./textsNew/" # folder for texts in new orthography
folderMod = "./textsMod/" # folder for texts in mod orthography

def dicLoad(schemeFile, separator):
    dic = {}
    with open(schemeFile, 'r', encoding="utf8") as f1:
        data = f1.read().split("\n")
        for d in data:
            if d[0] != '#':
                d = d.split(separator)
                dic[d[0]] = d[1]
    return(dic)

conversionScheme = dicLoad(schemeFile, separator)

def dictReplace(text, dic):
    for k, v in dic.items():
        text = text.replace(k, v)
    return(text)

def dictReplaceRE(text, dic):
    for k, v in dic.items():
        text = re.sub(r"%s" % k.strip(), "%s" % v.strip(), text)
    return(text)

def converter(sFolder, fileName, conversionScheme):
    with open(sFolder+fileName, "r", encoding="utf8") as f1:
        text = f1.read().lower()

        if key == "RE":
            tMod = dictReplaceRE(text, conversionScheme)
        if key == "PLAIN":
            tMod = dictReplace(text, conversionScheme)

        with open(folderMod+fileName.split(".")[0]+".txt", "w", encoding="utf8") as f9:
            f9.write(tMod)
            
        print("\tFile %s has been converted..." % fileName)
        
def process(folder):
    lof = os.listdir(folder)
    for f in lof:
        if f[0] != ".":
            print(f)
            converter(folder, f, conversionScheme)

process(folderOld)
process(folderNew)
