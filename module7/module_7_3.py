class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def find(self, word):
        founds = {}
        for key, value in self.get_all_words().items():
            for index, text in enumerate(value, 1):
                if text == word.lower():
                    founds[key] = index
                break
        return founds

    def count(self, word):
        counts = {}
        for key, value in self.get_all_words().items():
            counter = 0
            for text in value:
                if text == word.lower():
                    counter += 1
                    counts[key] = counter
            return counts

    def get_all_words(self) -> dict[str, list[str]]:
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    info = info.replace(sym, '')
                    all_words[file_name] = info.split()
        return all_words


finder1 = WordsFinder('test_file1.txt', 'test_file2.txt')
words = finder1.get_all_words()
print(words)
finded = finder1.find('привет')
print(finded)
counted = finder1.count('привет')
print('\n', counted)
