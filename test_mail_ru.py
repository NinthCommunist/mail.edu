import pytest
import math

'''
Пользователь вводит радиус окружности. Система проверяет больше ли площадь данной окружности 100?

'''

area = 100  # площадь должна быть меньше указанного значения


def area_circle(r):
    return math.pi * (r ** 2)


@pytest.mark.parametrize(
    "test_input,expected",
    [("area_circle(0)", area), ('area_circle(2.5555)', area),
     pytest.param("area_circle(5.645)", area, marks=pytest.mark.xfail)])  # Площадь больше 100
def test_areacircle(test_input, expected):
    assert eval(test_input) < expected


'''
Пользователь вводит фамилию ученика. Система выдает среднюю оценку ученика
'''

list_of_stedent = {'Иванов': 4.5, 'Петров': 4.8, 'Сидоров': 3.8}  # Фамилии учеников и их средние оценки


def get_assessment(surname):
    try:
        return list_of_stedent[surname]
    except KeyError:
        pass


def test_get_assessment():
    assert get_assessment('Иванов') == 4.5
    assert get_assessment('Петров') == 4.8
    assert get_assessment('Андреев') == None


'''
Пользователь вводит длину в сантиметрах. Система проверяет соответсвует ли длина целому числу дюймов
'''

inch = float(2.54)  # 1 дюйм = 2.54 см


def check_inch(lenght):
    return lenght % inch == 0


def test_check_inch():
    assert check_inch(5.08) == True
