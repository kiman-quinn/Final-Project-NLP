#take the input from wav file

## MAP KEYWORDS TO WEBPAGES ##
kw_map = {
    'ADMISSION': ['ADMISSION'],
    'APPLY': ['ADMISSION'],
    'APPLICATION': ['ADMISSION'],
    'FINANCIAL': ['ADMISSION'],
    'AID': ['ADMISSION'],
    'SCHOLARSHIP': ['ADMISSION'],
    'SCHOLARSHIPS': ['ADMISSION'],
    'COST': ['ADMISSION'],
    'PRICE': ['ADMISSION'],
    'AFFORD': ['ADMISSION'],
    'ADDORDABLE': ['ADMISSION'],
    'AFFORDABILITY': ['ADMISSION'],
    'TUITION': ['ADMISSION'],
    'EXPENSIVE': ['ADMISSION'],
    'TRANSFER': ['TRANSFER'],
    'TRANSFERS': ['TRANSFER'],
    'DINING': ['HOUSING_DINING'],
    'EAT': ['HOUSING_DINING'],
    'FOOD': ['HOUSING_DINING'],
    'MEAL': ['HOUSING_DINING'],
    'RESTAURANT': ['HOUSING_DINING'],
    'HALL': ['HOUSING_DINING'],
    'HALLS': ['HOUSING_DINING'],
    'MAJOR': ['ADVISING', 'DEPARMENTS'],
    'MINOR': ['ADVISING', 'DEPARTMENTS'],
    'DOUBLE': ['ADVISING'],
    'ADVISING': ['ADVISING'],
    'ADVISOR': ['ADVISING'],
    'ADVISING': ['ADVISING'],
    'CLASSES': ['ADVISING'],
    'CLASS': ['ADVISING'],
    'REGISTER': ['ADVISING'],
    'REGISTRATION': ['ADVISING'],
    'CREDITS': ['ADVISING'],
    'SCHOOL': ['ADVISING'],
    'SCHOOLS': ['ADVISING'],
    'AP': ['ADVISING'],
    'CREDIT': ['ADVISING', 'TRANSFER'],
    'DEPARTMENT': ['DEPARTMENTS'],
    'DEPARTMENTS': ['DEPARTMENTS'],
    'HOUSING': ['HOUSING_DINING'],
    'DORMS': ['HOUSING_DINING'],
    'DORM': ['HOUSING_DINING'],
    'CAMPUS': ['HOUSING_DINING'],
    'LIVE': ['HOUSING_DINING'],
    'ROOMMATE': ['HOUSING_DINING'],
    'ROOMMATES': ['HOUSING_DINING'],
    'RESIDENCE': ['HOUSING_DINING'],
    'APARTMENT': ['HOUSING_DINING'],
    'APAREMENTS': ['HOUSING_DINING'],
    'NEWTON': ['HOUSING_DINING'],
    'STUDY': ['DEPARTMENTS', 'OIP'],
    'RESEARCH': ['DEPARTMENTS'],
    'ABROAD': ['OIP'],
    'COUNTRY': ['OIP'],
    'INTERNATIONAL': ['OIP'],
    'DORM': ['HOUSING_DINING'],
    'CLUBS': ['ORGS'],
    'CLUB': ['ORGS'],
    'EXTRACURRICULARS': ['ORGS'],
    'ORGANIZATIONS': ['ORGS'],
    'SERVICE': ['ORGS'],
    'SPORTS': ['REC'],
    'SPORT': ['REC'],
    'TEAM': ['REC'],
    'INTRAMURAL': ['REC'],
    'INTRAMURALS': ['REC'],
    'RECREATION': ['REC'],
    'FITNESS': ['REC'],
    'GYM': ['REC'],
    'GYMS': ['REC'],
    'ATHLETICS': ['REC'],
    'ART': ['ORGS'],
    'ARTS': ['ORGS'],
    'BAND': ['ORGS'],
    'BANDS': ['ORGS'],
    'COVID': ['COVID'],
    'CORONAVIUS': ['COVID'],
    'NINETEEN': ['COVID'],
    'REOPEN': ['COVID'],
    'REOPENING': ['COVID'],
    'TEST': ['COVID'],
    'TESTING': ['COVID'],
    'RESTRICTIONS': ['COVID'],
    'DIVERSITY': ['DIVERSITY'],
    'DIVERSE': ['DIVERSITY'],
    'AHANA': ['DIVERSITY'],
    'RACIAL': ['DIVERSITY'],
    'GENDER': ['DIVERSITY'],
}

## MAP WEBPAGES TO URLS ##
url_map = {
    'ADMISSION': 'https://www.bc.edu/content/bc-web/admission.html',
    'DIVERSITY': 'https://www.bc.edu/content/bc-web/campus-life/diversity.html',
    'DEPARTMENTS': 'https://www.bc.edu/bc-web/schools/mcas/department-list.html',
    'OIP': 'https://www.bc.edu/bc-web/offices/office-of-international-programs/semester-abroad/programs.html',
    'REC': 'https://www.bc.edu/content/bc-web/campus-life/sports-and-recreation.html',
    'ORGS': 'https://www.bc.edu/content/bc-web/offices/student-affairs/sites/student-involvement/student-organizations.html',
    'ADVISING': 'https://www.bc.edu/bc-web/schools/mcas/undergraduate/advising.html',
    'TRANSFER': 'https://www.bc.edu/bc-web/admission/apply/transfer.html',
    'HOUSING_DINING': 'https://www.bc.edu/content/bc-web/campus-life/housing-and-dining.html',
    'COVID': 'https://www.bc.edu/bc-web/sites/reopening-boston-college.html'
}

# direct to an FAQ website page
def get_webpage(sentence_string):
    """Takes a sentence as a string and returns a URL to a webpage."""
    sentence = sentence_string.split(' ')   # tokenize sentence
    scores = {k: 0 for k in kw_map} # initialize scores for each webpage to 0

    # for each word in the sentence, add 1 to the associated webpage's score
    for word in sentence:
        if word in kw_map:
            for webpage in kw_map[word]:
                scores[webpage] += 1

    webpage = max(scores, key=scores.get)   # webpage with the highest score is returned to the user

    return webpage, url_map[webpage]

def parse_sentences():
    """Matches all question transcriptions to URLs and writes them to webpages.txt"""
    with open('questions.hyp', 'r') as rf, open('webpages.txt', 'w') as wf: # open input and output files
        for line in rf: # iterate over lines in input file (questions.hyp has the language model transcriptions)
            # get the relevant info from the line
            ls = line.split('(')
            question = ls[0][:-1]
            wavfile = ls[1].split(' ')[0]
            webpage, url = get_webpage(question)    # get webpage and url
            wf.write(f'{wavfile}\t{webpage}\t{url}\n')  # print to file

if __name__ == "__main__":
    parse_sentences()
