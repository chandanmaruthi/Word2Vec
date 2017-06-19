import sys
import gensim
new_model = gensim.models.Word2Vec.load('mymodel')
pVal = sys.argv[1]
stopWords = ['to','of','by','for','will','with','in','as']
if len(sys.argv)>2:
    nVal = sys.argv[2]
else:
    nVal=''
for a in new_model.most_similar(positive=[pVal],negative=[nVal], topn=300):
    if str(a[0]).find('_')>-1:
        if not any((True for x in str(a[0]).split('_') if x in stopWords)):
            print a[0]
