import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens]

    # step-4 removing stopwords and non-alphabet words.
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words]

    # step-5 stemming 
    tokens = [stemmer.stem(w) for w in tokens]

    return tokens

# Test
sentence = "I am playing cricket and watching movies" 
print(preprocess(sentence))