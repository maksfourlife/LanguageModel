from Model import Model

commands = ["help", "h", "load", "l", "save", "s", "generate", "g", "fit", "f", "quit", "q", "words", "w"]
args_err = "Пожалуйста, укажите аргументы"

class CommandCaller():
    @staticmethod
    def get_args(command: str):
        if not command:
            return False
        return command.split()

    @staticmethod
    def execute(args: list, model: Model):
        args_len = len(args)
        if not args_len:
            print("Пожалуйства, введите команду. Для получения документации введите help/h")
            return
        if not args[0] in commands:
            print("Пожалуйста, введите корректную коммандую. Для получения документации введите help/h")
            return
        if args[0] == "help" or args[0] == "h":
            print("Список комманд:\n\thelp/h - Получить документации\n\tload/l [путь к файлу + имя файла] - Загрузить модель из файла\n\tsave/s [путь к файлу + имя файла] - Сохранить модель в файл\n\tgenerate/g [стартовое слово] [длина последовательности] [??? путь к файлу + имя файла] - Генеация текста. Если указан третий параметр, запись текста в файл\n\tfit/f [путь к файлу + имя файла] [??? длина считывания] - Чтение файла и создания модели. Если указан второй параметр, то будет прочитано n-ое количество слов\n\twords / w - Список известных слов\n\tquit/q - Выход")
        elif args[0] == "load" or args[0] == "l":
            if args_len != 2:
                print(args_err)
                return
            model.load(args[1])
            return
        elif args[0] == "save" or args[0] == "s":
            if args_len != 2:
                print(args_err)
                return
            model.save(args[1])
        elif args[0] == "generate" or args[0] == "g":
            if args_len != 3 and args_len != 4:
                print(args_err)
                return
            try:
                seq_len = int(args[2])
            except Exception:
                print("Второй параметр должен являться числом")
                return
            if args_len == 3:
                print(model.generate(args[1], seq_len))
                return
            else:
                with open(args[3], "w") as f:
                    f.write(model.generate(args[1], seq_len))
                return
        elif args[0] == "fit" or args[0] == "f":
            if args_len != 2 and args_len != 3:
                print(args_err)
                return
            try:
                with open(args[1], "r") as f:
                    read_len = -1
                    if args_len == 3:
                        try:
                            read_len = int(args[2])
                        except FileNotFoundError:
                            print("Второй параметр должен являться числом")
                            return
                    if read_len != -1:
                        model.fit(f.read(read_len))
                    else:
                        print("here")
                        model.fit(f.read())
                    return
            except FileNotFoundError:
                print("Не удалось найти файл")
        elif args[0] == "quit" or args[0] == "q":
            return exit(0)
        elif args[0] == "words" or args[0] == "w":
            print(*model.words())
            return