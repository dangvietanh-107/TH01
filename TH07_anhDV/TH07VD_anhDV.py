# ví dụ 1
from tkinter import *
#Tạo một cửa sổ mới
window = Tk()
#Thêm tiêu đề cho cửa sổ
window.title('Welcome to EAUT')
#Đặt kích thước của cửa sổ
window.geometry('350x200')
#Lặp vô tận để hiển thị cửa sổ
window.mainloop()

# ví dụ 2
from tkinter import *
window = Tk()
window.title("Welcome to VniTeach app")
#Thêm label có nội dung Hello, font chữ
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
#Xác định vị trí của label
lbl.grid(column=0, row=0)
window.mainloop()

# ví dụ 3
from tkinter import *
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
#Thêm một nút nhấn Click Me
btn = Button(window, text="Click Me", bg="orange", fg="red")
#Thiết lập vị trí của nút nhấn có màu nền và màu chữ
btn.grid(column=1, row=0)
window.mainloop()

# ví dụ 4
from tkinter import *
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
#Hàm khi nút được nhấn
def clicked():
 lbl.configure(text="Button was clicked !!")
#Gọi hàm clicked khi nút được nhấn
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()

# ví dụ 5
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("100x100")
def helloCallBack():
 msg = messagebox.showinfo( "Hello Python", "Hello World")
B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 50)
top.mainloop()

# ví dụ 6

from tkinter import *
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
#Tạo một Textbox
txt = Entry(window,width=10)
#Vị trí xuất hiện của Textbox
txt.grid(column=1, row=0)
#Đặt vị trí con trỏ tại Textbox
txt.focus()
#Hàm xử lý khi nút được nhấn
def clicked():
 res = "Welcome to " + txt.get()
 lbl.configure(text= res)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
#Để tắt chức năng nhập của Textbox bằng state
#txt = Entry(window,width=10, state='disabled')
window.mainloop()

# ví dụ 7

from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
#Tạo hộp chọn Combobox
combo = Combobox(window)
#Các giá trị của hộp chọn
combo['values']= (1, 2, 3, 4, 5, "Text")
#Thiết lập giá trị được chọn
combo.current(1) #set the selected item
combo.grid(column=0, row=0)
#Lấy giá trị của hộp chọn bằng combo.get()
window.mainloop()

#. 5Làm việc với Checkbox
# ví dụ 8
from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome EAUT")
window.geometry('350x200')
#Thiết lập trạng thái của Checkbox

chk_state = BooleanVar()
chk_state.set(True) #set check state
#Tạo Checkbox có trạng thái đã tích chọn
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=0)
window.mainloop()

#6. Làm việc với Radio
# ví dụ 9
from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to EAUT")
selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
def clicked():
 print(selected.get())
btn = Button(window, text="Click Me", command=clicked)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
window.mainloop()

#7. Làm việc với ScrolledText
from tkinter import *
from tkinter import scrolledtext
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column=0,row=0)
window.mainloop()

#8 . Làm việc với Messagebox
#– Hộp thoại thông báo
# Làm việc với Messagebox
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Welcome to EAUT")
window.geometry('350x200')
def clicked():
 messagebox.showinfo('Message title', 'Message content')
btn = Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)
window.mainloop()

#Hộp thoại cảnh báo
messagebox.showwarning('Message title', 'Message content') 
# Hộp thoại báo lỗi 
#messagebox.showerror('Message title', 'Message content')

#Hộp thoại câu hỏi
from tkinter import messagebox
res = messagebox.askquestion('Message title','Message content')
res = messagebox.askyesno('Message title','Message content')
res = messagebox.askyesnocancel('Message title','Message content')
res = messagebox.askokcancel('Message title','Message content')
res = messagebox.askretrycancel('Message title','Message content')

#9. Làm việc với SpinBox
from tkinter import *
window = Tk()
window.title("Welcome to VniTeach app")
window.geometry('350x200')

#Tạo spinbox có chiều rộng 5, giá trị từ 0 đến 100
spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0,row=0)
window.mainloop()

# Liệt kê các giá trị của spinbox
#spinbox chỉ gồm có 3 giá trị là 3, 5 và 10
spin = Spinbox(window, values=(3, 5, 10), width=5)

# Đặt giá trị mặc định cho spinbox
var =IntVar()
#Đặt giá trị mặc định là 25
var.set(25)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)

#10. Làm việc với trình chọn tệp và thư mục
from tkinter import filedialog
file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
dir = filedialog.askdirectory()

#Chỉ định thư mục ban đầu cho hộp thoại tệp bằng cách chỉ định initialdir như thế này
from tkinter import filedialog
from os import path
file = filedialog.askopenfilename(initialdir= path.dirname(__file__))

#11. Làm việc với Menu
from tkinter import *
from tkinter import Menu
window = Tk()
window.title("Welcome to VniTeach app")
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()
#Sự kiện khi người dùng click chọn một bảng chọn nào đó:
#Thực hiện hàm clicked khi người dùng chọn New
new_item.add_command(label='New', command=clicked)

#12. Làm việc với các Tabs
#Để tạo một điều khiển tab, có một vài bước.
#• Đầu tiên, chúng ta tạo một điều khiển tab bằng cách sử dụng lớp Notebook.
#• Tạo một tab bằng cách sử dụng Frame lớp.
#• Thêm tab đó vào điều khiển tab.
#• Đóng gói điều khiển tab để nó hiển thị trong cửa sổ.

from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to VniTeach app")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.pack(expand=1, fill='both')
window.mainloop()

#Thêm Widgets vào Notebook
#Sau khi tạo các tab, bạn có thể đặt các widget bên trong các tab này bằng cách gán thuộc 
#tính cha cho tab mong muốn.

from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to LikeGeeks app")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text= 'label1')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text= 'label2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')
window.mainloop()

#Thêm khoảng cách cho các widget (Padding)
#Bạn có thể thêm các khoảng cách trước và sau của mỗi tab bằng cách sử dụng các thuộc 
#tính padx và pady .

lbl1 = Label(tab1, text= 'label1', padx=5, pady=5)
