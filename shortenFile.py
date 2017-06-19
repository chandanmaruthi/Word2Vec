file=open("../data/web/arise/data/product_manager/allfiles.txt")
file2=open("../data/web/arise/data/product_manager/shotendFile1.txt","wb")

strLines=""
for line in file:
    line = line.strip()
    words = line.split(" ")
    if len(words)>15:
        strLines += line
        print line
file.close()
file2.write(strLines)
file2.close()
