import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
# from tkinter import *
import requests

# 視窗設定
windows = tk.Tk()
windows.geometry("600x300")
var = tk.StringVar()
varSearchData01 = tk.StringVar()
varSearchData02 = tk.StringVar()
varSearchData03 = tk.StringVar()
varSearchData04 = tk.StringVar()
varSearchData05 = tk.StringVar()
varSearchData06 = tk.StringVar()
varSearchData07 = tk.StringVar()

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


# FunctionArea
def get_input_text():
    if inputTextField.get() == "":
        tk.messagebox.showerror(messageboxTitle, errorMessage)
    else:
        dataListaa = get_api(inputTextField.get())

# TODO 實作處理跌代問題 把所有資料完整顯示出來
# 抓取Covid19 API
def get_api(conname):
    r = requests.get(
        "https://covid-19.nchc.org.tw/api/covid19?CK=covid-19@nchc.org.tw&querydata=5001&limited=" + conname + "")
    dataList = r.json()

    for i in dataList:
        varSearchData01.set(i["id"])
        varSearchData02.set(i["a01"])
        varSearchData03.set(i["a02"])
        varSearchData04.set(i["a03"])
        varSearchData05.set(i["a04"])
        varSearchData06.set(i["a05"])
        varSearchData07.set(i["a06"])

        print(i["id"], i["a01"], i["a02"], i["a03"], i["a04"], i["a05"], i["a06"])


# DisplayText
buttonText: str = "搜尋"
titleLabelText: str = "請選擇縣市名稱:"
messageboxTitle: str = "message"
errorMessage: str = "請輸入縣市名稱"

# HostInfo
databasePath: str = "//10.152.110.2/pcinfo/INPCTW-PCIESSDCN.html"
databaseIP: str = "10.152.110.2"


# View
titleLabelTextLabel = tk.Label(windows, text=titleLabelText)
inputTextField = ttk.Combobox(windows, values=dataArray)
searchButton = tk.Button(windows, text=buttonText, height=1, command=get_input_text)
displayTextLabel01 = tk.Label(windows, textvariable=varSearchData01)
displayTextLabel02 = tk.Label(windows, textvariable=varSearchData02)
displayTextLabel03 = tk.Label(windows, textvariable=varSearchData03)
displayTextLabel04 = tk.Label(windows, textvariable=varSearchData04)
displayTextLabel05 = tk.Label(windows, textvariable=varSearchData05)
displayTextLabel06 = tk.Label(windows, textvariable=varSearchData06)
displayTextLabel07 = tk.Label(windows, textvariable=varSearchData07)


titleLabelTextLabel.place(x=10, y=15)
inputTextField.place(x=120, y=15)
searchButton.place(x=300, y=10)
displayTextLabel01.place(x=0, y=40)
displayTextLabel02.place(x=100, y=40)
displayTextLabel03.place(x=200, y=40)
displayTextLabel04.place(x=300, y=40)
displayTextLabel05.place(x=400, y=40)
displayTextLabel06.place(x=500, y=40)
displayTextLabel07.place(x=600, y=40)

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
