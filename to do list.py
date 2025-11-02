import csv
from enum import Enum

class Priority(Enum):
    HIGH = "بالا"
    MEDIUM = "متوسط"
    LOW = "پایین"

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
    
    def __str__(self):
        return f"نام: {self.name} | توضیحات: {self.description} | اولویت: {self.priority.value}"
    
    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'priority': self.priority.name
        }

class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print("کار با موفقیت اضافه شد.")
    
    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print(f"کار '{task_name}' با موفقیت حذف شد.")
                return
        print(f"کار با نام '{task_name}' یافت نشد.")
    
    def view_tasks(self):
        if not self.tasks:
            print("لیست کارها خالی است.")
            return
        
        print("\nلیست کارها:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
    
    def save_to_csv(self, filename="todo_list.csv"):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'description', 'priority'])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())
        print(f"لیست کارها در فایل '{filename}' ذخیره شد.")
    
    def load_from_csv(self, filename="todo_list.csv"):
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.tasks = []
                for row in reader:
                    priority = Priority[row['priority']]
                    self.tasks.append(Task(row['name'], row['description'], priority))
            print(f"لیست کارها از فایل '{filename}' بارگذاری شد.")
        except FileNotFoundError:
            print(f"فایل '{filename}' یافت نشد. یک لیست جدید ایجاد شد.")
        except Exception as e:
            print(f"خطا در بارگذاری فایل: {e}")

def display_menu():
    print("\nمنوی مدیریت لیست کارها:")
    print("1. اضافه کردن کار جدید")
    print("2. حذف کار")
    print("3. مشاهده لیست کارها")
    print("4. ذخیره لیست در فایل")
    print("5. بارگذاری لیست از فایل")
    print("6. خروج")

def get_priority_input():
    print("\nسطح اولویت:")
    for i, priority in enumerate(Priority, 1):
        print(f"{i}. {priority.value}")
    
    while True:
        try:
            choice = int(input("لطفاً عدد مربوط به اولویت را انتخاب کنید: "))
            if 1 <= choice <= len(Priority):
                return list(Priority)[choice-1]
            else:
                print("عدد وارد شده معتبر نیست. لطفاً مجدداً تلاش کنید.")
        except ValueError:
            print("لطفاً یک عدد وارد کنید.")

def main():
    todo_list = ToDoList()
    
    while True:
        display_menu()
        choice = input("لطفاً عدد مربوط به عملیات مورد نظر را انتخاب کنید: ")
        
        if choice == '1':
            name = input("نام کار: ")
            description = input("توضیحات کار: ")
            priority = get_priority_input()
            task = Task(name, description, priority)
            todo_list.add_task(task)
        
        elif choice == '2':
            if not todo_list.tasks:
                print("لیست کارها خالی است.")
                continue
            task_name = input("نام کاری که می‌خواهید حذف کنید: ")
            todo_list.remove_task(task_name)
        
        elif choice == '3':
            todo_list.view_tasks()
        
        elif choice == '4':
            filename = input("نام فایل برای ذخیره (پیش‌فرض: todo_list.csv): ") or "todo_list.csv"
            todo_list.save_to_csv(filename)
        
        elif choice == '5':
            filename = input("نام فایل برای بارگذاری (پیش‌فرض: todo_list.csv): ") or "todo_list.csv"
            todo_list.load_from_csv(filename)
        
        elif choice == '6':
            print("خروج از برنامه...")
            break
        
        else:
            print("گزینه نامعتبر. لطفاً عدد بین 1 تا 6 را انتخاب کنید.")

if __name__ == "__main__":
    main()