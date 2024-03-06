import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
from tkcalendar import Calendar 
from tkinter import Tk, Toplevel, Canvas, Button, PhotoImage
from PIL import Image, ImageTk

# Function to open the profile page
def open_profile_page():
    # Hide the main window (root)
    root.iconify()

    # Create a new window for the profile page
    profile_page = Toplevel(root)
    profile_page.title("Profile Page")
    profile_page.geometry("600x800")
    profile_page.minsize(600, 800)
    profile_page.maxsize(600, 800)

    # Define the height of the maroon section (25% of the window height)
    maroon_height = int(profile_page.winfo_reqheight() * 0.50)

    # Create a Canvas widget
    canvas = Canvas(profile_page, width=600, height=800, bg="white")
    canvas.pack()

    # Draw the maroon section
    canvas.create_rectangle(0, 0, 600, maroon_height, fill="maroon", outline="")

    # Load the image
    # Replace with the actual path to your image
    image_path = "C:\\Users\\acer\\Pictures\\Screenshots\\Screenshot 2024-02-14 195726.jpg"
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)

    # Create an image item on the canvas
    image_item = canvas.create_image(50, maroon_height // 2, anchor="center", image=photo)

    # Keep a reference to the image to prevent it from being garbage collected
    canvas.image = photo

    # Create buttons with icons and text
    icon1 = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\OneDrive\\Desktop\\1st.jpg").resize((30, 30)))
    button1 = Button(profile_page, text="Personal Details", image=icon1, compound="left", command=open_personal_details)
    button1.image = icon1
    button1.place(relx=0.85, rely=0.3, anchor="e")

    icon2 = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\OneDrive\\Desktop\\2nd.jpg").resize((30, 30)))
    button2 = Button(profile_page, text="Contact Details", image=icon2, compound="left", command=open_contact_details)
    button2.image = icon2
    button2.place(relx=0.85, rely=0.4, anchor="e")

    icon3 = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\OneDrive\\Desktop\\3rd.jpg").resize((30, 30)))
    button3 = Button(profile_page, text="Postal Details", image=icon3, compound="left", command=open_postal_details)
    button3.image = icon3
    button3.place(relx=0.85, rely=0.5, anchor="e")

    icon4 = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\OneDrive\\Desktop\\4th.jpg").resize((30, 30)))
    button4 = Button(profile_page, text="Change Password", image=icon4, compound="left", command=open_change_password)
    button4.image = icon4
    button4.place(relx=0.85, rely=0.6, anchor="e")

    icon5 = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\OneDrive\\Desktop\\5th.jpg").resize((30, 30)))
    button5 = Button(profile_page, text="Share App", image=icon5, compound="left", command=open_share_app)
    button5.image = icon5
    button5.place(relx=0.85, rely=0.7, anchor="e")

    icon6 = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\OneDrive\\Desktop\\6th.jpg").resize((30, 30)))
    button6 = Button(profile_page, text="Rate App", image=icon6, compound="left", command=open_rate_app)
    button6.image = icon6
    button6.place(relx=0.85, rely=0.8, anchor="e")

    icon7 = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\OneDrive\\Desktop\\7th.jpg").resize((30, 30)))
    button7 = Button(profile_page, text="Log Out", image=icon7, compound="left", command=open_log_out)
    button7.image = icon7
    button7.place(relx=0.85, rely=0.9, anchor="e")

    # Create a button to go back to the main window
    back_button = Button(profile_page, text="Back to Main", command=lambda: back_to_main(profile_page))
    back_button.place(relx=0.02, rely=0.95, anchor="sw")

    # Create an "Exit" button to close the profile page
    exit_button = Button(profile_page, text="Exit", command=profile_page.destroy)
    exit_button.place(relx=0.98, rely=0.95, anchor="se")

def open_personal_details():
    # Create a new window for personal details
    personal_details_window = Toplevel(root)
    personal_details_window.title("Personal Details")
    personal_details_window.geometry("600x800")
    personal_details_window.minsize(600, 800)
    personal_details_window.maxsize(600, 800)
   

    # Load the personal details image
    personal_details_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\python\\personal_detail.jpg"  # Replace with the actual path
    personal_details_image = Image.open(personal_details_image_path)
    personal_details_image = personal_details_image.resize((500, 700))  # Adjust the size as needed
    personal_details_photo = ImageTk.PhotoImage(personal_details_image)

    # Create an image item on the window
    image_item = Canvas(personal_details_window, width=500, height=700, bg="white")
    image_item.pack()
    image_item.create_image(250, 350, anchor="center", image=personal_details_photo)

    # Keep a reference to the image to prevent it from being garbage collected
    image_item.image = personal_details_photo

    # Create a button to go back to the profile page
    back_button = Button(personal_details_window, text="Back to Profile Page", command=personal_details_window.destroy)
    back_button.pack()


def open_contact_details():
    # Create a new window for contact details
    contact_details_window = Toplevel(root)
    contact_details_window.title("Contact Details")
    contact_details_window.geometry("600x800")
    contact_details_window.minsize(600, 800)
    contact_details_window.maxsize(600, 800)

    # Load the contact details image
    contact_details_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\python\\contact_details.jpeg"  # Replace with the actual path
    contact_details_image = Image.open(contact_details_image_path)
    contact_details_image = contact_details_image.resize((500, 700))  # Adjust the size as needed
    contact_details_photo = ImageTk.PhotoImage(contact_details_image)

    # Create an image item on the window
    image_item = Canvas(contact_details_window, width=500, height=700, bg="white")
    image_item.pack()
    image_item.create_image(250, 350, anchor="center", image=contact_details_photo)

    # Keep a reference to the image to prevent it from being garbage collected
    image_item.image = contact_details_photo

    # Create a button to go back to the profile page
    back_button = Button(contact_details_window, text="Back to Profile Page", command=contact_details_window.destroy)
    back_button.pack()

def open_postal_details():
    # Create a new window for postal details
    postal_details_window = Toplevel(root)
    postal_details_window.title("Postal Details")
    postal_details_window.geometry("600x800")
    postal_details_window.minsize(600, 800)
    postal_details_window.maxsize(600, 800)

    # Load the postal details image
    postal_details_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\python\\postal_details.jpeg"  # Replace with the actual path
    postal_details_image = Image.open(postal_details_image_path)
    postal_details_image = postal_details_image.resize((500, 700))  # Adjust the size as needed
    postal_details_photo = ImageTk.PhotoImage(postal_details_image)

    # Create an image item on the window
    image_item = Canvas(postal_details_window, width=500, height=700, bg="white")
    image_item.pack()
    image_item.create_image(250, 350, anchor="center", image=postal_details_photo)

    # Keep a reference to the image to prevent it from being garbage collected
    image_item.image = postal_details_photo

    # Create a button to go back to the profile page
    back_button = Button(postal_details_window, text="Back to Profile Page", command=postal_details_window.destroy)
    back_button.pack()


def open_change_password():
    # Create a new window for change password
    change_password_window = Toplevel(root)
    change_password_window.title("Change Password")
    change_password_window.geometry("600x800")
    change_password_window.minsize(600, 800)
    change_password_window.maxsize(600, 800)

    # Load the change password image
    change_password_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\python\\password.jpeg"  # Replace with the actual path
    change_password_image = Image.open(change_password_image_path)
    change_password_image = change_password_image.resize((500, 700))  # Adjust the size as needed
    change_password_photo = ImageTk.PhotoImage(change_password_image)

    # Create an image item on the window
    image_item = Canvas(change_password_window, width=500, height=700, bg="white")
    image_item.pack()
    image_item.create_image(250, 350, anchor="center", image=change_password_photo)

    # Keep a reference to the image to prevent it from being garbage collected
    image_item.image = change_password_photo

    # Create a button to go back to the profile page
    back_button = Button(change_password_window, text="Back to Profile Page", command=change_password_window.destroy)
    back_button.pack()


def open_share_app():
    # Create a new window for sharing the app
    share_app_window = Toplevel(root)
    share_app_window.title("Share App")
    share_app_window.geometry("600x800")
    share_app_window.minsize(600, 800)
    share_app_window.maxsize(600, 800)

    # Load the share app image
    share_app_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\python\\share_app.jpeg"  # Replace with the actual path
    share_app_image = Image.open(share_app_image_path)
    share_app_image = share_app_image.resize((500, 700))  # Adjust the size as needed
    share_app_photo = ImageTk.PhotoImage(share_app_image)

    # Create an image item on the window
    image_item = Canvas(share_app_window, width=500, height=700, bg="white")
    image_item.pack()
    image_item.create_image(250, 350, anchor="center", image=share_app_photo)

    # Keep a reference to the image to prevent it from being garbage collected
    image_item.image = share_app_photo

    # Create a button to go back to the profile page
    back_button = Button(share_app_window, text="Back to Profile Page", command=share_app_window.destroy)
    back_button.pack()

def open_rate_app():
    # Create a new window for rating the app
    rate_app_window = Toplevel(root)
    rate_app_window.title("Rate App")
    rate_app_window.geometry("600x800")
    rate_app_window.minsize(600, 800)
    rate_app_window.maxsize(600, 800)

    # Load the rate app image
    rate_app_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\python\\rate_app.jpeg"  # Replace with the actual path
    rate_app_image = Image.open(rate_app_image_path)
    rate_app_image = rate_app_image.resize((500, 700))  # Adjust the size as needed
    rate_app_photo = ImageTk.PhotoImage(rate_app_image)

    # Create an image item on the window
    image_item = Canvas(rate_app_window, width=500, height=700, bg="white")
    image_item.pack()
    image_item.create_image(250, 350, anchor="center", image=rate_app_photo)

    # Keep a reference to the image to prevent it from being garbage collected
    image_item.image = rate_app_photo

    # Create a button to go back to the profile page
    back_button = Button(rate_app_window, text="Back to Profile Page", command=rate_app_window.destroy)
    back_button.pack()


def open_log_out():
    # Create a new window for log out
    log_out_window = Toplevel(root)
    log_out_window.title("Log Out")
    log_out_window.geometry("600x800")
    log_out_window.minsize(600, 800)
    log_out_window.maxsize(600, 800)

    # Load the log out image
    log_out_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\python\\logout.jpeg"  # Replace with the actual path
    log_out_image = Image.open(log_out_image_path)
    log_out_image = log_out_image.resize((500, 700))  # Adjust the size as needed
    log_out_photo = ImageTk.PhotoImage(log_out_image)

    # Create an image item on the window
    image_item = Canvas(log_out_window, width=500, height=700, bg="white")
    image_item.pack()
    image_item.create_image(250, 350, anchor="center", image=log_out_photo)

    # Keep a reference to the image to prevent it from being garbage collected
    image_item.image = log_out_photo

    # Create a button to go back to the main profile page
    back_button = Button(log_out_window, text="Back to Profile Page", command=log_out_window.destroy)
    back_button.pack()





# Function to go back to the main window
def back_to_main(profile_page):
    # Close the profile page window and show the main window (root)
    profile_page.destroy()
    root.deiconify()



def open_id_card_page():
    
    # Create a new window for the ID card page
    id_card_page = tk.Toplevel(root)
    id_card_page.title("ID Card Page")
    id_card_page.geometry("600x800")
    id_card_page.minsize(600, 800)
    id_card_page.maxsize(600, 800)

    # Load the ID card image
    id_card_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\id_image.jpeg"  # Replace with your ID card image path
    id_card_image = Image.open(id_card_image_path)
    id_card_image = id_card_image.resize((500, 700))  # Adjust the size as needed
    id_card_photo = ImageTk.PhotoImage(id_card_image)

    # Create an image label on the ID card page
    id_card_label = tk.Label(id_card_page, image=id_card_photo, bd=0)
    id_card_label.image = id_card_photo
    id_card_label.pack(pady=20)

    # Create a button to go back to the main window
    back_button = tk.Button(id_card_page, text="Back to Main", command=id_card_page.destroy)
    back_button.pack(pady=10)

def back_to_main(open_id_card_page):
    # Close the profile page window and show the main window (root)
    open_id_card_page.destroy()
    root.deiconify()

def open_notification():
    # Create a new window or perform any action you desire
    notification_window = tk.Toplevel(root)
    notification_window.title("Notifications")
    notification_window.geometry("600x800")
    notification_window.minsize(600, 800)
    notification_window.maxsize(600, 800)

    # Load the notification image
    notification_image_path = "C:\\Users\\acer\\OneDrive\\Desktop\\notification_image.jpeg"  # Replace with your image path
    notification_image = Image.open(notification_image_path)
    notification_image = notification_image.resize((500, 700))  # Adjust the size as needed
    notification_photo = ImageTk.PhotoImage(notification_image)

    # Create an image label on the notification window
    notification_image_label = tk.Label(notification_window, image=notification_photo, bd=0)
    notification_image_label.image = notification_photo
    notification_image_label.pack(pady=20)

    # Create a "Back to Main" button
    back_to_main_button = tk.Button(notification_window, text="Back to Main", command=notification_window.destroy)
    back_to_main_button.pack(side="left", padx=10, pady=10)

def back_to_main(open_notification):
    # Close the profile page window and show the main window (root)
    open_notification.destroy()
    root.deiconify()


def open_calendar():
    # Create a new window for the calendar
    calendar_window = tk.Toplevel(root)
    calendar_window.title("Calendar")
    calendar_window.geometry("600x800")
    calendar_window.minsize(600, 800)
    calendar_window.maxsize(600, 800)

    # Create a maroon section
    maroon_height = int(calendar_window.winfo_reqheight() * 0.2)
    maroon_frame = tk.Frame(calendar_window, bg="maroon", height=maroon_height, width=600)
    maroon_frame.pack(side="top", fill="both", expand=True)

    # Create a Calendar widget below the maroon section
    cal_frame = tk.Frame(calendar_window, bg="white")
    cal_frame.pack(side="bottom", fill="both", expand=True)


    # Add calender text below the maroon section
    additional_text = "Calendar"
    additional_label = tk.Label(cal_frame, text=additional_text, fg="black", bg="white", font=("Arial", 16))
    additional_label.pack(pady=10)

    cal = Calendar(cal_frame, selectmode="day", year=2024, month=2, day=16)  # Set the default date as needed
    cal.pack(pady=20)

    # Create the footer frame
    footer_frame = tk.Frame(cal_frame, bg="white", height=400, width=600)
    footer_frame.pack(side="bottom", fill="x")

    # Create a button to close the calendar window
    close_button = tk.Button(cal_frame, text="Back to main", command=calendar_window.destroy)
    close_button.pack(pady=10)

def back_to_main(open_calendar):
    # Close the profile page window and show the main window (root)
    open_calendar.destroy()
    root.deiconify()




def close_splash():
    splash.destroy()
    root.deiconify()

def get_greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 5 <= hour < 12:
        return "Good Morning,"
    elif 12 <= hour < 18:
        return "Good Afternoon,"
    else:
        return "Good Evening,"

def next_image(event):
    global current_image_index
    if current_image_index < len(images) - 1:
        current_image_index += 1
        show_image(current_image_index)

def prev_image(event):
    global current_image_index
    if current_image_index > 0:
        current_image_index -= 1
        show_image(current_image_index)

def show_image(index):
    canvas.itemconfig(image_item, image=images[index])
    canvas.config(scrollregion=canvas.bbox("all"))

def create_label(frame, text, color, font, row, column):
    label = tk.Label(frame, text=text, fg=color, font=font, bg="white")
    label.grid(row=row, column=column, rowspan=2, columnspan=3)
    return label

def create_label_header(frame, text, color, font, row, column, columnspan):
    label = tk.Label(frame, text=text, fg=color, font=font, bg="white")
    label.grid(row=row, column=column, columnspan=columnspan, rowspan=3)
    return label

def create_frame(root):
    frame = tk.Frame(root, bg="white", bd=0, relief="raised")
    frame.pack(padx=20, pady=20)
    return frame

def create_separator(frame, row, column):
    separator = ttk.Separator(frame, orient="vertical")
    separator.grid(row=row, column=column, rowspan=2, padx=(10), sticky="ns")
    return separator


def create_button(image_path, text, row, column):
    # Load small image for button
    small_button_image = Image.open(image_path)
    small_button_image = small_button_image.resize((40, 40))  # Resize the image
    small_button_photo = ImageTk.PhotoImage(small_button_image)

    # Create button
    button = tk.Button(button_frame_inner, image=small_button_photo, borderwidth=0)
    button.image = small_button_photo  # Keep a reference to prevent garbage collection
    button.grid(row=row, column=column, padx=5, pady=5)

    # Add text below button
    text_label = tk.Label(button_frame_inner, text=text, bg="#e6e6e6")
    text_label.grid(row=row + 1, column=column, pady=(0, 5))

# Create the main window
root = tk.Tk()
root.title("Ruia Student Diary")
root.geometry("600x800")
root.minsize(600, 800)
root.maxsize(600, 800)
root.withdraw()  # Hide main window until splash screen closes

# Create a splash screen window
splash = tk.Toplevel(root)
splash.overrideredirect(True)  # Remove window decorations
splash.geometry("600x800")
splash.configure(bg="maroon")

# Load image
image_path = "images/college_logo.jpg"  # Change this to your image path
image = Image.open(image_path)
image = image.resize((400, 533))  # Resizing without ANTIALIAS for simplicity
photo = ImageTk.PhotoImage(image)

# Display image on splash screen
label = tk.Label(splash, image=photo, bg="maroon")
label.image = photo  # keep a reference
label.place(relx=0.5, rely=0.5, anchor="center")

# Close splash screen after 2 seconds
splash.after(2000, close_splash)

# Get greeting message
greeting = get_greeting()

# Create header
header = tk.Frame(root, bg="maroon", height=120, width=600)
header.pack(fill="x")

# Create label for greeting
greeting_label = tk.Label(header, text=greeting, fg="white", bg="maroon", font=("Arial", 16))
greeting_label.pack(side="left", padx=10, anchor="w")

# Student name (replace "Student Name" with actual name)
student_name = "Jagveer Kaur"
name_label = tk.Label(header, text=student_name, fg="white", bg="maroon", font=("Arial", 16))
name_label.pack(side="left", padx=10, anchor="w")

# Load small image on the right side
small_image_path = "images/college_logo.jpg"  # Change this to your small image path
small_image = Image.open(small_image_path)
small_image = small_image.resize((50, 50))  # Resizing the image
small_photo = ImageTk.PhotoImage(small_image)

small_image_label = tk.Label(header, image=small_photo, bg="maroon")
small_image_label.image = small_photo  # keep a reference
small_image_label.pack(side="right", padx=10, pady=10)

# Create a section below the header with a single slideable image
canvas = tk.Canvas(root, bg="white", width=600, height=120)
canvas.pack()

# Add slideable image (replace the path with your image path)
image_paths = ["images/image1.jpg", "images/image2.jpg", "images/image3.jpg", "images/image4.jpg"]
images = []
for path in image_paths:
    image = Image.open(path)
    image = image.resize((600, 100))  # Adjust size as needed
    images.append(ImageTk.PhotoImage(image))

current_image_index = 0
image_item = canvas.create_image(0, 0, anchor="nw", image=images[current_image_index])
canvas.itemconfig(image_item, tags=("image",))

# Text below the slideable image
college_text = "Ramnarian Ruia Autonomous College"
college_label = tk.Label(root, text=college_text, font=("Arial", 12), bg="white")
college_label.pack()

# Rectangle below the college text (for Attendance, Theory, Practical, Overall)
rectangle1 = tk.Frame(root, bg="#e6e6e6", height=120)
rectangle1.pack(fill="x", pady=10)

# Text on the rectangle1
attendance_text = "Attendance"
theory_text = "Theory"
practical_text = "Practical"
overall_text = "Overall"

attendance_label = tk.Label(rectangle1, text=attendance_text, font=("Arial", 12), bg="#e6e6e6", anchor="center")
attendance_label.grid(row=0, column=1, padx=5, pady=10)

theory_label = tk.Label(rectangle1, text=theory_text, font=("Arial", 12), bg="#e6e6e6", anchor="w")
theory_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

practical_label = tk.Label(rectangle1, text=practical_text, font=("Arial", 12), bg="#e6e6e6", anchor="w")
practical_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

overall_label = tk.Label(rectangle1, text=overall_text, font=("Arial", 12), bg="#e6e6e6", anchor="w")
overall_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Horizontal bars beside each text on rectangle1
theory_bar = tk.Canvas(rectangle1, bg="white", height=20, width=100, bd=0, highlightthickness=0)
theory_bar.create_rectangle(0, 0, 100, 20, fill="green")
theory_bar.grid(row=1, column=1, padx=(5, 10), pady=5)

practical_bar = tk.Canvas(rectangle1, bg="white", height=20, width=100, bd=0, highlightthickness=0)
practical_bar.create_rectangle(0, 0, 50, 20, fill="blue")
practical_bar.grid(row=2, column=1, padx=(5, 10), pady=5)

overall_bar = tk.Canvas(rectangle1, bg="white", height=20, width=100, bd=0, highlightthickness=0)
overall_bar.create_rectangle(0, 0, 75, 20, fill="red")
overall_bar.grid(row=3, column=1, padx=(5, 10), pady=5)

# Rectangle for small image buttons
rectangle2 = tk.Frame(root, bg="#e6e6e6")
rectangle2.pack(fill="both", expand=True)

# Create a frame to hold the buttons
button_frame = tk.Frame(rectangle2, bg="#e6e6e6")
button_frame.pack(fill="both", expand=True, padx=5, pady=5)

# Create a canvas for vertical scrolling
canvas = tk.Canvas(button_frame, bg="#e6e6e6")
canvas.pack(side="left", fill="both", expand=True)  # Expand both horizontally and vertically

# Add scrollbar for vertical scrolling
scrollbar = tk.Scrollbar(button_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Create a frame to hold the buttons
button_frame_inner = tk.Frame(canvas, bg="#e6e6e6")

# Add the frame to the canvas
canvas.create_window((0, 0), window=button_frame_inner, anchor="nw")

# Leave space for 4x4 small image buttons
# Create 14 small image buttons with text below them
button_frame_outer = tk.Frame(root, bg="#e6e6e6")
button_frame_outer.pack(padx=10, pady=10)

button_frame_inner = tk.Frame(button_frame_outer, bg="#e6e6e6")
button_frame_inner.pack()

# Create small image buttons with text below them in a 4x4 grid
create_button("images/button1.jpg", "Att", 0, 0)
create_button("images/button2.jpg", "Button 2", 0, 1)
create_button("images/button3.jpg", "Button 3", 0, 2)
create_button("images/button4.jpg", "Button 4", 0, 3)

create_button("images/button5.jpg", "Button 5", 1, 0)
create_button("images/button6.jpg", "Button 6", 1, 1)
create_button("images/button7.jpg", "Button 7", 1, 2)
create_button("images/button8.jpg", "Button 8", 1, 3)

create_button("images/button9.jpg", "Button 9", 2, 0)
create_button("images/button10.jpg", "Button 10", 2, 1)
create_button("images/button11.jpg", "Button 11", 2, 2)
create_button("images/button12.jpg", "Button 12", 2, 3)

create_button("images/button13.jpg", "Button 13", 3, 0)
create_button("images/button14.jpg", "Button 14", 3, 1)

# Update the scroll region
button_frame_inner.update_idletasks()
canvas.config(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))

# Add horizontal scrollbar to canvas for slideable images
hbar = tk.Scrollbar(root, orient="horizontal")
hbar.pack(side="bottom", fill="x")
hbar.config(command=canvas.xview)
canvas.config(xscrollcommand=hbar.set)

# Create footer frame
footer_frame = tk.Frame(root, bg="white", height=100, width=600)
footer_frame.pack(side="bottom", fill="x")

# Draw semi-circle void
semi_circle_canvas = tk.Canvas(footer_frame, bg="white", width=600, height=50, highlightthickness=0)
semi_circle_canvas.pack()

# Draw maroon button in the void
maroon_button = tk.Button(footer_frame, text="Maroon", bg="maroon", fg="white", width=10)
maroon_button.place(relx=0.5, rely=0.5, anchor="center")

# Draw house symbol button
# Draw maroon circular button in the void with house icon in the center
house_image = Image.open("images/house.jpg")  # Replace with your house symbol image
house_image = house_image.resize((40, 40))  # Adjust the size of the house icon
house_icon = ImageTk.PhotoImage(house_image)

def on_enter(event):
    house_button.config(bg="brown")

def on_leave(event):
    house_button.config(bg="maroon")

house_button = tk.Button(footer_frame, image=house_icon, bg="maroon", bd=0, width=50, height=50, compound="center")  # Adjust the button width and height
house_button.image = house_icon
house_button.place(relx=0.5, rely=0.5, anchor="center")
house_button.bind("<Enter>", on_enter)
house_button.bind("<Leave>", on_leave)

#Draw id card button
id_card_image = Image.open("images/id_card.jpg")  # Replace with your ID card image
id_card_image = id_card_image.resize((30, 30))
id_card_icon = ImageTk.PhotoImage(id_card_image)
id_card_button = tk.Button(footer_frame, image=id_card_icon, text="ID Card", compound="top", bg="white", bd=0, command=open_id_card_page)
id_card_button.image = id_card_icon
id_card_button.place(relx=0.8, rely=0.5, anchor="center")

# Draw calendar button
calendar_image = Image.open("images/calendar.jpg")  # Replace with your calendar image
calendar_image = calendar_image.resize((30, 30))
calendar_icon = ImageTk.PhotoImage(calendar_image)
calendar_button = tk.Button(footer_frame, image=calendar_icon, text="Calendar", compound="top", bg="white", bd=0, command=open_calendar)
calendar_button.image = calendar_icon
calendar_button.place(relx=0.2, rely=0.5, anchor="center")
calendar_button.config(width=40)

# Draw notification button
notification_image = Image.open("images/notification.jpg")  # Replace with your notification image
notification_image = notification_image.resize((30, 30))
notification_icon = ImageTk.PhotoImage(notification_image)
notification_button = tk.Button(footer_frame, image=notification_icon, text="Notification", compound="top", bg="white", bd=0, command=open_notification)
notification_button.image = notification_icon
notification_button.place(relx=0.4, rely=0.5, anchor="center")

# Draw profile button
profile_image = Image.open("images/profile.jpg")  # Replace with your profile image
profile_image = profile_image.resize((30, 30))
profile_icon = ImageTk.PhotoImage(profile_image)
profile_button = tk.Button(footer_frame, image=profile_icon, text="Profile", compound="top", bg="white", bd=0, command=open_profile_page)
profile_button.image = profile_icon
profile_button.place(relx=0.6, rely=0.5, anchor="center")


# Create the section for Outstanding Fees
outstanding_fees_frame = create_frame(root)

# Create the labels for Outstanding Fees
title_label = create_label_header(outstanding_fees_frame, "Outstanding Fees", None, ("Arial", 13), 0, 1, 7)

paid_label = create_label(outstanding_fees_frame, "₹0", "green", ("Arial Bold", 10), 4, 1)
paid_text = create_label(outstanding_fees_frame, " Paid Fees ", None, ("Arial", 8), 6, 1)

separator = create_separator(outstanding_fees_frame, 5, 4)

balance_label = create_label(outstanding_fees_frame, "₹0", "red", ("Arial Bold", 10), 4, 5)
balance_text = create_label(outstanding_fees_frame, "Balance Fees", None, ("Arial", 8), 6, 5)

# Run the Tkinter event loop
root.mainloop()