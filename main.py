print("AI CHATBOT WITH ML + UTILITIES")
print("Bot: processing your request...")

import json
import nltk 
import math
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

memory = {}


# Load data
with open('intent.json') as file:
    data = json.load(file)

stemmer = PorterStemmer()

words = []
labels = []
docs_x = []
docs_y = []

# Process data
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = word_tokenize(pattern)

        words.extend(tokens)
        docs_x.append(tokens)
        docs_y.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])    

# Clean data
words = [stemmer.stem(w.lower()) for w in words if w.isalpha()]
words = sorted(list(set(words)))
labels = sorted(labels)



import numpy as np 
training = []
output = []

out_empty = [0]*len(labels)


for x, doc in enumerate(docs_x):
    bag = []

    # stem words
    wrds = [stemmer.stem(w.lower()) for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)

    # create output row
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)   

#print("Training:", training)
#print("Output:", output)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=200)
model.fit(training, docs_y)

#print("Model trained successfully!")

import numpy as np

def bag_of_words(s, words):
    bag = [0] * len(words)

    s_words = word_tokenize(s)
    s_words = [stemmer.stem(w.lower()) for w in s_words]

    for i, w in enumerate(words):
        if w in s_words:
            bag[i] = 1

    return np.array(bag)

import random 

def chat():
    print("""
    AI Assistant Started!
    Type 'help' to see commands
    Type 'quit' to exit
    """)

    while True:
        user_input = input("You: ").lower().strip()

        if "help" in user_input:
            print("""
        Available Commands:
        - Basic chat (hello, bye, etc.)
        - Memory: 'my name is ...'
        - Ask: 'what is my name'
        - Calculator: 2 + 3 * 4
        - Pie Chart: type 'pie'
        - Bar Chart: type 'bar'
        - Quit: exit chatbot
        """)
            continue

        if user_input.lower() == "quit":
            print("Bot: Goodbye! ")
            break 
        
                # CALCULATOR (ADD HERE)
        try:
            if any(op in user_input for op in ["+", "-", "*", "/"]):
                result = eval(user_input)
                print(f"Bot: Answer = {result}")
                continue
        except Exception:
            print("Bot: Invalid calculation. Try something like 2 + 3 * 4")
            continue

        # PIE CHART 
        if "pie" in user_input.lower():
            try:
                labels = input("Enter labels(comma separated): ").split(",")
                values = list(map(float, input("Enter values (comma separated): ").split(",")))

                if len(labels) != len(values):
                    print("Bot: Labels and values count must match!")
                    continue
                plt.pie(values, labels=labels, autopct='%1.1f%%')
                plt.title("Your Pie Chart")
                plt.show()
                continue
            except:
                print("Bot: Invalid input for pie chart.")
                continue
        # BAR CHART    
        if "bar" in user_input.lower():
            try:
                labels = input("Enter labels (comma separated): ").split(",")
                values = list(map(float, input("Enter values (comma separated): ").split(",")))

                if len(labels) != len(values):
                    print("Bot: Labels and values count must match!")
                    continue

                plt.bar(labels, values)
                plt.title("Sample Bar Chart")
                plt.show()
                continue
            except:
                print("Bot: Invalid input for bar chart.")
                continue
           
        if "my name is" in user_input.lower():
            name = user_input.split("my name is")[1].strip()
            memory["name"] = name
            print(f"Bot: Nice to meet you {name}!")

        if "what is my name" in user_input.lower():
            if "name" in memory:
                print(f"Bot: Your name is {memory['name']}" )
            else:
                print("Bot: I don't know your name yet.")
                continue    

        # Predict intent
        probs = model.predict_proba([bag_of_words(user_input,words)])[0]

        max_prob = max(probs)
        tag_index = np.argmax(probs)
        tag = labels[tag_index]

        if max_prob < 0.6:
            print("Bot: I didn't understand that. Can you rephrase?")
            continue

        # Find response
        for intent in data["intents"]:
            if intent["tag"] == tag:
                response = random.choice(intent["responses"])
                print("Bot:", response)

chat()