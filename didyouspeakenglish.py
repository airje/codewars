import re
def sp_eng(sentence):
    if re.search('english', sentence, re.IGNORECASE):
        return True
    else:
        return False