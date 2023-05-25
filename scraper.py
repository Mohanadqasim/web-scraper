import requests
from bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count (URL):
    """
    Retrieves the number of citations needed from a Wikipedia page.

    Args:
        URL (str)

    Returns:
        The count of citations needed on the given Wikipedia page.
    """
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_post=soup.find_all('sup',class_="noprint")
    return print("The citation nedded count is : ",len(all_post))


def get_citations_needed_report(URL):
    """
    This function provides a report of the citations needed in the given URL.
    """
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    paragraphs = soup.find_all("p")
    citations_needed = []
    for paragraph in paragraphs:
        if paragraph.find("sup", class_="noprint"):
            citation_text = paragraph.text.strip()
            citations_needed.append(citation_text)
    report = "\n\n".join(citations_needed)
    return print (report)

get_citations_needed_count(URL)
get_citations_needed_report(URL)