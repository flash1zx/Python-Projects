def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
    
    
    
  #end  
  
  #create new file and copy paste this from line 12
  
from utils import find_max

numbers = [10, 2, 4, 6]
max = find_max(numbers)
print(max)
    
    
