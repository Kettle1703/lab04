import random
from lib import returnMatches


def random_testing():
    for _ in range(1000):
        result_count = random.randint(0, 5)
        common = random.randint(-10, 10)
        counter = common + 1
        count_list = random.randint(2, 17)
        plenty = []
        for _ in range(count_list):
            length = random.randint(result_count + 1, 13)
            element = []
            for _ in range(result_count):
                element.append(common)
            for _ in range(length - result_count):
                element.append(counter)
                counter += 1
            random.shuffle(element)
            plenty.append(element)

        if result_count != returnMatches(*plenty):
            return False
    return True


print(f'\nСтохастическое тестирование. Результат - {random_testing()}')