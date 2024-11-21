team1_num = 5
team2_num = 6
score_2 = 42
team1_time = 18015.2
score_1 = 40
tasks_total = 82
time_avg = 45.2


exs1 = "В команде Мастера кода участников: %(team1_num)s!" % {'team1_num' :5}
print(exs1)

exs2 = "Итого сегодня в командах участников: %(team1_num)s, %(team2_num)s !" % {'team1_num' :5,'team2_num' :6}
print(exs2)

exs3 ="Команда Волшебники данных решила задач: {}!".format(score_2)
print(exs3)

exs4 = "Волшебники данных решили задачи за {}с!".format(team1_time)
print(exs4)

exs5 = f"Команды решили {score_1} и {score_2} задач"
print(exs5)

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

exs6 = f"Результат битвы:{challenge_result}"
print(exs6)

exs7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(exs7)


