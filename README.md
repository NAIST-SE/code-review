# ReviewMappingStudy
Mapping Study for Code Review Papers in SE

## What is contained

* Collected paper data (`data/`)
* Our analysis source code (`src/`)
* Our web page (`docs/`)

## Replication of each Research Question

### Preparing

* Methodologies.csv
* Contributions.csv
* paper_names_premium.csv
* paper_names_snowballed.csv

#### Preprocessing

* Source: src/Convert_table2paper.r
* Input: Methodologies.csv, Contributions.csv
* Output: papers.csv

### RQ1

#### step 1

* Input: papers.csv
* Source: src/RQ1/devide_paper.py
* Output: research_type.csv

#### step 2

* Source: src/RQ１/contribution_vs_methodology_bubble.r
* Input: research_type.csv
* Output: Fig4: Visual Map for RQ1, showing the contributions andmethodologies of CR research

#### step 3
* Source: src/RQ1/contribution_vs_methodology_latexTab.py
* Input: paper_names_premium.csv, papers.csv
* Output: (Old version) TABLE 6: Top 5 combination of contributions and methodologies


### RQ2

#### step 1
* Source: src/RQ2/paper2replication.py
* Input: paper_names_premium.csv
* Output: rep.csv

#### step 2
* Source: ** (Changed by wang?) src/RQ2/Replication.r **
* Input: rep.csv
* Output: Fig. 5: Visual Map for RQ2, showing replicability of thecollected papers

### RQ3

#### step 1

* Source: src/RQ3/paper2words.py
* Input: paper_names_premium.csv
* Output: word_vs_count_review.csv

#### step 2

* Source: src/RQ3/word_vs_count.r
* Input: word_vs_count_review.csv
* Output:Fig. 6: Trends of Terms used in CR researc

### RQ4

#### step 1

* Input: paper_names_premium.csv, paper_names_snowballed.csv
* Source: src/RQ4/conf_vs_year.py
* Output: year_vs_conf.csv, year_vs_conf2.csv

#### step 2

* Source: ** (Changed by wang?) src/RQ4/conf_vs_year.r **
* Input: year_vs_conf.csv, year_vs_conf2.csv
* Output: Fig. 7: Conference and journal papers on CR research