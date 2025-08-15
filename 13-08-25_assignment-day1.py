#1.Reverse a given string without using built-in reverse functions.
string = input()
rev=''
for i in range(len(string)-1, -1, -1):
    rev=rev+string[i]
print (rev)

Output:
ram shankar sivaji
ijavis raknahs mar


#2. Check if a string is palindrome or not
str=input()
rev=''
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
if rev==str:
    print("Palindrome")
else:
    print("Not")

Output_1:
ram
Not
Output_2:
madam
Palindrome



#3.Count the no.of vowels and consonents in a string
str=input()
str=str.lower()
vowels_set="aeiou"
vowels_count=0
consonants_count=0
for i in str:
    if i.isalpha():  
        if i in vowels_set:
            vowels_count += 1
        else:
            consonants_count += 1
print("Vowels:", vowels_count)
print("Consonants:", consonants_count)

Output:
ram shankar sivaji
Vowels: 6
Consonants: 10


#4.Remove all spaces from a given string
str = input()
no_spaces = ""
for i in str:
    if i != " ":   
        no_spaces += i
print("String without spaces:", no_spaces)

Output:
Ram Shankar Sivaji
String without spaces: RamShankarSivaji




#5.Count the frequency of each character in a string
str = input()
freq = {}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key, value in freq.items():
    #print(f"'{key}': {value}")
    print(key, ":", value)

Output:
ram shankar sivaji
r : 2
a : 4
m : 1
  : 2
s : 2
h : 1
n : 1
k : 1
i : 2
v : 1
j : 1
