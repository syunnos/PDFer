import tkinter as tk

win = tk.Tk()
win.title("PDFer")
win.geometry("250x150")


label = tk.Label(win, text='File name?')
label.pack(anchor='center')

# テキストボックスを作成
text = tk.Entry(win)
text.pack(anchor='center')
text.insert(tk.END, '')
text.focus_set()

#関数部分
import re,glob,os
from PIL import Image
import img2pdf
import PyPDF2
from tkinter import messagebox

def change(s):
    os.mkdir("C://Users/syunnosukesuwa/Videos/Captures/buffer")
    files = glob.glob("C://Users/syunnosukesuwa/Videos/Captures/pic/*.png")
    match = re.compile("(png)")
    for file_name in files:
        im = Image.open(file_name)
        im = im.convert("RGB")

        new_file_name: str = match.sub("jpeg", file_name)
        os.remove(file_name)
        im.save(new_file_name, quality=100)
       # print(file_name + " convert is completed")

    path = "C://Users/syunnosukesuwa/Videos/Captures/pic"
    pdf_path = "C://Users/syunnosukesuwa/Videos/Captures/buffer"
    os.chdir(path)

    for i in os.listdir(path):
        pdf_name = pdf_path + "/" + "PDF_" + str(i.strip(".jpeg")) + ".pdf"
        img = Image.open(i)
        cov_pdf = img2pdf.convert(i)
        file = open(pdf_name, "wb")
        file.write(cov_pdf)
        img.close()
        file.close()

    merge = PyPDF2.PdfFileMerger()
    for j in os.listdir(pdf_path):
        merge.append(pdf_path + "/" + j)

    merge.write(pdf_path + "/../" + s + ".pdf")
    merge.close()

    pdf_list = glob.glob(pdf_path+"/"+"*.pdf")
    for pdf in pdf_list:
        os.remove(pdf)

    os.rmdir("C://Users/syunnosukesuwa/Videos/Captures/buffer/")

    messagebox.showinfo('infomation','transformed successfully!!')

#-------------------------------------------------------------

def ok_click():
    s = text.get()
    change(s)

#------------------------------------------------------------
import shutil
def delete_pic():
    shutil.rmtree("C://Users/syunnosukesuwa/Videos/Captures/pic")
    os.mkdir("C://Users/syunnosukesuwa/Videos/Captures/pic")

#------------------------------------------------------------


okButton = tk.Button(win, text='GO!!', command=ok_click)
okButton.pack(anchor='center',pady=5)

closebutton = tk.Button(win, text='✕', command=win.destroy)
closebutton.pack(pady=2)

okButton = tk.Button(win, text='Delete pictures', command=delete_pic)
okButton.pack(anchor='center',pady=2)

win.mainloop()