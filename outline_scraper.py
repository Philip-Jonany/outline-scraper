# outline-scraper.py

import re

BOOK_ABBREVIATIONS = [
    "Gen.", "Exo.", "Lev.", "Num.", "Deut.", "Josh.", "Judg.", "Ruth", "1 Sam.", "2 Sam.", 
    "1 Kings", "2 Kings", "1 Chron.", "2 Chron.", "Ezra", "Neh.", "Esth.", "Job", "Ps.", "Prov.",
    "Eccl.", "Song", "Isa.", "Jer.", "Lam.", "Ezek.", "Dan.", "Hos.", "Joel", "Amos", "Obad.", 
    "Jonah", "Mic.", "Nah.", "Hab.", "Zeph.", "Hag.", "Zech.", "Mal.", "Matt.", "Mark", "Luke", 
    "John", "Acts", "Rom.", "1 Cor.", "2 Cor.", "Gal.", "Eph.", "Phil.", "Col.", "1 Thess.", 
    "2 Thess.", "1 Tim.", "2 Tim.", "Titus", "Phlm.", "Heb.", "James", "1 Pet.", "2 Pet.", "1 John", 
    "2 John", "3 John", "Jude", "Rev."
]

f = open("message2.txt", "r") 

def split_by_books(text):
    pattern = r'(' + '|'.join(re.escape(book) for book in BOOK_ABBREVIATIONS) + r')'
    sections = re.split(pattern, text)
    result = []
    # Starts with message title before any verses
    i = 1
    while i < len(sections):
        book = sections[i]
        section = sections[i + 1] if (i + 1) < len(sections) else ""
        result.append((book, section))
        # sections contains book, section, book, section...
        i += 2
    return result

def runAndPrint(s):
    result = split_by_books(s)
    for book, section in result:
        print("-----")
        print(book + "\n" + section)

s = f.read()
runAndPrint(s)
f.close()

'''
Edge cases:
1) Matt. 12:26
2) Josh. 1:2-6; 5:11-6:27
3) Gen. 1:9; 2 Pet. 3:5;
4) Genesis 1:9-10 and 13
5)
'''
f.close()