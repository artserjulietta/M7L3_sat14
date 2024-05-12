import random
import string

def generate_password(length=12, digits=True, special=True):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters
    if digits:
        characters += string.digits
    if special:
        characters += string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

# Пример использования
password_length = 12  # Вы можете выбрать любую длину пароля
password = generate_password(password_length, digits=False, special=True)
print("Ваш новый пароль:", password)
