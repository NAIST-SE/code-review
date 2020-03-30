"""
require: pip3 install pyyaml
"""
import yaml
import json
import csv
from collections import defaultdict

paper_year = defaultdict(int)
outputs = []
with open("data/Data_Cat.csv", "r") as csvdata:
    reader = csv.DictReader(csvdata)

    for paper in reader:
        bibkey = paper["Conference"] + str(paper["Year"])
        paper_year[bibkey] += 1
        methodology = [x for x in [paper["Methodology"], paper["Methodology2"], paper["Methodology3"]] if not x.isspace() and x != ""]
        researcher = [x for x in [paper["Researcher"], paper["Researcher2"]] if not x.isspace() and x != ""]
        practitioner = [x for x in [paper["Practitioner"], paper["Practitioner2"], paper["Practitioner3"]] if not x.isspace() and x != ""]

        outputs.append({
            "No": paper["No"],
            "title": paper["Title"],
            "conference": paper["Conference"],
            "year": int(paper["Year"]),
            "Data": paper["Cat."],
            "Replicatable": paper["Replicatable"],
            "Type": paper["Type"],
            "bibkey": bibkey + "_" + str(paper_year[bibkey]),
            "methodology": methodology,
            "researcher": researcher,
            "practitioner": practitioner,
            "summary": paper["Summary"]
        })
    with open(f"data/Papers.json", "w") as jsondata:
        json.dump(outputs, jsondata, indent=1)
