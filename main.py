def main():
    alphabet_dict = {chr(i): 0 for i in range(97, 123)}
    book = "Frankenstein"
    book_path = f"books/{book}.txt"
    book_content = get_book_content(book_path)
    word_count = len(split_book(book_content))
    alphabet = get_character_count(book_content,alphabet_dict)
    make_report(book_path,word_count,alphabet)
    
def get_book_content(path):
    with open(path,"r") as bk:
        content = bk.read()
    return content

def split_book(content):
    return content.split()

def get_character_count(book_content,alphabet):
    words = split_book(book_content.lower())
    for word in words:
        for char in word:
            if char in alphabet.keys():
                alphabet[char] += 1 
    return alphabet

def print_character_count(alphabetto):
    for key,value in alphabetto.items():
        print(f"The '{key}' character was found {value}")
        
def make_report(book_path,word_count,alphabet):
    print(f"--- Begin report of {book_path} ---")
    print(f"The{word_count} words found in the document")
    print_character_count(alphabetto=alphabet)
    
main()
    