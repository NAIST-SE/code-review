"""
require: pip3 install pyyaml
"""
import csv
from yaml import dump

with open("data/Metric_Listing.csv", "r") as csvdata:
    reader = csv.DictReader(csvdata)


    with open("data/Data_Cat.csv", "r") as csvdata:
        papers = list(csv.DictReader(csvdata))

        for data in reader:
            id = data["PaperId"]
            titles = [x for x in papers if x['No'] == data['PaperId']]

            output_format = {
                "title": "" if len(titles) == 0 else titles[0]['Title'],
                "id": id,
                "metric": data["Metric"] if "Metric" in data else "---",
                "metric_set": data["MetricSet"] if "MetricSet" in data and data["MetricSet"] != ""  else "---",
                "target": data["Target"] if "Target" in data and data["Target"] != "" else "---",
                "topic": data["Topic"] if "Topic" in data and data["Topic"] != "" else "---",
            }
            with open(f"docs/_metricses/{id}.md", "w") as yamldata:
                yamldata.write("---\n" + dump(output_format) + "---\n")