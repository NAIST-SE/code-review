library(ggplot2)
library(reshape2)

papers <- read.csv("Excel_data/year_vs_conf.csv",
                   header = TRUE, sep = ",")

# papers <- read.csv("Excel_data/year_vs_conf_snowballed.csv",
#                    header = TRUE, sep = ",")


# g <- ggplot(papers, aes(x=Year, y=Count,fill=Publication)) +
# scale_fill_grey() +
# theme_light() + 
# geom_bar(stat="identity", colour="black")

papers <- read.csv("Excel_data/year_vs_conf2.csv",
                   header = TRUE, sep = ",")
g <- ggplot(papers, aes(x=Year, y=Publication,size=as.numeric(Count),colour=Type,label=Count)) +
scale_y_discrete(limits=rev(c("TSE", "EMSE", "ASEJ", "TOSEM", "IST", "ICSE", "FSE", "ASE", "ICSME", "MSR", "Other")))+
geom_point() +
scale_colour_grey() +
theme_light() +
geom_text(size=4, color="white") +
guides(size=FALSE) +
scale_size_area(max_size=13)
plot(g)