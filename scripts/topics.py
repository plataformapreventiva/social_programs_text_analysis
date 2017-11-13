import nltk
import matplotlib.pyplot as plt

from gensim import models
from gensim.corpora import Dictionary, MmCorpus
from gensim.models import CoherenceModel


def create_corpus(matrix, stoplist=[], stemming=True):
    """
    Generates corpus eliminating stop words

    Parameters:
    -----------
    matrix: corpus for elimintating stopwords or to stem
    stoplist (list): list of words to remove from corpus
    stemming (bool): boolean for stemming words

    Returns:
    --------
    corpus (list)
    """
    if stemming:
        stemmer = nltk.SnowballStemmer("spanish")
        corpus = [[stemmer.stem(word) for word in document.lower().split()
                   if word not in stops]
                 for document in matrix]
    else:
        corpus = [[word for word in document.lower().split()
                   if word not in stops]
                 for document in matrix]
    return corpus


def evaluate_graph(dictionary, corpus, texts, limit):
    """
    Function to calculate and plot coherence for the
    number of topcis generated with LDA

    Parameters:
    ----------
    dictionary : diccionario de gensim
    corpus : corpus de gensim
    limit : topic limit

    Returns:
    -------
    lm_list : List of LDA topic models
    c_v : Coherence values corresponding to the LDA model with respective number of topics
    plot of topics vs coherence
    """
    c_v = []
    u_mass = []
    lm_list = []
    for num_topics in range(1, limit):
        lm = models.ldamodel.LdaModel(corpus=corpus, num_topics=num_topics, id2word=dictionary,
                                      passes=500, iterations=10)
        lm_list.append(lm)
        cm1 = CoherenceModel(model=lm, texts=texts, dictionary=dictionary, coherence='c_v')
        cm2 = CoherenceModel(model=lm, corpus=corpus, dictionary=dictionary, coherence='u_mass')
        c_v.append(cm1.get_coherence())
        u_mass.append(cm2.get_coherence())

    # Show graph
    x = range(1, limit)
    with plt.style.context('ggplot'):
        f, ax = plt.subplots(figsize=(10, 6))
        plt.subplot(2, 1, 2)
        plt.plot(x, u_mass, 'g')
        plt.xlabel('topicos')
        plt.ylabel('U mass')

        plt.show()

    return lm_list, c_v
