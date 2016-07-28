# corpusDenominator

This is a small program written to bring corpora in the same language but in different orthographies to common orthographic denominator. It creates a “deformed” but orthographically uniform corpus for stylometric analysis with `R` ((https://github.com/computationalstylistics/stylo)[https://github.com/computationalstylistics/stylo]).

# Parameters in `corpusDenominator.py`
```
# Define parameters here

separator = "\t" # you can change the separator here ("\t" for TAB, "," for COMMA, etc.)
schemeFile = "conversionList.txt" # you can change the file name of the scheme
key = "RE" # use "RE" for regular expressions, "PLAIN" for simple find/replace

# Folder variables

folderOld = "./textsOld/" # folder for texts in old orthography
folderNew = "./textsNew/" # folder for texts in new orthography
folderMod = "./textsMod/" # folder for texts in mod orthography
```