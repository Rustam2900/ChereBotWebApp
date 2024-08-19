from aiogram.fsm.state import StatesGroup, State


class RegisterFormUser(StatesGroup):
    CHOOSE_LANGUAGE = State()
    NAME = State()


class RegisterForm(StatesGroup):
    company_name = State()
    company_employee_name = State()
    company_contact = State()
    employee_number = State()
    lifetime = State()


class RegisterFormUserBot(StatesGroup):
    name = State()
    contact = State()
    add_contact = State()
