import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file if line.strip()]
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Введите новую задачу: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Задача добавлена: '{task}'")
    else:
        print("Задача не может быть пустой.")

def view_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    
    print("\n=== Ваши задачи ===")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("===================\n")

def delete_task(tasks):
    if not tasks:
        print("Список задач пуст. Нечего удалять.")
        return
    
    view_tasks(tasks)
    
    try:
        number = int(input("Введите номер задачи для удаления: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Задача удалена: '{removed}'")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите число.")

def show_menu():
    print("\n=== МЕНЮ ===")
    print("1. Посмотреть задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выйти")
    print("==============")

def main():
    tasks = load_tasks()
    print("Добро пожаловать в To-Do List!")
    
    while True:
        show_menu()
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
