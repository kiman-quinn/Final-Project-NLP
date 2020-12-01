#add more sentences to best.corpus

#pseudocode:
#take 3 start phrases
start = []
plus = []
size = []
toppings = []
sentences = []

sentences.append("<s> I'D LIKE TO ORDER A SMALL PIZZA WITH PINEAPPLE AND BROCCOLI </s>")
sentences.append('<s> I WANT A MEDIUM PIZZA WITH ANCHOVIES PEPPERS AND EXTRA CHEESE </s>')
sentences.append('<s> GIVE ME A MEDIUM PIZZA WITH SPINACH SAUSAGE PEPPERONI BLACK OLIVES AND GREEN PEPPER </s>')
sentences.append('<s> I WANT TO ORDER A LARGE PIZZA WITH HAM AND BACON </s>')
sentences.append("<s> I'D LIKE A SMALL PIZZA WITH BACON AND ONION </s>")
sentences.append('<s> I WANT A LARGE PIZZA WITH HAM AND PINEAPPLE </s>')
sentences.append("<s> I'D LIKE TO ORDER A MEDIUM PIZZA WITH MUSHROOMS AND SAUSAGE </s>")
sentences.append("<s> I'D LIKE A MEDIUM PIZZA WITH PEPPERS BLACK OLIVES AND HAM </s>")
sentences.append('<s> I WANT A SMALL PIZZA WITH EXTRA ONIONS </s>')
sentences.append('<s> I WANT AN EXTRA LARGE PIZZA WITH MUSHROOMS AND TOMATOES </s>')
sentences.append('<s> GIVE ME A SMALL PIZZA WITH SPINACH AND EXTRA CHEESE </s>')
sentences.append("<s> I'D LIKE TO ORDER A MEDIUM PIZZA WITH PINEAPPLE AND BROCCOLI </s>")
sentences.append('<s> I WANNA ORDER A SMALL PIZZA FOR DELIVERY </s>')
sentences.append('<s> GIVE ME A LARGE PIZZA FOR PICKUP </s>')

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
outF = open("best.corpus", "w")
for line in sentences:
  print(line, file=outF)
outF.close()
