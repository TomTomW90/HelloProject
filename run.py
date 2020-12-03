doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']


def word_search(doc_list, keyword):
    index_list = []
    for doc in doc_list:
        temp_doc = doc.split()
        for word in temp_doc:
            if word.lower().strip('., ') == keyword.lower():
                index_list.append(doc_list.index(doc))
                break
    return index_list

print(word_search(doc_list, "Casino"))

def multi_word_search(doc_list, keywords):

    dictionary = {}

    for key in keywords:
        dictionary[key] = word_search(doc_list, key)

    return dictionary

print(multi_word_search(doc_list, keywords))