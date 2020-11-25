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
    download("stopwords")

def ex4():
    print(stopwords.words("russian"))

def ex5():


#SplitByParagraphs = GetData().split('\n')
#ex1(SplitByParagraphs[0])
#ex2(SplitByParagraphs[1])
#ex3()
ex4()
