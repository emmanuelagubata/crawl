import requests

Url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=7152508&retmode=json&tool=my_tool&email=my_email@example.com"

r = requests.get(url = Url)

data = r.json()

print(data)