# import modules & set up logging
import gensim, logging
from gensim.models import Phrases
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import sys
import unicodedata
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# Step 1: Clean data
# Step 2: Verify trigrams
# Step 3 : Review
# Step 4 : Get the best matches based on cosine distance
def trainWord2Vec(fileName, modelName):
    # train word2vec on the two sentences
    file = open("../data/mergedDatasets/"+fileName,"r")
    #sentences = file.read()
    bigram = Phrases()
    lines =[]
    for line in file:
        line = str(line.decode('ascii','ignore'))
        #replace special charecters with spaces to it does not confuce for words
        for charec in line:
            if charec in [',','\'','.','-','_','!','|','@','#','$','%','^','*','~','(',')','{','}']:
                line = line.replace(charec,' ')
        #remove pre and post white spaces
        line = line.strip()

        if len(line)>0:
            wordArray = line.split(" ")
            wordArray = map(str.lower,wordArray)
            if len(wordArray)>15:
                lines.append(wordArray)
    sentences = lines

    print sentences

    bigram.add_vocab(sentences)
    trigram = Phrases(bigram[sentences])
    fourgram = Phrases(trigram[bigram[sentences]])
    #for a in bigram.vocab.keys():
    #    if str(a).find("_")>0 :print a
    mymodel = gensim.models.Word2Vec(fourgram[trigram[bigram[sentences]]], min_count=15, size=200, workers=4)
    mymodel.save("../word2VecModels/"+ modelName)


def evaluateWord2Vec():
    new_model = gensim.models.Word2Vec.load('mymodel')
    print new_model.accuracy('questions-words.txt')


def plot_with_labels(low_dim_embs, labels, filename='tsne.png'):
  assert low_dim_embs.shape[0] >= len(labels), "More labels than embeddings"
  plt.figure(figsize=(36, 36))  #in inches
  for i, label in enumerate(labels):
    x, y = low_dim_embs[i,:]
    plt.scatter(x, y)
    plt.annotate(label,
                 xy=(x, y),
                 xytext=(5, 2),
                 textcoords='offset points',
                 ha='right',
                 va='bottom')

  plt.savefig(filename)

def plotWord2Vec(modelName):
    try:
      w2vModel = gensim.models.Word2Vec.load("../word2VecModels/" + modelName)
      tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000)
      plot_only = 1000
      vectors =[]
      labels = w2vModel.index2word
      selected_labels =[]
      for word in w2vModel.index2word:
          if "_" in word:
              vectors.append(w2vModel[word])
              selected_labels.append(word)

      low_dim_embs = tsne.fit_transform(vectors[:plot_only])
      #labels = [reverse_dictionary[i] for i in xrange(plot_only)]
      labels = selected_labels[:plot_only]
      plot_with_labels(low_dim_embs, labels,modelName + ".png")

    except ImportError:
      print("Please install sklearn, matplotlib, and scipy to visualize embeddings.")


fileName = sys.argv[1]
modelName = sys.argv[2]
trainWord2Vec(fileName,modelName)
plotWord2Vec(modelName)
