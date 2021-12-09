# Parameters:
#  str1: str
#  str2: str
# return type: int

def substrIndex(str1, str2):
  # your code here
  length2 = len(str2)
  diffLen = len(str1) - len(str2)
  for i in range(diffLen +1) :
      found = compareJing( str1[i:i+length2], str2[0:])
      print("result", found)
      if found:
          return i
  
  return -1
      
def compareJing(str1, str2):
    print(str1, str2)
    for i in range(len(str2)) :
        if(str1[i] != str2[i]):
            return False
    
    return True
      

print(substrIndex("a","a"))