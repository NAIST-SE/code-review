import csv
from collections import defaultdict

type_papers = defaultdict(list)


with open("data/papers.csv", "r") as papers_file:
    # read paper
    papers = csv.DictReader(papers_file)

    research_types = defaultdict(int) 
    practice_types = defaultdict(int)
    for paper in papers:
        research_type = paper["researcher"] + " $/$ " + paper["types"]
        research_types[research_type] += 1
        type_papers[research_type].append(paper["paper_id"])

        practice_type = paper["practitioner"] + " $/$ " + paper["types"]
        practice_types[practice_type] += 1
        type_papers[practice_type].append(paper["paper_id"])

# print(type_papers)
type_papers = sorted(type_papers.items(), key=lambda x: len(x[1]), reverse=True)
# print(type_papers)

for i, type_paper in enumerate(type_papers):
    if i > 5:
        break
    papers = list(set([x for x in type_paper[1]]))
    content = ", ".join(papers)
    print(type_paper[0] + "  & " + str(len(papers)) + " & " + "\cite{" + content + "}\\\\")
