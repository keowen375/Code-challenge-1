import string

def word_frequency(sentence):
    #convert to small letters and remove spaces with translate
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()

    count ={}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)






