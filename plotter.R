n<- function(){
  readline(prompt="enter x value to plot: ")
}
m<- function(){
  readline(prompt="enter y value to plot: ")
}

plotfun <- function(dat) {
  colx <- n()
  coly <- m()
  plot(dat[,colx], dat[,coly], main="Scatterplot Example", pch=20)      
}

if(interactive()) plotfun(dat=iris)
