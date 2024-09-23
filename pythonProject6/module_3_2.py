
def send_email ( messages, recipient,sender = "university.help@gmail.com") :

    if not ("@" in recipient and recipient.endswith((".com", ".net", ".ru"))) or \
       not ("@" in sender and sender.endswith((".com", ".net", ".ru"))):
            print( f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
            return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return


    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено от {sender} на {recipient}")

    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

messages = "Привет! Это тестовое сообщение."
recipient = "student@example.com"
sender = "university.help@gmail.com"

send_email(messages, recipient, sender="university.help@gmail.com")


messages = 'Вы видите это сообщение как лучший студент курса!'
recipient = 'urban.fan@mail.ru'
sender = "urban.info@gmail.com"

send_email(messages, recipient,sender)


messages = 'Вы видите это сообщение!'
recipient = 'urban.student@mail.ru'
sender = 'urban.teacher@mail.uk'

send_email (messages, recipient, sender)

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

