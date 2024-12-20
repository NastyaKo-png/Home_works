class StringUtils:
    """Класс с полезными утилитами для обработки и анализа строк."""

    def capitilize(self, string: str) -> str:
        """Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст.

        Args:
            string: Строка для обработки.

        Returns:
            Строка с заглавной первой буквой.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.capitilize("skypro")
            'Skypro'
        """
        return string.capitalize()

    def trim(self, string: str) -> str:
        """Принимает на вход текст и удаляет пробелы в начале, если они есть.

        Args:
            string: Строка для обработки.

        Returns:
            Строка без пробелов в начале.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.trim("   skypro")
            'skypro'
        """
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def to_list(self, string: str, delimeter=",") -> list[str]:
        """Принимает на вход текст с разделителем и возвращает список строк.

        Args:
            string: Строка для обработки.
            delimeter: Разделитель строк. По умолчанию запятая (",").

        Returns:
            Список строк.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.to_list("a,b,c,d")
            ['a', 'b', 'c', 'd']
            >>> string_utils.to_list("1:2:3", ":")
            ['1', '2', '3']
        """
        if self.is_empty(string):
            return []

        return string.split(delimeter)

    def contains(self, string: str, symbol: str) -> bool:
        """Возвращает True, если строка содержит искомый символ и False - если нет.

        Args:
            string: Строка для обработки.
            symbol: Искомый символ.

        Returns:
            True, если строка содержит символ, False - если нет.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.contains("SkyPro", "S")
            True
            >>> string_utils.contains("SkyPro", "U")
            False
        """
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        """Удаляет все подстроки из переданной строки.

        Args:
            string: Строка для обработки.
            symbol: Искомый символ для удаления.

        Returns:
            Строка без символа.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.delete_symbol("SkyPro", "k")
            'SyPro'
            >>> string_utils.delete_symbol("SkyPro", "Pro")
            'Sky'
        """
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string

    def starts_with(self, string: str, symbol: str) -> bool:
        """Возвращает True, если строка начинается с заданного символа и False - если нет.

        Args:
            string: Строка для обработки.
            symbol: Искомый символ.

        Returns:
            True, если строка начинается с символа, False - если нет.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.starts_with("SkyPro", "S")
            True
            >>> string_utils.starts_with("SkyPro", "P")
            False
        """
        return string.startswith(symbol)

    def end_with(self, string: str, symbol: str) -> bool:
        """Возвращает True, если строка заканчивается заданным символом и False - если нет.

        Args:
            string: Строка для обработки.
            symbol: Искомый символ.

        Returns:
            True, если строка заканчивается символом, False - если нет.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.end_with("SkyPro", "o")
            True
            >>> string_utils.end_with("SkyPro", "y")
            False
        """
        return string.endswith(symbol)

    def is_empty(self, string: str) -> bool:
        """Возвращает True, если строка пустая и False - если нет.

        Args:
            string: Строка для проверки.

        Returns:
            True, если строка пуста, False - если нет.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.is_empty("")
            True
            >>> string_utils.is_empty(" ")
            True
            >>> string_utils.is_empty("SkyPro")
            False
        """
        string = self.trim(string)
        return string == ""

    def list_to_string(self, lst: list, joiner=", ") -> str:
        """Преобразует список элементов в строку с указанным разделителем.

        Args:
            lst: Список элементов.
            joiner: Разделитель элементов в строке. По умолчанию запятая (", ").

        Returns:
            Строка из элементов списка с разделителем.

        Examples:
            >>> string_utils = StringUtils()
            >>> string_utils.list_to_string([1, 2, 3, 4])
            '1, 2, 3, 4'
            >>> string_utils.list_to_string(["Sky", "Pro"])
            'Sky, Pro'
            >>> string_utils.list_to_string(["Sky", "Pro"], "-")
            'Sky-Pro'
        """
        string = ""
        length = len(lst)

        if length == 0:
            return string

        for i in range(0, length - 1):
            string += str(lst[i]) + joiner

        return string + str(lst[-1])
