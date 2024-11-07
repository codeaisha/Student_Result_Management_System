from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3

class reportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="View Student Result", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626")
        title.place(x=10, y=15, width=1180, height=50)

        self.var_search = StringVar()

        # Search Section
        lbl_search = Label(self.root, text="Search By Roll No.", font=("goudy old style", 20, "bold"), bg="white").place(x=280, y=120)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20), bg="lightyellow").place(x=540, y=120, width=150)
        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=700, y=120, width=100, height=35)
        btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"), bg="gray", fg="white", cursor="hand2", command=self.clear).place(x=810, y=120, width=100, height=35)

        btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, "bold"), bg="red", fg="white", cursor="hand2", command=self.delete)
        btn_delete.place(x=500, y=350, width=100, height=35)

   

        lbl_roll = Label(self.root,text="Roll No.", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root,text="Name", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root,text="Course", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=450, y=230, width=150, height=50)
        lbl_marks = Label(self.root,text="Marks Obtained", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=600, y=230, width=160, height=50)
        lbl_full = Label(self.root,text="Total Marks", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=760, y=230, width=150, height=50)
        lbl_per = Label(self.root,text="percentage", font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=910, y=230, width=150, height=50)


        self.roll = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=160, height=50)
        self.full = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.full.place(x=760, y=280, width=150, height=50)
        self.per = Label(self.root, font=("goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=910, y=280, width=150, height=50)



    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll No. Should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row is not None:
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_search.set("")
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll No. Should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row is not None:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete this record?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM result WHERE roll=?", (self.var_search.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
                        self.clear()
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
