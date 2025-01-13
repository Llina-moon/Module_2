import threading
import time

TOTAL_ENEMIES = 100

class Knight(threading.Thread):

    def __init__(self,name:str ,power:int):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        global TOTAL_ENEMIES
        print(f'{self.name}, на нас напали!"')

        while TOTAL_ENEMIES > 0:
            time.sleep(1)
            self.days +=1

            if TOTAL_ENEMIES > 0:
                enemies_defeated = min(self.power,TOTAL_ENEMIES)
                TOTAL_ENEMIES -= enemies_defeated
                print(f'{self.name} сражается {self.days} день(дня)..., осталось {TOTAL_ENEMIES} воинов.')

        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot',6 )
second_knight = Knight("Sir Galahad", 3)

first_knight.start()
second_knight.start()



print('Все битвы закончились!')