'''import tkinter as tk
from tkinter import ttk, messagebox

# Sample list of products (you can replace this with your actual product data)
products = [
    {"id": 1, "name": "Product A", "quantity": 10, "price": 20.99},
    {"id": 2, "name": "Product B", "quantity": 5, "price": 15.49},
    {"id": 3, "name": "Product C", "quantity": 8, "price": 25.99}
]

def add_to_cart(product_id):
    # Placeholder function to simulate adding a product to the cart
    selected_product = next((product for product in products if product["id"] == product_id), None)
    if selected_product:
        messagebox.showinfo("Success", f"Added '{selected_product['name']}' to cart!")
    else:
        messagebox.showerror("Error", "Product not found.")

def on_add_to_cart(product_id):
    add_to_cart(product_id)

def main():
    root = tk.Tk()
    root.title("Product Catalog")

    # Create Treeview widget to display products
    columns = ("Name", "ID", "Quantity", "Price", "Add to Cart")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    tree.heading("Name", text="Product Name")
    tree.heading("ID", text="ID")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.heading("Add to Cart", text="")

    # Insert products into the Treeview
    for product in products:
        item_id = product["id"]
        name = product["name"]
        quantity = product["quantity"]
        price = f"${product['price']:.2f}"

        # Create a custom style for the Add to Cart button
        style = ttk.Style()
        style.configure("Add.TButton", foreground="green", font=("Arial", 10, "bold"))

        # Create a button widget for Add to Cart
        button = ttk.Button(root, text="Add to Cart", style="Add.TButton",
                             command=lambda item_id=item_id: on_add_to_cart(item_id))

        # Insert product information and button into the Treeview
        tree.insert("", "end", values=(name, item_id, quantity, price, ""),
                    tags=(item_id,), iid=item_id)
        
        # Attach the button to the last column (Add to Cart)
        tree.window_create(tree.tag_configure(item_id), window=button)

    # Pack the Treeview widget
    tree.pack(padx=20, pady=10, fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
'''
import tkinter as tk

# Function to handle button click (placeholder function)
'''def on_submit():
    print("Submit button clicked!")  # Placeholder action for demonstration

# Function to create a box with a label and a button inside on the canvas
def create_box_with_label_and_button(pid,pname,qty,price,canvas, x_offset):
    # Define the coordinates of the rectangle (x1, y1, x2, y2) based on x_offset
    x1 = 50 + x_offset
    y1 =200  # Top-left corner
    x2 = 250 + x_offset
    y2 = 350  # Bottom-right corner

    # Create the rectangle on the canvas
    canvas.create_rectangle(x1, y1, x2, y2, outline="black")

    # Define the text to be displayed inside the rectangle
    text = f"PID: {pid}\n {pname}\n Qty: {qty}\nPrice: {price}"  # Concatenate pid with the text

    # Calculate the center coordinates of the rectangle
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    # Create a Label widget inside the rectangle
    label = tk.Label(canvas, text=text, font=("Helvetica", 10))
    label.place(x=center_x, y=center_y, anchor="center")

    # Create a button inside the rectangle
    button = tk.Button(canvas, text="Submit", command=on_submit)
    canvas.create_window(center_x, center_y + 30, window=button)

# Create a new Tkinter window
def main():
    global qty
    window = tk.Tk()
    window.title("Multiple Boxes with Label and Button Example")

    # Create a Canvas widget
    canvas_width = 800
    canvas_height = 600
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Call the function to create the first box with label and button
    create_box_with_label_and_button(101,"laptop",3,4000,canvas, x_offset=0)

    # Call the function to create the second box with label and button (adjacent)
    #create_box_with_label_and_button(canvas, x_offset=250,102)
    #create_box_with_label_and_button(canvas, x_offset=500,103)

    # Run the Tkinter event loop
    window.mainloop()
main()'''
'''
import tkinter as tk
from PIL import Image, ImageTk

# Function to load and display an image on a canvas
def display_image_on_canvas(canvas,x, y):
    # Open and load the image using PIL
    img = Image.open("C:/Users/Admin/Desktop/dbms project/lap1.png")

    # Resize the image if needed (optional)
    img = img.resize((100, 100), Image.LANCZOS)

    # Convert the Image object into a Tkinter PhotoImage object
    photo_img = ImageTk.PhotoImage(img)

    # Display the image on the canvas at the specified coordinates (x, y)
    canvas.create_image(x, y, image=photo_img, anchor=tk.NW)

    # Keep a reference to the PhotoImage object to prevent it from being garbage collected
    canvas.image = photo_img

# Create a new Tkinter window
window = tk.Tk()
window.title("Image on Canvas Example")

# Create a Canvas widget with a specified width and height
canvas_width = 400
canvas_height = 300
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Specify the path to the image file
#image_path = "path_to_your_image_file.jpg"  # Update this with your image file path

# Call the function to display the image on the canvas at coordinates (100, 50)
display_image_on_canvas(canvas, x=100, y=50)

# Run the Tkinter event loop
window.mainloop()

'''
# Import module 
from tkinter import *

# Create object 
root = Tk() 

# Adjust size 
root.geometry("400x400") 

# Add image file 
bg = PhotoImage(file = "C:/Users/Admin/Desktop/dbms project/bg3.png") 

# Create Canvas 
canvas1 = Canvas( root, width = 600, 
				height = 600) 

canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image( 0, 0, image = bg, 
					anchor = "nw") 

# Add Text 
canvas1.create_text( 200, 250, text = "Welcome") 

# Create Buttons 
button1 = Button( root, text = "Exit") 
button3 = Button( root, text = "Start") 
button2 = Button( root, text = "Reset") 

# Display Buttons 
button1_canvas = canvas1.create_window( 100, 10, 
									anchor = "nw", 
									window = button1) 

button2_canvas = canvas1.create_window( 100, 40, 
									anchor = "nw", 
									window = button2) 

button3_canvas = canvas1.create_window( 100, 70, anchor = "nw", 
									window = button3) 

# Execute tkinter 
root.mainloop() 
