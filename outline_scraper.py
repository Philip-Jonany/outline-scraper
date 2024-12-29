# outline-scraper.py

import re
f = open("message2.txt", "r") 

BOOK_ABBREVIATIONS = [
    "Gen.", "Exo.", "Lev.", "Num.", "Deut.", "Josh.", "Judg.", "Ruth", "1 Sam.", "2 Sam.", 
    "1 Kings", "2 Kings", "1 Chron.", "2 Chron.", "Ezra", "Neh.", "Esth.", "Job", "Psa.", "Prov.",
    "Eccl.", "Song", "Isa.", "Jer.", "Lam.", "Ezek.", "Dan.", "Hos.", "Joel", "Amos", "Obad.", 
    "Jonah", "Mic.", "Nah.", "Hab.", "Zeph.", "Hag.", "Zech.", "Mal.", "Matt.", "Mark", "Luke", 
    "John", "Acts", "Rom.", "1 Cor.", "2 Cor.", "Gal.", "Eph.", "Phil.", "Col.", "1 Thess.", 
    "2 Thess.", "1 Tim.", "2 Tim.", "Titus", "Phlm.", "Heb.", "James", "1 Pet.", "2 Pet.", "1 John", 
    "2 John", "3 John", "Jude", "Rev."
]

# returns list of tuples (book, text_between_books)
def split_by_books(text):
    # Sort books so 1 John is deteced before John
    pattern = r"(" + "|".join(map(re.escape, sorted(BOOK_ABBREVIATIONS))) + r")"
    print(pattern)
    sections = re.split(pattern, text)
    result = []
    # Starts with message title before any verse refs, so skip 0
    i = 1
    while i < len(sections):
        book = sections[i]
        section = sections[i + 1] if (i + 1) < len(sections) else ""
        result.append((book, section))
        # sections contains book, section, book, section...
        i += 2
    return result

# Takes one section between books, and splits it by chapters
def split_by_chapters(text):
    pattern = r"(\d+:\d+)"

    # split into alternating between chapter and section between chapter
    sections = re.split(pattern, text)
    result = []

    # Find first chapter ref
    i = 0
    while i < len(sections):
        section = sections[i]
        if re.match(r"\d+", section):
            break
        i += 1
    if i >= len(sections): 
        print("UNEXPECTED ERROR: NO CHAPTERS FOUND IN " + text)

    while i < len(sections):
        section = sections[i]
        colonIndex = section.find(":")
        section_after_chapter = sections[i + 1] if (i + 1) < len(sections) else ""
        result.append((section[:colonIndex], section[colonIndex:] + section_after_chapter))
        i += 2
    return result

# Finds all number-number patterns and single numbers, return list of integers.
def getAllVerseNumbers(s):
    pattern = r"(\d+-\d+)"

def runAndPrint(s):
    result = split_by_books(s)
    for book, section in result:
        print("-----")
        print(book)
        verses = split_by_chapters(section)
        for chapter, section in verses:
            print("\t" + chapter)
            print("\t\t" + section)

# main
def main():
    s = f.read()
    runAndPrint(s)
    f.close()
if __name__ == "__main__":
    main()
'''
Edge cases:
1) Matt. 12:26
2) Josh. 1:2-6; 5:11-6:27
3) Gen. 1:9; 2 Pet. 3:5;
4) Genesis 1:9-10 and 13
5)
'''