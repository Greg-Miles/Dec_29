class TxtFileHandler():
    def __init__(self, file_path:str):
        self.file_path = file_path
    
    def __str__(self):
        return f"Путь к файлу: {self.file_path}"
    
    def read_file(self)->str:
        """
        Метод для чтения файла.
        
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.read()
        except: 
            if FileNotFoundError:
                return ""
            elif PermissionError:
                return "Нет прав на чтение файла"
            else:
                return "Неизвестная ошибка"
        
    def write_file(self, data:str)->None:
        """
        Метод для записи в файл.
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write(data)

    def append_file(self, data:str)->None:
        """
        Метод для добавления данных в файл.
        """
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(data)

handler = TxtFileHandler("test.txt")
test_phrase = "Здравствуйте Владимир.\n"

def main():
    print(handler.read_file())
    print(handler)
    handler.write_file(test_phrase)
    handler.append_file(test_phrase)

if __name__ == "__main__":
    main()