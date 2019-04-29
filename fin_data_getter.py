from tkinter import *
from tkinter import ttk
from bases import urls_set
import datetime
import time
from brain import core



class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title("Financial Tool for Brazilian Humans Beings" +
                        " "*37 + "By github.com/marcelo-franceschini")
        self.root.resizable(width=False, height=False)

        self.bacen_date1 = (datetime.datetime.now() -
                            datetime.timedelta(days=-30)).strftime(r"%d/%m/%Y")
        self.bacen_date2 = datetime.datetime.now().strftime(r"%d/%m/%Y")

        self.bmf_date = (datetime.datetime.now() -
                         datetime.timedelta(days=-5)).strftime(r"%d/%m/%Y")

        # Bacen
        self.bacen_rb_var = IntVar()
        self.bacen_frame = LabelFrame(
            self.root, text="Bacen - Cotações e Boletins")
        self.bacen_combobox = ttk.Combobox(self.bacen_frame,
                                           values=list(urls_set.bacen_urls.keys()))
        self.bacen_rb1 = Radiobutton(self.bacen_frame,
                                     text="Cotações de fechamento de uma moeda em um período. ",
                                     value=1,
                                     variable=self.bacen_rb_var)
        self.bacen_rb2 = Radiobutton(self.bacen_frame,
                                     text="Cotações de fechamento de todas as moedas em uma data. ",
                                     value=2,
                                     variable=self.bacen_rb_var)
        self.bacen_data_label1 = Label(self.bacen_frame, text="Data Inicial: ")
        self.bacen_data_label2 = Label(self.bacen_frame, text="Data Final: ")
        self.bacen_data_1 = Entry(self.bacen_frame)
        self.bacen_data_1.insert(0, self.bacen_date2)
        self.bacen_data_2 = Entry(self.bacen_frame)
        self.bacen_data_2.insert(0, self.bacen_date1)
        self.bacen_button = Button(self.bacen_frame,
                                   text="Exportar para Excel",
                                   command=lambda: core.get_bacen_data(option=self.bacen_rb_var.get(), data1=self.bacen_data_1.get(),
                                                                       data2=self.bacen_data_2.get(),
                                                                       currency=str(urls_set.bacen_urls[self.bacen_combobox.get()])))

        # BMF
        self.bmf_frame = LabelFrame(
            self.root, text="BM&F - Taxas Referenciais")
        self.bmf_combobox = ttk.Combobox(
            self.bmf_frame, values=list(urls_set.bmf_options.keys()))
        self.bmf_data_label = Label(self.bmf_frame, text="Data: ")
        self.bmf_button = Button(self.bmf_frame, text="Exportar para Excel")
        self.bmf_data_entry = Entry(self.bmf_frame)
        self.bmf_data_entry.insert(0, self.bmf_date)

    def run_it(self):
        self.bacen_frame.grid(column=0, row=0, ipady = 8)
        self.bacen_rb1.grid(column=0, row=1, sticky="w")
        self.bacen_rb2.grid(column=0, row=2, sticky="w")

        self.bacen_data_label1.grid(column=1, row=1, sticky="w")
        self.bacen_data_label2.grid(column=1, row=2, sticky="w")
        self.bacen_data_1.grid(column=2, row=1)
        self.bacen_data_2.grid(column=2, row=2)
        self.bacen_combobox.grid(column=0, row=3, ipadx=100)
        self.bacen_combobox.current(53)
        self.bacen_button.grid(column=2, row=3)

        self.bmf_frame.grid(column=1, row=0, sticky="nw")
        self.bmf_combobox.pack()
        self.bmf_combobox.current(0)
        self.bmf_data_label.pack()
        self.bmf_data_entry.pack()
        self.bmf_button.pack()

        self.root.mainloop()


voidmain = GUI()
voidmain.run_it()
