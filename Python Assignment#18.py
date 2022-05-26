#!/usr/bin/env python
# coding: utf-8

# In[2]:


##Answer1:

import re
 
regex = r'^[a-z]$|^([a-z]).*\1$'

def check(string):

    if(re.search(regex, string)): 
        print("Valid") 
    else: 
        print("Invalid") 
 
if __name__ == '__main__' :
 
    sample1 = "abba"
    sample2 = "a"
    sample3 = "abcd"
 
    check(sample1)
    check(sample2)
    check(sample3)


# In[6]:


##Answer2:

import re

def match(text):

        pattern = '[A-Z]+[a-z]+$'

        if re.search(pattern, text):
                return('Yes')
        else:
                return('No')

print(match("Tit"))
print(match("TitforTat"))
print(match("tat"))


# In[8]:


##Answer3:

from collections import Counter
 
def remov_duplicates(input):

    input = input.split(" ")

    UniqW = Counter(input)

    s = " ".join(UniqW.keys())
    print (s)

if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    remov_duplicates(input)


# In[9]:


##Answer4:

import re

ini_string = "123abcjw:, .@! eiw"

print ("initial string : ", ini_string)

result = re.sub('[\W_]+', '', ini_string)

print ("final string", result)


# In[16]:


##Answer5:

import re

regex = '[a-zA-z0-9]$'

def check(string):

    if(re.search(regex, string)):
        print("Accept")
         
    else:
        print("Discard")
     
 
  
if __name__ == '__main__' :

    string = "giri"

    check(string)
 
    string = "giridharan"
    check(string)
 
    string = "giri."
    check(string)
 
    string = "neuron"
    check(string)


# In[19]:


##Answer6:

import re

regex = '^[aeiouAEIOU][A-Za-z0-9_]*'

def check(string):

    if(re.search(regex, string)):
        print("Valid")
         
    else:
        print("Invalid")
     
 
  
if __name__ == '__main__' :

    string = "ankit"

    check(string)
 
    string = "dharan"
    check(string)
 
    string = "giridharan"
    check(string)


# In[22]:


##Answer7:

import re

def find(string, sample) :

  if (sample in string):
  
      y = "^" + sample

      x = re.search(y, string)
  
      if x :
          print("string starts with the given substring")
  
      else :
          print("string doesn't start with the given substring")
  
  else :
      print("entered string isn't a substring")

string = "RCB makes cricket fun"  
sample = "RCB"

find(string, sample)
  
sample = "makes"

find(string, sample)


# In[24]:


##Answer8:

import re

def isValidURL(str):

    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    p = re.compile(regex)

    if (str == None):
        return False

    if(re.search(p, str)):
        return True
    else:
        return False

url = "https://www.cricbuzz.com"
 
if(isValidURL(url) == True):
    print("Yes")
else:
    print("No")


# In[25]:


##Answer9:

import re  

s = 'https://www.cricbuzz.com/'
 
obj1 = re.findall('(\w+)://',
                  s)
print(obj1)

obj2 = re.findall('://www.([\w\-\.]+)', 
                  s)
print(obj2)


# In[26]:


##Answer10:

import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def check(Ip):

    if(re.search(regex, Ip)):
        print("Valid Ip address")
         
    else:
        print("Invalid Ip address")
     
      
if __name__ == '__main__' :

    Ip = "192.168.0.1"

    check(Ip)
 
    Ip = "110.234.52.124"
    check(Ip)
 
    Ip = "366.1.2.2"
    check(Ip)

