import os, sys
mergedFilePath = "../data/mergedDatasets"
files = os.listdir(mergedFilePath)
#print files
for fileName in files:
    lenOfFileName = len(fileName)
    systaxStr = "python gensimWordtoVec.py '" +  fileName + "' '" + fileName[:lenOfFileName-4]+"'"
    print systaxStr
    os.system(systaxStr)
