
def is_balanced(expression):
    #print(expression)
    my_stack = []
    for e in expression:
        if e in '([{':
           my_stack.append(e)
        elif e in ')]}':
            if not my_stack:
                return False
            added_val = my_stack.pop()
            if added_val == '(' and e != ')' or added_val == '[' and e != ']' or added_val == '{' and e != '}':
                return False
    return not my_stack

            
expression1 = "([]{})"
expression2 = "([)]"
print('--------------------')
print('QUESTION ONE OUTPUT')
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

# Question 2: Write a function remove_duplicates(sequence) that takes a 
# sequence (list or tuple) and returns a new sequence with duplicates 
# removed while maintaining the original order of elements. 

# sample input = 

# input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
# result = remove_duplicates(input_sequence)

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
def remove_duplicates(sequence):
    sequence_no_duplicates = list(set(sequence))
    return (sequence_no_duplicates)

result = remove_duplicates(input_sequence)
print("----------------------")
print('QUESTION TWO OUTPUT')
print(result)  # Output: [2, 3, 4, 5, 6, 7]


# Question 3: Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 

# Ignore punctuation and consider words in a case-insensitive manner. 
import string
def word_frequency(sentence):
    #translate: Return a copy of the string in which each character has been mapped through the given translation table
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    # sentence = sentence.removeprefix(',')
    # sentence1 = sentence.removeprefix('.')
    # sentence2 = sentence1.removeprefix(' ')
    # sentence3 = sentence2.removeprefix('.')

    words = sentence.split()
    # print(words)
    word_frequency_counter = {}
    for word in words:
        if word in word_frequency_counter:
            word_frequency_counter[word] += 1
        else:
            word_frequency_counter[word] = 1

    print("----------------------")
    print('QUESTION THREE OUTPUT')
    print(word_frequency_counter)

    # unique_char = [char for char in sentence if char not in ". ," ]
    # #print(unique_char)
sentence = "This is a test sentence. This sentence is a test."
word_frequency(sentence)