from data import list1
from collections import Counter
list = []
for words in list1:
    list.append(words.lower())

repetitives = []
for words in list:
    first = words[0]
    second = words[1]
    third = words[2]
    fourth = words[3]
    fifth = words[4]
    word_letters= [first, second, third, fourth, fifth]
    letter_count_dict = dict(Counter(word_letters))
    for i in letter_count_dict:
        if letter_count_dict[i] > 1:
            repetitives.append(words)

not_rep = []
for item in list:
    if not item in repetitives:
        not_rep.append(item)



key_dict = {"a":0, "b": 0, "c": 0, "ç": 0,"d": 0,"e": 0,"f": 0,"g": 0,"ğ": 0,"h": 0, "ı": 0, "i": 0, "j": 0,
 "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "ö": 0,"p": 0, "r": 0, "s": 0, "ş": 0, "t": 0, "u": 0, "ü": 0, "v": 0,
 "y": 0, "z": 0}

for word in list:
    for i in key_dict:
        letter_list = []
        letter_list.append(word[0])
        letter_list.append(word[1])
        letter_list.append(word[2])
        letter_list.append(word[3])
        letter_list.append(word[4])
        for letter in letter_list:
            if letter == i:
                key_dict[i] +=1
print (key_dict)

last_dict= {}
for word in not_rep:
    letter_list = []
    letter_score = []
    letter_list.append(word[0])
    letter_list.append(word[1])
    letter_list.append(word[2])
    letter_list.append(word[3])
    letter_list.append(word[4])
    for letter in letter_list:
        score = key_dict.get(letter, 0)
        letter_score.append(score)
    last_dict[word] = sum(letter_score)

last = dict(sorted(last_dict.items(), key=lambda item: item[1]))

print(last)

master_dict = {}
for word in list:
    letter_list_2 = []
    letter_score_2 = []
    letter_list_2.extend((word[0], word[1], word[2], word[3], word[4]))
    for letter in letter_list_2:
        score = key_dict.get(letter, 0)
        letter_score_2.append(score)
    master_dict[word] = sum(letter_score_2)

master = dict(sorted(master_dict.items(), key=lambda item: item[1]))

second_word_dict = {}
for i in last:
    let_list = []
    let_list.extend((i[0], i[1], i[2], i[3], i[4]))
    if "e" not in let_list and "r"not in let_list and "i" not in let_list \
            and "k" not in let_list and "a" not in let_list:
        second_word_dict[i] = last[i]

print(second_word_dict)

def wordle_helper():
    contain_list = []
    while True:
        input_contain = input("Doğru cevabın içerdiği harfleri yazıp her seferinde enter'a basın. "
                              "Bütün harfleri girince 'off' yazın ve enter'a basın : ").lower()
        if input_contain == "off":
            break
        contain_list.append(input_contain)
    not_contain_list = []
    while True:
        input_not_contain = input("Doğru cevabın içermemesi gereken harfleri yazın ve her seferinde enter'a basın. "
                                  "Bütün harfleri girince 'off' yazın ve enter'a basın : ").lower()
        if input_not_contain == "off":
            break
        not_contain_list.append(input_not_contain)

    print(contain_list)
    print(not_contain_list)
    third_word_dict = {}
    for i in master:
        let_list = []
        let_list.extend((i[0], i[1], i[2], i[3], i[4]))
        check_not_contain = any(item in let_list for item in not_contain_list)
        check_contain = all(item in let_list for item in contain_list)
        if check_not_contain is False and check_contain is True:
            third_word_dict[i] = master[i]

    print(third_word_dict)

wordle_helper()







