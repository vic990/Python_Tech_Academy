def rango(start1, end, step=1):
    
    while start1 <= end:               
        yield start1
        start1+=step
        
        
      
for i in rango(1,100):
    print(i)