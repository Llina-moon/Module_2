import threading
import time



class Knight(threading.Thread):

    def __init__(self,name:str ,power:int):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.TOTAL_ENEMIES = 100

    def run(self):

        print(f'{self.name}, на нас напали!"')

        while self.TOTAL_ENEMIES > 0:
            time.sleep(1)
            self.days +=1

            if self.TOTAL_ENEMIES > 0:
                enemies_defeated = min(self.power,self.TOTAL_ENEMIES)
                self.TOTAL_ENEMIES -= enemies_defeated
                print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.TOTAL_ENEMIES} воинов.')

        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot',10 )
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()



print('Все битвы закончились!')