# ReviewMappingStudy
Mapping Study for Code Review Papers in SE

Top 10 journal and conference:
1. TSE
2. TOSEM
3. IST
4. EMSE
5. ASEJ
6. FSE/ESEC
7. ICSE
8. ICSME
9. MSR

In this paper, we would like to analyze the trend in code review topic and form a guide book for reviewers in the CR field 



* Most updated
    * Methodologies.csv
    * Contributions.csv
    * Excel_data/paper_names_premium.csv
    * Excel_data/paper_names_snowballed.csv

## Preparing
* Source: src/Convert_table2paper.r
* Input: Methodologies.csv, Contributions.csv
* Output: papers.csv

## RQ1

### step 1

* Input: Excel_data/papers.csv
* Source: src/RQ1/devide_paper.py
* Output: Excel_data/research_type.csv

### step 2

* Source: src/RQ１/contribution_vs_methodology_bubble.r
* Input: Excel_data/research_type.csv
* Output: Fig4: Visual Map for RQ1, showing the contributions andmethodologies of CR research


* Source: src/RQ1/contribution_vs_methodology_latexTab.py
* Input: Excel_data/paper_names_premium.csv, Excel_data/papers.csv
* Output: (Old version) TABLE 6: Top 5 combination of contributions and methodologies


## RQ2

### step 1
* Source: src/RQ2/paper2replication.py
* Input: Excel_data/paper_names_premium.csv
* Output: Excel_data/rep.csv

### step 2
* Source: ** (Changed by wang?) src/RQ2/Replication.r **
* Input: Excel_data/rep.csv
* Output: Fig. 5: Visual Map for RQ2, showing replicability of thecollected papers

## RQ3

### step 1

* Source: src/RQ3/paper2words.py
* Input: Excel_data/paper_names_premium.csv
* Output: Excel_data/word_vs_count_review.csv

### step 1

* Source: src/RQ3/word_vs_count.r
* Input: Excel_data/word_vs_count_review.csv
* Output:Fig. 6: Trends of Terms used in CR researc

## RQ4

### step 1

* Input: Excel_data/paper_names_premium.csv, Excel_data/paper_names_snowballed.csv
* Source: src/RQ4/conf_vs_year.py
* Output: year_vs_conf.csv, year_vs_conf2.csv

### step 1

* Source: ** (Changed by wang?) src/RQ4/conf_vs_year.r **
* Input: year_vs_conf.csv, year_vs_conf2.csv
* Output: Fig. 7: Conference and journal papers on CR research