import requests
from bs4 import BeautifulSoup
from bases import urls_set
import pandas as pd
import os
try:
    import tkinter
    from tkinter import messagebox
except:
    pass


class core():
    def __init__(self):
        pass

    def get_bacen_data(data1, data2, currency, option):
        try:
            url = urls_set.bacen_get_url.replace(
                "ii/ii/iiii", data1).replace("ff/ff/ffff", data2).replace("XX", currency)
            content = requests.get(url, allow_redirects=True).content
            with open("temp_csv.csv", "wb") as temp_file:
                temp_file.write(content)
            if option == 1:
                pd.read_csv("temp_csv.csv", delimiter=";").to_clipboard()
                os.remove("temp_csv.csv")
            elif option == 2:
                pd.read_csv(requests.get(
                    "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVTodasAsMoedas&id=60888").content).to_clipboard()
            
            
            
            else:
                messagebox.showwarning("Erro!", "Selecione algo!")
        except:
            messagebox.showwarning("Algo deu errado. Por favor, verifique as datas!")