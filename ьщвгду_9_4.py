import random

first = 'Мама мыла раму'
second ='Рамена мало было'
k = list(map(lambda x,y:x == y, first, second))
print(k)


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a', encoding = 'utf-8') as file:
            for i in data_set:
                file.write(f'{i}\n')
    return write_everything

m = get_advanced_writer('t.txt')
print(m('Это строчка', ['А', 'это', 5]))


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

ball_1 =  MysticBall('аверс', 'реверс', 'ребро', 'зависла в воздухе')
print(ball_1())
print(ball_1())
print(ball_1())
