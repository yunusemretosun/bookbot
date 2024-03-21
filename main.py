import os
def main():
    
    path = "books"
    book_names = os.listdir(path)
    book_analyze(book_names,path=path)

    
def book_analyze(book_names,path):
    for name in book_names:
        base_dict = {chr(i): 0 for i in range(97, 123)}
        book_path = f"{path}/{name}"
        book_content = get_book_content(book_path)
        word_count = len(split_book(book_content))
        alphabet = get_character_count(book_content,base_dict)
        make_report(book_path,word_count,alphabet)
        
        

        
def get_book_content(book_name):
    with open(book_name,"r") as bk:
        content = bk.read()
    return content

def split_book(content):
    return content.split()

def get_character_count(book_content,alphabet):
    words = split_book(book_content.lower())
    for word in words:
        for char in word:
            if char in alphabet:
                alphabet[char] += 1
    sorted_list = sorted(alphabet.items(),key=lambda x:x[1])
    sorted_dict = dict(sorted_list)
    return sorted_dict

def print_character_count(alphabet):
    for key,value in alphabet.items():
        print(f"The '{key}' character was found {value}")
        
def make_report(book_path, word_count, alphabet):
    print(f"--- Begin report of {book_path} ---")
    print(f"The {word_count} words found in the document.")
    print_character_count(alphabet)
    print("--- End report ---")
    
    
    
main()
    