library(ggplot2)
library(plyr)
library(reshape2)

researchtype <- read.csv("Excel_data/Methodologies.csv", header=FALSE, sep=",")
classification <- read.csv("Excel_data/Contributions.csv", header=TRUE, sep=",")


paper_id <- c()
researchers <- c()
practitioners <- c()

for (i in 3:7) {
    practitioner <- classification[[i]][1]
    for (j in 2:5) {
        researcher <- classification[[2]][j]
        elements <- strsplit(as.character(classification[[i]][j]), ",")[[1]]
        researchers <- append(researchers, rep(as.character(researcher), length(elements)))
        practitioners <- append(practitioners, rep(as.character(practitioner), length(elements)))
        new_elements <- c()
        for (element in elements) {
            element <- gsub("^[ ]+|[ ]+$", "", element)
            new_elements <- append(new_elements, as.character(element))
        }
        paper_id <- append(paper_id, new_elements)

   }
}
new_classification <- data.frame(paper_id=paper_id, researcher = researchers, practitioner = practitioners)

paper_id <- c()
types <- c()

for (i in 1:5) {
    type <- researchtype[[i]][1]
    elements <- strsplit(as.character(researchtype[[i]][2]), ",")[[1]]
    new_elements <- c()

    for (element in elements) {
        element <- gsub("^[ ]+|[ ]+$", "", element)
        new_elements <- append(new_elements, as.character(element))
    }
    paper_id <- append(paper_id, new_elements)
    types <- append(types, rep(as.character(type), length(elements)))
}

new_types <- data.frame(paper_id=paper_id, types = types)

projects <- merge(new_classification, new_types,
by = "paper_id", all=T)
write.csv(projects, file = "Excel_data/papers.csv", row.names=FALSE)