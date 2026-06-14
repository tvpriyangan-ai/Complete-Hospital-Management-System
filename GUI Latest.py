import tkinter as tk
from tkinter import messagebox
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from tkinter import simpledialog

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

        tk.Label(main_panel, text='surname', bg='#1e1e1e', fg='white').pack()
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
    


    def register_patient():

        for widget in main_panel.winfo_children():
            widget.destroy()

        tk.Label(
            main_panel,
            text="Register Patient",
            bg="#1e1e1e",
            fg="white",
            font=("Arial",16,"bold")
            ).pack(pady=10)

        tk.Label(main_panel,text="First Name",
             bg="#1e1e1e",fg="white").pack()

        first_name_entry = tk.Entry(main_panel)
        first_name_entry.pack()

        tk.Label(main_panel,text="Surname",
             bg="#1e1e1e",fg="white").pack()

        surname_entry = tk.Entry(main_panel)
        surname_entry.pack()

        tk.Label(main_panel,text="Age",
             bg="#1e1e1e",fg="white").pack()

        age_entry = tk.Entry(main_panel)
        age_entry.pack()

        tk.Label(main_panel,text="Mobile",
             bg="#1e1e1e",fg="white").pack()

        mobile_entry = tk.Entry(main_panel)
        mobile_entry.pack()

        tk.Label(main_panel,text="Postcode",
             bg="#1e1e1e",fg="white").pack()

        postcode_entry = tk.Entry(main_panel)
        postcode_entry.pack()




        def save_patient():

            if first_name_entry.get() == "" or surname_entry.get() == "":
                messagebox.showerror(
                    "Error",
                    "First Name and Surname are required"
                )
                return
            
            try:
                age=int(age_entry.get())
            except ValueError:
                    messagebox.showerror(

                        'Error',
                        'Age must be a Number'
                    )
                    return

            patients.append(
                Patient(
                    first_name_entry.get(),
                    surname_entry.get(),
                    age,
                    mobile_entry.get(),
                    postcode_entry.get()
                )
            )

            messagebox.showinfo(
                "Success",
                "Patient Registered"
            )

            print("Saved")
            print(len(patients))

        tk.Button(
            main_panel,
            text="Save Patient",
            bg="green",
            fg="white",
            command=save_patient
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


    


    def view_patients():

        for widget in main_panel.winfo_children():
            widget.destroy()

        tk.Label(

            main_panel,
            text="Patient List",
            bg="#1e1e1e",
            fg="white",
            font=("Arial",16,"bold")

        ).pack(pady=10)

        for index, patient in enumerate(patients, start=1):

            tk.Label(
                main_panel,
                text=str(patient),
                bg="#1e1e1e",
                fg="white",
                font=("Consolas",11),
                anchor="w",
                justify="left"
            ).pack(fill="x", padx=20)
        print("Viewing")
        print(len(patients))
        

    def assign_doctor():

        patient_id = simpledialog.askinteger(
            "Assign Doctor",
            "Enter Patient ID:"
        )

        doctor_id = simpledialog.askinteger(
            "Assign Doctor",
            "Enter Doctor ID:"
        )

        if patient_id is None or doctor_id is None:
            return

        patient_id = patient_id - 1
        doctor_id = doctor_id - 1

        if patient_id in range(len(patients)) and doctor_id in range(len(doctors)):

            patients[patient_id].link(
            doctors[doctor_id]
        )

            messagebox.showinfo(
                "Success",
                "Doctor Assigned Successfully"
            )

        else:

            messagebox.showerror(
                "Error",
                "Invalid ID"
            )






    def delete_doctor():
        doctor_id = simpledialog.askinteger(
        "Delete Doctor",
        "Enter Doctor ID:"
        )

        if doctor_id is None:
            return

        doctor_id = doctor_id - 1

        if doctor_id >= 0 and doctor_id < len(doctors):

            doctors.pop(doctor_id)

            messagebox.showinfo(
                "Success",
                "Doctor Deleted"
            )

        else:
            messagebox.showerror(
                "Error",
                "Invalid Doctor ID"
            )

        

    def update_doctor():

        doctor_id = simpledialog.askinteger(
            "Update Doctor",
            "Enter Doctor ID:"
        )

        if doctor_id is None:
            return

        doctor_id = doctor_id - 1

        if doctor_id >= 0 and doctor_id < len(doctors):

            new_first_name = simpledialog.askstring(
                "Update",
                "Enter New First Name:"
            )

            new_surname = simpledialog.askstring(
                "Update",
                "Enter New Surname:"
            )

            new_speciality = simpledialog.askstring(
                "Update",
                "Enter New Speciality:"
            )

            doctors[doctor_id].set_first_name(new_first_name)
            doctors[doctor_id].set_surname(new_surname)
            doctors[doctor_id].set_speciality(new_speciality)

            messagebox.showinfo(
                "Success",
                "Doctor Updated Successfully"
            )

        else:
            messagebox.showerror(
                "Error",
                "Invalid Doctor ID"
            )



    def show_doctor_management():
        for widget in main_panel.winfo_children():
            widget.destroy()
        tk.Label(main_panel, text='Doctor Management', bg='#1e1e1e', fg='white', font=('Arial', 16, 'bold')).pack(pady=10)

        tk.Button(main_panel, text='Register Doctor', bg='#3a3a3a', fg='white', width=20, command=register_doctor).pack(pady=5)
        tk.Button(main_panel, text='View Doctor', bg='#3a3a3a', fg='white', width=20, command=view_doctors).pack(pady=5)
        tk.Button(
            main_panel,
            text='Update Doctor',
            bg='#3a3a3a',
            fg='white',
            width=20,
            command=update_doctor
        ).pack(pady=5)

        tk.Button(
            main_panel,
            text='Delete Doctor',
            bg='#3a3a3a',
            fg='white',
            width=20,
            command=delete_doctor
        ).pack(pady=5)



    def show_patient_management():

        for widget in main_panel.winfo_children():
            widget.destroy()

        tk.Label(
            main_panel,
            text="Patient Management",
            bg="#1e1e1e",
            fg="white",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        tk.Button(
            main_panel,
            text="Register Patient",
            width=20,
            command=register_patient
        ).pack(pady=5)
    

        tk.Button(
            main_panel,
            text="View Patient",
            width=20,
            command=view_patients
        ).pack(pady=5)

        tk.Button(
            main_panel,
            text="Assign Doctor",
            width=20,
            command=assign_doctor
        ).pack(pady=5)




    def view_discharged_patients():

        for widget in main_panel.winfo_children():
            widget.destroy()

        tk.Label(
            main_panel,
            text="Discharged Patients",
            bg="#1e1e1e",
            fg="white",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        if len(discharged_patients) == 0:

            tk.Label(
                main_panel,
                text="No Discharged Patients",
                bg="#1e1e1e",
                fg="white"
            ).pack(pady=20)

        else:

            for index, patient in enumerate(discharged_patients, start=1):

                tk.Label(
                    main_panel,
                    text=f"{index}. {patient}",
                    bg="#1e1e1e",
                    fg="white",
                    font=("Consolas",11)
                ).pack(anchor="w", padx=20)



    def show_panel(text):
        for widget in main_panel.winfo_children():
            widget.destroy()
        tk.Label(main_panel, text=text, bg="#1e1e1e", fg="white", font=("Arial", 14)).pack(pady=20)
    




    def update_admin():

        for widget in main_panel.winfo_children():
            widget.destroy()

        tk.Label(
            main_panel,
            text="Update Admin",
            bg="#1e1e1e",
            fg="white",
            font=("Arial",16,"bold")
        ).pack(pady=10)

        tk.Label(main_panel,text="Username").pack()
        username_entry=tk.Entry(main_panel)
        username_entry.pack()

        tk.Label(main_panel,text="Password").pack()
        password_entry=tk.Entry(main_panel)
        password_entry.pack()

        tk.Label(main_panel,text="Postcode").pack()
        postcode_entry=tk.Entry(main_panel)
        postcode_entry.pack()

        def save_admin():
            admin.username = username_entry.get()
            admin.password = password_entry.get()
            admin.postcode = postcode_entry.get()

            messagebox.showinfo(
                "Success",
                "Admin Updated"
            )

        tk.Button(
            main_panel,
            text="Update Admin",
            bg="green",
            fg="white",
            command=save_admin
        ).pack(pady=15)



    #sidebar button design
    buttons_commands =[

        show_doctor_management,
        show_patient_management,
        view_discharged_patients,
        assign_doctor,
        update_admin,
        window.destroy

        ]


    for button_text, cmd in zip(buttons, buttons_commands):
        tk.Button(sidebar, text=button_text, bg="#3a3a3a", fg="white",width=22, anchor="w",padx=10,command=cmd).pack(pady=4)
       


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
