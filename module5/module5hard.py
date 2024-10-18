class User:
    """
        Класс пользователя, содержащий атрибуты: логин,пароль,возраст
    """

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.__hash_password(password)
        self.age = int(age)

    def __hash_password(self, password):
        hashed = hash(password)
        return hashed

    def __str__(self):
        return f"User with nick: {self.nickname}"


class Video:
    """
        Класс видео, содержащий атрибуты: заголовок, продолжительность, время остановки и ограничение по возрасту
    """

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = bool(adult_mode)

    def __str__(self):
        return f"Video Title: {self.title}"


class Urtube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register_user(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print("Такой пользователь уже существует")
                return None

        user = User(nickname, password, age)
        self.users.append(user)
        print("Вы успешно зарегистрировались!")
        self.current_user = user
        return user

    def log_in(self, nickname: str, password: str):
        if self.current_user:
            print("Сперва выйдите из аккаунта!")
            return self.current_user
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                print("Успешная Авторизация")
                self.current_user = user
                return user
        print("Такого пользователя не существует")

    def log_out(self):
        if self.current_user:
            print("Вы успешно вышли из аккаунта!")
            self.current_user = None
            return self.current_user
        else:
            print("Вы и так не в аккаунте!")
            return self.current_user

    def add_video(self, title: str, duration: int, adult_mode: bool = False):
        video = Video(title, duration, adult_mode)
        self.videos.append(video)

    def search_videos(self, title: str):
        matches = []
        for video in self.videos:
            if title.lower() in video.title.lower():
                matches.append(video)

        return matches

    def watch_video(self, title: str):
        if not self.current_user:
            print("Для просмотра видео авторизируйтесь")
            return None

        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18-ти лет для просмотра")
                    return None
                while video.time_now < video.duration:
                    print(video.time_now + 1, end=' ')
                    video.time_now += 1

                print('Просмотр видео завершено!')
                video.time_now = 0
                return
        print("Такого видео не существует!")


urtube = Urtube()

urtube.add_video('Jimmy: The Movie', 4, True)
urtube.add_video('Jimmy 2: The Movie', 150)

matches = urtube.search_videos("Movie")
print("From Search:", [video.title for video in matches])

urtube.watch_video('Jimmy: The Movie')
current_user = urtube.register_user('jim', '123', 66)
urtube.watch_video('Jimmy: The Movie')
urtube.watch_video('Jimmy: The Movie')