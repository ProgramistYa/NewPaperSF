from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

#нежелательные слова, при расширении списка вынесем в отдельный файл
bad_list = ['fuck',
            'rediska',
            'nigga',
            'сука',
            'редиска',
             ]


@register.filter()
@stringfilter #чтобы не вызывать ошибки, приведем в строку
def censor(value, bad_words=bad_list):
    words = value.split()#разделим строку
    new_line = ''

    for word in words:
        #проверяем, не входит ли слово в нежелательный список
        if word.lower() in bad_words in bad_words:
            new_line += word[0] #если да, первый символ оставляем
            for i in word[1:]:
                new_line += '*'#остальные заменяем на *
            new_line += ' '
        #здесь все тоже, но учитываем знаки пунктуации в переданной строке
        elif (word[:-1].lower()) in bad_words:
            new_line += word[0]
            for i in word[1:-1]:
                new_line += '*'
            new_line += (word[-1] + ' ')
        #склеиваем в строку обычне слова без запретов
        else:
            new_line += (word + ' ')

    return new_line.rstrip()
