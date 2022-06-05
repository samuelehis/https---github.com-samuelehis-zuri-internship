# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

str1 = "hello"
str2 = "check"


def find_anagram(word, anagram):
    # [assignment] Add your
   if(len(str1) == len(str2)):

      anagram_str1 = sorted(str1)
      anagram_str2 = sorted(str2)

      if (anagram_str1 == anagram_str2):
          return True

      else:
          return False
    
   else:
       return False

print(find_anagram(str1,str2))