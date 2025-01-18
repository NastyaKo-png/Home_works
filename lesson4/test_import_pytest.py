import pytest
from StringUtils import StringUtils

# Создаем экземпляр класса
utils = StringUtils()

# Тесты для capitilize
def test_capitilize_positive():
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("Hello") == "Hello"
    assert utils.capitilize("123") == "123"
    assert utils.capitilize("") == ""

def test_capitilize_negative():
    with pytest.raises(TypeError):
        utils.capitilize(123)


# Тесты для trim
def test_trim_positive():
    assert utils.trim("   hello") == "hello"
    assert utils.trim("\t\n world") == "world" # различные типы пробелов
    assert utils.trim("hello ") == "hello " # пробел в конце строки
    assert utils.trim("hello") == "hello" # строка без пробелов
    assert utils.trim("") == "" # пустая строка


def test_trim_negative():
    with pytest.raises(TypeError):
        utils.trim(123)


# Тесты для to_list
def test_to_list_positive():
    assert utils.to_list("apple,banana,cherry") == ["apple", "banana", "cherry"]
    assert utils.to_list("1;2;3", ";") == ["1", "2", "3"]
    assert utils.to_list("single") == ["single"] # строка без разделителей
    assert utils.to_list("") == [] # пустая строка


def test_to_list_negative():
    with pytest.raises(TypeError):
        utils.to_list(123)


# Тесты для contains
def test_contains_positive():
    assert utils.contains("hello", "l") is True
    assert utils.contains("world", "o") is True
    assert utils.contains("123", "2") is True

def test_contains_negative():
    assert utils.contains("hello", "z") is False
    assert utils.contains("", "a") is False # пустая строка
    with pytest.raises(TypeError):
        utils.contains(123, "a") # Некорректный тип данных


# Тесты для delete_symbol
def test_delete_symbol_positive():
    assert utils.delete_symbol("hello", "l") == "heo"
    assert utils.delete_symbol("world", "o") == "wrld"
    assert utils.delete_symbol("12345", "3") == "1245"
    assert utils.delete_symbol("hello", "") == "hello" # пустой символ


def test_delete_symbol_negative():
    assert utils.delete_symbol("hello", "z") == "hello" # символ отсутствует
    assert utils.delete_symbol("", "a") == "" # пустая строка
    with pytest.raises(TypeError):
        utils.delete_symbol(123, "a") # Некорректный тип данных



# Тесты для starts_with
def test_starts_with_positive():
    assert utils.starts_with("hello", "h") is True
    assert utils.starts_with("World", "W") is True
    assert utils.starts_with("123", "1") is True

def test_starts_with_negative():
    assert utils.starts_with("hello", "w") is False
    assert utils.starts_with("", "a") is False # пустая строка
    with pytest.raises(TypeError):
        utils.starts_with(123, "a") # Некорректный тип данных


# Тесты для ends_with
def test_ends_with_positive():
    assert utils.end_with("hello", "o") is True
    assert utils.end_with("World", "d") is True
    assert utils.end_with("123", "3") is True

def test_ends_with_negative():
    assert utils.end_with("hello", "l") is False
    assert utils.end_with("", "a") is False # пустая строка
    with pytest.raises(TypeError):
        utils.end_with(123, "a") # Некорректный тип данных


# Тесты для is_empty
def test_is_empty_positive():
    assert utils.is_empty("") is True
    assert utils.is_empty("   ") is True # только пробелы

def test_is_empty_negative():
    assert utils.is_empty("hello") is False
    assert utils.is_empty("123") is False
    with pytest.raises(TypeError):
        utils.is_empty(123) # Некорректный тип данных


def test_list_to_string_empty():
    assert utils.list_to_string([]) == ""

def test_list_to_string_single_element():
    assert utils.list_to_string([1]) == "1"
    assert utils.list_to_string(["a"]) == "a"

def test_list_to_string_multiple_elements():
    assert utils.list_to_string([1, 2, 3]) == "1, 2, 3"
    assert utils.list_to_string(["apple", "banana", "cherry"]) == "apple, banana, cherry"

def test_list_to_string_custom_joiner():
    assert utils.list_to_string([1, 2, 3], "; ") == "1; 2; 3"
    assert utils.list_to_string(["apple", "banana", "cherry"], "-") == "apple-banana-cherry"

def test_list_to_string_mixed_types():
    assert utils.list_to_string([1, "a", 2.5]) == "1, a, 2.5"

def test_list_to_string_negative():
    with pytest.raises(TypeError):
        utils.list_to_string(123) # Некорректный тип данных

print ("finish")