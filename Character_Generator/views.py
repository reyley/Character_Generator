import random
from django.shortcuts import render


def generate_view(request, region):
    if region == 'worldwide':
        traits = get_worldwide_statistics()
    elif region == 'usa':
        traits = get_usa_statistics()
    else:
        return render(request, 'index.html')
    return render(request, 'generate.html', {'traits': traits, 'region': region})


def get_worldwide_statistics():
    traits = [("Sex", generate_from_distribution(
        [("Female", 100),
         ("Male", 101)])),
        ("Vision", generate_from_distribution(
            [("Normal", 960),
             ("Impaired", 35),
             ("Blind", 5)])),
        ("Hearing", generate_from_distribution(
            [("Normal", 95),
             ("Deaf", 5)])),
        ("Handedness", generate_from_distribution(
            [("Right-handed", 89),
             ("Left-handed", 10),
             ("Ambidextrous", 1)]))]
    return traits


def get_usa_statistics():
    traits = [("Sex", generate_from_distribution(
        [("Female", 100),
         ("Male", 97)])),
        ("Race", generate_from_distribution(
            [("White", 637),
             ("Black", 122),
             ("Asian", 47),
             ("Hispanic/Latino", 164),
             ("Native American", 7),
             ("Native Hawaiian", 2),
             ("Mixed race", 19),
             ("Other (Too small to categorize)", 2)])),
        ("Vision", generate_from_distribution(
            [("Normal", 979),
             ("Impaired", 21)])),
        ("Hearing", generate_from_distribution(
            [("Normal", 98),
             ("Deaf", 2)])),
        ("Handedness", generate_from_distribution(
            [("Right-handed", 89),
             ("Left-handed", 10),
             ("Ambidextrous", 1)]))]
    return traits


def generate_from_distribution(distribution):
    total_sum = sum(value for trait, value in distribution)
    x = random.randrange(total_sum)
    index = 0
    partial_sum = distribution[0][1]
    while partial_sum <= x:
        index += 1
        partial_sum += distribution[index][1]
    return distribution[index][0]
