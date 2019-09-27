library(ggplot2)

dataset <- read.csv("data/rep.csv")
dataset$Percentage <- paste(dataset$Count / 50 * 100, "%")
g <- ggplot(dataset, aes(x=reorder(Data, Count), y=Count,fill=Replicatable)) +
geom_bar(stat="identity", colour="black") +
scale_fill_grey(start = 0.9, end = 0.4) +
theme_light() +
geom_text(aes(label=Percentage),hjust=1.0,size=5, color="black") +
guides(fill=guide_legend(reverse=TRUE)) +
xlab("Data Replication") +
theme(axis.title=element_text(size=18),
axis.text=element_text(size=15))+
coord_flip()
# scale_fill_brewer(pallette="Pastel1")
# jpeg("Visualize_Code/RQ3/result/data_approach.jpg")

plot(g)