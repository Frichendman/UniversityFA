import os
import shutil


def create():
    n = str(input("Введите название создаваеммой папки: "))
    if not os.path.isdir(n):
        os.mkdir(n)
        main()
    else: print("Такая папка уже существует: ")


def delete():
    n = str(input("Введите название удаляемой папки: "))
    os.rmdir(n)
    main()


def move():
    n = str(input("Введите название куда хотите перейти: "))
    os.chdir(n)
    print("Вы перешли в: ", os.getcwd())
    main()


def createf():
    n = str(input("Введите название содаваемого файла: "))
    text_file = open(n, "w")
    main()
    

def addtxt():
    n = str(input("Введите название файла в который хотите написать: "))
    text_file = open(n, "w")
    k = str(input("Введите содержание нового файла: "))
    text_file.write(k)
    text_file.close()
    main()


def seef():
    n = str(input("Введите название для просмотра: "))
    text_file = open(n, "r")
    content = text_file.readlines() 
    print(content)
    text_file.close()
    main()


def deletef():
    n = str(input("Введите название файла который вы хотите удалить: "))
    os.remove(n)
    main()


def copyf():
    n = str(input("Введите название файла который хотите скопировать: "))
    k = str(input("Введите название нового файла: "))
    shutil.copy2(n,k)
    main()



def movef():
    n = str(input("Введите название файла который хотите переместить: "))
    n2 = str(input("Введите куда хотите преместить: "))
    os.replace(n, n2 + "/"+ n)
    main()


def rename():
    n = str(input("Введите название файла которого хотите переименовать: "))
    d = str(input("Введите новое название: "))
    os.rename(n, d)
    main()

def main():
    print("Это Файловый менеджер.  Для того чтобы начать надо написать одну из команд.\n Команды:\n1. Создать папку(ПапкаСоздать)\n2. Удалить папку(ПапкаУдалить)\n3. Переход по папкам(Переместиться)\n4. Создать файл(СоздатьФайл)\n"
                  '5. Записать текст в файл(Написать)\n6. Чтение из файла(Просмотр)\n7. Удалить файл(УдалитьФайл)\n8. Скопировать файл(СкопироватьФайл)\n'
                  '9. Переместить файл(ПереместитьФайл)\n10. Переименовать файл(Переименовать)\n11. Выход\n')
    a = str(input("Введите команду: "))

    while True:
        if a == 'ПапкаСоздать':
            create()
        elif a == 'ПапкаУдалить':
            delete()
        elif a == 'Переместиться':
            move()
        elif a == 'СоздатьФайл':
            createf()
        elif a == 'Написать':
            addtxt()
        elif a == 'Просмотр':
            seef()
        elif a == 'УдалитьФайл':
            deletef()
        elif a == 'СкопироватьФайл':
            copyf()
        elif a == 'ПереместитьФайл':
            movef()
        elif a == 'Переименовать':
            rename()
        elif a =='Выход':
            break
        else:
            print("Вы ввели неверную команду")
            main()

if __name__ == '__main__':
    main()

