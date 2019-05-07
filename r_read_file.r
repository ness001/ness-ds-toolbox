tute1 <- read.csv("tute1.csv", header=TRUE)
View(tute1)
mytimeseries <- ts(tute1[,-1], start=1981, frequency=4)#-1代表把第一行丢弃了
autoplot(mytimeseries, facets=TRUE)#代表分别做子图，不共享坐标轴

retaildata <- readxl::read_excel("retail.xlsx", skip=1)
myts <- ts(retaildata[,"A3349873A"],
  frequency=12, start=c(1982,4))