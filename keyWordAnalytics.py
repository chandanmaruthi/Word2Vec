import sys
import gensim
import os
import csv
#  "product_backlog" "willing_to"
def runKeywordAnalytics(Role, Positive_Keys, Negative_Keys):
    aVal = Role
    pVal = Positive_Keys
    nVal = Negative_Keys
    selectedWords = {}

    print 'analyzing role' , aVal

    scriptDir = os.path.dirname(__file__)
    relPath = "../word2VecModels/all_" + aVal
    modelPath = os.path.join(scriptDir,relPath)
    print modelPath
    new_model = gensim.models.Word2Vec.load(modelPath)
    stopWords = ['to','of','by','for','will','with','in','as','or','2','3+','5+','+','e','g']

    for a in new_model.most_similar(positive=[pVal],negative=[nVal], topn=100):
        if not any((True for x in str(a[0]).split('_') if x in stopWords)):
            for b in new_model.most_similar(positive=[a[0]], topn=100):
                if not any((True for x in str(b[0]).split('_') if x in stopWords)):
                    if b[0] in selectedWords:
                        selectedWords[b[0]] +=1
                    else:
                        selectedWords[b[0]] =1

    #for key in sorted(selectedWords,key=selectedWords.get, reverse=True):
    #    if key.find('_')>-1:
    #        print key , '->', selectedWords[key]
    #    if str(a[0]).find('_')>-1:
    #        if not any((True for x in str(a[0]).split('_') if x in stopWords)):
    #            selectedWords[a[0].replace('_',' ')]= 0
    #            print a[0]



    #selectedWords['product manager'] = 0
    #selectedWords['product management'] = 0
    selectedWordsInFile={}
    scriptDir = os.path.dirname(__file__)
    relPath = "../data/roleWiseDataFolders/" + aVal + "/"
    dirPath = os.path.join(scriptDir, relPath)
    intFileCount = len(os.listdir(dirPath))
    for file in os.listdir(dirPath):
    #file = open("../data/allProfiles.txt","r")
        filePath = os.path.join(scriptDir, relPath,file)
        file = open(filePath,"rb")
        intLines = 0
        for line in file:
            line = str(line.decode('ascii','ignore'))
            for keyWord,keyVal in selectedWords.iteritems():
                if keyWord.find("_")>-1:
                    if line.lower().find(keyWord.replace("_"," "))>-1 :
                        if keyWord in selectedWordsInFile:
                            selectedWordsInFile[keyWord] +=1
                        else:
                            selectedWordsInFile[keyWord]  =1
            #print line
            intLines +=1

    summaryFilePath = os.path.join(scriptDir, "../word2Vec_Summary/"+ aVal+ ".csv")
    summaryFile = open(summaryFilePath,"wt")
    for key in sorted(selectedWordsInFile,key=selectedWordsInFile.get, reverse=True):
        print key, selectedWordsInFile[key], intFileCount
        writer = csv.writer(summaryFile)
        a = [key,selectedWordsInFile[key],intFileCount]
        writer.writerow(a)
    summaryFile.close()
