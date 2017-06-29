library(ggplot2)
nflData=read.csv(file="c:/users/Mitch/projects/PyCharmProjects/newProj/NFL Stats.csv", header=TRUE, sep=",")
y = nflData$Score
attributes = list(nflData$First.Downs,nflData$Total.Yards,nflData$Passing.Yards,nflData$Rushing.Yards,nflData$Penalty.Count,nflData$Penalty.Yards,nflData$Turnovers,nflData$Punt.Count,nflData$Punt.Yards,nflData$Punt.Average)
fileNames = list("scoreX First Downs.png","scoreX Total Yards.png","scoreX Passing Yards.png","scoreX Rushing Yards.png","scoreX Penalty Count.png","scoreX Penalty Yards.png","scoreX Turnovers.png","scoreX Punt Count.png","scoreX Punt Yards.png","scoreX Punt Average.png")
labels = list(labs(title="Score as a Function of First Downs"),labs(title="Score as a Function of Total Yards"),labs(title="Score as a Function of Passing Yards"),labs(title="Score as a Function of Rushing Yards"),labs(title="Score as a Function of Penalty Count"),labs(title="Score as a Function of Penalty Yards"),labs(title="Score as a Function of Turnovers"),labs(title="Score as a Function of Punt Count"),labs(title="Score as a Function of Punt Yards"),labs(title="Score as a Function of Punt Average"))
for (i in 1:length(attributes)){
  x = attributes[[i]]
  df = data.frame(x,y)
  png(file = fileNames[[i]])
  label = labels[[i]]
  print(ggplot(df,aes(x=x,y=y))+geom_point(alpha = 0.3)+geom_smooth(method = "lm",colour="red") + label)
  dev.off()
}