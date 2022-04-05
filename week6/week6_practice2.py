#1



dic={2: 'carballo', 1: 'villareal', 3:'alvarado', 4: 'angulo', 5:'jaen' }

ordered=sorted(dic.keys())
for i in dic:
    print()
print(ordered)
   
    
print('\n')
print('*******************************')
    
  #2
  
print("max value")
dic1= {'a':450, 'b':5000, 'c': 2684 , "d":3200} 
dic_values= dic1.values()

max_value=max(dic_values)

print(max_value)
   
print("min value")    
min_value=min(dic1.values())
print(min_value)

print('\n')
print('*******************************')   

#3 remove duplicates 
dict2 = {'A': 50, 'B': 30, 'C': 50, 'D': 10, 'E': 20}
temp = []
res = dict()
for key, val in dict2.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)

print('\n')
print('*******************************') 

#4 all unique values only, remove repeat 
Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
dic_values= set(val for dic in Sample_Data for val in dic.values())
print("unique values", dic_values)