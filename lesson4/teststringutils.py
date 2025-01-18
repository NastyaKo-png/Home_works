import pytest
from class_StringUtils import StringUtils

class TestStringUtils:

    def setup_method(self):
        """Настройка для каждого теста."""
        self.string_utils = StringUtils()

    def test_capitilize(self):
        """Тест функции capitilize."""
        assert self.string_utils.capitilize("skypro") == "Skypro"
        assert self.string_utils.capitilize("hello world") == "Hello world"
        assert self.string_utils.capitilize("123") == "123"

    def test_trim(self):
        """Тест функции trim."""
        assert self.string_utils.trim("   skypro") == "skypro"
        assert self.string_utils.trim(" hello world ") == "hello world "
        assert self.string_utils.trim("") == ""
        assert self.string_utils.trim(" ") == ""

    def test_to_list(self):
        """Тест функции to_list."""
        assert self.string_utils.to_list("a,b,c,d") == ['a', 'b', 'c', 'd']
        assert self.string_utils.to_list("1:2:3", ":") == ['1', '2', '3']
        assert self.string_utils.to_list("") == []
        assert self.string_utils.to_list("a,b,c,d", "-") == ['a', 'b', 'c', 'd']

    def test_contains(self):
        """Тест функции contains."""
        assert self.string_utils.contains("SkyPro", "S") == True
        assert self.string_utils.contains("SkyPro", "U") == False
        assert self.string_utils.contains("SkyPro", "y") == True
        assert self.string_utils.contains("", "S") == False

    def test_delete_symbol(self):
        """Тест функции delete_symbol."""
        assert self.string_utils.delete_symbol("SkyPro", "k") == "SyPro"
        assert self.string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
        assert self.string_utils.delete_symbol("SkyPro", "S") == "kyPro"
        assert self.string_utils.delete_symbol("SkyPro", "x") == "SkyPro"
        assert self.string_utils.delete_symbol("", "S") == ""

    def test_starts_with(self):
        """Тест функции starts_with."""
        assert self.string_utils.starts_with("SkyPro", "S") == True
        assert self.string_utils.starts_with("SkyPro", "P") == False
        assert self.string_utils.starts_with("SkyPro", "Sk") == True
        assert self.string_utils.starts_with("", "S") == False

    def test_end_with(self):
        """Тест функции end_with."""
        assert self.string_utils.end_with("SkyPro", "o") == True
        assert self.string_utils.end_with("SkyPro", "y") == False
        assert self.string_utils.end_with("SkyPro", "ro") == True
        assert self.string_utils.end_with("", "S") == False

    def test_is_empty(self):
        """Тест функции is_empty."""
        assert self.string_utils.is_empty("") == True
        assert self.string_utils.is_empty(" ") == True
        assert self.string_utils.is_empty("SkyPro") == False
        assert self.string_utils.is_empty("   ") == True

    def test_list_to_string(self):
        """Тест функции list_to_string."""
        assert self.string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
        assert self.string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
        assert self.string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
        assert self.string_utils.list_to_string([]) == ""
        assert self.string_utils.list_to_string([1]) == "1"
        assert self.string_utils.list_to_string(["a", "b", "c", "d"], " ") == "a b c d"
