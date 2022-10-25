import pytest
from mimesis import Person, Address
from mimesis.random import Random
from selenium.webdriver import Firefox


@pytest.fixture(scope="function", autouse=True, name='driver')
def get_driver():
    driver = Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope="function", name='person')
def get_person():
    person = Person('ru')
    yield person


@pytest.fixture(scope="function", name='name')
def get_person_name(person):
    yield person.name()


@pytest.fixture(scope="function", name='surname')
def get_person_surname(person):
    yield person.surname()


@pytest.fixture(scope="function", name='phone')
def get_person_phone(person):
    yield person.telephone().replace('(', '').replace(')', '').replace('-', '').replace(' ', '')


@pytest.fixture(scope="function", name='address')
def get_person_address():
    address = Address('ru')
    full_address = f'{address.city()}, {address.street_name()}, {address.street_number()}'
    yield full_address


@pytest.fixture(scope="function", name='comment')
def get_person_comment(person):
    random = Random('ru')
    yield random.generate_string(str_seq='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', length=100)
