from difflib import SequenceMatcher
 

def similar(str1, str2):
    return SequenceMatcher(None, str1, str2).ratio()
 

test_string1 = 'durga'
test_string2 = 'devi'
 

res = similar(test_string1, test_string2)
 

print ("The similarity between 2 strings is : " + str(res))
