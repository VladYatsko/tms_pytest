from page_object.data.data import Email
from faker import Faker


faker_en = Faker('en-US')
Faker.seed()


def generated_data():
    yield Email(
        email=faker_en.email(),
        password=faker_en.password()
    )
    