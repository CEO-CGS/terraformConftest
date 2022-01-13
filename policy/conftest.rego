package main

deny[msg]{
  x:=0
  not x == 0
  msg:="This works!"
}


deny[msg]{
  x:= 3
  not x == 2
  msg:="This works!"
}
