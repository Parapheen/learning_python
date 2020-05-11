def counting_words(file):
    f = open(file, 'r')
    line = f.read().replace('\n', ' ').lower().split()
    words = dict()

    for word in line:
        words[word] = line.count(word)

    maximum = 0
    first_word = 'a'
    top_words = dict()

    for key, value in words.items():
        if value > maximum:
            maximum = value
        top_words[key] = maximum

    print(top_words)

    f.close()

counting_words("dataset_3363_3.txt")