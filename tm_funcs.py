from nltk.tokenize import word_tokenize


if __name__ == '__main__':
    with open("data/hindu.txt") as fin:
        text = fin.read()
    print("The lenght of the corpus: %d" % len(text))
    # print(text)

    # print(text.split(" "))
    print(word_tokenize(text))