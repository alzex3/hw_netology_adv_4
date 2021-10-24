import hashlib


def generator(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            for i in f:
                yield hashlib.md5(i.encode('utf-8')).hexdigest()
    except IOError:
        print('File does not detected!')


for _ in generator('test_file.txt'):
    print(_)
