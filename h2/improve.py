#add more sentences to best.corpus

#pseudocode:
#take 3 start phrases
start = []
plus = []
size = []
keyword = []
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

keyword = ['ADMISSION','APPLY','APPLICATION','FINANCIAL','AID','SCHOLARSHIP','SCHOLARSHIPS','COST','PRICE','AFFORD','AFFORDABLE',
'AFFORDABILITY',
'TUITION',
'EXPENSIVE',
'TRANSFER',
'TRANSFERS',
'DINING',
'EAT',
'FOOD',
'MEAL',
'RESTAURANT',
'HALL',
'HALLS',
'MAJOR',
'MINOR',
'DOUBLE',
'ADVISING',
'ADVISOR',
'ADVISING',
'CLASSES',
'CLASS',
'REGISTER',
'REGISTRATION',
'CREDITS',
'SCHOOL',
'SCHOOLS',
'AP',
'CREDIT',
'DEPARTMENT',
'DEPARTMENTS',
'HOUSING',
'DORMS',
'DORM',
'CAMPUS',
'LIVE',
'ROOMMATE',
'ROOMMATES',
'RESIDENCE',
'APARTMENT',
'APAREMENTS',
'NEWTON',
'STUDY',
'RESEARCH',
'ABROAD',
'COUNTRY',
'INTERNATIONAL',
'DORM',
'CLUBS',
'CLUB',
'EXTRACURRICULARS',
'ORGANIZATIONS',
'SERVICE',
'SPORTS',
'SPORT',
'TEAM',
'INTRAMURAL',
'INTRAMURALS',
'RECREATION',
'FITNESS',
'GYM',
'GYMS',
'ATHLETICS',
'ART',
'ARTS','BAND','BANDS',
'COVID','CORONAVIUS','NINETEEN','REOPEN','REOPENING','TEST','TESTING','RESTRICTIONS','DIVERSITY','DIVERSE','AHANA','RACIAL','GENDER']

for i in range(len(start)):
    for j in range(len(size)):
        for k in range(len(toppings)):
            sentences.append('<s> ' + start[i]+ size[j] + ' PIZZA ' + 'WITH ' + keyword[k] + ' </s>')
            sentences.append('<s> ' + start[i] + size[j] + ' PIZZA' + plus[0]  + 'WITH ' + keyword[k] + ' </s>')
            sentences.append('<s> ' + start[i] + size[j] + ' PIZZA' + plus[1]  + 'WITH ' + keyword[k] + ' </s>')


#add list to corpus
outF = open("faq.corpus", "w")
for line in sentences:
  print(line, file=outF)
outF.close()
