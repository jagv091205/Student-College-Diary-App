# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.title("Student Dashboard")
# root.geometry("800x600")

# # Create a maroon-colored frame at the top
# header_frame = tk.Frame(root, bg="maroon", height=50, width=800)
# header_frame.pack(side="top", fill="x")

# # Student Dashboard Label in Header
# dashboard_label = tk.Label(header_frame, text="Student Dashboard", fg="white", bg="maroon", font=("Arial", 16))
# dashboard_label.pack(pady=5)

# # Create a white-colored frame to hold the buttons
# button_frame = tk.Frame(root, bg="white")
# button_frame.pack(pady=20)

# # Definecreate_button1 function
# def create_button1(image_path, row, column, command_func=None):
#     small_button_image = Image.open(image_path).resize((40, 40))
#     small_button_photo = ImageTk.PhotoImage(small_button_image)

#     button = tk.Button(
#         button_frame,
#         image=small_button_photo,
#         borderwidth=0,
#         command=command_func if command_func else lambda: None
#     )
#     button.image = small_button_photo
#     button.grid(row=row, column=column, padx=5, pady=5)

# # Function to open the attendance window
# def open_attendance_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Attendance")
#     new_window.geometry("360x640")

#     footer_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     footer_frame.pack(side="top", fill="x")

#     attendance_label = tk.Label(footer_frame, text="Attendance", fg="white", bg="maroon", font=("Arial", 16))
#     attendance_label.pack(side="top", pady=5)

#     back_arrow_image = Image.open("images/back_arrow.png")
#     back_arrow_image = back_arrow_image.resize((30, 30))
#     back_arrow_icon = ImageTk.PhotoImage(back_arrow_image)

#     back_button = tk.Button(footer_frame, image=back_arrow_icon, bg="maroon", bd=0, command=new_window.destroy)
#     back_button.image = back_arrow_icon
#     back_button.pack(side="left", padx=10)
    
# # Function to open the class schedule window
# def open_schedule_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Class Schedule")
#     new_window.geometry("360x640")

#     # Header Frame
#     header_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     header_frame.pack(side="top", fill="x")

#     # Class Schedule Label in Header
#     schedule_label = tk.Label(header_frame, text="Class Schedule", fg="white", bg="maroon", font=("Arial", 16))
#     schedule_label.pack(side="top", fill="x", pady=5)

#     # Days Frame
#     days_frame = tk.Frame(new_window, bg="maroon")
#     days_frame.pack(side="top", fill="x")

#     # Days of the Week Buttons
#     days_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT"]

#     for day in days_of_week:
#         day_button = tk.Button(days_frame, text=day, font=("Arial", 12), fg="white", bg="maroon", padx=100, command=lambda d=day: print(f"{d} clicked!"))
#         day_button.pack(side="left")

#     # Back Arrow Button
#     back_arrow_image = Image.open("images/back_arrow.png")
#     back_arrow_image = back_arrow_image.resize((30, 30))
#     back_arrow_icon = ImageTk.PhotoImage(back_arrow_image)

#     back_button = tk.Button(new_window, image=back_arrow_icon, bg="maroon", bd=0, command=new_window.destroy)
#     back_button.image = back_arrow_icon
#     back_button.pack(pady=10)

# # Function to open online classes
# def open_onlineclass_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Online Classes")
#     new_window.geometry("360x640")

#     # Header Frame
#     header_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     header_frame.pack(side="top", fill="x")

#     # Online Classes Label in Header
#     onlineclass_label = tk.Label(header_frame, text="Online Classes", fg="white", bg="maroon", font=("Arial", 16))
#     onlineclass_label.pack(side="top",pady=5)

#     # Buttons for Today, Upcoming, Completed
#     button_frame = tk.Frame(new_window, bg="white")
#     button_frame.pack(pady=5, expand=True, fill="both")  # Adjusted the padding here

#     today_button = tk.Button(button_frame, text="Today", font=("Arial", 12), bg="white", fg="maroon", command=lambda: print("Today clicked!"), width=15)
#     today_button.pack(side="left", padx=10)

#     upcoming_button = tk.Button(button_frame, text="Upcoming", font=("Arial", 12), bg="white", fg="maroon", command=lambda: print("Upcoming clicked!"), width=15)
#     upcoming_button.pack(side="left", padx=10)

#     completed_button = tk.Button(button_frame, text="Completed", font=("Arial", 12), bg="white", fg="maroon", command=lambda: print("Completed clicked!"), width=15)
#     completed_button.pack(side="left", padx=10)


# # Function to open the exam timetable window
# def open_examtimetable_window():
#     def go_back():
#         new_window.destroy()

#     new_window = tk.Toplevel(root)
#     new_window.title("Exam Timetable")
#     new_window.geometry("360x640")

#     # Header Frame
#     header_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     header_frame.pack(side="top", fill="x")

#     # Exam Timetable  Label in Header
#     examTimetable_label = tk.Label(header_frame, text="Exam Timetable", fg="white", bg="maroon", font=("Arial", 16))
#     examTimetable_label.pack(pady=5)

#     # Form Frame
#     form_frame = tk.Frame(new_window, bg="white")
#     form_frame.pack(pady=20)

#     # Session Label and Drop-down
#     session_label = tk.Label(form_frame, text="Session", font=("Arial", 12), bg="white")
#     session_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

#     session_options = ["MARCH-2024 (NEP)", "OCTOBER-2023 (NEP)", "FEBRUARY-2024 ONDE (NEP)"]  # Example options
#     session_var = tk.StringVar(value=session_options[0])
#     session_dropdown = ttk.Combobox(form_frame, values=session_options, textvariable=session_var, state="readonly")
#     session_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

#     # Course Label and Drop-down
#     course_label = tk.Label(form_frame, text="Course", font=("Arial", 12), bg="white")
#     course_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

#     course_options = ["FYB.SC. COMPUTER SCIENCE SEMESTER I","FYB.SC. COMPUTER SCIENCE SEMESTER II"]  # Example options
#     course_var = tk.StringVar(value=course_options[0])
#     course_dropdown = ttk.Combobox(form_frame, values=course_options, textvariable=course_var, state="readonly")
#     course_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="w")

#     # Exam Type Label and Radio Buttons
#     examtype_label = tk.Label(form_frame, text="Exam Type", font=("Arial", 12), bg="white")
#     examtype_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

#     examtype_var = tk.StringVar(value="Internal")
#     internal_radio = tk.Radiobutton(form_frame, text="Internal", variable=examtype_var, value="Internal", bg="white")
#     internal_radio.grid(row=3, column=1, padx=10, pady=5, sticky="w")

#     external_radio = tk.Radiobutton(form_frame, text="External", variable=examtype_var, value="External", bg="white")
#     external_radio.grid(row=3, column=2, padx=10, pady=5, sticky="w")
#     # Back arrow button
#     back_arrow_image = Image.open("images/back_arrow.png")
#     back_arrow_image = back_arrow_image.resize((30, 30))
#     back_arrow_icon = ImageTk.PhotoImage(back_arrow_image)

#     back_button = tk.Button(header_frame, image=back_arrow_icon, bg="maroon", bd=0, command=go_back)
#     back_button.image = back_arrow_icon
#     back_button.pack(side="left", padx=10)


# # Function to open the exam hall ticket
# def open_examhallticket_window():
#     def go_back():
#         new_window.destroy()

#     new_window = tk.Toplevel(root)
#     new_window.title("Exam HallTicket")
#     new_window.geometry("360x640")

#     # Header Frame
#     header_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     header_frame.pack(side="top", fill="x")

#     # Exam HallTicket Label in Header
#     examhallticket_label = tk.Label(header_frame, text="Exam HallTicket", fg="white", bg="maroon", font=("Arial", 16))
#     examhallticket_label.pack(pady=5)

#     # Form Frame
#     form_frame = tk.Frame(new_window, bg="white")
#     form_frame.pack(pady=20)

#     # Session Label and Drop-down
#     session_label = tk.Label(form_frame, text="Session", font=("Arial", 12), bg="white")
#     session_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

#     session_options = ["MARCH-2024 (NEP)", "OCTOBER-2023 (NEP)", "FEBRUARY-2024 ONDE (NEP)"]  # Example options
#     session_var = tk.StringVar(value=session_options[0])
#     session_dropdown = ttk.Combobox(form_frame, values=session_options, textvariable=session_var, state="readonly")
#     session_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

#     # Course Label and Drop-down
#     course_label = tk.Label(form_frame, text="Course", font=("Arial", 12), bg="white")
#     course_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

#     course_options = ["FYB.SC. COMPUTER SCIENCE SEMESTER I","FYB.SC. COMPUTER SCIENCE SEMESTER II"]  # Example options
#     course_var = tk.StringVar(value=course_options[0])
#     course_dropdown = ttk.Combobox(form_frame, values=course_options, textvariable=course_var, state="readonly")
#     course_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="w")

#     # Exam Label and Drop-down
#     exam_label = tk.Label(form_frame, text="Exam", font=("Arial", 12), bg="white")
#     exam_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

#     exam_options = ["Theory-INTERNAL ASSESSMENT"]  # Example options
#     exam_var = tk.StringVar(value=exam_options[0])
#     exam_dropdown = ttk.Combobox(form_frame, values=exam_options, textvariable=exam_var, state="readonly")
#     exam_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="w")

#     # Exam Type Label and Radio Buttons
#     examtype_label = tk.Label(form_frame, text="Exam Type", font=("Arial", 12), bg="white")
#     examtype_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

#     examtype_var = tk.StringVar(value="Internal")
#     internal_radio = tk.Radiobutton(form_frame, text="Internal", variable=examtype_var, value="Internal", bg="white")
#     internal_radio.grid(row=3, column=1, padx=10, pady=5, sticky="w")

#     external_radio = tk.Radiobutton(form_frame, text="External", variable=examtype_var, value="External", bg="white")
#     external_radio.grid(row=3, column=2, padx=10, pady=5, sticky="w")


#     # Back arrow button
#     back_arrow_image = Image.open("images/back_arrow.png")
#     back_arrow_image = back_arrow_image.resize((30, 30))
#     back_arrow_icon = ImageTk.PhotoImage(back_arrow_image)

#     back_button = tk.Button(header_frame, image=back_arrow_icon, bg="maroon", bd=0, command=go_back)
#     back_button.image = back_arrow_icon
#     back_button.pack(side="left", padx=10)


# # Function to open result
# def open_result_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Result")
#     new_window.geometry("360x640")

#     # Header Frame
#     header_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     header_frame.pack(side="top", fill="x")

#     # Result Label in Header
#     result_label = tk.Label(header_frame, text="Result", fg="white", bg="maroon", font=("Arial", 16))
#     result_label.pack(pady=5)

#     # Form Frame
#     form_frame = tk.Frame(new_window, bg="white")
#     form_frame.pack(pady=20)

#     # Session Label and Drop-down
#     session_label = tk.Label(form_frame, text="Select Session", font=("Arial", 12), bg="white")
#     session_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

#     session_options = [""]
#     session_var = tk.StringVar(value=session_options[0])
#     session_dropdown = ttk.Combobox(form_frame, values=session_options, textvariable=session_var, state="readonly")
#     session_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

#     # Course Label and Drop-down
#     course_label = tk.Label(form_frame, text="Select Course", font=("Arial", 12), bg="white")
#     course_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

#     course_options = [""]
#     course_var = tk.StringVar(value=course_options[0])
#     course_dropdown = ttk.Combobox(form_frame, values=course_options, textvariable=course_var, state="readonly")
#     course_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky="w")


# # Functions to open internal mark
# def open_internalmark_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Internal Mark")
#     new_window.geometry("360x640")

#     # Header Frame
#     header_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     header_frame.pack(side="top", fill="x")

#     # Internal Mark Label in Header
#     internal_mark_label = tk.Label(header_frame, text="Internal Mark", fg="white", bg="maroon", font=("Arial", 16))
#     internal_mark_label.pack(pady=5)

#     # Form Frame
#     form_frame = tk.Frame(new_window, bg="white")
#     form_frame.pack(pady=20)

#     # Session Label and Drop-down
#     session_label = tk.Label(form_frame, text="Select Session", font=("Arial", 12), bg="white")
#     session_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

#     session_options = [""]
#     session_var = tk.StringVar(value=session_options[0])
#     session_dropdown = ttk.Combobox(form_frame, values=session_options, textvariable=session_var, state="readonly")
#     session_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# # Function to open fees paid
# def open_FeesPaid_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Fees Paid")
#     new_window.geometry("360x640")

#     # Header Frame
#     header_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     header_frame.pack(side="top", fill="x")

#     # Fees Paid Label in Header
#     fees_paid_label = tk.Label(header_frame, text="Fees Paid", fg="white", bg="maroon", font=("Arial", 16))
#     fees_paid_label.pack(pady=5)

#     # Form Frame
#     form_frame = tk.Frame(new_window, bg="white")
#     form_frame.pack(pady=20)

#     # Select Course Label and Drop-down
#     select_course_label = tk.Label(form_frame, text="Select Course", font=("Arial", 12), bg="white")
#     select_course_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

#     course_options = ["FYB.SC COMPUTER SCIENCE SEMESTER II", "FYB.SC COMPUTER SCIENCE I"]  # Add your course options
#     course_var = tk.StringVar(value=course_options[0])
#     course_dropdown = ttk.Combobox(form_frame, values=course_options, textvariable=course_var, state="readonly")
#     course_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")

#     # Buttons
#     academic_fees_button = tk.Button(form_frame, text="Academic Fees", bg="maroon", fg="white", font=("Arial", 12), command=lambda: print("Academic Fees clicked!"))
#     academic_fees_button.grid(row=1, column=0, padx=10, pady=10)

#     scholarships_button = tk.Button(form_frame, text="Scholarships", bg="maroon", fg="white", font=("Arial", 12), command=lambda: print("Scholarships clicked!"))
#     scholarships_button.grid(row=1, column=1, padx=10, pady=10)

#     other_fees_button = tk.Button(form_frame, text="Other Fees", bg="maroon", fg="white", font=("Arial", 12), command=lambda: print("Other Fees clicked!"))
#     other_fees_button.grid(row=1, column=2, padx=10, pady=10)
    

# # Function to open register subject
# def open_registersubject_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Register Subject")
#     new_window.geometry("360x640")

#     # Create a maroon-colored footer at the top
#     footer_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     footer_frame.pack(side="top", fill="x")

#     # Register Subject class label
#     Register_Subject_label = tk.Label(footer_frame, text="Register Subject", fg="white", bg="maroon", font=("Arial", 16))
#     Register_Subject_label.pack(side="top", pady=5)

#     # Grid of Subjects
#     subjects = [
#         "COMPUTER ORGANIZATION AND ARCHITECTURE",
#         "PRACTICALS BASED ON RUSCS.E111",
#         "PYTHON PROGRAMMING",
#         "PRACTICALS BASED ON RUSCS.E112",
#         "WEB PROGRAMMING",
#         "PRACTICAL BASED ON RUSVSCCS.E111",
#         "OBJECT-ORIENTED PROGRAMMING WITH JAVA",
#         "PRACTICAL BASED ON RUSSECCSCS.E111",
#         "DESIGN THINKING-II",
#         "CREATIVE CONTENT WRITING-II",
#         "COMMUNICATION SKILLS",
#         "UNDERSTANDING INDIA",
#         "COCURRICULAR COURSES"
#     ]

#     subject_frame = tk.Frame(new_window, bg="white")
#     subject_frame.pack(pady=10, padx=10, fill="both", expand=True)

#     for i, subject in enumerate(subjects):
#         subject_label = tk.Label(subject_frame, text=subject, font=("Arial", 12), bg="white", pady=5, anchor='w')
#         subject_label.grid(row=i, column=0, sticky="nsew")


# # Function to open career workshop
# def open_CareerWorkshop_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Career Workshop")
#     new_window.geometry("360x640")

#     # Create a maroon-colored footer at the top
#     footer_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     footer_frame.pack(side="top", fill="x")

#     # Career Workshop classlabel
#     Career_Workshop_label = tk.Label(footer_frame, text="Career Workshop", fg="white", bg="maroon", font=("Arial", 16))
#     Career_Workshop_label.pack(side="top", pady=5)

# # Function to open certificate
# def open_Certificate_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Certificate")
#     new_window.geometry("360x640")

#     # Create a maroon-colored footer at the top
#     footer_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     footer_frame.pack(side="top", fill="x")

#     # Certificate class label
#     Certificate_label = tk.Label(footer_frame, text="Certificate", fg="white", bg="maroon", font=("Arial", 16))
#     Certificate_label.pack(side="top", pady=5)

#     # Function to open Bonofide Certificate window
#     def open_bonofide_window():
#         bonofide_window = tk.Toplevel(new_window)
#         bonofide_window.title("Bonofide Certificate")
#         bonofide_window.geometry("360x640")

#         # Header Frame
#         bonofide_header_frame = tk.Frame(bonofide_window, bg="maroon", height=50, width=360)
#         bonofide_header_frame.pack(side="top", fill="x")

#         # Bonofide Certificate Label in Header
#         bonofide_label = tk.Label(bonofide_header_frame, text="Bonofide Certificate", fg="white", bg="maroon", font=("Arial", 16))
#         bonofide_label.pack(pady=5)

#         # Session Label and Drop-down
#         session_label = tk.Label(bonofide_window, text="Select Session", font=("Arial", 12), bg="white")
#         session_label.pack(pady=10)

#         session_options = ["FYB.SC COMPUTER SCIENCE SEMESTER 1", "FYB.SC COMPUTER SCIENCE SEMESTER II"]
#         session_var = tk.StringVar(value=session_options[0])
#         session_dropdown = ttk.Combobox(bonofide_window, values=session_options, textvariable=session_var, state="readonly")
#         session_dropdown.pack(pady=5)

#         # Reason Entry
#         reason_label = tk.Label(bonofide_window, text="Enter Reason", font=("Arial", 12), bg="white")
#         reason_label.pack(pady=10)

#         reason_entry = tk.Entry(bonofide_window, font=("Arial", 12))
#         reason_entry.pack(pady=5)

#         # Apply Bonofide Button
#         apply_bonofide_button = tk.Button(bonofide_window, text="Apply Bonofide", bg="maroon", fg="white", font=("Arial", 12))
#         apply_bonofide_button.pack(pady=10)

#     # Function to open Other Certificate window
#     def open_other_certificate_window():
#         other_certificate_window = tk.Toplevel(new_window)
#         other_certificate_window.title("Other Certificate")
#         other_certificate_window.geometry("360x640")

#         # Header Frame
#         other_certificate_header_frame = tk.Frame(other_certificate_window, bg="maroon", height=50, width=360)
#         other_certificate_header_frame.pack(side="top", fill="x")

#         # Other Certificate Label in Header
#         other_certificate_label = tk.Label(other_certificate_header_frame, text="Other Certificate", fg="white", bg="maroon", font=("Arial", 16))
#         other_certificate_label.pack(pady=5)

#         # Certificate Type Label and Drop-down
#         cert_type_label = tk.Label(other_certificate_window, text="Certificate Type", font=("Arial", 12), bg="white")
#         cert_type_label.pack(pady=10)

#         cert_type_options = ["BONOFIDE CERTIFICATION", "TRANSCRIPT CERTIFICATE", "RETENTION CERTIFICATE(JUNIOR)", "NOC CERTIFICATE(JUNIOR)", "TRANSFER CERTIFICATE"]
#         cert_type_var = tk.StringVar(value=cert_type_options[0])
#         cert_type_dropdown = ttk.Combobox(other_certificate_window, values=cert_type_options, textvariable=cert_type_var, state="readonly")
#         cert_type_dropdown.pack(pady=5)

#         # Fees Bar
#         fees_label = tk.Label(other_certificate_window, text="Fees", font=("Arial", 12), bg="white")
#         fees_label.pack(pady=10)

#         fees_var = tk.DoubleVar(value=0)
#         fees_entry = tk.Entry(other_certificate_window, textvariable=fees_var, font=("Arial", 12))
#         fees_entry.pack(pady=5)

#         # Reason Entry
#         reason_label = tk.Label(other_certificate_window, text="Enter Reason", font=("Arial", 12), bg="white")
#         reason_label.pack(pady=10)

#         reason_entry = tk.Entry(other_certificate_window, font=("Arial", 12))
#         reason_entry.pack(pady=5)

#         # Number of Copies Frame
#         copies_frame = tk.Frame(other_certificate_window, bg="white")
#         copies_frame.pack(pady=10)

#         copies_label = tk.Label(copies_frame, text="Number of Copies", font=("Arial", 12), bg="white")
#         copies_label.pack(side="left")

#         copies_options = list(range(1, 11))
#         copies_var = tk.IntVar(value=copies_options[0])
#         copies_dropdown = ttk.Combobox(copies_frame, values=copies_options, textvariable=copies_var, state="readonly", width=2)
#         copies_dropdown.pack(side="left")

#         # Apply Button
#         apply_button = tk.Button(other_certificate_window, text="Apply", bg="yellow", font=("Arial", 12))
#         apply_button.pack(pady=10)

#     # Buttons for Bonofide and Other Certificate
#     bonofide_button = tk.Button(new_window, text="Bonofide Certificate", command=open_bonofide_window)
#     bonofide_button.pack(pady=10)

#     other_certificate_button = tk.Button(new_window, text="Other Certificate", command=open_other_certificate_window)
#     other_certificate_button.pack(pady=10)
    
# # Function to open message
# def open_message_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("MESSAGE")
#     new_window.geometry("360x640")

#     # Create a maroon-colored footer at the top
#     footer_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     footer_frame.pack(side="top", fill="x")

#     # message classlabel
#     message_label = tk.Label(footer_frame, text="MESSAGE", fg="white", bg="maroon", font=("Arial", 16))
#     message_label.pack(side="top", pady=5)

# # Function to open railway concession apply
# def open_Railway_Concession_Apply_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("Railway Concession Apply")
#     new_window.geometry("360x640")

#     # Create a maroon-colored footer at the top
#     footer_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     footer_frame.pack(side="top", fill="x")

#     # Railway Concession Apply class label
#     Railway_Concession_Apply_label = tk.Label(footer_frame, text="Railway Concession Apply", fg="white", bg="maroon", font=("Arial", 16))
#     Railway_Concession_Apply_label.pack(side="top", pady=5)

#     # Create a button in the footer with the name "New Application" and maroon background, white text
#     new_app_button = tk.Button(footer_frame, text="New Application", bg="maroon", fg="white", font=("Arial", 12))
#     new_app_button.pack(side="bottom", pady=5)

# # Function to open itle
# def open_ITLE_window():
#     new_window = tk.Toplevel(root)
#     new_window.title("ITLE")
#     new_window.geometry("360x640")

#     # Create a maroon-colored footer at the top
#     footer_frame = tk.Frame(new_window, bg="maroon", height=50, width=360)
#     footer_frame.pack(side="top", fill="x")

#     # ITLE classlabel
#     ITLE_label = tk.Label(footer_frame, text="SUBJECT", fg="white", bg="maroon", font=("Arial", 16))
#     ITLE_label.pack(side="top", pady=5)


# # Create 14 small image buttons without text below them
# create_button1("images/button1.jpg", 0, 0, open_attendance_window)
# create_button1("images/button2.jpg", 0, 1, open_schedule_window)
# create_button1("images/button3.jpg", 0, 2, open_onlineclass_window)
# create_button1("images/button4.jpg", 0, 3, open_examtimetable_window)

# create_button1("images/button5.jpg", 1, 0, open_examhallticket_window)
# create_button1("images/button6.jpg", 1, 1, open_result_window)
# create_button1("images/button7.jpg", 1, 2, open_internalmark_window)
# create_button1("images/button8.jpg", 1, 3, open_FeesPaid_window)

# create_button1("images/button9.jpg", 2, 0, open_registersubject_window)
# create_button1("images/button10.jpg", 2, 1, open_CareerWorkshop_window)
# create_button1("images/button11.jpg", 2, 2, open_Certificate_window)
# create_button1("images/button12.jpg", 2, 3, open_message_window)

# create_button1("images/button13.jpg", 3, 0, open_Railway_Concession_Apply_window)
# create_button1("images/button14.jpg", 3, 1, open_ITLE_window)

# root.mainloop()

# ##############################################################################
# import tkinter as tk
# from PIL import Image, ImageTk

# def next_image(event=None):
#     global current_image_index
#     current_image_index = (current_image_index + 1) % len(images)
#     canvas.itemconfig(image_item, image=images[current_image_index])

# def prev_image(event=None):
#     global current_image_index
#     current_image_index = (current_image_index - 1) % len(images)
#     canvas.itemconfig(image_item, image=images[current_image_index])

# root = tk.Tk()
# root.title("Slideable Image")

# # Create a canvas below the header
# canvas = tk.Canvas(root, bg="white", width=600, height=120)
# canvas.pack()

# # Add slideable image (replace the path with your image path)
# image_paths = ["images/img1.jpg", "images/img2.jpg"]
# images = [Image.open(path) for path in image_paths]
# images = [image.resize((600, 100)) for image in images]
# images = [ImageTk.PhotoImage(image) for image in images]

# current_image_index = 0
# image_item = canvas.create_image(0, 0, anchor="nw", image=images[current_image_index])

# # Bind mouse clicks to change images
# canvas.tag_bind(image_item, "<Button-1>", lambda event: next_image())

# # Bind arrow keys for image navigation
# root.bind("<Right>", next_image)
# root.bind("<Left>", prev_image)

# root.mainloop()

########################################################3

# import tkinter as tk

# # Create the main window
# root = tk.Tk()
# root.geometry("300x200")

# # Create a frame to contain the canvas and scrollbars
# button_frame = tk.Frame(root)
# button_frame.pack(fill="both", expand=True)

# # Create a canvas for vertical scrolling
# canvas = tk.Canvas(button_frame, bg="#e6e6e6", width=280, height=180)  # Adjusted canvas size
# canvas.pack(side="left", fill="both", expand=True)  # Expand both horizontally and vertically

# # Add scrollbar for vertical scrolling
# scrollbar_vertical = tk.Scrollbar(button_frame, orient="vertical", command=canvas.yview)
# scrollbar_vertical.pack(side="right", fill="y")

# # Link the scrollbars to the canvas
# canvas.config(yscrollcommand=scrollbar_vertical.set)

# # Create a frame to hold the content
# content_frame = tk.Frame(canvas, bg="#e6e6e6")

# # Add the frame to the canvas
# canvas.create_window((0, 0), window=content_frame, anchor="nw")

# # Update the scroll region
# content_frame.update_idletasks()
# canvas.config(scrollregion=canvas.bbox("all"))

# # Add horizontal scrollbar to canvas for slideable images
# hbar = tk.Scrollbar(button_frame, orient="horizontal", command=canvas.xview)
# hbar.pack(side="bottom", fill="x")
# canvas.config(xscrollcommand=hbar.set)

# root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk

# # Create a Tkinter window
# splash = tk.Tk()
# splash.title("Splash Screen")

# # Load image
# image_path = ""  # Change this to your image path
# image = Image.open(image_path)
# image = image.resize((400, 533))  # Resizing without ANTIALIAS for simplicity
# photo = ImageTk.PhotoImage(image)

# # Display image on splash screen
# label = tk.Label(splash, image=photo, bg="maroon")
# label.image = photo  # keep a reference
# label.place(relx=0.5, rely=0.5, anchor="center")

# # Run the Tkinter event loop
# splash.mainloop()

# from PIL import Image, ImageTk
# import tkinter as tk

# # Function to close the splash screen
# def close_splash():
#     splash.destroy()
#     root.deiconify()  # Show the main window after splash screen closes

# # Create the main window
# root = tk.Tk()
# root.title("Ruia Student Diary")
# root.geometry("600x800")
# root.minsize(600, 800)
# root.maxsize(600, 800)
# root.withdraw()  # Hide main window until splash screen closes

# # Create a splash screen window
# splash = tk.Toplevel(root)
# splash.overrideredirect(True)  # Remove window decorations
# splash.geometry("600x800")
# splash.configure(bg="maroon")

# # Load image
# image_path = "C:\\Users\\Admin\\Documents\\GitHub\\Student-College-Diary-App\\images\\clg_logo.jpg"  # Change this to your image path
# image = Image.open(image_path)
# image = image.resize((400, 533))  # Resizing without ANTIALIAS for simplicity
# photo = ImageTk.PhotoImage(image)

# # Display image on splash screen
# label = tk.Label(splash, image=photo, bg="maroon")
# label.image = photo  # Keep a reference to the image object
# label.place(relx=0.5, rely=0.5, anchor="center")

# # Close splash screen after 2 seconds
# splash.after(2000, close_splash)

# root.mainloop()


# # # Run the Tkinter event loop
# # root.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk

# # Create the main window
# splash = tk.Tk()

# # Load the image file
# try:
#     image = Image.open("C:\\Users\\Admin\\Documents\\GitHub\\Student-College-Diary-App\\images\\clg_logo.jpg")  # Replace "path_to_your_image_file.jpg" with the actual path to your image file
# except FileNotFoundError:
#     print("Image file not found.")
#     splash.destroy()
#     exit()

# # Resize the image if needed
# # image = image.resize((width, height), Image.ANTIALIAS)  # Replace "width" and "height" with your desired dimensions

# # Convert the Image object into a Tkinter PhotoImage object
# photo = ImageTk.PhotoImage(image)

# # Create a label widget to display the image
# label = tk.Label(splash, image=photo, bg="maroon")
# label.image = photo  # Keep a reference to the image object
# label.place(relx=0.5, rely=0.5, anchor="center")

# # Run the Tkinter event loop
# splash.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk

# # Create the main window
# header = tk.Tk()

# # Load the small image
# small_image_path = "C:\\Users\\Admin\\Documents\\GitHub\\Student-College-Diary-App\\images\\clg_logo.jpg"  # Change this to your small image path
# try:
#     small_image = Image.open(small_image_path)
# except FileNotFoundError:
#     print("Small image file not found.")
#     header.destroy()
#     exit()

# # Resize the small image
# small_image = small_image.resize((50, 50))  # Resizing the image

# # Convert the small image object into a Tkinter PhotoImage object
# small_photo = ImageTk.PhotoImage(small_image)

# # Create a label widget to display the small image on the right side
# small_image_label = tk.Label(header, image=small_photo, bg="maroon")
# small_image_label.image = small_photo  # Keep a reference to the small image object
# small_image_label.pack(side="right", padx=10, pady=10)

# # Run the Tkinter event loop
# header.mainloop()



# import tkinter as tk

# # Create the main window
# splash = tk.Tk()

# # Load the image file
# try:
#     photo = tk.PhotoImage(file="C:\\Users\\Admin\\Documents\\GitHub\\Student-College-Diary-App\\images\\clg_logo.jpg")  # Replace "path_to_your_image_file.gif" with the actual path to your image file
# except tk.TclError:
#     print("Image file not found.")
#     splash.destroy()
#     exit()

# # Create a label widget to display the image
# label = tk.Label(splash, image=photo, bg="maroon")
# label.place(relx=0.5, rely=0.5, anchor="center")

# # Run the Tkinter event loop
# splash.mainloop()
