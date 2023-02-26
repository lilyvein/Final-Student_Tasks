import random


class Model:

    def __init__(self):
        self.students = []
        self.tasks = []
        self.result = []

    def open_students_list(self, filename):
        self.students = []
        with open(filename, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()
            for name in all_lines:
                name = name.strip()
                self.students.append(name)

    def open_file_tasks(self, filename):
        self.tasks = []
        with open(filename, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()
            for task in all_lines:
                task = task.strip()
                self.tasks.append(task)

    def shuffle_task(self):
        random.shuffle(self.tasks)
