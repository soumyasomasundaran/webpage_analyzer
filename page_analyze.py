import re
from collections import Counter
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#function to find unique words
def unique_words(words):
    unique = []
    for i in words:
        if words[i] == 1:
            unique.append(i)
    return(unique)

#function to remove symbols
def rem_symbol(sent):
    return(re.sub(r'[^A-Za-z ]+', '',sent)) # removing symbols)

#function to remove stop words
def rem_stopwords(example_sent):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(example_sent)
    #filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


def page_analyze(url):
    my_source_code = requests.get(url).text
    my_soup = BeautifulSoup(my_source_code, 'html.parser')
    linecount = []
    wordcount = []

    for s in my_soup.findAll('p'):
        for line in s.text.split((".")):
            linecount.append(line)
            line=rem_symbol(line) #removes all punctuations and symbols
            line = rem_stopwords(line)#remove stopwords
            for word in line:
                wordcount.append(word)
    mostcommon= Counter(wordcount).most_common(5)
    words=Counter(wordcount)
    u_words=unique_words(words)
    return(mostcommon,len(linecount),len(wordcount),len(u_words))

url="https://www.tutorialspoint.com/python3/python_overview.htm/"
page_analyze(url)