import random
import time
import threading


class Bank:
    def __init__(self,balance:int):
        self.balance = balance
        self.lock = threading.Lock()


    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                print(f"Пополнение: {amount} . Баланс: {self.balance}")
                if self.balance >= 500 and self.lock.locked():
                    self.lock.realise()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()
            time.sleep(0.001)





bank = Bank(balance=0)

thread1 = threading.Thread(target=bank.deposit)
thread2 = threading.Thread(target=bank.take)

thread1.start()
thread2.start()


thread1.join()
thread2.join()


print(f"Итоговый баланс: {bank.balance}")