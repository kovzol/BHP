# Create an OSIS XML file based on the .txt version of BHP
import pandas as pd

numbertrans = {
    40: 'Matthew',
    41: 'Mark',
    42: 'Luke',
    43: 'John',
    44: 'Acts',
    45: 'Romans',
    46: '1 Corinthians',
    47: '2 Corinthians',
    48: 'Galatians',
    49: 'Ephesians',
    50: 'Philippians',
    51: 'Colossians',
    52: '1 Thessalonians',
    53: '2 Thessalonians',
    54: '1 Timothy',
    55: '2 Timothy',
    56: 'Titus',
    57: 'Philemon',
    58: 'Hebrews',
    59: 'James',
    60: '1 Peter',
    61: '2 Peter',
    62: '1 John',
    63: '2 John',
    64: '3 John',
    65: 'Jude',
    66: 'Revelation'
}

def osis_head():
    return """<?xml version="1.0" encoding="UTF-8"?>
<osis
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns="http://www.bibletechnologies.net/2003/OSIS/namespace"
 xmlns:osis="http://www.bibletechnologies.net/2003/OSIS/namespace"
 xsi:schemaLocation="http://www.bibletechnologies.net/2003/OSIS/namespace https://www.crosswire.org/osis/osisCore.2.1.1.xsd">

 <osisText osisIDWork="BHPGNT" osisRefWork="Bible" xml:lang="grc" canonical="true">
  <header>
   <work osisWork="BHPGNT">
    <title>Bunning Heuristic Prototype Greek New Testamen</title>
    <identifier type="OSIS">Bible.BHPGNT</identifier>
    <refSystem>Bible.Calvin</refSystem>
   </work>
  </header>
"""

def osis_tail():
    return """
 </osisText>

</osis>"""

print(osis_head())

bhp_txt = pd.read_csv('BHP_Data.txt', sep='\t')
book_old = ""
book_chapter_old = ""
book_chapter_verse_old = ""
verse_rawstring = ""
for word in bhp_txt.itertuples():
    word_code = str(word[1])
    # word_rawstring = str(word[2])
    word_rawstring = str(word[3])
    book = word_code[0:2]
    chapter = word_code[2:5]
    verse = word_code[5:8]
    book_chapter = book + chapter
    book_chapter_verse = book_chapter + verse
    book_formatted = numbertrans[int(book)]
    book_chapter_formatted = book_formatted + "." + str(int(chapter))
    if book != book_old:
        if verse_rawstring != "": # a new book has been started
            print("  </div>")
        # output the current book name
        print(f"  <div osisID=\"{book_formatted}\" type=\"book\">")
        verse_rawstring = ""
    if book_chapter != book_chapter_old:
        if verse_rawstring != "": # a new chapter has been started
            print("   </chapter>")
        # output the current chapter name
        print(f"   <chapter osisID=\"{book_chapter_formatted}\">")
        verse_rawstring = ""
    if book_chapter_verse != book_chapter_verse_old and verse_rawstring != "": # a new verse has been started
        # output the old verse
        print(f"    <verse osisID=\"{book_chapter_verse_formatted}\">{verse_rawstring}</verse>")
        verse_rawstring = ""
    book_chapter_verse_formatted = book_chapter_formatted + "." + str(int(verse))
    if verse_rawstring != "":
        verse_rawstring += " "
    verse_rawstring += word_rawstring
    book_chapter_verse_old = book_chapter_verse
    book_chapter_old = book_chapter
    book_old = book

# finish Revelations
print("   </chapter>")
print("  </div>") # book

print(osis_tail())
