from tkinter import *
from tkinter import messagebox

class StudentInfo:
    def __init__(self, name, age, student_id, email, phone):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.email = email
        self.phone = phone
        
students = [
    StudentInfo("Cadiz", "19", "76586", "cadiz@lpunetwork.edu.ph", "09120312932"),
    StudentInfo("Kenjo", "20", "21351", "kenjo@lpunetwork.edu.ph", "09121231312"),
    StudentInfo("Salapantan", "19", "76436", "salapantan@lpunetwork.edu.ph", "09121231214"),
    StudentInfo("Nebril", "18", "32574", "nebril@lpunetwork.edu.ph", "0914124123"),
    StudentInfo("Mariano", "20", "23623", "mariano@lpunetwork.edu.ph", "09124123123"),
    StudentInfo("Dy", "21", "78978", "dy@lpunetwork.edu.ph", "09120312932"),
    StudentInfo("Fortuno", "21", "46836", "fortuno@lpunetwork.edu.ph", "0912123124"),
    StudentInfo("Cruz", "20", "83568", "cruz@lpunetwork.edu.ph", "0911231231"),
    StudentInfo("Ang", "19", "12312", "ang@lpunetwork.edu.ph", "09120312932"),
    StudentInfo("Torres", "20", "12361", "torres@lpunetwork.edu.ph", "09124123124"),
    StudentInfo("Valzado", "21", "71234", "valzado@lpunetwork.edu.ph", "09151532424"),
]

def login():
    entered_id = txtboxlogin_username.get()
    for student in students:
        if entered_id == student.student_id:
            login_label.config(text = "Login Succesful!", fg = "green")
            login_window.destroy()
            open_main_window(student)
            return
        login_label.config(text = "Invalid Please try again", fg = "red")
        
def open_main_window(student):
    def clear_content():
        for widget in content_frame.winfo_children():
            widget.destroy()
            
def create_menu_button(text, command):
    button = Button(menu_frame, text = text, font = ("Times New Roman", 14), bg = "#3b3b3b", fg = "purple", activebackground="575757", activeforeground = "white", relief = "flat", command = command)
    button.pack(fill = "x", padx = 10, pady = 10)
    button.bind("<Enter>", lambda e: button.config(bg = "#575757"))
    button.bind("<Exit>", lambda e: button.config(bg = "#3b3b3b"))

def add_student():
    clear_content()
    Label(content_frame, text = "Add Student Form", font = ("Times New Roman", 16), bg = "white").pack(pady =10)
    
    for field in ["Name", "Age", "Student ID", "Email", "Phone"]:
        Label (content_frame, text = f"{field}:", font = ("Times New Roman", 12), bg = "white").pack(pady=5)
        entry = Entry (content_frame, width = 40, font = ("Time New Roman", 12), relief = "solid", bd = 1)
        entry.pack(pady=5)
        
    Button(content_frame, text = "Save", font = ("Time New Roman", 12), bg = "3b3b3b", fg = "white", relief = "flat").pack(pady=20)
    
def view_student_info():
    clear_content()
    Label (content_frame, text = f"Name:{student.name}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
    Label (content_frame, text = f"Age:{student.name}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
    Label (content_frame, text = f"Student ID:{student.student_id}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
    Label (content_frame, text = f"Email:{student.email}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
    Label (content_frame, text = f"Phone:{student.phone}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
    
def search_student_info():
    clear_content()
    Label(content_frame, text = "Search Student Info", font = ("Times New Roman", 16), bg = "white").pack(pady=10)
    Label(content_frame, text = "Enter Student ID: ", font = ("Times New Roman", 12), bg = "white").pack(pady=5)
    
    search_entry = Entry (content_frame, width = 40, font = ("Time New Roman", 12), relief = "solid", bd = 1)
    search_entry.pack(pady=5)

def perform_search():
    student_id = search_entry.get()
    for s in students:
        if s.students_id == students_id:
            clear_content()
            Label (content_frame, text = f"Name:{student.name}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
            Label (content_frame, text = f"Age:{student.name}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
            Label (content_frame, text = f"Student ID:{student.student_id}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
            Label (content_frame, text = f"Email:{student.email}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
            Label (content_frame, text = f"Phone:{student.phone}", font = ("Times New Roman", 16), bg = "white").pack(pady=5)
            return
        messagebox.showinfo("Not Found", "Invalid ID...")
        
    Button(content_frame, text = "Search", font = ("Times New Roman", 12), bg = "#3b3b3b", fg = "white", relief = "flat", command = perform_search),pack(pady=10)
    
def view_all_students():
    clear_content()
    Label(content_frame, text = "All Students", font = ("Times New Roman", 16), bg = "white").pack(pady=10)
    for s in students:
        Label(content_frame, text = f"{s.name}({s.student_id})", font = ("Times New Roman", 12), bg = "white").pack(pady=2)

def exit_app():
    main_window.destroy()
    main_window = Tk()
    main_window.geometry(f"1280x800+{(main_window.winfo_screenwidth() - 1280)//2}+{(main_window,winfo_screeningheight() - 800)//2}")
    
    menu_frame = Frame (main_window, bf = "5b5b5b", width = 220, relief = "sunken")
    menu_frame.pack(side = "left", fill = "y")
    
    content_frame = Frame(main_window, bg = "white")
    content_frame.pack (side = "right", fill = "both", expand = True)
    
    Label(menu_frame, text = "Menu", font = ("Times New Roman", 16, "bold"), bg = "#5b5b5b", fg = "white").pack(pady=20)
    
    search_box = Entry(menu_frame, font = ("Times New Roman", 12), width = 20, relief = "solid", bd = 1, justify = "center")
    search_box.pack(pady=10)
    search_box.insert(0, "Search...")
    
    create_menu_button("Add Student", add_student)
    create_menu_button("View Student Info", view_student_info)
    create_menu_button("Search Student Info", search_student_info)
    create_menu_button("View All Students", view_all_students)
    create_menu_button("Exit", exit_app)
    
    clear_content() 
    Label(content_frame, text = f"Welcome, {student.name}!", font = ("Times New Roman", 20), bg = "white").pack(pady=50)
    
    main_window.mainloop()
    
    login_window = Tk()
    login_window.title("Login")
    login_window.geometry(f"400x300+{(login_window.winfo_screenwidth() - 400)//2}+{(login_window.winfo_screenheight() - 300)//2}")
    login_window.configure(bg = "#222222")
    
    label_titlelogin = Label(login_window, text = "Enter Student ID", fg = "#BBBBBB", bg = "#222222", font = ("Times New Roman", 20))
    label_titlelogin.pack(pady=20)
    
    txtboxlogin_username = Entry(login_window, width = 30, font = ("Times New Roman", 14), justify = "center", relief = "solid" bf = 1)
    
    txtboxlogin_username.pack(pady=10)
    
    btn_login = Button(login_wind)
    
    
    
    
    