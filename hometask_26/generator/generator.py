import random

from hometask_26.data.data import User
from faker import Faker


faker_en = Faker('en-US')
Faker.seed()


def generated_data():
    yield User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        gender=random.choice(['male', 'female']),
        status=random.choice(['active', 'inactive'])
    )
    