#take the input from wav file

## MAP KEYWORDS TO WEBPAGES ##
kw_map = {
    'TRANSFER': ['TRANSFER'],
    # 'BOSTON COLLEGE'
    # 'BC'
    'DINING': ['HOUSING_DINING'],
    'FOOD': ['HOUSING_DINING'],
    'ADVISING': ['ADVISING'],
    'JESUIT'
    'MAJOR': ['ADVISING', 'DEPARMENTS'],
    'DEPARTMENT': ['DEPARTMENTS'],
    'HOUSING': ['HOUSING_DINING'],
    # 'CLASS SIZE'
    'STUDY': ['DEPARTMENTS', 'OIP'],
    'ABROAD': ['OIP'],
    'CLASSES': ['ADVISING'],
    'CREDITS': ['ADVISING'],
    # 'COST':
    'DORM': ['HOUSING_DINING'],
    'CLUBS': ['OSI', 'ORGS'],
    'EXTRACURRICULARS': ['OSI', 'ORGS'],
    'SERVICE': ['OSI'],
    'SPORTS': ['OSI'],
    'ATHLETICS': ['OSI'],
}

## MAP WEBPAGES TO URLS ##
url_map = {
    'DIVERSITY': 'https://www.bc.edu/content/bc-web/campus-life/diversity.html',
    'DEPARTMENTS': 'https://www.bc.edu/bc-web/schools/mcas/department-list.html',
    'OIP': 'https://www.bc.edu/bc-web/offices/office-of-international-programs/semester-abroad/programs.html',
    'OSI': 'https://www.bc.edu/bc-web/offices/student-affairs/sites/student-involvement.html',
    'ORGS': 'https://www.bc.edu/content/bc-web/offices/student-affairs/sites/student-involvement/student-organizations.html',
    'ADVISING': 'https://www.bc.edu/bc-web/schools/mcas/undergraduate/advising.html',
    'TRANSFER': 'https://www.bc.edu/bc-web/admission/apply/transfer.html',
    'HOUSING_DINING': 'https://www.bc.edu/content/bc-web/campus-life/housing-and-dining.html',
}

# direct to an FAQ website page
def get_webpage(sentence):
    """Takes a sentence as a list of words and returns a URL to a webpage."""

    scores = {k: 0 for k in kw_map} # initialize scores for each webpage to 0

    # for each word in the sentence, add 1 to the associated webpage's score
    for word in sentence:
        if word in kw_map:
            for webpage in kw_map[word]:
                scores[webpage] += 1

    webpage = max(scores, key=scores.get)   # webpage with the highest score is returned to the user

    return url_map[webpage]
