import calculator
import tkinter as tk

def calculate():
    a = int(entry1.get())
    b = int(entry2.get())

    result.set("Addition: " + str(calculator.add(a, b)))
    result.set(result.get() + "\nSubstraction: " + str(calculator.sub(a, b)))
    result.set(result.get() + "\nMultiplication: " + str(calculator.mult(a, b)))
    result.set(result.get() + "\nDivision: " + str(calculator.divide(a, b)))

root = tk.Tk()
root.title("Calculator App")
root.geometry("300x250")
root.configure(bg="lightblue")

entry1 = tk.Entry(root, font=("Arial",10))
entry1.pack(pady=10)

entry2 = tk.Entry(root, font=("Arial",10) )
entry2.pack(pady=10)

result = tk.StringVar()

btn = tk.Button ( root, text="Calculate", bg="green", fg="white", command=calculate)
btn.pack(pady=10)

label = tk.Label(root, textvariable=result, bg="lightblue", font=("Arial",14))
label.pack()

root.mainloop()