from pathlib import Path
from nltk.tokenize import word_tokenize
import string 
def preprocess_text(txt: str, calamancy_model, tl_stopwords, join: bool=True):
    """
    Preprocesses input text by converting it to lowercase,
    removing punctuation, tagalog stopword removal, and tagalog lemmatization
    
    Args:
        txt (str): The string input to preprocess
        calamancy_model: calamanCy model to perform tagalog lemmatization
        tl_stopwords: A list of tagalog stopwords for stopword removal
        join (bool): return joined tokens
    """

    # convert text to lowercase
    lower_text = txt.lower()

    # remove punctuation
    no_punc = lower_text.translate(str.maketrans('', '', string.punctuation))

    # tokenize
    tokenized = word_tokenize(no_punc)

    # remove stopwords
    tokens_no_stopword = [token for token in tokenized if token not in tl_stopwords]

    # join for NLP model
    res = ' '.join(tokens_no_stopword)

    # lemmatization using calamancy_model
    doc = calamancy_model(res)
    tokens = [token.lemma_ for token in doc]
    
    if join:
        preprocessed = ' '.join(tokens)
        return preprocessed

    return tokens

def load_stopwords(path: Path = "./stopwords-tl.txt"):
    """ Opens the tagalog stopwords file """
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]