def single_root_words(root_word, *other_words):
    same_words = []
    upper = root_word.upper()
    for i in other_words:
        if upper in i.upper() or i.upper() in upper:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)

print(result2)












                




