import re
import unicodedata
import nltk
import pandas as pd
from nltk.corpus import stopwords

nltk.download('stopwords')


def clean_strings(var_string):
    """
    Function that cleans strings removing digits and simbols

    Parameters:
    -----------
    var_string (str): string to clean
    """
    if isinstance(var_string, str):
        var_string = re.sub(r'[^\w\s]','',var_string)
        sub_string = " ".join(re.findall("[a-zA-Z]+", var_string))
        return sub_string.strip()

def clean_and_lower(var_string):
    """
    Function that calls function for cleaning
    and returns them in lower case

    Paramaters:
    ----------
    var_string (str): string to clean
    """
    var_string = strip_accents(var_string)
    if isinstance(var_string, str):
        return clean_strings(var_string).lower()


def strip_accents(var_string):
    """
    Function that removes accents on a string

    Parameters:
    -----------
    var_string (str): string to clean
    """
    return ''.join(c for c in unicodedata.normalize('NFD', var_string)
                   if unicodedata.category(c) != 'Mn')


def stopwords_list(stopfilename='', nltkwords=True, stemming=True):
    """
    Generate a stopwords list based on a file and the nltk stopwords

    Parameters:
    ------------
    stopfilename (str): name of file that contains stop words
    nltkwords (bool): to include nltk words

    Returns:
    ---------
    stoplist (list)
    """
    stemmer = nltk.SnowballStemmer("spanish")

    stoplist = []
    if nltkwords:
        stoplist = stoplist +  stopwords.words('spanish')

    if stopfilename:
        stopfile = pd.read_csv(stopfilename, sep='\t',header=None)[0].values
        stoplist =  stoplist + list(stopfile)

    if stemming:
        stoplist = [stemmer.stem(i) for i in stoplist]

    return stoplist
