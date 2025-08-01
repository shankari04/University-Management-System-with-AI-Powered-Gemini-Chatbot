import tkinter as tk
from tkinter import Scrollbar, Label
from PIL import Image, ImageTk
import google.generativeai as genai

# Configure the Gemini API key
GEMINI_API_KEY = "AIzaSyCEdnuOR7pW__ydEyyiJD0QtOtHUufLfwg"  
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini AI Model
model = genai.GenerativeModel("gemini-1.5-flash")

# 🎯 University Knowledge Base (Modify as needed)

university_faq = {
    "exam date": "The upcoming university exams start from November 10th, 2025. Check the official website for the full schedule.",
    "fees structure": "The tuition fee for this semester is $5000. You can pay online through the university portal.",
    "faculty details": "We have experienced faculty members with PhDs in various domains. Visit the faculty page for more info.",
    "results": "Results will be announced on August 20th, 2025. Students can check their results on the university portal.",
    "leave request": "Students can apply for leave through the student portal under 'Leave Management'. Approval depends on the faculty.",
    "attendance":"You can view your attendance percentage in the student portal under 'Attendance Report'. Minimum 75% is required to sit for exams.",
    "semester result":"Semester results will be published on the official portal. Use your student ID to log in and view your grades.",
    "student details":"Student profiles including name, department, attendance, and marks can be viewed in the student dashboard.",
    "admissions":"Admissions for the next academic year begin in June 2025. Apply online through the admission section on our website.",
    "placements":"The university has an active placement cell. Top companies visit the campus from September to December every year.",
    "training and skills":"Skill development programs are available in AI, Data Science, Web Development, and more. Check the Training section in your student portal.",
    "departments":"We offer courses under departments such as CSE, AI&DS, ECE, Mechanical, Civil, and Management Studies.",
    "research":"Research opportunities are available for UG, PG, and PhD scholars. Contact your department research coordinator for more details.",
    "labs":"Our university is equipped with modern labs for AI, Robotics, IoT, Chemistry, Physics, and Computer Science.",
    "campus life":"Campus life includes student clubs, sports, tech fests, cultural events, and a vibrant learning atmosphere.",
    "attendance percentage":"You can view your attendance percentage in the student portal under 'Attendance Report'. Minimum 75% is required to sit for exams.",
    "project": "This is a University Management System desktop application developed using Java Swing and MySQL. It manages faculty, students, exams, fees, leaves, and includes an AI chatbot module.",
    "project details": "The project features modules for student and faculty management, leave requests, exam and result handling, fee management, and a chatbot that answers university-related queries.",
    "project creators": "The University Management System project was developed by Sree Shankari V, Subha Sanchitha K, and Sudalaimuthumari M.",
    "team": "The project team includes Sree Shankari V, Subha Sanchitha K, and Sudalaimuthumari M, third-year AI & DS students.",
    "about project": "Our University Management System aims to simplify administrative tasks by integrating various university operations into a single desktop application using Java and MySQL."

}

# Function to fetch chatbot response
def get_bot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for better matching
   
    # 🎯 Check if the query is university-related
    for key in university_faq:
        if key in user_input:
            return university_faq[key]  # Return predefined response

    # If not university-related, use Gemini API
    try:
        response = model.generate_content(user_input)
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to display bot response with typing effect
def type_bot_response(bot_response, index=0):
    if index < len(bot_response):
        chat_window.insert(tk.END, bot_response[index], "bot")
        chat_window.yview(tk.END)
        root.after(50, type_bot_response, bot_response, index + 1)
    else:
        chat_window.insert(tk.END, " ", "bot")
        chat_window.config(state=tk.DISABLED)

# Function to send user input and display chat
def send_message(event=None):
    user_input_text = entry_box.get().strip()
    if not user_input_text:
        return

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "\n", "user_space")
    chat_window.insert(tk.END, " " + user_input_text + " ", "user")
    chat_window.window_create(tk.END, window=user_icon_label())

    bot_response = get_bot_response(user_input_text)

    chat_window.insert(tk.END, "\n", "bot_space")
    chat_window.window_create(tk.END, window=bot_icon_label())
    chat_window.insert(tk.END, " ", "bot")
    root.after(500, type_bot_response, bot_response, 0)

    chat_window.yview(tk.END)
    entry_box.delete(0, tk.END)

# Function to create a user icon label
def user_icon_label():
    label = tk.Label(chat_window, image=user_icon, bg="#D9FDD3")
    label.image = user_icon
    return label

# Function to create a bot icon label
def bot_icon_label():
    label = tk.Label(chat_window, image=bot_icon, bg="#F1F0F0")
    label.image = bot_icon
    return label

# Creating main window
root = tk.Tk()
root.title("AI Chatbot")
root.geometry("500x600")
root.configure(bg="#EDEDED")

# Load user and bot images
user_icon_path = "C:/Users/HP/Desktop/university management sys/java/src/university/user.png"
bot_icon_path = "C:/Users/HP/Desktop/university management sys/java/src/university/botun.gif"

# Resize user and bot images
def resize_image(image_path, size=(40, 40)):
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(image)

user_icon = resize_image(user_icon_path)
bot_icon = resize_image(bot_icon_path)

# Chat window frame
chat_frame = tk.Frame(root, bg="#FFFFFF")
chat_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Chat window
chat_window = tk.Text(chat_frame, wrap=tk.WORD, font=("Arial", 12), bg="#FFFFFF", state=tk.DISABLED)
chat_window.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Apply text formatting
chat_window.tag_config("user", foreground="white", background="#0B93F6", justify="right")
chat_window.tag_config("bot", foreground="black", background="#EAEAEA", justify="left")
chat_window.tag_config("user_space", spacing1=10)
chat_window.tag_config("bot_space", spacing1=10)

# Scrollbar
scrollbar = Scrollbar(chat_frame, command=chat_window.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_window.config(yscrollcommand=scrollbar.set)

# Input Frame
input_frame = tk.Frame(root, bg="#EDEDED")
input_frame.pack(pady=5, padx=10, fill=tk.X)

# Entry box
entry_box = tk.Entry(input_frame, font=("Arial", 14), bg="#F5F5F5")
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
entry_box.bind("<Return>", send_message)

# Custom Send Button
def on_hover(event):
    send_button.config(bg="#388E3C")

def on_leave(event):
    send_button.config(bg="#4CAF50")

send_button = tk.Button(input_frame, text="➤", command=send_message, font=("Arial", 14, "bold"), 
                        bg="#4CAF50", fg="white", relief="flat", width=3, height=1)
send_button.pack(side=tk.RIGHT)

send_button.bind("<Enter>", on_hover)
send_button.bind("<Leave>", on_leave)

root.mainloop()
 