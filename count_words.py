from collections import Counter
def get_most_used_words(text, n=3):
    """
    3 or less most frequent words in a string
    sorted alphabetically
    and the number of occurrences
    1. case insensitive

    If there is more than 3 words in a certain number of occurrences n or more only show the words appearing more than n+1 times
    """
    # Split the text into words
    words = text.lower().split()
    # Count the frequency of each word
    word_counts = Counter(words)
    occurrences = sorted(set(word_counts.values()), reverse=True)
    count0=sum([1 for i in word_counts.values() if i == occurrences[0]])
    most_common=[]
    most_common = [(word, count) for word, count in word_counts.items() if count == occurrences[0]]

    # most_common = []
    # for occ in occurrences:
    #     words_with_occ = [(word, count) for word, count in word_counts.items() if count == occ]
    #     most_common.extend(words_with_occ)
    #     if len(most_common) >= n:
    #         break
    # # Only keep up to n words, sorted alphabetically
    # most_common = sorted(most_common, key=lambda x: x[0])[:n]

    if count0 < n and len(occurrences) > 1:
        most_common1 = [(word, count) for word, count in word_counts.items() if count >= occurrences[1]]
        if len(most_common1) == n:
            most_common = most_common1
        elif len(most_common1) < n:
            most_common2 = [(word, count) for word, count in word_counts.items() if count == occurrences[2]]
            if len(most_common2) > n:
                most_common = most_common1
            elif len(most_common2) <= n:
                most_common = most_common2
    return sorted(most_common, key=lambda x: (x[0]))



tests=[
    ('Fear leads to anger Anger leads to hatred Hatred leads to conflicts Conflict leads to suffering', 3, [('leads', 4), ('to', 4)]),   
    ('Hello world hello my dear friend hello all of you wherever you are How are you doing today', 3, [('are', 2), ('hello', 3), ('you', 3)]),   

    ('test TEST Test tesT', 10, [('test', 4)]),   
    ('test TEST Test tesT a b c d', 3, [('test', 4)]),   
    ('hello world hello', 2, [('hello', 2), ('world', 1)]),
    ('one fish two fish red fish blue fish', 3, [('fish', 4)]),
    ('a a a b b c', 2, [('a', 3), ('b', 2)])
]
for text, n, expected in tests:
    result = get_most_used_words(text, n)
    if result != expected: 
        print(f'Wrong For text="{text}" and n={n}, expected {expected} but got {result}')
    # else:
    #     print('ok for', text, n)
    assert result == expected, f'For text="{text}" and n={n}, expected {expected} but got {result}'
print('All tests passed!')