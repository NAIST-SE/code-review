library(ggplot2)
library(plyr)
library(reshape2)

dataset <- read.csv("data/research_type.csv", header=TRUE, sep=",")

g <- ggplot(dataset, aes(x=Category, y=Methodology, size=as.numeric(size),colour=Subclass)) + 
geom_point() +
scale_size_continuous(range=c(1,20), name="Count", breaks=c(0, 10, 20, 30)) +
scale_x_discrete(limits=c("Automation","Program comprehension", "Socio-technical effects","Other", "Communication","Potential benefits","Quality assurance", "Understanding"))+
scale_colour_grey() +
theme_light() + 
theme(axis.title=element_text(size=18),
axis.text=element_text(size=15),
axis.text.x=element_text(angle=30, hjust=1, vjust=1)
)+
xlab("Contribution")
plot(g)