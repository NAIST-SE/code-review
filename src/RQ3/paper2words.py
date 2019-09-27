import csv
from collections import Counter

def make_word_point(word: str):
    base_keywords = ["inspection", "pull request", "patch","review"]
    for base in base_keywords:
        if base in word:
            if base == "review":
                if word == "peer code review" or word == "peer review":
                    return "peer (code) review"
                return word.strip()
            return base

    return "other"

def conv_year(year):
    if int(year) > 2008:
        return year
    else:
        return "~2008"

keywords = []

with open("Excel_data/paper_names_premium.csv", "r") as premium_file:
    premium = csv.DictReader(premium_file)
    premium_words = [{"word": make_word_point(x["word"]), "No": x["No"], "Year": x["Year"]} for x in premium]
    premium_words2 = [x["word"] for x in premium_words]
    with open("Excel_data/paper_names_snowballed.csv", "r") as snowballed_file:
        snowball = csv.DictReader(snowballed_file)
        snowball_words = [{"word": make_word_point(x["word"]), "No": x["No"], "Year": x["Year"]} for x in snowball]
        snowball_words2 = [x["word"] for x in snowball_words]
        words = snowball_words + premium_words
        words2 = snowball_words2 + premium_words2
        
        # for review
        # words = [x for x in words if "review" in x["word"]]
        # words2 = [x for x in words2 if "review" in x]

        for word in list(set(words2)) :
            print(word)
            worded_year = [conv_year(x["Year"]) for x in words if make_word_point(x["word"]) == word]
            for y in list(set(worded_year)):
                year_count = len([x for x in worded_year if x == y])
                keywords.append({"word": word, "count": year_count, "year": y})

        # for word in list(set(snowball_words2)) :
        #     print(word)
        #     worded_year = [conv_year(x["Year"]) for x in snowball_words if make_word_point(x["word"]) == word]
        #     for y in list(set(worded_year)):
        #         year_count = len([x for x in worded_year if x == y])
        #         keywords.append({"word": word, "count": year_count, "type": "snowball", "year": y})
        # for word in list(set(premium_words2)) :
        #     print(word)
        #     worded_year = [conv_year(x["Year"]) for x in premium_words if make_word_point(x["word"]) == word]
        #     for y in list(set(worded_year)):
        #         year_count = len([x for x in worded_year if x == y])
        #         keywords.append({"word": word, "count": year_count, "type": "premium", "year": y})
        print(keywords)
        with open("Excel_data/word_vs_count_review.csv", "w") as target:
            writer = csv.DictWriter(target,["word", "count", "year"])
            writer.writeheader()
            writer.writerows(keywords)

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