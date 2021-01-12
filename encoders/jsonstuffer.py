import base64
import random
import string

from faker import Faker

faker = Faker("en_US")


def randomstr(dictionary=string.printable, leng=10):
    a = []
    for i in range(leng):
        a.append(random.choice(dictionary))
    return a


def stuffjson(json):
    stuffed = {}
    for i in range(random.randint(20, 700)):
        key = "".join(randomstr())
        while key in json.keys():
            key = "".join(randomstr())
        val = faker.text()
        stuffed[key] = val
    for i in range(random.randint(20, 700)):
        key = "".join(randomstr())
        while key in json.keys():
            key = "".join(randomstr())
        val = faker.text()
        stuffed[key] = base64.b64encode(val.encode()).decode()
    json |= stuffed
    return json
