import tkinter
from tkinter import *
import tkinter.font as tkfont


class View(Tk):

    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model

        # Font
        self.default_style = tkfont.Font(family='Arial', size=12)
        self.default_style_2 = tkfont.Font(family='Monotype Corsiva', size=25)

        # Window properties
        self.geometry('1400x800')
        self.title('Õpilaste ülesanded')
        self.center(self)

        # Frames
        self.frame_top, self.frame_bottom = self.create_two_frames()

        # Create all buttons
        self.btn_open_file, self.btn_choose_file, self.btn_mix, self.btn_save, self.btn_clear = self.create_all_buttons()
        self.lbl_students, self.lbl_tasks, self.lbl_result = self.create_all_labels()

        # Textbox
        self.tbx_students, self.tbx_tasks, self.tbx_result = self.create_textbox()

    def main(self):
        self.mainloop()

    @staticmethod
    def center(win):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def create_two_frames(self):
        frame_top = Frame(self, bg='#006d77', height=80)   # tume roheline
        frame_bottom = Frame(self, bg='#83c5be')  # sinakas roheline

        frame_top.pack(fill='both')
        frame_bottom.pack(expand=True, fill='both')

        return frame_top, frame_bottom

    def create_all_buttons(self):
        btn_open_file = Button(self.frame_top, text='Ava fail', font=self.default_style,
                               command=self.controller.click_btn_open_file)

        btn_choose_file = Button(self.frame_top, text='Vali ülesanded', font=self.default_style,
                                 command=self.controller.click_btn_choose_file)

        btn_mix = Button(self.frame_top, text='Sega ülesanded', font=self.default_style,
                         command=self.controller.click_btn_mix)

        btn_save = Button(self.frame_bottom, text='Salvesta fail', font=self.default_style,
                          command=self.controller.click_btn_save)

        btn_clear = Button(self.frame_bottom, text='Puhasta', font=self.default_style,
                           command=self.controller.click_btn_clear)

        btn_open_file.grid(row=2, column=0, padx=50, pady=5, sticky=EW)
        btn_choose_file.grid(row=2, column=1, padx=100, pady=5, sticky=EW)
        btn_mix.grid(row=2, column=5, padx=250, pady=5, sticky=EW)

        btn_save.place(x=1160, y=600)
        btn_clear.place(x=800, y=600)

        return btn_open_file, btn_choose_file, btn_mix, btn_save, btn_clear

    def create_all_labels(self):
        lbl_students = Label(self.frame_top, text='Õpilaste nimed', font=self.default_style_2, fg='#edf6f9', bg='#006d77')
        lbl_tasks = Label(self.frame_top, text='Ülesanded õpilastele', font=self.default_style_2, fg='#edf6f9', bg='#006d77')
        lbl_result = Label(self.frame_top, text='Tulemus', font=self.default_style_2, fg='#edf6f9', bg='#006d77')

        lbl_students.grid(row=1, column=0, sticky=EW, padx=25, pady=6)
        lbl_tasks.grid(row=1, column=1, sticky=EW, padx=100, pady=6)
        lbl_result.grid(row=1, column=5, sticky=EW, padx=25, pady=6)

        return lbl_students, lbl_tasks, lbl_result

    def create_textbox(self):
        tbx_students = tkinter.Text(self.frame_bottom, height=35, width=30, bg='white')
        tbx_tasks = tkinter.Text(self.frame_bottom, height=35, width=55, bg='white')
        tbx_result = tkinter.Text(self.frame_bottom, height=35, width=65, bg='white')

        tbx_students.grid(row=0, column=0, padx=10, pady=20)
        tbx_tasks.grid(row=0, column=1, padx=10, pady=20)
        tbx_result.grid(row=0, column=2, padx=10, pady=20)

        return tbx_students, tbx_tasks, tbx_result
