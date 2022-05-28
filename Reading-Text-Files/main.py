# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('python-files\Reading-Text-Files\story.txt') as f:
        file_content = f.read()

    return "file_content"

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    counts = dict()
    words = str.split(text)

    for word in words:
        if word in counts:
            counts[word] += 1

        else:
            counts[word] = 1

        return count
        
    #return {"as": 10, "would": 20}