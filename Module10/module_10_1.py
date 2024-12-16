import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово {i+1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


th1 = Thread(target=write_words, args=(10, 'example1.txt'))
th2 = Thread(target=write_words, args=(30, 'example2.txt'))
th3 = Thread(target=write_words, args=(200, 'example3.txt'))
th4 = Thread(target=write_words, args=(100, 'example4.txt'))

start = time.time()
th1.start()
th2.start()
th3.start()
th4.start()

th3.join()
end = time.time()


print(f'Threading time: {round(end-start, 2)}s')
start = time.time()

write_words(2, 'example5.txt')
write_words (4, 'example6.txt')
write_words (200, 'example7.txt')
write_words (100, 'example8.txt')
end = time.time()

print(f'Basic Implementation time: {round(end-start, 2)}s')