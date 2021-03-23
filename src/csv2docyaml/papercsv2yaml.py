"""
require: pip3 install pyyaml
"""
import csv
from yaml import dump
from collections import defaultdict

paper_year = defaultdict(int)

with open("data/Data_Cat.csv", "r") as csvdata:
    reader = csv.DictReader(csvdata)

    for paper in reader:
        bibkey = paper["No"]
        paper_year[bibkey] += 1
        methodology = [x for x in [paper["Methodology"], paper["Methodology2"], paper["Methodology3"]] if not x.isspace() and x != ""]
        researcher = [x for x in [paper["Researcher"], paper["Researcher2"]] if not x.isspace() and x != ""]
        practitioner = [x for x in [paper["Practitioner"], paper["Practitioner2"], paper["Practitioner3"]] if not x.isspace() and x != ""]

        output_format = {
            "layout": "publication",
            "title": paper["Title"],
            "conference": paper["Conference"],
            "year": int(paper["Year"]),
            "bibkey": bibkey + "_" + str(paper_year[bibkey]),
            "methodology": methodology,
            "researcher": researcher,
            "practitioner": practitioner,
            "summary": paper["Summary"]
        }
        with open(f"docs/_publications/{bibkey}.md", "w") as yamldata:
            yamldata.write("---\n" + dump(output_format) + "---\n")