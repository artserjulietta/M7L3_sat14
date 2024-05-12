import random
import string


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
password_length = 12
# password_length = int(input('Введите желаемую длину пароля: '))
print("Ваш новый пароль:", generate_password(password_length))
