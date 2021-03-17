library(ggplot2)
library(plyr)
library(reshape2)

dataset <- read.csv("data/research_type.csv", header=TRUE, sep=",")


contributions <- c("Other", "Communication", "Quality assurance","Program comprehension","Automation","Potential benefits", "Socio-technical effects",   "Understanding")

g <- ggplot(dataset, aes(x=Category, y=Methodology, size=as.numeric(size), label=as.numeric(size))) + 
geom_point(shape = 21, fill = "white") +
geom_text(size=4)+
 scale_size(range = c(5, 20), guide = F) +
theme(axis.title=element_text(size=18),
axis.text=element_text(size=15),
axis.text.x=element_text(angle=30, hjust=1, vjust=1))+
facet_grid(~Subclass, scales = "free_x") +
xlab("Contribution")
plot(g)