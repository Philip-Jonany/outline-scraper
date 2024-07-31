shortened_books = ["John", "yuh"]
f = open("message1.txt", "r") 

s = f.read()
print(len(s))

# get indices of every occurence of shortened_books in s.
# between every shortened_books, find all colons or verse references.

f.close()