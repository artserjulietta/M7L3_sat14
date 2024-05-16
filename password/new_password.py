import random
import string

def new_generate_password(length=12, digits=True, special=True):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation

def generate_password(length=12):
    """Генерация случайного пароля заданной длины."""
    if length <= 0:
        return 'Пароль не может иметь такое количество символов'
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password


# Пример использования

password_length = 12  # Вы можете выбрать любую длину пароля
password = new_generate_password(password_length, digits=False, special=True)
print("Ваш новый пароль:", password)
