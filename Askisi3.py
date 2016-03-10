import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import itertools

def Synonym_Checker(word1, word2):
    equivalence = WordNetLemmatizer()
    word1 = equivalence.lemmatize(word1)
    word2 = equivalence.lemmatize(word2)

    word1_synonyms = wordnet.synsets(word1)
    word2_synonyms = wordnet.synsets(word2)

    scores = [i.wup_similarity(j) for i, j in list(itertools.product(word1_synonyms, word2_synonyms))]
    max_index = scores.index(max(scores))
    best_match = (max_index/len(word1_synonyms), max_index % len(word1_synonyms)-1)

    word1_set = word1_synonyms[best_match[0]].lemma_names()
    word2_set = word2_synonyms[best_match[1]].lemma_names()
    match = False
    match = [match or word in word2_set for word in word1_set][0]

    return match

phrase1 = raw_input('Dose tin frasi 1')
phrase2 = raw_input('Dose tin frasi 2')

stop_words = set(stopwords.words("english"))
words1 = word_tokenize(phrase1)
words2 = word_tokenize(phrase2)

filtered_sentence1 = []
for w in words1:
    if w not in stop_words:
        filtered_sentence1.append(w)

filtered_sentence2 = []
for w in words2:
    if w not in stop_words:
        filtered_sentence2.append(w)

print filtered_sentence1
print filtered_sentence2

for i in range(0 , len(filtered_sentence1) ):
    for j in range(0 , len(filtered_sentence2) ):
        print Synonym_Checker(filtered_sentence1[i], filtered_sentence2[j])
        if Synonym_Checker(filtered_sentence1[i], filtered_sentence2[j]) == "True":
          print filtered_sentence1[i]+" is synonymous with "+filtered_sentence2[j]
        else:
          print filtered_sentence1[i]+" is not synonymous with "+filtered_sentence2[j]
