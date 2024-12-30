# outline-scraper.py

import re
f = open("outlines/2024ST8.txt", "r") 

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
def split_by_books(text) -> []:
    # Sort books so 1 John is deteced before John
    # TODO: bug where Ep. \n 2:20 will not get detected. Chapter must be in same line as book
    pattern = r"((?:" + "|".join(map(re.escape, sorted(BOOK_ABBREVIATIONS))) + r") \d+:\d+)"
    sections = re.split(pattern, text)
    result = []
    # Starts with message title before any verses, so skip 0
    i = 1
    while i < len(sections):
        section = sections[i]
        spaceIndex = section.rfind(" ") # rfind because 1 John has space
        # book = sections[i]
        section_after_book = sections[i + 1] if (i + 1) < len(sections) else ""
        result.append((section[:spaceIndex], section[spaceIndex:] + section_after_book))
        # sections contains book, section, book, section...
        i += 2
    return result

# Takes one section between books, and splits it by chapters
def split_by_chapters(text):
    # TODO: make exception for books with only one chapter
    pattern = r"(\d+:\d+)"

    # split into alternating between chapter and text between chapter
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
        colonIndex = section.rfind(":")
        section_after_chapter = sections[i + 1] if (i + 1) < len(sections) else ""
        result.append((section[:colonIndex], section[colonIndex:] + section_after_chapter))
        i += 2
    return result

# Finds all number-number patterns and single numbers, return list of integers.
def get_all_verse_numbers(s):
    # TODO: remove duplicates. Maybe only add if (pre_verse < curr_verse)?
    # TODO: don't include verse if it's a digit preceded by newline
    # this pattern excludes MOST num lists, but also has false negatives
    # pattern = r"\d+-\d+" + "|" + r"(?<!\n)\b\d+" 

    # this pattern works but includes all num lists
    pattern = r"\d+-\d+" + "|" + r"\d+"
    return re.findall(pattern, s)

# returns list of tuples (string book, list[(string chapter, list[string] verses))] chapters) 
def get_all_books_and_verses(s):
    result = []
    books_split = split_by_books(s)
    for book, section in books_split:
        chapters_split = split_by_chapters(section)
        chapter_tuples = []
        for chapter, chapter_section in chapters_split:
            chapter_tuples.append((chapter, get_all_verse_numbers(chapter_section)))
        result.append((book, chapter_tuples))
    return result

def print_result(result: list):
    for (book, chapters) in result:
        print(book)
        for (chapter, verses) in chapters:
            print("\t" + chapter)
            for v in verses:
                print("\t\t" + v)

def runAndPrint(s):
    result = get_all_books_and_verses(s)
    print_result(result)

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
4) Gen. 1:9-10 and 13
5) Gen. 1:7-8a
'''