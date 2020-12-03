#add more sentences to best.corpus

#pseudocode:
#take 3 start phrases
start = []
plus = []
size = []
toppings = []
sentences = []

start.append("I'D LIKE TO ORDER A ")
start.append("I WANNA ORDER A")
start.append("I WANT TO ORDER A ")
start.append("GIVE ME A ")

plus.append(" FOR DELIVERY ")
plus.append(" FOR PICKUP ")

#followed by size:
size.append("SMALL")
size.append("MEDIUM")
size.append("LARGE")
size.append("EXTRA LARGE")

#plus toppings: start w one, iterate through, then keep adding

toppings = ['EXTRA CHEESE', 'MUSHROOMS','MUSHROOM', 'ONIONS','ONION', 'BLACK OLIVES',
'GREEN OLIVES', 'PINEAPPLE', 'GREEN PEPPERS', 'PEPPERS','PEPPER', 'HOT PEPPERS', 'BROCCOLI', 'TOMATOES', 'TOMATO',
'SPINACH', 'ANCHOVIES', 'SAUSAGE', 'PEPPERONI', 'HAM', 'BACON']

for i in range(len(start)):
    for j in range(len(size)):
        for k in range(len(toppings)):
            sentences.append('<s> ' + start[i]+ size[j] + ' PIZZA ' + 'WITH ' + toppings[k] + ' </s>')
            sentences.append('<s> ' + start[i] + size[j] + ' PIZZA' + plus[0]  + 'WITH ' + toppings[k] + ' </s>')
            sentences.append('<s> ' + start[i] + size[j] + ' PIZZA' + plus[1]  + 'WITH ' + toppings[k] + ' </s>')


for i in range(len(start)):
    for j in range(len(size)):
        for k in range(len(toppings)-1):
            sentences.append('<s> ' + start[i]+ size[j] + ' PIZZA ' + 'WITH ' + toppings[k] + ' AND ' + toppings[k+1] + ' </s>')
            sentences.append('<s> ' + start[i] + size[j] + ' PIZZA' + plus[0] + 'WITH ' + toppings[k] + ' AND ' + toppings[k+1] + ' </s>')
            sentences.append('<s> ' + start[i] + size[j] + ' PIZZA' + plus[1] + 'WITH ' + toppings[k] + ' AND ' + toppings[k+1] + ' </s>')

#add list to corpus
outF = open("faq.corpus", "w")
for line in sentences:
  print(line, file=outF)
outF.close()
