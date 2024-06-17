def are_anagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    
    return sorted_string1 == sorted_string2

string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print("Listen and Silent are anagrams.")
else:
    print("Listen and Silent are not anagrams.")