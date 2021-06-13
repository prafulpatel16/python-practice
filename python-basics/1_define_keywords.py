# importing "keyword" for keyword operations
#Python code to demonstrate working of iskeyword()
# importing "keyword" for keyword operations

import keyword
import keyword

keys = ["for", "while", "tanisha", "break", "sky",
"elif", "assert", "pulkit", "lambda", "else", "sakshar"] 

for i in range(len(keys)):
    #checking which are keywords
    if keyword.iskeyword(keys[i]):
        print(keys[i] + "is python keyword")
    else:
        print(keys[i] + "is not a keyword")

#Python code to demonstrate working of iskeyword()
  
# importing "keyword" for keyword operations

import keyword

print ("The list of keywords are: ")
print (keyword.kwlist)

