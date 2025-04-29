def factorial_recursive(n):
    """
    Обчислює факторіал числа n рекурсивно.

    Аргументи:
        n (int): ціле невід’ємне число

    Повертає:
        int: факторіал числа n

    Викликає:
        ValueError: якщо n є від’ємним числом
        TypeError: якщо n не є цілим числом
    """
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом.")
    if n < 0:
        raise ValueError("Факторіал визначено лише для невід’ємних чисел.")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    """
    Обчислює n-те число Фібоначчі рекурсивно.

    Аргументи:
        n (int): ціле невід’ємне число

    Повертає:
        int: n-те число Фібоначчі

    Викликає:
        ValueError: якщо n є від’ємним числом
        TypeError: якщо n не є цілим числом
    """
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом.")
    if n < 0:
        raise ValueError("Числа Фібоначчі визначені лише для невід’ємних чисел.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Примітка: Рекурсивний підхід до Фібоначчі неефективний при великих n, бо обчислює одні й ті самі значення багато разів (експоненціальна складність O(2^n)). Ітеративні або мемоізовані версії значно ефективніші.


def sum_list_recursive(lst):
    """
    Обчислює суму елементів списку рекурсивно.

    Аргументи:
        lst (list): список чисел

    Повертає:
        float або int: сума елементів списку

    Викликає:
        TypeError: якщо аргумент не є списком або елементи не є числами
    """
    if not isinstance(lst, list):
        raise TypeError("Аргумент має бути списком.")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("Усі елементи списку мають бути числами.")
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])


def is_palindrome_recursive(s):
    """
    Рекурсивно перевіряє, чи є рядок паліндромом (ігноруючи пробіли, регістр і неалфанумеричні символи).

    Аргументи:
        s (str): вхідний рядок

    Повертає:
        bool: True, якщо рядок є паліндромом, False інакше

    Викликає:
        TypeError: якщо s не є рядком
    """
    if not isinstance(s, str):
        raise TypeError("Аргумент має бути рядком.")
    
    import re
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    if len(cleaned) <= 1:
        return True
    if cleaned[0] != cleaned[-1]:
        return False
    return is_palindrome_recursive(cleaned[1:-1])

# Факторіал
print(factorial_recursive(5))    
print(factorial_recursive(0))     

# Числа Фібоначчі
print(fibonacci_recursive(6))       
print(fibonacci_recursive(0))      
print(fibonacci_recursive(1))       
# Сума елементів списку
print(sum_list_recursive([1, 2, 3, 4, 5]))  
print(sum_list_recursive([]))             

# Перевірка паліндромів
print(is_palindrome_recursive("Радар"))          
print(is_palindrome_recursive("A man a plan a canal Panama"))  
print(is_palindrome_recursive("Hello"))             
