import nlkt
import pandas as pd
import gensim
import numpy as np

def gen_corpus(fname, tokens_only=False, stemming=True):
    """
    Function generates gensim corpus

    Parameters:
    ----------
    fname : text
    tokens_only (bool): return only tokens
    stemming (bool): for stemming the words

    Returns:
    -------
    corpus: matrix
    """
    stemmer = nltk.SnowballStemmer("spanish")

    for i, line in enumerate(fname['descripcion_clean']):
        if tokens_only and stemming:
            yield [stemmer.stem(word) for word in gensim.utils.simple_preprocess(line) if word not in stops]
        elif tokens_only and not stemming:
            yield [word for word in gensim.utils.simple_preprocess(line) if word not in stops]
        elif not tokens_only and stemming:
            # For training data, add tags
            words = [stemmer.stem(word) for word in gensim.utils.simple_preprocess(line) if word not in stops]
            yield gensim.models.doc2vec.TaggedDocument(words, [i])
        else:
            words = [word for word in gensim.utils.simple_preprocess(line) if word not in stops]
            yield gensim.models.doc2vec.TaggedDocument(words, [i])

def similarities(train_corpus, model, lower=True):
    # Generate similarity matrix
    similarities = []
    mitad = int(round(len(train_corpus) / 2, 0))

    for doc_id in range(len(train_corpus)):
        inferred_vector = model.infer_vector(train_corpus[doc_id].words)
        sims = model.docvecs.most_similar([inferred_vector], topn= len(model.docvecs))
        similarities.append(dict(sims))

    # Get only lower matrix and replace with None's
    similarities_df = pd.DataFrame(similarities)
    if lower:
        similarities_df = pd.DataFrame(np.tril(similarities_df.values, k=-1))
    similarities_df.index = df_p.index
    similarities_df.columns = df_p.index
    similarities_df['nombre_programa'] = df_p['nombre_programa']
    similarities_df.replace(0, similarities_df.replace([0], [None]), inplace=True)
    return similarities_df

