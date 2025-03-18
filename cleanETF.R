setwd('C:/Users/z30060762/Desktop/Rtest/THS')

library(tidyverse)
library(openxlsx) 
library(stringr)
list_name = dir("./",pattern = "-2ETF.xlsx$") 

len=length(list_name)
for (i in 1:len) {
  data=read.xlsx(list_name[i], startRow = 1, sheet=1)
  #clean
  data[,"现手"]=as.numeric(str_replace_all(data[,"现手"], "[↑↓-]", ""))
  data[,"涨幅"]=as.numeric(str_replace_all(data[,"涨幅"], "--", "0"))
  data[,"涨跌"]=as.numeric(str_replace_all(data[,"涨跌"], "--", "0"))  
  data[,"总手"]=as.numeric(str_replace_all(data[,"总手"], "--", "0"))  
  data[,"卖价"]=as.numeric(str_replace_all(data[,"卖价"], "--", "0"))  
  data=data[,-c(13:18,30)]
  data <- data[order(data$代码), ]
  #output
  write_xlsx(data, path=str_c("./ETF/2025/", list_name[i]))
}


