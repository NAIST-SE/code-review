library(ggplot2)
library(magrittr)
library(dplyr)
library(tidyr)
papers <- read.csv("Excel_data/word_vs_count_review.csv",
                   header = TRUE, sep = ",")

# papers <- read.csv("Excel_data/year_vs_conf_snowballed.csv",
#                    header = TRUE, sep = ",")
# library(gcookbook)

papers <- papers %>%
    tidyr::spread(key = word, value = count, fill = 0) %>%
    tidyr::gather(key = word, value = count, - year) %>%
    arrange(year, word)
papers$count <- ave(papers$count, papers$word, FUN=cumsum)
# papers$count <- papers

# g <- ggplot(papers[order(papers$count, decreasing=T),], aes(x=year, y=count,fill=word,group=word)) +
# geom_area()+
# theme_light()+
# theme(axis.title=element_text(size=18),
# axis.text=element_text(size=15),
# axis.text.x=element_text(angle=30, hjust=1, vjust=1)
# )

g <- ggplot(papers[order(papers$count, decreasing=T),], aes(x=year, y=count, colour=word,group=word)) +
geom_line()+
theme_light()+
theme(axis.title=element_text(size=18),
axis.text=element_text(size=15),
axis.text.x=element_text(angle=30, hjust=1, vjust=1)
)
plot(g)

# g <- ggplot(papers[order(papers$count, decreasing=T),], aes(x=year, y=word,size=count,label=count)) +
# geom_point() +
# scale_size_continuous(range=c(1,20), name="Count", breaks=c(0, 10, 20, 30)) +
# scale_y_discrete(limits=rev(c("review","pull request", "patch","inspection", "other")))+
# scale_colour_manual(values=c("blue", "red"))+
# theme(axis.title=element_text(size=18),
# # axis.text=element_text(size=15),
# axis.text=element_text(size=15,angle=30, hjust=1, vjust=1)
# )+
# geom_text(size=4, colour="white")+
# guides(size=FALSE)

# geom_bar(stat="identity", colour="black")+
# theme(axis.title=element_text(size=18),
# axis.text=element_text(size=15),
# axis.text.x=element_text(angle=30, hjust=1, vjust=1)
# )
