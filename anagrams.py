def anagrams(word, words):
    anagrams = []
    for i in words:
        if sorted(i) == sorted(word):
            anagrams.append(i)
    return anagrams




anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])
