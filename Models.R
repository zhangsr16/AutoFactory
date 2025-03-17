calculate_metrics <- function(model_name, predictions, train_y, Recall, Precis, i) {
  table_result <- table(train_y, predictions, dnn = c("真实值", "预测值"))
  if (table_result[2, 1] != 0) {
    Recall[i, model_name] <- table_result[2, 2] / table_result[2, 1]
  }
  if (table_result[1, 2] != 0) {
    Precis[i, model_name] <- table_result[2, 2] / table_result[1, 2]
  }
}

Methods = c('dire', 'buy', 'max', 'min')

for (i in 1:4) {
  method = Methods[i]
  
  if (method=='buy') {
    bef=a0[(2*alth+1):(6*alth),-c(1:4)]
    tim=TIME[(2*alth+1):(6*alth)]
  }else{
    bef=a0[(2*alth+1):(5*alth),-c(1:4)]
    tim=TIME[(2*alth+1):(5*alth)]
  }
  names(bef)=c("涨幅o", "现价o", "涨跌o", "涨速.o","DDE净量o","总手o", "换手.o","量比o","现手o", "开盘o", "昨收o", "最高o", "最低o", "买价o", "卖价o", "市盈.动o","市净率o" ,"买量o", "卖量o", "委比.o","振幅.o","金额o", "均笔额o","笔数o","手.笔o","外盘o", "内盘o", "总市值o","流通市值o")
  
  #Input
  x.temp <- switch(method,
                   "dire" = as.numeric(xn$现价 > 0.01 * tm),
                   "buy" = as.numeric(xn$最低 < (-0.01 * tm)),
                   "max" = as.numeric(xn$最高 > 0.02 * tm),
                   "min" = as.numeric(xn$最低 > 0.02 * tm)
  )
  if (method=='buy') {
    pre<-x.temp[(2*alth+1):(6*alth)]
    temp=cbind(xn[1:(4*alth),],xn1[1:(4*alth),],pre,bef,tim)
  }else{
    pre<-x.temp[(3*alth+1):(6*alth)]
    temp=cbind(xn[1:(3*alth),],xn1[1:(3*alth),],pre,bef,tim)
  }
  
  test=temp
  source("F:/Desktop/THS/Code/20240717/GetModel.R")
  
  #TEST_cm
  if (method=='buy') {
    bef=a0[(6*alth+1):(7*alth),-c(1:4)]
    tim=TIME[(6*alth+1):(7*alth)]
    pre<-x.temp[(6*alth+1):(7*alth)]
    temp=cbind(xn[(4*alth+1):(5*alth),],xn1[(4*alth+1):(5*alth),],pre,bef,tim)
  }else{
    bef=a0[(5*alth+1):(6*alth),-c(1:4)]
    tim=TIME[(5*alth+1):(6*alth)]
    pre<-x.temp[(6*alth+1):(7*alth)]
    temp=cbind(xn[(3*alth+1):(4*alth),],xn1[(3*alth+1):(4*alth),],pre,bef,tim)
  }
  names(bef)=c("涨幅o", "现价o", "涨跌o", "涨速.o","DDE净量o","总手o", "换手.o","量比o","现手o", "开盘o", "昨收o", "最高o", "最低o", "买价o", "卖价o", "市盈.动o","市净率o" ,"买量o", "卖量o", "委比.o","振幅.o","金额o", "均笔额o","笔数o","手.笔o","外盘o", "内盘o", "总市值o","流通市值o")
  
  
  test=temp
  source("F:/Desktop/THS/Code/20240717/TestModel.R")
  
  # 调用函数计算各模型的指标
  calculate_metrics("GLM", GLMpre, train_y, Recall, Precis, i)
  calculate_metrics("LM", LMpre, train_y, Recall, Precis, i)
  calculate_metrics("NB", NBpre, train_y, Recall, Precis, i)
  calculate_metrics("XG", XGpre, train_y, Recall, Precis, i)
  calculate_metrics("RF", RFpre, train_y, Recall, Precis, i)
  
  #Predict
  bef=a0[(7*alth+1):(8*alth),-c(1:4)]
  names(bef)=c("涨幅o", "现价o", "涨跌o", "涨速.o","DDE净量o","总手o", "换手.o","量比o","现手o", "开盘o", "昨收o", "最高o", "最低o", "买价o", "卖价o", "市盈.动o","市净率o" ,"买量o", "卖量o", "委比.o","振幅.o","金额o", "均笔额o","笔数o","手.笔o","外盘o", "内盘o", "总市值o","流通市值o")
  tim=TIME[(7*alth+1):(8*alth)]
  temp=cbind(xn[(5*alth+1):(6*alth),],xn1[(5*alth+1):(6*alth),],rep(1,1*alth),bef,tim)
  
  test=temp
  source("F:/Desktop/THS/Code/20240717/UseModel.R")
  dire=data.frame(ID=a0[1:alth,c(1:4)],LM=lmpre,GLM=glmpre,NB=NBpre,XG=XGpre,RF=RFpre)
  
  switch(method,
         "dire" = {
           dire=data.frame(ID=a0[1:alth,c(1:4)],LM=lmpre,GLM=glmpre,NB=NBpre,XG=XGpre,RF=RFpre)
           pdata=data.frame(ID=a0[(lth-alth+1):lth,c(1:4,17)],IP=ipan,OP=opan,uIP=l.ipan,uOP=l.opan,Stavg=stavg,Safety=rate,LM=lmpre,GLM=glmpre,NB=NBpre,XG=XGpre,RF=RFpre)
         },
         "buy" = {
           buy=data.frame(ID=a0[1:alth,c(1:4)],LM=lmpre,GLM=glmpre,NB=NBpre,XG=XGpre,RF=RFpre)
         },
         "max" = {
           max=data.frame(ID=a0[1:alth,c(1:4)],LM=lmpre,GLM=glmpre,NB=NBpre,XG=XGpre,RF=RFpre)
         },
         "min" = {
           min=data.frame(ID=a0[1:alth,c(1:4)],LM=lmpre,GLM=glmpre,NB=NBpre,XG=XGpre,RF=RFpre)
         }
  )
}

#Report
Precis[Precis<0.2/tm]=0
Precis[,-1]=round(Precis[,-1],1)
Recall[Recall<2]=0
Recall[,-1]=round(Recall[,-1],0)
st=c(sum(is.na(Precis[,1:4])+is.na(Recall[,1:4]))+length(which(Precis==Inf))+length(which(Recall==Inf)),length(grep("ST", Hot)))
Precis;Recall;st

if (tm==2) {
  statis=read.table("AIHOT.txt", header = T);
  statis=rbind(statis,st)
  write.table(statis, "AIHOT.txt", quote = F, sep = "\t", row.names = F)
  par(mfrow=c(3,1))
  hist(stavg);plot(statis$AI);plot(statis$HOT)
}
