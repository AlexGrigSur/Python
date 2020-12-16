from pymorphy2 import MorphAnalyzer
import nltk


def ex1():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    for i in morph.parse('стали'):
        print(i)


def ex2():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    p = morph.parse('стали')[0]
    print(p.normal_form)  # стать
    print(p.normalized)


def ex3():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    p = morph.parse('стали')[0]
    print(p.tag)


def ex4():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    print(morph.parse('бутявковедами'))


def ex5():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    p = morph.parse('стали')[0]
    print('VERB' in p.tag)
    print('NOUN' in p.tag)
    print({'plur', 'past'} in p.tag)
    print({'NOUN', 'plur'} in p.tag)


def ex6():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    p = morph.parse('стали')[0]
    # часть речи
    print(p.tag.POS)  # VERB
    # одушевленность
    print(p.tag.animacy)  # None
    # вид: совершенный или несовершенный
    print(p.tag.aspect)  # perf
    # падеж
    print(p.tag.case)  # None
    # род (мужской, женский, средний)
    print(p.tag.gender)  # None
    # включенность говорящего в действие
    print(p.tag.involvement)  # None
    # наклонение (повелительное, изъявительное)
    print(p.tag.mood)  # indc
    # число (единственное, множественное)
    print(p.tag.number)  # plur
    # лицо (1, 2, 3)
    print(p.tag.person)  # None
    # время (настоящее, прошедшее, будущее)
    print(p.tag.tense)  # past
    # переходность (переходный, непереходный)
    print(p.tag.transitivity)  # intr
    # залог (действительный, страдательный)
    print(p.tag.voice)  # None


def ex7():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    p = morph.parse('стали')[0]
    print('foobar' in p.tag)  # ValueError: Grammeme is unknown: foobar
    print({'NOUN', 'foo', 'bar'} in p.tag)


def ex8():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    p = morph.parse('стали')[0]
    print(p.tag.POS == 'plur')


def ex9():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    butyavka = morph.parse('бутявка')[0]
    print(butyavka)


def ex10():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    butyavka = morph.parse('бутявка')[0]
    # нет кого? (родительный падеж)
    print(butyavka.inflect({'gent'}))
    print(butyavka.inflect({'plur', 'gent'}))


def ex11():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    butyavka = morph.parse('бутявка')[0]
    print(butyavka.lexeme)


def ex12():
    from pymorphy2 import MorphAnalyzer
    m = MorphAnalyzer()
    print(m.parse('думающему')[0].normal_form)


def ex13():
    from pymorphy2 import MorphAnalyzer
    m = MorphAnalyzer()
    print(m.parse('думающему')[0].inflect({'sing', 'nomn'}).word)


def ex14():
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    butyavka = morph.parse('бутявка')[0]
    print(butyavka.make_agree_with_number(1).word)  # бутявка
    print(butyavka.make_agree_with_number(2).word)  # бутявки
    print(butyavka.make_agree_with_number(5).word)  # бутявок


def lin2():
    file = open("DataSet_CL.txt", 'r', encoding = "utf8")
    SplitByParagraphs = file.read().split('\n')[0]
    text=""
    text = text.join([paragraph for paragraph in SplitByParagraphs])
    words = [word for word in nltk.word_tokenize(text) if word.isalpha()]
    #words = set(words)
    #words = sorted(words)
    morph = MorphAnalyzer()

    for word in words:
        p = morph.parse(word)[0]

        par=''
        par=par.join(f"""\nИсходная форма = {word}
        Нормальная форма = {p.normal_form}
        Часть речи = {p.tag.POS}
        Одушевленность = {p.tag.animacy}
        Вид = {p.tag.aspect}
        Падеж = {p.tag.case}
        Род = {p.tag.gender}
        Включенность = {p.tag.involvement}
        Наклонение = {p.tag.mood}
        Число = {p.tag.number}
        Лицо = {p.tag.person}
        Время = {p.tag.tense}
        Переходность = {p.tag.transitivity}
        Залог = {p.tag.voice}
        Лексемы = {', '.join([l[0] for l in p.lexeme])}
    """)
        print(par)
#ex11
lin2()

