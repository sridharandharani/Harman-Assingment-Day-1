#Display the smallest and largest word from the string
string=input("Enter the string:")
string_list = list(string.split(" "))
print(string_list)
sort_list = sorted(string_list, key = len)
print(sort_list[-1])