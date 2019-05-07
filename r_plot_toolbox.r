#2.1
y <- ts(c(123,39,78,59,110),start=2012)
y <- ts(z,start=2003,frequency=12)# z is a numerical vector
frequency(gold)


#seasonal plots
ggseasonplot(a10, year.labels=TRUE, year.labels.left=TRUE) +
  ylab("$ million") +
  ggtitle("Seasonal plot: antidiabetic drug sales")

ggseasonplot(a10, polar=TRUE) +
  ylab("$ million") +
  ggtitle("Polar seasonal plot: antidiabetic drug sales")

  #seasonal subseries plots 见2.5的图 瘦瘦的 带mean
ggsubseriesplot(a10) +
  ylab("$ million") +
  ggtitle("Seasonal subseries plot: antidiabetic drug sales")


#auto plot
autoplot(melsyd[,"Economy.Class"]) + #'col_name'
  ggtitle("Economy class passengers: Melbourne-Sydney") +
  xlab("Year") +
  ylab("Thousands")

#facets选项是做子图
autoplot(elecdemand[,c("Demand","Temperature")], facets=TRUE) +#concat cols
  xlab("Year: 2014") + ylab("") +
  ggtitle("Half-hourly electricity demand: Victoria, Australia") 

#scatter plot- relationship between varrables
qplot(Temperature, Demand, data=as.data.frame(elecdemand)) +
  ylab("Demand (GW)") + xlab("Temperature (Celsius)")

#2.6 chapter. correlation ---- the strength of the LINEAR Relationship
*只对于线性关系有用，非线性相关系数没有意义，所以一定要看一下散点图

#pair plots! 相关矩矩阵图，既有散点图又有相关系数
GGally::ggpairs(as.data.frame(visnights[,1:5])) #注意，只处理df格式的数据而不是ts格式的数据

#lag plots#也能看出frequency的大小，即有没有seasonality
beer2 <- window(ausbeer, start=1992) #slice 数据
gglagplot(beer2)

#acf图
ggACF（beer2）

aelec <- window(elec, start=1980)
autoplot(aelec) + xlab("Year") + ylab("GWh")
ggAcf(aelec, lag=48)

