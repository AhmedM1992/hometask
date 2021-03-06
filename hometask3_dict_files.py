#Created file

example = {'title': 'LhmQH4viLO4S x m 2AmXECPhYu5e90k', 'pid': 'f626be28', 'name': 'Crimson Lemur',
           'lang_code': 'text', 'lang': 'Text',
           'paste': '<div class="text" style="font-family:monospace;"><ol><li style="font-weight: normal; vertical-align:top;"><div style="font: normal normal 1em/1.2em monospace; margin:0; padding:0; background:none; vertical-align:top;">m3DVLV1L hJn6xpNRivm8TT8KVNCBC5GnMeR9y 0AIHPFo90 pReOZsowJq iYAVNheF 2gcy &nbsp;2z7jaCow OXrwHps9o4p xKDk8t gW3MdROSbyfAE7NQvc UgT8DY</div></li>\n</ol></div>',
           'created': '1507207620', 'url': 'http://text-share.com/view/f626be28',
           'raw': 'm3DVLV1L hJn6xpNRivm8TT8KVNCBC5GnMeR9y 0AIHPFo90 pReOZsowJq iYAVNheF 2gcy  2z7jaCow OXrwHps9o4p xKDk8t gW3MdROSbyfAE7NQvc UgT8DY',
           'hits': '0', 'hits_updated': '0', 'snipurl': '0',
           'inreply': {'title': 'Re: Re: Re: Re: Re: Re: Re: Untitled',
                       'name': 'Gracious Kangaroo', 'url': 'http://text-share.com/view/e104ae95'}}

my_dict = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

#Task 2 - сложность *** - три снежинки

def get_value(some_dict, key):
    '''
    Написать фунуцию, которая принимает два значения/аргумента 
    первое - словарь
    второе ключ
    и возвращает значение этого ключа, если он есть, 
    если такого ключа нет - возвращает None
    '''
    for k, v in some_dict.items():
        if k == key:
            return some_dict.get(key)
           
def get_value(some_dict, key):
    '''
    Вторая версия функции для словаря
    '''
    if key in some_dict:
        return some_dict[key]
            
#Task 3 - сложность первый класс 2-я четверть

def count_words(path, some_string):
    '''
    на сервере 0.0.0.0 -22
    в папке /.../.../... лежат 2 файла
    *.txt  **.txt
    
    Написать функцию, которая принимает два значения/аргумента 
    первый аргумент - путь к файлу
    второй - любое слово
    
    Возвращает функция число - сколько раз встречается слово в файле
    '''
    file = open(path, 'r')
    file_read = file.read()

    split_file = file_read.split()
    split_string = some_string.split()

    count = 0

    for word in split_file:
        for search in split_string:
            if search == word:
                count += 1

    return count

# Answer for count_words('/tmp/dz_files/romeo_and_juliet.txt', 'Romeo') is 51 !!!


