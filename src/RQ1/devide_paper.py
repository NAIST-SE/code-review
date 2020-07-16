import csv
from collections import defaultdict

with open("data/Data_Cat.csv", "r") as papers_file:
    papers = list(csv.DictReader(papers_file))

    research_types = defaultdict(int)
    practice_types = defaultdict(int)
    paper_ids = []
    research_papers = [{
        "id": x["No"],
         "researcher": [x["Researcher"], x["Researcher2"]],
         "types": x["Methodology"]
    } for x in papers]
    practice_papers = [{
        "id": x["No"],
         "practitioner": [x["Practitioner"], x["Practitioner2"], x["Practitioner3"]],
         "types": x["Methodology"]
    } for x in papers]
    # research_papers = [dict(y) for y in set(tuple(x.items()) for x in research_papers)]
    # practice_papers = [dict(y) for y in set(tuple(x.items()) for x in practice_papers)]

    for paper in research_papers:
        for subclass in [x for x in paper['researcher'] if len(x) > 0]:
            research_type = subclass + ",," + paper["types"] + ",," + "Researcher"
            research_types[research_type] +=  1
    for paper in practice_papers:
        for subclass in [x for x in paper['practitioner'] if len(x) > 0]:
            practice_type = subclass + ",," + paper["types"] + ",," + "Practitioner"
            practice_types[practice_type] +=  1

    with open("data/research_type.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Category", "Methodology", "Subclass", "size"])
        for research_type, count in research_types.items():
            writer.writerow(research_type.split(",,") +  [int(count)])
        for practice_type, count in practice_types.items():
            writer.writerow(practice_type.split(",,") +  [int(count)])
