class TxtFileHandler:
    """
    Класс для работы с текстовыми файлами. Имеет методы для чтения, записи и дополнения файлов.
    Атрибуты:
    filepath (str): Путь к файлу.
    
    """
    def __init__(self, filepath:str):
        self.filepath = filepath
    
    def __str__(self):
        return f"Путь к файлу: {self.filepath}"
    
    def read_file(self, filepath:str)->str:
        """
        Метод для чтения файла.
        Аргументы:
        filepath:str - Путь к файлу.
        Возвращает:
        Содержимое файла:str.
        
        """
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ""
        except PermissionError:
            print ("Нет прав на чтение файла")
        except:
            print("Неизвестная ошибка")
        
    def write_file(self, filepath:str, *data:str)->None:
        """
        Метод для записи в файл.
        Аргументы:
        filepath:str - Путь к файлу.
        data:str - Данные для записи в файл.
        """
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(*data)

    def append_file(self, filepath:str, data:str)->None:
        """
        Метод для добавления данных в файл.
        Аргументы:
        filepath:str - Путь к файлу.
        data:str - Данные для добавления в файл.
        """
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(data)

handler = TxtFileHandler("test.txt")
test_phrase = "Здравствуйте Владимир.\n"

def main():
    
    print(handler)
    #handler.write_file("test.txt", test_phrase)
    handler.append_file("test.txt", test_phrase)
    print(handler.read_file("test.txt"))

if __name__ == "__main__":
    main()