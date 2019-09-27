import csv
from collections import defaultdict

with open("Excel_data/papers.csv", "r") as papers_file:
    papers = list(csv.DictReader(papers_file))

    research_types = defaultdict(int)
    practice_types = defaultdict(int)
    paper_ids = []
    research_papers = [{
        "id": x["paper_id"],
         "researcher": x["researcher"],
         "types": x["types"]
    } for x in papers]
    practice_papers = [{
        "id": x["paper_id"],
         "practitioner": x["practitioner"],
         "types": x["types"]
    } for x in papers]
    research_papers = [dict(y) for y in set(tuple(x.items()) for x in research_papers)]
    practice_papers = [dict(y) for y in set(tuple(x.items()) for x in practice_papers)]

    for paper in research_papers:
        research_type = paper["researcher"] + ",," + paper["types"] + ",," + "Researcher"
        research_types[research_type] +=  1
    for paper in practice_papers:
        practice_type = paper["practitioner"] + ",," + paper["types"] + ",," + "Practitioner"
        practice_types[practice_type] +=  1

    with open("Excel_data/research_type.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Category", "Methodology", "Subclass", "size"])
        for research_type, count in research_types.items():
            writer.writerow(research_type.split(",,") +  [int(count)])
        for practice_type, count in practice_types.items():
            writer.writerow(practice_type.split(",,") +  [int(count)])
