"""
require: pip3 install pyyaml
"""
import csv
from typing import Set
from yaml import dump

output = {}

with open("data/Metric_Listing.csv", "r") as csvdata:
    reader = csv.DictReader(csvdata)


    with open("data/Data_Cat.csv", "r") as csvdata:
        papers = list(csv.DictReader(csvdata))

        for data in reader:
            id = data["PaperId"]
            if id in output:
                output[id]['Metric'] += ',' + data['Metric']
                output[id]['MetricSet'] += ',' + data['MetricSet']
            else:
                titles = [x for x in papers if x['No'] == data['PaperId']]
                output[id] = data
                output[id]['title'] = "" if len(titles) == 0 else titles[0]['Title']

for id, data in output.items():
    metric = ','.join(sorted(list(set(data['Metric'].split(',')))))
    metric_set = ','.join(sorted(list(set(data['MetricSet'].split(',')))))

    output_format = {
        "title": data['title'],
        "id": id,
        "metric": metric,
        "metric_set": metric_set,
        "topic": data["Topic"] if "Topic" in data and data["Topic"] != "" else "---",
    }
    with open(f"docs/_metricses/{id}.md", "w") as yamldata:
        yamldata.write("---\n" + dump(output_format) + "---\n")