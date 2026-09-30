import pandas as pd
import re 

df = pd.read_csv('frequency\\search_terms.csv')

first_column = [row[0] for row in df.values]

words = []
for term in first_column:
    result = re.findall(r'\w+', term.lower())
    words.extend(result) 

    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    top15 = sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:15]


    for word, count in top15:
        print(f"{word}: {count}")

word_counts = {}
weighted_counts = {}

for row in df.values:
    term = row[0]
    clicks = row[1]
    for word in re.findall(r'\w+', term.lower()):
        word_counts[word] = word_counts.get(word, 0) + 1
        weighted_counts[word] = weighted_counts.get(word, 0) + clicks

top_raw = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:15]
top_weighted = sorted(weighted_counts.items(), key=lambda x: x[1], reverse=True)[:15]

raw_rank = {word: i + 1 for i, (word, c) in enumerate(top_raw)}
weighted_rank = {word: i + 1 for i, (word, c) in enumerate(top_weighted)}

print("Top 15 by raw count: ")
for word, count in top_raw:
    print(f"{raw_rank[word]}. {word}: {count}")

print("\nTop 15 by clicks: ")
for word, total in top_weighted:
    print(f"{weighted_rank[word]}. {word}: {total}")

print("\nRanking comparison: ")
for word, total in top_weighted:
    print(f"{word}: raw rank {raw_rank.get(word, 'not in top 15')}, click rank {weighted_rank[word]}")


"""  print(f"{term}: {words_count[term]}")
    tempCounter = 0
    if counter > tempCounter:
        tempCounter = counter
        most_frequent_term = term

print(words)

print(f"Most frequent term: {most_frequent_term} with {tempCounter} occurrences")

"""