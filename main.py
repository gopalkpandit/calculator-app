import calculator
import tkinter as tk

def calculate():
    a = int(entry1.get())
    b = int(entry2.get())

    result.set("Add: " + str(calculator.add(a, b)))
    result.set(result.get() + "\nSub: " + str(calculator.sub(a, b)))
    result.set(result.get() + "\nMult: " + str(calculator.mult(a, b)))
    result.set(result.get() + "\nDivision: " + str(calculator.divide(a, b)))

root = tk.Tk()
root.title("Calculator App")
root.geometry("300x250")
root.configure(bg="lightblue")

entry1 = tk.Entry(root, font=("Arial",14))
entry1.pack(pady=10)

entry2 = tk.Entry(root, font=("Arial",14) )
entry2.pack(pady=10)

result = tk.StringVar()

btn = tk.Button ( root, text="Add", bg="green", fg="white", command=calculate)
btn.pack(pady=10)

label = tk.Label(root, textvariable=result, bg="lightblue", font=("Arial",14))
label.pack()

root.mainloop()