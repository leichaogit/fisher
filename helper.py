def is_key_or_isbn(word):
    """
    判断，word是isbn还是查询关键字
    isbn10 '-'加上0-9的10个数字组成
    isbn13 0-9的13个数字组成
    :param word: key or isbn
    :return:
    """
    key_or_isbn = 'key'
    if len(word) == 13 and word.isdigit():
        key_or_isbn = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        key_or_isbn = 'isbn'
    return key_or_isbn
