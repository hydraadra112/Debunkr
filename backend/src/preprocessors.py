import nltk
from pathlib import Path
import string
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def preprocess_text(txt: str, calamancy_model, tl_stopwords, join: bool=True):
    """
    Preprocesses input text by converting it to lowercase,
    removing punctuation, applying Tagalog & English stopword removal,
    and performing Tagalog & English lemmatization.

    Args:
        txt (str): Input text
        calamancy_model: calamanCy model for Tagalog lemmatization
        tl_stopwords (list): Tagalog stopword list
        join (bool): Whether to return a joined string or list of tokens
    """
    # Initialize English tools
    en_stopwords = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    # Step 1: Lowercase
    lower_text = txt.lower()

    # Step 2: Remove punctuation
    no_punc = lower_text.translate(str.maketrans('', '', string.punctuation))

    # Step 3: Tokenize
    tokenized = word_tokenize(no_punc)

    # Step 4: Remove Tagalog and English stopwords
    tokens_no_stop = [
        token for token in tokenized
        if token not in tl_stopwords and token not in en_stopwords
    ]

    # Step 5: Lemmatize with calamancy (Tagalog)
    calamancy_doc = calamancy_model(' '.join(tokens_no_stop))
    calamancy_lemmas = [token.lemma_ for token in calamancy_doc]

    # Step 6: Lemmatize again with English lemmatizer (handles English tokens better)
    final_tokens = [lemmatizer.lemmatize(token) for token in calamancy_lemmas]

    # Step 7: Return
    if join:
        return ' '.join(final_tokens)
    else:
        return final_tokens

def load_stopwords(path: Path = Path("./src/notebooks/stopwords-tl.txt")):
    """ Opens the tagalog stopwords file """
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

from PyPDF2 import PdfReader
from io import BytesIO

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    try:
        pdf_file = BytesIO(pdf_bytes)
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"PDF processing error: {str(e)}")