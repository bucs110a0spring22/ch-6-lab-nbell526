import turtle 

def seq3np1(n):
  count=0
  while(n!=1):
      if(n % 2) == 0:        
        n = n // 2
      else:                
        n = n * 3 + 1
      count+=1
  return count
  
def iterationgraph(upper_limit): 
  turtle_write=turtle.Turtle()
  turtle_graph=turtle.Turtle()
  window=turtle.Screen()
  window.setworldcoordinates(0,0,10,10)
  max_so_far= 0
  turtle_graph.goto(0,10)
  turtle_graph.pd()
  
  for x in range(1,upper_limit+1): 
    result= seq3np1(x)
    if result>max_so_far: 
      max_so_far=result
    turtle_graph.goto(0,max_so_far)
    str="max so far:",x,result 
    turtle_graph.clear()
    turtle_graph.write(str)
    window.setworldcoordinates(0,0,x+10,max_so_far+10)
    turtle_write.goto(x, result)
  window.exitonclick()    
  
def main():
  upper_limit=int(input("upper limit:"))
  if 0>upper_limit:
    return
  for start in range(1,upper_limit+1):
    seq3np1(upper_limit)
    print("Current loop value:",start,"Iterations:", seq3np1(start))
  iterationgraph(upper_limit)
  seq3np1(3)
main()