import numpy as np
from numpy import random


def random_predict(number: int=1) -> int:
    """Рандомно загадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно\
            загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток
    """
    
    count = 0 # Счетчик числа попыток
    limit_min = 0 # Минимальное значение диапазона, в котором загадывается число
    limit_max = 101 # Максимальное значение диапазона, в котором загадывается число
    number_count = 0 # Переменная для промежуточных вычислений
    
    number = np.random.randint(limit_min, limit_max) # Компьютер загадывает число
       
    while number_count != number: # Сравниваем загаданное число с расчетной \
                                  # переменной
        count += 1 # Увеличиваем счетчик на 1
        number_count = round((limit_min+limit_max) / 2) # Вычисляем среднее \
                                                    # арифметическое диапазона
        if number < number_count:
            limit_max = number_count # Если загаданное число меньше среднего \
                                     # значения диапазона, то приравниваем \
                                     # максимальное значение к среднему
        
        elif number > number_count:
            limit_min = number_count # Если загаданное число больше среднего \
                                     # значения диапазона, то приравниваем \
                                     # минимальное значение к среднему
            
    return count
  
     
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш 
    алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # Список для сохранения количества попыток
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # Находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)