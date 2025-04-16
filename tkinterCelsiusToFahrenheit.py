import tkinter as tk

def conversion():  # Function to convert Celsius to Fahrenheit
    try:
        c = float(t.get())  # Get the Celsius input
        f = (c * 9/5) + 32   # Convert to Fahrenheit
        l2.config(text=f)   # Display the result
    except ValueError:
        l2.config(text="Invalid input")  # Handle invalid input

root = tk.Tk()  # Create the main window
root.title("Celsius to Fahrenheit Converter")

# Create and place the widgets
l1 = tk.Label(root, text="Enter Temperature in Celsius:")
l1.pack()

t = tk.Entry(root)
t.pack()

b = tk.Button(root, text="Convert", command=conversion)
b.pack()

l2 = tk.Label(root, text="Result: ")
l2.pack()

root.mainloop()  # Run the main event loop
