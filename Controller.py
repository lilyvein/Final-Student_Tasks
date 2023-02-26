from Model import Model
from View import View
from tkinter import messagebox, filedialog, INSERT


class Controller:

    def __init__(self):
        self.current_mixmatch = None
        self.model = Model()
        self.view = View(self, self.model)

    def main(self):
        self.view.main()

    def click_btn_open_file(self):
        self.view.tbx_students.delete('1.0', 'end')
        students = filedialog.askopenfilename(filetypes=(('text files', '*.txt'), ('All files', '*.*')))
        if students != '':  # Kui fail on tühi
            self.model.open_students_list(students)
            if len(self.model.students) > 0:
                for names in self.model.students:
                    self.view.tbx_students.insert(INSERT, names + '\n')
            else:
                messagebox.showwarning('Hoiatus!', 'Fail on tühi!')

    def click_btn_choose_file(self):
        # self.view.btn_choose_file['state'] = 'normal'
        self.view.tbx_tasks.delete('1.0', 'end')
        tasks = filedialog.askopenfilename(filetypes=(('text files', '*.txt'), ('All files', '*.*')))
        if tasks != '':
            self.model.open_file_tasks(tasks)
            if len(self.model.students) > len(self.model.tasks):
                messagebox.showerror('Error', 'Ülessandeid on vähem kui õpilasi.')
            else:
                for tasks in self.model.tasks:
                    self.view.tbx_tasks.insert(INSERT, tasks + '\n')

    def click_btn_mix(self):
        self.view.btn_mix['state'] = 'normal'
        self.model.result = []
        self.view.tbx_result.delete('1.0', 'end')
        self.model.shuffle_task()
        x = 0
        for name in self.model.students:
            self.view.tbx_result.insert(INSERT, name + '-' + self.model.tasks[x] + '\n')
            self.model.result.append(name + '-' + self.model.tasks[x])
            x += 1

    def click_btn_save(self):
        if len(self.model.result) != 0:
            result = filedialog.asksaveasfilename(
                filetypes=[('txt file', '.txt')],
                defaultextension='generated.txt',
                initialdir='D:\\my_data\\my_html\\')
            if result != "":
                with open(result, "a", encoding="utf'8") as f:
                    for save in self.model.result:
                        f.write(save + "\n")
        else:
            messagebox.showerror('Viga', 'Tabel on tühi, ei saa faili salvestada.')

    def click_btn_clear(self):
        self.view.tbx_students.delete('1.0', 'end')
        self.view.tbx_tasks.delete('1.0', 'end')
        self.view.tbx_result.delete('1.0', 'end')
        self.model.students = []
        self.model.tasks = []
        self.model.result = []
