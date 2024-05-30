result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == 'heads':
        count += 1
print('Heads count:' ,count)

for i in range(1,11):
    if i%2 == 0:
        continue
    print(i*i)
    
    


