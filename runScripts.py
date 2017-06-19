import csv
import os
import sys
scriptDir = os.path.dirname(__file__)
sys.path.append(scriptDir)
from keyWordAnalytics import *

paramFile = open("role_relevant_parameters.csv","rb")
dictParams = csv.DictReader(paramFile)

for dictParam in dictParams:
    if dictParam["Evaluate"] == "Y":
        strCommand =  "Executing for  " + dictParam["Role"] + " " + dictParam["Positive_Keys_Functional"] + " " +  dictParam["Negative_Keys_Functional"] + " "
        print strCommand
        runKeywordAnalytics(dictParam["Role"],dictParam["Positive_Keys_Functional"],dictParam["Negative_Keys_Functional"])
