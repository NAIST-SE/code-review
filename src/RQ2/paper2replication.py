import csv
from collections import Counter
from operator import itemgetter
category = []
category_result = []
Replicatables = ["Open data available via link", "Reference to dataset"]

with open("Excel_data/Data_Cat.csv", "r") as premium_file:
    category = list(csv.DictReader(premium_file))
    for paper in category:
        category_result.append(paper["Cat."])
    counted = Counter([x for x in category_result if x != ""])
    print(counted)
with open("Excel_data/rep.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow(["Data","Count", "Replicatable"])
    for value, count in counted.items():
        replicatable = True if value in Replicatables else False
        writer.writerow([value, count, replicatable])

# with open("Excel_data/papers.csv", "r") as papers_file:
#     papers = csv.DictReader(papers_file)
#     type_count = {}
#     for paper in papers:
#         category_result.extend([paper["paper_id"] + "," 
#         + paper["types"] + "," 
#         + x["Cat."]
#         for x in category if x["No"] == paper["paper_id"]])
# # print(category_result)
# category_result = [x.split(",") for x in list(set(category_result)) if not x.endswith(",")]
# category_count = Counter([x[1] + "," + x[2] for x in category_result])
# print(category_count)
# category_result = sorted(category_result, key=lambda k: k[0]) 
# with open("Excel_data/rep_vs_method.csv", "w") as output:
#     writer = csv.writer(output)
#     writer.writerow(["Method","Replication","Count"])
#     for value, count in category_count.items():
#         writer.writerow(value.split(",") + [count])


# with open("Excel_data/paper_names_snowballed.csv", "r") as snowballed_file:
#     premium = csv.DictReader(snowballed_file)
#     premium_words = [{"word": make_word_point(x["word"]), "No": x["No"]} for x in premium]
#     premium_words2 = [x["word"] for x in premium_words]
#     for word in list(set(premium_words2)) :
#         print(word)
#         worded_title = [x["No"] for x in premium_words if make_word_point(x["word"]) == word]
#         print(len(worded_title))
#         print(worded_title)
#         print()