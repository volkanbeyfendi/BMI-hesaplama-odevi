import tkinter

my_window = tkinter.Tk()
my_window.title("Vücut İndexi Hesaplama")
my_window.config(bg="white")
my_window.minsize(10,10)

#boş gridler
my_bosluk1_label = tkinter.Label(width=5, bg= "white")
my_bosluk1_label.grid(row=0, column=0)
my_bosluk2_label = tkinter.Label(width=5, bg= "white")
my_bosluk2_label.grid(row=10, column=2)

#labellar(yazılar)

my_weight_label = tkinter.Label(text="Kilonuzu giriniz(kg)",font=("Arial", 7, "normal"), width=20)
my_weight_label.config(bg="white")
my_weight_label.config(fg="black")
my_weight_label.config(padx=20,pady=5)
my_weight_label.grid(row=1, column=1)


my_height_label = tkinter.Label(text="Boyunuzu giriniz(cm)",font=("Arial", 7, "normal"), width=20)
my_height_label.config(bg="white")
my_height_label.config(fg="black")
my_height_label.config(padx=20,pady=5)
my_height_label.grid(row=4, column=1)

#entryler(boy-kilo girişleri)

my_weight_entry = tkinter.Entry()
my_weight_entry.grid(row=2,column=1)
weight = my_weight_entry.get()

my_height_entry = tkinter.Entry()
my_height_entry.grid(row=5,column=1)
height = my_height_entry.get()

#hesaplama fonksiyonu
def hesaplama():
    try:
        w = my_weight_entry.get()
        h = my_height_entry.get()
        h = float(h)
        h = h / 100
        w = int(w)
    except ValueError :
        my_BMIresult_label = tkinter.Label(text="Sayı giriniz", font=("Arial", 7, "normal"), width=20)
        my_BMIresult_label.grid(row=7, column=1)

    BMI = w / (h*h)
    if BMI < 18.5 :
        result = "Aşırı zayıfsınız"
    elif 18.5 <= BMI < 25 :
        result = "Normal kilodasınız"
    elif 25 <= BMI < 30 :
        result = "Kilolusunuz"
    elif 30 <= BMI < 35 :
        result = "1. Derece Obezsiniz"
    elif 35 <= BMI <= 40 :
        result = "2. Derece Obezsiniz"
    elif BMI > 40 :
        result = "Aşırı obezsiniz"

    BMI = round(BMI,2)
    my_BMIresult_label = tkinter.Label(text="BMI: {}, {}".format(BMI, result), font=("Arial", 15, "normal"))
    my_BMIresult_label.grid(row=9, column=1)


#buton
my_BMIcalc_button = tkinter.Button(text="HESAPLA",font=("Arial", 10, "normal"), width=10,command = hesaplama)
my_BMIcalc_button.grid(row=8, column=1)

my_window.mainloop()

