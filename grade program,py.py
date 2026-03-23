import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

students = []   # (name, total, avg, grade, marks)

def calculate_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    elif avg >= 60: return "C"
    elif avg >= 50: return "D"
    else: return "F"

def add_student():

    name = entry_name.get().strip()
    marks_text = entry_marks.get().strip()

    if name == "" or marks_text == "":
        messagebox.showerror("Error", "All fields required!")
        return

    try:
        marks = list(map(int, marks_text.split()))
    except:
        messagebox.showerror("Error", "Marks must be valid numbers separated by spaces")
        return

    total = sum(marks)
    avg = total / len(marks)
    grade = calculate_grade(avg)

    students.append((name, total, avg, grade, marks))

    result_box.insert(tk.END, f"{name}   | Avg: {avg:.2f}  | Grade: {grade}")

    refresh_dropdown()

    entry_name.delete(0, tk.END)
    entry_marks.delete(0, tk.END)

    entry_name.focus()   # <<< FIXED

def jump_from_name(event):
    entry_marks.focus()

def jump_from_marks(event):
    add_student()

def refresh_dropdown():
    menu = dropdown["menu"]
    menu.delete(0, "end")
    for s in students:
        menu.add_command(label=s[0], command=lambda v=s[0]: dropdown_var.set(v))

def show_graph():

    if len(students) == 0:
        messagebox.showerror("Error", "No student data available!")
        return

    names = [s[0] for s in students]
    avgs = [s[2] for s in students]

    fig = Figure(figsize=(4,3))
    fig.subplots_adjust(bottom=0.25)

    ax = fig.add_subplot(111)
    ax.set_title("Students Average Comparison")
    ax.set_xlabel("Students")
    ax.set_ylabel("Average Marks")

    ax.bar(names, avgs, width=0.4)     # thinner bars
    ax.set_xticklabels(names, rotation=20)

    fig.tight_layout()

    win2 = tk.Toplevel()
    win2.title("Class Performance Graph")

    canvas = FigureCanvasTkAgg(fig, master=win2)
    canvas.draw()
    canvas.get_tk_widget().pack()


win = tk.Tk()
win.title("Grade Management System")
win.geometry("500x520")

title = tk.Label(win, text="GRADE MANAGEMENT SYSTEM", font=("Arial", 16))
title.pack(pady=10)

tk.Label(win, text="Student Name:").pack()
entry_name = tk.Entry(win, width=40)
entry_name.pack()
entry_name.bind("<Return>", jump_from_name)

tk.Label(win, text="Marks (space separated):").pack()
entry_marks = tk.Entry(win, width=40)
entry_marks.pack()
entry_marks.bind("<Return>", jump_from_marks)

btn_add = tk.Button(win, text="Add Student", width=20, command=add_student)
btn_add.pack(pady=10)

result_box = tk.Listbox(win, width=55, height=12)
result_box.pack()

dropdown_var = tk.StringVar()
dropdown = tk.OptionMenu(win, dropdown_var, ())
dropdown.pack(pady=8)

btn_graph = tk.Button(win, text="Show Class Performance Graph", width=30, command=show_graph)
btn_graph.pack(pady=8)

entry_name.focus()
win.mainloop()





    

