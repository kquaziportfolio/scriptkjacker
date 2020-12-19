from .xor import xorencode,xordecode,xordecodepadded,randomstr
from faker import Faker
import random
faker=Faker("en_US")
def stuffjson(json):
    stuffed={}
    for i in range(random.randint(20,700)):
        key="".join(randomstr())
        while key in json.keys():
            key="".join(randomstr())
        val=faker.text()
        stuffed[key]=val
    json|=stuffed
    return json
