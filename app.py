from Model import Model
from CommandCaller import CommandCaller

def main():
    model = Model()
    while 1:
        print("Комманда >>> ", end="")
        args = CommandCaller.get_args(input())
        CommandCaller.execute(args, model)


if __name__ == "__main__":
    main()