import trafilatura
import re

def parse_link(url: str) -> str:
    """ Parses and cleans the given link input and returns the link content """
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