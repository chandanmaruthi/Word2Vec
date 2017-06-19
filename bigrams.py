import nltk
from nltk.collocations import *
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist

class preProcessText:
    tokens = None
    listRemoveWords = ['equal', 'opportunity','Linked','in','Job', 'Employer','The', 'This', 'religion','color','sex','United','Full','years','Contact','gender','veteran','span','li','Refer','Friend','Affirmative','Equal','class','age','disability','and','or','race','regard','without','oppurtunity','sexual','orientation','long','term','a','e','g','s','we','re','p']

    def __init__(self):
        strFilePath = '/Users/chandannm/Documents/chandanWorkspace/aiWorkspace/data/web/arise/data/product_manager/shotendFile1.txt'
        raw = open(strFilePath).read().decode('utf8')
        stops = set(stopwords.words("english"))
        raw = raw.split(" ")
        filtered_words = [word for word in raw if word not in stops]
        #print filtered_words
        strText = " ".join(str(x) for x in filtered_words)
        tokenizer = RegexpTokenizer(r'\w+')

        self.tokens = tokenizer.tokenize(strText)
        print "number of tokens", len(self.tokens)
        #fdist = FreqDist(tokens)
        #print list(fdist)[:10]
        text = nltk.Text(self.tokens)
        #tokens = nltk.word_tokenize(raw)


        #finder = BigramCollocationFinder.from_words(text)
        #finder.apply_freq_filter(5)
        #listA= finder.nbest(bigram_measures.pmi, 1000)  # doctest: +NORMALIZE_WHITESPACE
        #for a in listA:
        #    print a[0] , a[1]
        #-----------------------------

    def getBigramsWithScore(self):
        #tokens = nltk.word_tokenize(raw)

        #Create your bigrams
        bgs = nltk.bigrams(self.tokens)

        #compute frequency distribution for all the bigrams in the text
        fdist = nltk.FreqDist(bgs)
        print fdist.most_common(100)
        #for k,v in fdist.items():
        #    print k,v

    def getBigrams(self):
        bigram_measures = nltk.collocations.BigramAssocMeasures()

        finder = BigramCollocationFinder.from_words(self.tokens)
        scored = finder.score_ngrams(bigram_measures.raw_freq)
        finder.apply_word_filter(lambda w: w in self.listRemoveWords)
        set(bigram for bigram, score in scored) == set(nltk.bigrams(self.tokens))
        listA = sorted(finder.nbest(bigram_measures.raw_freq, 1000))
        for a in listA:
            print a[0] , a[1]
    def getTrigrams(self):
        trigram_measures = nltk.collocations.TrigramAssocMeasures()
        finder = TrigramCollocationFinder.from_words(self.tokens)
        scored = finder.score_ngrams(trigram_measures.raw_freq)
        finder.apply_word_filter(lambda w: w in self.listRemoveWords)
        set(trigram for trigram, score in scored) == set(nltk.trigrams(self.tokens))
        listA = sorted(finder.nbest(trigram_measures.raw_freq, 1000))
        for a in listA:
            print a[0] , a[1], a[2]

objPreProcessText = preProcessText()

#objPreProcessText.getBigramsWithScore()
objPreProcessText.getBigrams()
