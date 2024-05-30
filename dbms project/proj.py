import mysql.connector
import tkinter as tk
from tkinter import messagebox

def sqlmain():
# Establish connection to MySQL
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="system",
        database="project"
    )
def login(uid,passwd) :
   
    # Assume 'input_data' contains the data inputted by the user


    # Create a cursor object to interact with the database
    mycursor = mydb.cursor()

    # SQL query to insert data into the table
    
   
    #mycursor.execute("select * from login");
    sql = "select uid from login where uid =%s"
    val = (uid,)
    mycursor.execute(sql, val)
    r=mycursor.fetchall()

    
    if r:
        print("existing user")
        messagebox.showinfo("Login successful", "Login successful")

        
    else:
        print("new user id created!")
        messagebox.showinfo("Account created", "New user account created")

        sql = "INSERT INTO login VALUES (%s,%s)"
        val = (uid,passwd)
        mycursor.execute(sql, val)
        mycursor.execute("select * from login")
        records=mycursor.fetchall()
        for i in records:
            print(i)


    mydb.commit()
    
  
    dashboard()

def on_submit_login(uid_entry, passwd_entry):
    global userid
    userid = uid_entry.get()
    passwd = passwd_entry.get()
    print(userid,passwd)
    login(userid,passwd)

def dashboard():   #create canvas and  fetch stuff from db
    global photo_images,window
    count=1
    x_offset=0
    mycursor = mydb.cursor()
    sql = "select * from product"
    mycursor.execute(sql)
    r1=mycursor.fetchall()
    
    window = tk.Toplevel()
    window.title("Product Page")
    
    '''image_path=tk.PhotoImage(file="C:/Users/Admin/Desktop/dbms project/pbg4.png")
    bg_image=tk.Label(window,image=image_path)
    bg_image.place(relheight=1,relwidth=1)'''

    header_frame = tk.Frame(window, bg="#333333")
    header_frame.pack(fill="x")  # Pack to the top and stretch horizontally

    # Create a large heading label inside the header frame
    welcome_label = tk.Label(header_frame, text="WELCOME!!", font=("Helvetica", 40), fg="white", bg="#333333", padx=20, pady=10)
    welcome_label.pack()

    canvas_width = 800
    canvas_height = 600
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)  #canvas is within window 'window'
    

    canvas.pack()
    for i in r1:
        dashboard_pdt_boxes(i[0],i[1],i[2],i[3],canvas, x_offset,count)
        x_offset=x_offset+250
        count+=1
    window.mainloop()
        
def dashboard_pdt_boxes(pid,pname,qty,price,canvas, x_offset,count): 
 #creating the boxes for the pdts
    from PIL import ImageTk, Image
    global photo_images
    x1 = 50 + x_offset
    y1 =200  # Top-left corner
    x2 = 250 + x_offset
    y2 = 380  # Bottom-right corner

    # Create the rectangle on the canvas
    canvas.create_rectangle(x1, y1, x2, y2, outline="black")

    # Define the text to be displayed inside the rectangle
    text = f"PID: {pid}\n {pname}\n Qty: {qty}\nPrice: {price}"  # Concatenate pid with the text

    # Calculate the center coordinates of the rectangle
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    print(center_x,center_y)

    
    # Create a Label widget inside the rectangle
  
    label = tk.Label(canvas, text=text, font=("Helvetica", 10,"bold"))
    label.place(x=center_x, y=center_y, anchor="center")

    
        #image
    if (count==1):
        img = Image.open("C:/Users/Admin/Desktop/dbms project/lap1.png")
        # Create a button inside the rectangle
        button1 = tk.Button(canvas, text="Add to cart", command=lambda:on_submit_dashboard(canvas,pid,pname,qty,price,button1,center_x,center_y+55), 
                    bg="#4CAF50", fg="white",        # Background and foreground colors
                    font=("Helvetica", 12, "bold"),  # Font settings
                    relief=tk.RAISED,                # Button relief style
                    bd=2,                            # Border width
                    padx=5, pady=5) 
        canvas.create_window(center_x, center_y + 55, window=button1)
    elif count==2:
        img = Image.open("C:/Users/Admin/Desktop/dbms project/lap2.png")
         # Create a button inside the rectangle
        button2 = tk.Button(canvas, text="Add to cart", command=lambda:on_submit_dashboard(canvas,pid,pname,qty,price,button2,center_x,center_y+55), 
                    bg="#4CAF50", fg="white",        # Background and foreground colors
                    font=("Helvetica", 12, "bold"),  # Font settings
                    relief=tk.RAISED,                # Button relief style
                    bd=2,                            # Border width
                    padx=5, pady=5)  
        canvas.create_window(center_x, center_y + 55, window=button2)
    elif count==3:
        img = Image.open("C:/Users/Admin/Desktop/dbms project/lap3.png")
         # Create a button inside the rectangle
        button3 = tk.Button(canvas, text="Add to cart", command=lambda:on_submit_dashboard(canvas,pid,pname,qty,price,button3,center_x,center_y+55), 
                    bg="#4CAF50", fg="white",        # Background and foreground colors
                    font=("Helvetica", 12, "bold"),  # Font settings
                    relief=tk.RAISED,                # Button relief style
                    bd=2,                            # Border width
                    padx=5, pady=5)        
        canvas.create_window(center_x, center_y + 55, window=button3)
    
    #view cart
    #viewcart=tk.Button(window,text="VIEW CART",command=lambda:on_view_cart(pid))
    viewcart= tk.Button(window, text="VIEW CART", command=lambda:on_view_cart(pid), 
                    bg="dark blue", fg="white",        # Background and foreground colors
                    font=("Helvetica", 12, "bold"),  # Font settings
                    relief=tk.RAISED,                # Button relief style
                    bd=2,                            # Border width
                    padx=5, pady=5) 
    viewcart.place(x=370,y=500)

    #make payment
 
    payment= tk.Button(window, text="PAYMENT", command=lambda:payment_fn(pid), 
                    bg="dark blue", fg="white",        # Background and foreground colors
                    font=("Helvetica", 12, "bold"),  # Font settings
                    relief=tk.RAISED,                # Button relief style
                    bd=2,                            # Border width
                    padx=5, pady=5) 
    payment.place(x=375,y=550)
    

    # Resize the image if needed (optional)
    img = img.resize((150, 150), Image.LANCZOS)

    # Convert the Image object into a Tkinter PhotoImage object
    photo_img = ImageTk.PhotoImage(img)

    # Display the image on the canvas at the specified coordinates (x, y)
    canvas.create_image(center_x,center_y-110 , image=photo_img)

    # Keep a reference to the PhotoImage object to prevent it from being garbage collected
    photo_images.append(photo_img)



def on_view_cart(pid):
    global win2
    pid1 = pid

    # Fetch cart items from the database
    mycursor = mydb.cursor()
    sql = "SELECT * FROM add_to_cart WHERE uid = %s"
    val = (userid,)
    mycursor.execute(sql, val)
    cart_items = mycursor.fetchall()
    mydb.commit()

    # Create a new top-level window for displaying the cart
    win2 = tk.Toplevel()
    win2.title("Cart")

    # Add a centered heading "CART" at the top
    heading_label = tk.Label(win2, text="CART", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white", pady=10)
    heading_label.grid(row=0, column=0, columnspan=5, sticky='ew')  # Span across all columns

    # Display cart items with headings
    row = 1  # Start row for displaying items
    headings = ["PID", "PName", "Qty", "Price"]

    # Display headings in the grid
    for col, heading in enumerate(headings):
        heading_label = tk.Label(win2, text=heading, font=("Helvetica", 12, "bold"))
        heading_label.grid(row=row, column=col, padx=10, pady=5, sticky="ew")

    row += 1  # Move to the next row for item values

    # Display cart items in the grid
    for item in cart_items:
        for col, value in enumerate(item[1:]):
            label = tk.Label(win2, text=value)
            label.grid(row=row, column=col, padx=10, pady=5, sticky="w")
            remove_item = tk.Button(win2, text="Remove item", command=lambda: remove_button(pid))
            remove_item.grid(row=row, column=4, padx=10, pady=5, sticky="e")

        row += 1

    # Update the window to display changes
    win2.update()




def remove_button(pid):
    mycursor = mydb.cursor()
    sql = "delete from add_to_cart where Pid=%s"
    val=(pid,)
    mycursor.execute(sql,val)
    mydb.commit()
    #win2.update()
    win2.destroy()
    on_view_cart(pid)
    
    
def payment_fn(pid):
    global win3
    win3 = tk.Toplevel()
    win3.title("Payment")

    # Fetch cart items from the database
    mycursor = mydb.cursor()
    sql = "SELECT * FROM add_to_cart WHERE uid = %s"
    val = (userid,)
    mycursor.execute(sql, val)
    cart_items = mycursor.fetchall()

    # Create a heading label for "CART"
    heading_label = tk.Label(win3, text="CART", font=("Helvetica", 16, "bold"),bg="green",fg="white")
    heading_label.grid(row=0, column=0, columnspan=4, pady=10, sticky='ew')  # Span across all columns

    # Display cart items with headings
    row = 1  # Start row for displaying items
    headings = ["PID", "PName", "Qty", "Price"]

    # Display headings in the grid
    for col, heading in enumerate(headings):
        heading_label = tk.Label(win3, text=heading, font=("Helvetica", 12, "bold"))
        heading_label.grid(row=row, column=col, padx=10, pady=5, sticky="w")

    row += 1  # Move to the next row for item values

    # Display cart items in the grid
    for item in cart_items:
        for col, value in enumerate(item[1:]):
            label = tk.Label(win3, text=value)
            label.grid(row=row, column=col, padx=10, pady=5, sticky="w")

        row += 1

    # Calculate total price
    mycursor.execute("SELECT SUM(Price) FROM add_to_cart WHERE uid = %s", (userid,))
    total_price = mycursor.fetchone()[0]

    # Display total price label
    total_label = tk.Label(win3, text=f"Total: {total_price}", font=("Helvetica", 12, "bold"))
    total_label.grid(row=row, column=2, padx=10, pady=5, sticky="w")

    # Button for making payment
    payment_button = tk.Button(win3, text="Make Payment", bg="#4CAF50", fg="white",relief=tk.RAISED,
                               font=("Helvetica", 10, "bold"),command=payment_success)
    payment_button.grid(row=row+1, column=2, padx=10, pady=10, sticky="ew")
    


def payment_success():
    
    messagebox.showinfo("Payment successful", "Payment successful!!")
    mycursor = mydb.cursor()
    sql = "delete from add_to_cart where uid=%s"
    val=(userid,)
    mycursor.execute(sql,val)
    mydb.commit()
    win3.destroy()
    


def on_submit_dashboard(canvas,pid,pname,qty,price,button,button_pos1,button_pos2):
    from datetime import datetime

    print("Add to cart button clicked!")
    response = messagebox.askquestion("Add to cart", "Add to cart??")

    # Process the user's response
    if response == "yes":
        print(userid)
        messagebox.showinfo("Done", "Product added to cart.")
        messagebox.showinfo("Done", "Page will return to dashboard.")
        

        mycursor = mydb.cursor()
        sql = "insert into  add_to_cart values (%s,%s,%s,%s,%s)"

        val=(userid,pid,pname,qty,price,)
        mycursor.execute(sql,val)
        sql1 = "insert into  system_cart values (%s,%s,%s,%s,%s,%s)"
        val1=(userid,pid,pname,qty,price,datetime.now(),)
        mycursor.execute(sql1,val1)

        mydb.commit()
        #mycursor.execute("select * from add_to_cart")
        #r1=mycursor.fetchall()
        #for i in r1:
        #    print(i)

        
        

        
        if qty==0:
            print("hi")
            
            button.destroy()
            out_of_stock_button = tk.Label(canvas, text="Out of stock")
           # canvas.create_window()
            out_of_stock_button.place(x=button_pos1, y=button_pos2)

           
            
        elif qty>0:
            sql1="update product set Qty=%s where Pid=%s"
            val=(qty-1,pid,)
            mycursor.execute(sql1,val)
            mydb.commit()
            

        window.destroy()
        dashboard()
        
        # Add your code here to handle 'Yes' response
    else:
        pass
        # Add your code here to handle 'No' response

    # Call the function to create the first box with label and button
   # create_box_with_label_and_button(101,"laptop",3,4000,canvas, x_offset=0)

def loginwindow():
    global root
    root = tk.Tk()
    root.title("Login Form")

    # Set background color for the main window
    root.configure(bg="#d9d9d9" )  # Light gray background color

    # Heading label
    heading_label = tk.Label(root, text="Login", font=("Helvetica", 20, "bold"), bg="#333333", fg="white", padx=20, pady=10)
    heading_label.grid(row=0, column=0, columnspan=2, sticky="ew")  # Span across two columns

    # User ID entry
    tk.Label(root, text="User ID:", bg="#d9d9d9").grid(row=1, column=0, padx=10, pady=5)
    uid_entry = tk.Entry(root)
    uid_entry.grid(row=1, column=1, padx=10, pady=5)

    # Password entry
    tk.Label(root, text="Password:", bg="#d9d9d9" ).grid(row=2, column=0, padx=10, pady=5)
    passwd_entry = tk.Entry(root, show="*")  # Show '*' for password
    passwd_entry.grid(row=2, column=1, padx=10, pady=5)

    # Submit button
    submit_button = tk.Button(root, text="Login", command=lambda: on_submit_login(uid_entry, passwd_entry))
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)



    root.mainloop()
   # root.destroy()
def main():
    import tkinter as tk
    from PIL import ImageTk, Image
    sqlmain()
    loginwindow()
    
    
    

    # Close cursor and database connection
    
photo_images=[]
main()