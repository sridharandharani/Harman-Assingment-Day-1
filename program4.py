# Accept a string and count the frequency of vowels
vowels = "aeiou"
string = input("Enter the string :")
count = 0
for i in string.lower():
    for j in vowels:
        if ( i == j ):
            count = count + 1

print(count)
