from tkinter import *
from datetime import datetime
from PIL import ImageTk, Image
from tkinter import Toplevel
import pandas as pd

users_register = []






"""define window_2"""

def window_2():
    new_window=Toplevel()
    new_window.title("maneger of library")
    new_window.geometry("700x600")
    new_window.resizable(width=False, height=False)
    image=Image.open("brain.jpg")
    back=ImageTk.PhotoImage(image)
    background_label=Label(new_window, image=back)
    background_label.image=back
    background_label.place(x=0, y=0)



    def register_book():
        try:
            global notebook
            notebook = pd.read_csv("books_list.csv")
            books_text = notebook.to_string(index=False)
            books_show.config( text=str(books_text))  
        except FileNotFoundError:
            books_show.config(text="فایل کتاب‌ها یافت نشد")
        except pd.errors.EmptyDataError:
            books_show.config(text="هیچ کتابی در لیست وجود ندارد")

    

    def search_book():
        global noteBook
        print("jjjjjjjj")
        print(e_search.get())
        number=notebook[notebook['name']==e_search.get()]["count"]
        print("number",number)
        if (e_search.get()) in str(notebook["name"].values)   :
            if int(number) > 0:
                search_notebook.config(text=f"کتاب موجود است{e_search.get()}")
                number-=1
                notebook.loc[notebook['name'] == e_search.get(), "count"] = number
                notebook.to_csv("books_list.csv", index=False)
            else:
                 search_notebook.config(text="noch",fg="black")   
  
        else:
             search_notebook.config(text="noch",fg="black")   
    
    
    
    
    def book_trust():
        pass
    
    
    
    
    
    
    
    
    
    books=Button(new_window,text="لیست کتابهای موجود در کتابخانه",bg="yellow" , command=register_book)
    books.place(x=50, y=50)
    books_show=Label(new_window,text=" ",bg="blue",width=40,height=10,fg="black")
    books_show.place(x=500,y=100)
    
    search=Label(new_window, text=" :نام کتاب مورد جسنجو ",bg="orange")
    search.place(x=300, y=200)
    e_search=Entry(new_window, width=30)
    e_search.place(x=50, y=200)
    search_notebook=Label(new_window,text="",width=40,bg="orange")
    search_notebook.place(x=30,y=220)
    b_search=Button(new_window, text="جستجو ", bg="orange", command=search_book)
    b_search.place(x=210, y=250, width=70)
    # lst_book=Message(new_window, text="",bg="green")
    # lst_book.place(x=100, y=50)
    
    
    "trust books"
    trust_book=Label(new_window, text=":نام کتاب مورد امانت  ",bg="purple")
    trust_book.place(x=300, y=300, width=150)
    e_trust=Entry(new_window, width=30)
    e_trust.place(x=50, y=300)
    trust=Button(new_window, text="امانت", command=book_trust,bg="purple")
    trust.place(x=210, y=350, width=90)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

"""define GUI"""
tk=Tk()
tk.title("library digital")
tk.geometry("630x450")
tk.resizable(width=False, height=False)
image=Image.open("library.jpg")
back=ImageTk.PhotoImage(image)
background_label=Label(tk, image=back)
background_label.place(x=0, y=0)


id=Label(tk, text="  :کد ملی  "   ,bg="pink")
id.place(x=350, y=100, width=70)
e_id=Entry(tk, bg="pink",)
e_id.place(x=200, y=100, width=90,)

id_repeat=Message(tk,text="",bg="pink")
id_repeat.place(x=70, y=80)




family=Label(tk, text="  :نام و نام  خانوادگی  ",bg="pink")
family.place(x=350, y=150, width=70)
e_family=Entry(tk, bg="pink")
e_family.place(x=200, y=150, width=90)


"""register user in window 1"""
users_id = []  
users_family = []
users_register = []
def register_user():
    global users_id
    global users_family
    global users_register
    global users_id
    if e_id.get() not in users_id  and ((e_id.get()).isdigit()==True and len(e_id.get())==10):
        (users_id.append(e_id.get())) and (users_family.append(e_family.get()))
        submit_msg.config(text="با موفثیت ثبت شد")
        welcome_message.config(text=f"خوش آمدید {e_family.get()}عزیز")
        # e_family.delete(0,END)
        # e_id.delete(0,END)
        print(users_id)
        submit_msg.delete(0,END)
        users_register=list(zip(users_id, users_family))
        print(1)
        print(users_register)
    else:
        id_repeat.config(text="  فقط عدد وارد کنید یا \nکد ملی تکراری است ")
        # id_repeat.delete(0, 'end')
    
    
    
    
    
    



"""enter user to window_2"""            
   
def enter_user():
    global users_register
    global users_id
    if e_id.get() in users_id :
        window_2()
        e_id.delete(0,END)
        e_family.delete(0,END)
    else:
        # print(users_id,"uuuu")
        # print(e_id.get(),"idid")
        enter_repeat.config(text="اول ثبت نام کن")
        register_user()    




def role():
    role_label.config(text="نشتسیسشنمیتمش ستشسیتشسایتن ستنیاتنشسای سنیتانتسشای نسیاتتشاسیتن سشتنی نتشاسیتنشسی نشسیاتنسشی نشتسیاتنشسی نشسیانتشسیگکمنکمی عدنتسید یسادسیت یخیحش یح8ی شنساشیت سنتیاتنساشی نستیانتسشای نشسیاتنسشیا نسشیاتنسشیا سیاتنسیا ")




    
register=Button(tk, text="ثبت", bg="pink",border=3, command=register_user)
register.place(x=280, y=200, width=90)
submit_msg=Message(tk,text="", bg="yellow")
submit_msg.place(x=200, y=200)



enter=Button(tk, text="ورود", bg="green",command=enter_user)
enter.place(x=290, y=250, width=70)

enter_repeat=Label(tk, text="",bg="pink")
enter_repeat.place(x=350, y=230)

role_library=Button(tk, text="آئین کتابخانه" ,command=role)
role_library.place(x=290, y=300)
role_label=Message(tk, text="",bg="green")
role_label.place(x=200, y=300)
welcome_message=Label(tk, text="",bg="red")
welcome_message.place(x=200, y=400)











# global users_register
# print(users_register)


















tk.mainloop()






























# إإإإإإإإإإإإإإإإإإإإإإإإإإإإإإ
# from tkinter import *
# from datetime import datetime
# from PIL import ImageTk, Image
# from tkinter import Toplevel
# import pandas as pd

# users_register = []


# def window_2():
#     new_window = Toplevel()
#     new_window.title("مدیریت کتابخانه")
#     new_window.geometry("700x600")
#     new_window.resizable(width=False, height=False)
#     image = Image.open("brain.jpg")
#     back = ImageTk.PhotoImage(image)
#     background_label = Label(new_window, image=back)
#     background_label.image = back
#     background_label.place(x=0, y=0)
    
#     def register_book():
#         pass
    
#     def search_book():
#         pass
    
#     def book_trust():
#         pass
    
#     def books_list():
#         listbooks = pd.read_csv("books_list.csv")
    
    
#     books = Button(new_window, text="لیست کتابهای موجود در کتابخانه", bg="yellow", command=books_list)
#     books.place(x=50, y=50)
#     search = Label(new_window, text=":نام کتاب مورد جستجو", bg="orange")
#     search.place(x=300, y=200)
#     e_search = Entry(new_window, width=30)
#     e_search.place(x=50, y=200)
#     b_search = Button(new_window, text="جستجو", bg="orange", command=search_book)
#     b_search.place(x=210, y=250, width=70)
#     lst_book = Message(new_window, text="", bg="green")
#     lst_book.place(x=100, y=50)
    
#     trust_book = Label(new_window, text=":نام کتاب مورد امانت", bg="purple")
#     trust_book.place(x=300, y=300, width=150)
#     e_trust = Entry(new_window, width=30)
#     e_trust.place(x=50, y=300)
#     trust = Button(new_window, text="امانت", command=book_trust, bg="purple")
#     trust.place(x=210, y=350, width=90)


# def register_user():
#     global users_register
#     users_id = []
#     users_family = []
#     if e_id.get() not in users_id and e_id.get().isdigit() and len(e_id.get()) == 10:
#         users_id.append(e_id.get())
#         users_family.append(e_family.get())
#         submit_msg.config(text="با موفقیت ثبت شد")
#         welcome_message.config(text=f"خوش آمدید {e_family.get()} عزیز")
#         e_family.delete(0, END)
#         e_id.delete(0, END)
#         submit_msg.delete(0, END)
#         users_register = list(zip(users_id, users_family))
#         print(1)
#         print(users_register)
#     else:
#         id_repeat.config(text="فقط عدد وارد کنید یا کد ملی تکراری است")
#         id_repeat.delete(0, 'end')


# def enter_user():
#     global users_register
#     if e_id.get() in users_register:
#         window_2()
#     else:
#         enter_repeat.config(text="ابتدا ثبت نام کنید")
#         register_user()


# def role():
#     role_label.config(text="آئین‌نامه کتابخانه را در این قسمت قرار دهید")


# tk = Tk()
# tk.title("کتابخانه دیجیتال")
# tk.geometry("630x450")
# tk.resizable(width=False, height=False)
# image = Image.open("library.jpg")
# back = ImageTk.PhotoImage(image)
# background_label = Label(tk, image=back)
# background_label.place(x=0, y=0)

# id = Label(tk, text=":کد ملی", bg="pink")
# id.place(x=350, y=100, width=70)
# e_id = Entry(tk, bg="pink")
# e_id.place(x=200, y=100, width=90)

# id_repeat = Message(tk, text="", bg="pink")
# id_repeat.place(x=70, y=80)

# family = Label(tk, text=":نام و نام خانوادگی", bg="pink")
# family.place(x=350, y=150, width=70)
# e_family = Entry(tk, bg="pink")
# e_family.place(x=200, y=150, width=90)

# register = Button(tk, text="ثبت", bg="pink", border=3, command=register_user)
# register.place(x=280, y=200, width=90)
# submit_msg = Message(tk, text="", bg="yellow")
# submit_msg.place(x=200, y=200)

# enter = Button(tk, text="ورود", bg="green", command=enter_user)
# enter.place(x=290, y=250, width=70)

# enter_repeat = Label(tk, text="", bg="pink")
# enter_repeat.place(x=350, y=230)

# role_library = Button(tk, text="آئین‌نامه کتابخانه", command=role)
# role_library.place(x=290, y=300)
# role_label = Message(tk, text="", bg="green")
# role_label.place(x=200, y=300)

# welcome_message = Label(tk, text="", bg="red")
# welcome_message.place(x=200, y=400)

# tk.mainloop()
