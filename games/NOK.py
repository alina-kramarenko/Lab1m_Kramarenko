import math
import random

game_name = "Find the smallest common multiple of given numbers."


def play():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    answer = math.lcm(*numbers)
    return question, answer