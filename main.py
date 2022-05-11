import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from tkinter import *
import requests

# 視窗設定
windows = tk.Tk()
windows.geometry("400x300")
var = tk.StringVar()
varSearchData = tk.StringVar()

# Database
dataArray: [str] = [
    "桃園市",
    "台北市",
    "新北市",
    "彰化縣",
    "員林市",
    "新竹縣",
    "基隆市"
]


def get_api(conmane):
    # 抓取Covid19 API
    r = requests.get(
        "https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=5001&limited=" + conmane + "")
    dataList = r.json()

    for i in dataList:
        print(i["id"], i["a01"], i["a02"], i["a03"], i["a04"], i["a05"], i["a06"], i["a07"])


# DisplayText
buttonText: str = "搜尋"
titleLabelText: str = "請輸入軟體名稱:"
messageboxTitle: str = "message"
errorMessage: str = "請輸入軟體名稱"

# HostInfo
databasePath: str = "//10.152.110.2/pcinfo/INPCTW-PCIESSDCN.html"
databaseIP: str = "10.152.110.2"


# FunctionArea
def get_input_text():
    if inputTextField.get() == "":
        tk.messagebox.showerror(messageboxTitle, errorMessage)
    else:
        varSearchData.set(inputTextField.get())
        get_api(inputTextField.get())
        # canvas.forget()


# View
titleLabelTextLabel = tk.Label(windows, text=titleLabelText)
inputTextField = ttk.Combobox(windows, values=dataArray)
searchButton = tk.Button(windows, text=buttonText, height=1, command=get_input_text)
displayTextLabel = tk.Label(windows, textvariable=varSearchData)

titleLabelTextLabel.place(x=10, y=15)
inputTextField.place(x=120, y=15)
searchButton.place(x=300, y=10)
displayTextLabel.place(x=10, y=40)

# searchData
testText = pd.read_html(databasePath)

# databasePathFor testText in varSearchData:

# print(testText)

# 圖片顯示隱藏
# canvas = Canvas(windows, width=300, height=300)
# canvas.pack()
# img = PhotoImage(file="C:/Users/fred.fu/Desktop/aaaa.png")
# canvas.create_image(150, 200, image=img)

windows.mainloop()
