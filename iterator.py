import json


class Iterator:
    def __init__(self, filename):
        self.file = json.load(open(filename))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            name = self.file[self.index]['name']['common']
            result = {name: f'https://en.wikipedia.org/wiki/{name.replace(" ", "_")}'}
            with open('result.json', 'a', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=1)
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


iterator = Iterator('countries.json')
