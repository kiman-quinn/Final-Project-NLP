#add more sentences to faq.corpus

#take 3 start phrases
start = []
plus = []
size = []
keyword = []
sentences = []

start.append("WHY DID YOU ")
start.append("WHAT IS ")
start.append("HOW IS ")
start.append("WHAT DOES ")
start.append("WHAT ARE ")
start.append("IS IT ")
start.append("HOW DOES ")
start.append("HOW MANY ")
start.append("WHAT HAS ")
start.append("WHO ARE ")
start.append("ARE THERE ")
start.append("HOW DO ")

#plus toppings: start w one, iterate through, then keep adding

keyword = ['ADMISSION','APPLY','APPLICATION','FINANCIAL','AID','SCHOLARSHIP','SCHOLARSHIPS','COST','PRICE','AFFORD','AFFORDABLE',
'AFFORDABILITY','TUITION','EXPENSIVE','TRANSFER','TRANSFERS','DINING','EAT','FOOD','MEAL','RESTAURANT','HALL','HALLS','MAJOR',
'MINOR','DOUBLE','ADVISING','ADVISOR','ADVISING','CLASSES','CLASS','REGISTER','REGISTRATION','CREDITS','SCHOOL','SCHOOLS','AP',
'CREDIT','DEPARTMENT','DEPARTMENTS','HOUSING','DORMS','DORM','CAMPUS','LIVE','ROOMMATE','ROOMMATES','RESIDENCE','APARTMENT',
'APARTMENTS','NEWTON','STUDY','RESEARCH','ABROAD','COUNTRY','INTERNATIONAL','DORM','CLUBS','CLUB','EXTRACURRICULARS','ORGANIZATIONS','SERVICE',
'SPORTS','SPORT','TEAM','INTRAMURAL','INTRAMURALS','RECREATION','FITNESS','GYM','GYMS','ATHLETICS','ART','ARTS','BAND','BANDS',
'COVID','CORONAVIUS','NINETEEN','REOPEN','REOPENING','TEST','TESTING','RESTRICTIONS','DIVERSITY','DIVERSE','AHANA','RACIAL','GENDER']

for i in range(len(start)):
    for j in range(len(keyword)):
            sentences.append('<s> ' + start[i]+ keyword[j] + ' </s>')
            sentences.append('<s> ' + start[i]+ keyword[j] + ' </s>')
            sentences.append('<s> ' + start[i]+ keyword[j] + ' </s>')


#add list to corpus
outF = open("faq.corpus", "w")
for line in sentences:
  print(line, file=outF)
outF.close()
