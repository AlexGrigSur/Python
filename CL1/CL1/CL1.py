from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import download
from nltk.corpus import stopwords

def GetData():
    file = open("DataSet_CL.txt", 'r', encoding = "utf8")
    return file.read()

def ex1(paragraphs):
    iterator=0
    sentences=sent_tokenize(paragraphs)
    for i in sentences:
        iterator +=1
        print(i)
    print("\nВ первом абзаце ",iterator," предложений")

def ex2(paragraphs):
    print(str(word_tokenize(paragraphs)) + '\n')

def ex3():
    download()

def ex4():
    print(stopwords.words("russian"))

def ex5(text):
    stopWords = set(stopwords.words('russian')) 
    sentence = sent_tokenize(text)
    WSW = []
    for word in word_tokenize(text):
        if(not word in stopWords): 
            WSW.append(word)
    for word in WSW:
        print(word, end =" ");

def ex6(text):
    wordListInSent = []
    sentences = sent_tokenize(text)
    for i in sentences:
        wordListInSent.append(word_tokenize(i))
    for i in range(len(wordListInSent)):
        print(f"\nSentence #{i+1}")
        for word in wordListInSent[i]:
            print(word)

text = GetData()
#ex1(text.split('\n')[0])
#ex2(text.split('\n')[1])
#ex3()
#ex4()
ex5(text.split('\n')[2]);
#ex6(text)