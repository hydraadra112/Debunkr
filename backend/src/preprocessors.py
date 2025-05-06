from pathlib import Path
from nltk.tokenize import word_tokenize
import string 

import trafilatura
import re

def parse_and_clean_link(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return ""

    result = trafilatura.extract(downloaded, output_format='txt')
    if not result:
        return ""

    # Clean text: remove non-alphanumeric characters (except apostrophes), normalize whitespace
    cleaned_text = re.sub(r"[^\w\s']", ' ', result)
    cleaned_text = re.sub(r'[\t\n\r\f\v]', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip()


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

def load_stopwords(path: Path = Path("./src/notebooks/stopwords-tl.txt")):
    """ Opens the tagalog stopwords file """
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]