from olclient.openlibrary import OpenLibrary
import json
from collections import namedtuple
Credentials = namedtuple("Credentials", ["username", "password"])
credentials = Credentials("openlibrary@example.com", "admin123")
ol = OpenLibrary(base_url="http://localhost:8080", credentials=credentials)

with open("adding identifiers/Hits.jsonl", "r") as f:
    isbn_dict = {data['OpenAlex'].split('/')[-1]: data['edition'].split('/')[-1] for data in map(json.loads, f)}

for id, edition in isbn_dict.items():
    edition = ol.Edition.get(edition)
    edition.add_id("OpenAlex",id)
    print(edition.identifiers)
    edition.save("edit adds an OpenAlex identifier.")
    break

