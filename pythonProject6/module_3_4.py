def single_root_words(root_word , *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)

    return same_words

a = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies' )
print(a)
b = single_root_words('Able', 'Disablement','Able', 'Mable', 'Disable', 'Bagel')
print(b)