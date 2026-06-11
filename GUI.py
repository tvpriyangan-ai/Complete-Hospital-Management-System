import tkinter as tk
from tkinter import messagebox
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

#Area - Login window Function 
def open_main_window(admin, doctors,patients, discharged_patients):
    window=tk.Toplevel()
    window.title("Hospital Management System")
    window.geometry("800x500")
    window.configure(bg="#1e1e1e")

    

    #side bar design
    sidebar=tk.Frame(window, bg="#2d2d2d", width=200)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)
    tk.Label(sidebar, text='HMS', bg="#2d2d2d", fg="white", font=("Arial", 16, "bold")).pack(pady=20)


    #main panel design
    main_panel=tk.Frame(window, bg="#1e1e1e")
    main_panel.pack(side="right", fill="both", expand=True)

    buttons =[
        "1. Doctor Management",
        "2. View / Discharge Patient",
        "3. View Discharged",
        "4. Assign Doctor",
        "5. Update Admin",
        "6. Quit"
    ]
    def register_doctor():
        for widget in main_panel.winfo_children():
            widget.destroy()

        tk.Label(
            main_panel,
            text='Register Doctor',
            bg='#1e1e1e',
            fg='white',
            font=('Arial', 16, 'bold')
        ).pack(pady=10)

        tk.Label(main_panel, text='First Name', bg='#1e1e1e', fg='white').pack()
        first_name_entry = tk.Entry(main_panel)
        first_name_entry.pack(pady=5)

        tk.Label(main_panel, text='surename', bg='#1e1e1e', fg='white').pack()
        surname_entry=tk.Entry(main_panel)
        surname_entry.pack(pady=5)

        tk.Label(main_panel, text='speciality', bg='#1e1e1e', fg='white').pack()
        speciality_entry=tk.Entry(main_panel)
        speciality_entry.pack(pady=5)

        def save_doctor():
            first_name=first_name_entry.get()
            surname=surname_entry.get()
            speciality=speciality_entry.get()

            if first_name == ''or surname==''or speciality =='':
                messagebox.showerror('Error', 'All fields are required')
                return
            
            doctors.append(
                Doctor(first_name, surname, speciality)
            )
            messagebox.showinfo('success', 'Doctor registered successfully')
            show_doctor_management()


        tk.Button(
                main_panel,
                text='Save Doctor',
                bg='green',
                fg='white',
                width=20,
                command=save_doctor
            ).pack(pady=15)

    def view_doctors():
        for widget in main_panel.winfo_children():
            widget.destroy()

        tk.Label(
            main_panel,
            text='Doctor List',
            bg='#1e1e1e',
            fg='white',
            font=('Arial', 16, 'bold')
        
        ).pack(pady=10)

        for index, doctor in enumerate (doctors, start=1):
            tk.Label(
                main_panel,
                text=f'{index},{doctor}',
                bg='#1e1e1e',
                fg='white',
                font=('Consolas', 11)
            ).pack(anchor='w', padx=20)


        


    def show_doctor_management():
        for widget in main_panel.winfo_children():
            widget.destroy()
        tk.Label(main_panel, text='Doctor Management', bg='#1e1e1e', fg='white', font=('Arial', 16, 'bold')).pack(pady=10)

        tk.Button(main_panel, text='Register Doctor', bg='#3a3a3a', fg='white', width=20, command=register_doctor).pack(pady=5)
        tk.Button(main_panel, text='View Doctor', bg='#3a3a3a', fg='white', width=20, command=view_doctors).pack(pady=5)
            
    def show_panel(text):
        for widget in main_panel.winfo_children():
            widget.destroy()
        tk.Label(main_panel, text=text, bg="#1e1e1e", fg="white", font=("Arial", 14)).pack(pady=20)
    
    #sidebar button design
    buttons_commands =[

        show_doctor_management,
        lambda:show_panel("2. View / Discharge Patient"),
        lambda:show_panel("3. View Discharged"),
        lambda:show_panel("4. Assign Doctor"),
        lambda:show_panel("5. Update Admin"),
        window.destroy

    ]


    for button_text, cmd in zip(buttons, buttons_commands):
        tk.Button(sidebar, text=button_text, bg="#3a3a3a", fg="white",width=22, anchor="w",padx=10,command=cmd).pack(pady=4)
    window.mainloop()    


def main():
    admin =Admin ('admin', '123', 'B1 1AB')
    doctors = [Doctor ('John', 'Smith', 'Internal Med'), Doctor('John', 'Smith', 'Pediatrics'), Doctor ('John', 'Carlos', 'Cardiology')]
    patients=[]
    discharged_patients=[]

    page1=tk.Tk()
    page1.title('Hospital Management System - Login')
    page1.geometry('400x250')
    page1.configure(bg='#1e1e1e')
   
    tk.Label(page1, text='Username', bg='#1e1e1e', fg='white').pack(pady=5)
    username_entry=tk.Entry(page1)
    username_entry.pack()

    tk.Label(page1, text='Password', bg='#1e1e1e', fg='white').pack(pady=5)
    password_entry = tk.Entry(page1, show='*')
    password_entry.pack()

    def login_click():
        u = username_entry.get()
        p=password_entry.get()
        if u == 'admin' and p=='123':
            page1.withdraw()
            open_main_window(admin,doctors, patients, discharged_patients)
        else:
            messagebox.showerror('Error','Wrong username or password')

    tk.Button(page1, text='Login', command=login_click, bg='#3a3a3a', fg='white').pack(pady=20)
    page1.mainloop()

    
    


   






main()
