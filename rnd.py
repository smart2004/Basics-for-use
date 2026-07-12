import random

print(random.random())
print(random.randint(10, 100000))
print(random.choices('april'))
print(random.choice('august'))
print(random.betavariate(1, 10))

x = list('yamaika')
random.shuffle(x)
print(x)

print(random.seed(8, 4))

print(random.randrange(10))
print(random.randrange(5, 11))
print(random.randrange(0, 11, 2))

letters = 'abcdefg'
print(random.sample(letters, 3))
numbers = range(1, 11)
print(random.sample(numbers, 2))

# Сохраняем текущее состояние генератора
state = random.getstate()
# ... (выполняем другие операции с random)
# Восстанавливаем состояние
random.setstate(state)

print(random.randint(1, 10))

print(random.randint(1, 100))
print(random.random())

random.seed(42)
print(random.randint(1, 100))
print(random.random())

random.seed()
print(random.randint(1, 100))

def generate_random_numbers(n):
    random.seed(100)
    return [random.randint(1, 100) for _ in range(n)]

print(generate_random_numbers(5))
print(generate_random_numbers(5)) 
