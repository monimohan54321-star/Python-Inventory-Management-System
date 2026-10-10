import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import json
import os

# =========================================================
# INVENTORY MANAGEMENT SYSTEM
# Python + Tkinter + Pillow + JSON
# =========================================================

root = tk.Tk()
root.title("Inventory Management System")
root.geometry("1000x650")
root.minsize(900, 600)

DATA_FILE = "products.json"

products = []
product_images = []


# =========================================================
# JSON FUNCTIONS
# =========================================================

def save_products():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4)


def load_products():
    global products

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                products = json.load(file)
        except (json.JSONDecodeError, OSError):
            products = []
    else:
        products = []


load_products()


# =========================================================
# LOGIN
# =========================================================

def show_login():

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#2F66C5")

    # Login background image
    try:
        image = Image.open("59308.jpg")

        # Use fixed size matching your window
        image = image.resize(
            (1000, 650),
            Image.Resampling.LANCZOS
        )

        background_photo = ImageTk.PhotoImage(image)

        background_label = tk.Label(
            root,
            image=background_photo
        )

        background_label.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        background_label.image = background_photo

    except Exception as e:
        print("Background image error:", e)

    # Login form
    login_frame = tk.Frame(
        root,
        bg="white",
        padx=45,
        pady=30
    )

    login_frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    tk.Label(
        login_frame,
        text="INVENTORY MANAGEMENT SYSTEM",
        font=("Arial", 20, "bold"),
        bg="white",
        fg="#24549C"
    ).grid(
        row=0,
        column=0,
        columnspan=3,
        pady=(0, 25)
    )

    # Username
    tk.Label(
        login_frame,
        text="USERNAME",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#24549C"
    ).grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )

    username_entry = tk.Entry(
        login_frame,
        font=("Arial", 12),
        width=25
    )

    username_entry.grid(
        row=1,
        column=1,
        columnspan=2,
        padx=10,
        pady=10
    )

    # Password
    tk.Label(
        login_frame,
        text="PASSWORD",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#24549C"
    ).grid(
        row=2,
        column=0,
        padx=10,
        pady=10
    )

    password_entry = tk.Entry(
        login_frame,
        font=("Arial", 12),
        width=21,
        show="*"
    )

    password_entry.grid(
        row=2,
        column=1,
        padx=(10, 0),
        pady=10
    )

    def show_password():

        if password_entry.cget("show") == "*":
            password_entry.config(show="")
        else:
            password_entry.config(show="*")

    tk.Button(
        login_frame,
        text="👁",
        font=("Arial", 11),
        width=3,
        command=show_password
    ).grid(
        row=2,
        column=2,
        padx=5,
        pady=10
    )

    def login():

        username = username_entry.get().strip()
        password = password_entry.get()

        if username == "admin" and password == "1234":
            open_dashboard()
        else:
            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password."
            )

    def clear_login():

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        username_entry.focus()

    tk.Button(
        login_frame,
        text="LOGIN",
        font=("Arial", 12, "bold"),
        bg="#28A745",
        fg="white",
        width=12,
        command=login
    ).grid(
        row=3,
        column=0,
        pady=20
    )

    tk.Button(
        login_frame,
        text="CLEAR",
        font=("Arial", 12, "bold"),
        bg="#FF8C00",
        fg="white",
        width=12,
        command=clear_login
    ).grid(
        row=3,
        column=1,
        pady=20
    )

    username_entry.focus()


# =========================================================
# ADD PRODUCT
# =========================================================

def add_product():

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#2F66C5")

    tk.Label(
        root,
        text="ADD PRODUCT",
        font=("Arial", 24, "bold"),
        bg="#2F66C5",
        fg="white"
    ).pack(pady=20)

    form_frame = tk.Frame(
        root,
        bg="white",
        padx=40,
        pady=20
    )

    form_frame.pack()

    def create_entry(row, text):

        tk.Label(
            form_frame,
            text=text,
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#24549C"
        ).grid(
            row=row,
            column=0,
            padx=15,
            pady=8
        )

        entry = tk.Entry(
            form_frame,
            font=("Arial", 12),
            width=25
        )

        entry.grid(
            row=row,
            column=1,
            padx=15,
            pady=8
        )

        return entry

    product_id_entry = create_entry(0, "PRODUCT ID")
    product_name_entry = create_entry(1, "PRODUCT NAME")
    category_entry = create_entry(2, "CATEGORY")
    quantity_entry = create_entry(3, "QUANTITY")
    price_entry = create_entry(4, "PRICE")
    supplier_entry = create_entry(5, "SUPPLIER")

    # Product Image
    tk.Label(
        form_frame,
        text="PRODUCT IMAGE",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#24549C"
    ).grid(
        row=6,
        column=0,
        padx=15,
        pady=8
    )

    image_path = tk.StringVar()

    image_name_label = tk.Label(
        form_frame,
        text="No image selected",
        bg="white",
        fg="#777777",
        width=25,
        anchor="w"
    )

    image_name_label.grid(
        row=6,
        column=1,
        padx=15,
        pady=8
    )

    def upload_image():

        path = filedialog.askopenfilename(
            title="Select Product Image",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png")
            ]
        )

        if path:
            image_path.set(path)

            image_name_label.config(
                text=os.path.basename(path)
            )

    tk.Button(
        form_frame,
        text="UPLOAD IMAGE",
        font=("Arial", 11, "bold"),
        bg="#24549C",
        fg="white",
        command=upload_image
    ).grid(
        row=6,
        column=2,
        padx=5,
        pady=8
    )

    # Submit
    def submit_product():

        product_id = product_id_entry.get().strip()
        product_name = product_name_entry.get().strip()
        category = category_entry.get().strip()
        quantity = quantity_entry.get().strip()
        price = price_entry.get().strip()
        supplier = supplier_entry.get().strip()
        image = image_path.get()

        if not product_id or not product_name or not category:
            messagebox.showwarning(
                "Missing Information",
                "Please enter Product ID, Product Name and Category."
            )
            return

        if not quantity.isdigit():
            messagebox.showwarning(
                "Invalid Quantity",
                "Quantity must be a number."
            )
            return

        try:
            float(price)
        except ValueError:
            messagebox.showwarning(
                "Invalid Price",
                "Price must be a number."
            )
            return

        for product in products:

            if product[0] == product_id:

                messagebox.showerror(
                    "Duplicate Product ID",
                    "This Product ID already exists."
                )

                return

        product = [
            product_id,
            product_name,
            category,
            quantity,
            price,
            supplier,
            image
        ]

        products.append(product)

        save_products()

        messagebox.showinfo(
            "Success",
            "Product added successfully."
        )

        view_products()

    tk.Button(
        form_frame,
        text="SUBMIT",
        font=("Arial", 12, "bold"),
        bg="#28A745",
        fg="white",
        width=12,
        command=submit_product
    ).grid(
        row=7,
        column=1,
        padx=15,
        pady=20
    )

    # Back
    tk.Button(
        form_frame,
        text="BACK",
        font=("Arial", 12, "bold"),
        bg="#FF8C00",
        fg="white",
        width=12,
        command=open_dashboard
    ).grid(
        row=8,
        column=1,
        padx=15,
        pady=8
    )


# =========================================================
# VIEW PRODUCTS
# =========================================================

def view_products():

    global product_images

    for widget in root.winfo_children():
        widget.destroy()

    product_images = []

    root.configure(bg="#F4F6F9")

    tk.Label(
        root,
        text="VIEW PRODUCTS",
        font=("Arial", 24, "bold"),
        bg="#F4F6F9",
        fg="#24549C"
    ).pack(pady=20)

    table_frame = tk.Frame(
        root,
        bg="white",
        bd=1,
        relief="solid"
    )

    table_frame.pack(
        fill="both",
        expand=True,
        padx=25,
        pady=10
    )

    headings = [
        "Product ID",
        "Product Name",
        "Category",
        "Quantity",
        "Price",
        "Supplier",
        "Image"
    ]

    widths = [
        12,
        18,
        15,
        10,
        12,
        18,
        12
    ]

    # Heading
    for i, heading in enumerate(headings):

        tk.Label(
            table_frame,
            text=heading,
            font=("Arial", 10, "bold"),
            bg="#24549C",
            fg="white",
            width=widths[i],
            pady=10
        ).grid(
            row=0,
            column=i
        )

    if not products:

        tk.Label(
            table_frame,
            text="No products available.",
            font=("Arial", 13),
            bg="white",
            fg="#777777"
        ).grid(
            row=1,
            column=0,
            columnspan=7,
            pady=40
        )

    # Product rows
    for row_index, product in enumerate(products, start=1):

        for column_index in range(6):

            tk.Label(
                table_frame,
                text=product[column_index],
                font=("Arial", 10),
                bg="white",
                width=widths[column_index]
            ).grid(
                row=row_index,
                column=column_index,
                padx=2,
                pady=5
            )

        image_path = product[6]

        if image_path and os.path.exists(image_path):

            try:

                image = Image.open(image_path)

                image.thumbnail(
                    (60, 60),
                    Image.Resampling.LANCZOS
                )

                photo = ImageTk.PhotoImage(image)

                product_images.append(photo)

                tk.Label(
                    table_frame,
                    image=photo,
                    bg="white",
                    width=70,
                    height=60
                ).grid(
                    row=row_index,
                    column=6,
                    padx=2,
                    pady=5
                )

            except Exception:

                tk.Label(
                    table_frame,
                    text="Image Error",
                    bg="white",
                    fg="red",
                    width=12
                ).grid(
                    row=row_index,
                    column=6
                )

        else:

            tk.Label(
                table_frame,
                text="No Image",
                font=("Arial", 10),
                bg="white",
                fg="#777777",
                width=12
            ).grid(
                row=row_index,
                column=6,
                padx=2,
                pady=5
            )

    # Back
    tk.Button(
        root,
        text="BACK",
        font=("Arial", 12, "bold"),
        bg="#FF8C00",
        fg="white",
        width=12,
        command=open_dashboard
    ).pack(pady=15)


# =========================================================
# UPDATE PRODUCT
# =========================================================

def update_product():

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#2F66C5")

    tk.Label(
        root,
        text="UPDATE PRODUCT",
        font=("Arial", 24, "bold"),
        bg="#2F66C5",
        fg="white"
    ).pack(pady=20)

    form_frame = tk.Frame(
        root,
        bg="white",
        padx=40,
        pady=20
    )

    form_frame.pack()

    # Product ID
    tk.Label(
        form_frame,
        text="PRODUCT ID",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#24549C"
    ).grid(
        row=0,
        column=0,
        padx=15,
        pady=8
    )

    product_ids = [
        product[0]
        for product in products
    ]

    product_id_var = tk.StringVar()

    product_id_box = ttk.Combobox(
        form_frame,
        textvariable=product_id_var,
        values=product_ids,
        font=("Arial", 12),
        width=23,
        state="readonly"
    )

    product_id_box.grid(
        row=0,
        column=1,
        padx=15,
        pady=8
    )

    def create_update_entry(row, text):

        tk.Label(
            form_frame,
            text=text,
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#24549C"
        ).grid(
            row=row,
            column=0,
            padx=15,
            pady=8
        )

        entry = tk.Entry(
            form_frame,
            font=("Arial", 12),
            width=25
        )

        entry.grid(
            row=row,
            column=1,
            padx=15,
            pady=8
        )

        return entry

    product_name_entry = create_update_entry(
        1,
        "PRODUCT NAME"
    )

    category_entry = create_update_entry(
        2,
        "CATEGORY"
    )

    quantity_entry = create_update_entry(
        3,
        "QUANTITY"
    )

    price_entry = create_update_entry(
        4,
        "PRICE"
    )

    supplier_entry = create_update_entry(
        5,
        "SUPPLIER"
    )

    # Image
    tk.Label(
        form_frame,
        text="PRODUCT IMAGE",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#24549C"
    ).grid(
        row=6,
        column=0,
        padx=15,
        pady=8
    )

    image_path = tk.StringVar()

    image_name_label = tk.Label(
        form_frame,
        text="No image selected",
        bg="white",
        fg="#777777",
        width=25,
        anchor="w"
    )

    image_name_label.grid(
        row=6,
        column=1,
        padx=15,
        pady=8
    )

    def upload_image():

        path = filedialog.askopenfilename(
            title="Select Product Image",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png")
            ]
        )

        if path:

            image_path.set(path)

            image_name_label.config(
                text=os.path.basename(path)
            )

    tk.Button(
        form_frame,
        text="CHANGE IMAGE",
        font=("Arial", 11, "bold"),
        bg="#24549C",
        fg="white",
        command=upload_image
    ).grid(
        row=6,
        column=2,
        padx=5,
        pady=8
    )

    # Select product
    def select_product(event=None):

        selected_id = product_id_var.get()

        for product in products:

            if product[0] == selected_id:

                product_name_entry.delete(
                    0,
                    tk.END
                )

                product_name_entry.insert(
                    0,
                    product[1]
                )

                category_entry.delete(
                    0,
                    tk.END
                )

                category_entry.insert(
                    0,
                    product[2]
                )

                quantity_entry.delete(
                    0,
                    tk.END
                )

                quantity_entry.insert(
                    0,
                    product[3]
                )

                price_entry.delete(
                    0,
                    tk.END
                )

                price_entry.insert(
                    0,
                    product[4]
                )

                supplier_entry.delete(
                    0,
                    tk.END
                )

                supplier_entry.insert(
                    0,
                    product[5]
                )

                image_path.set(
                    product[6]
                )

                if product[6]:

                    image_name_label.config(
                        text=os.path.basename(
                            product[6]
                        )
                    )

                else:

                    image_name_label.config(
                        text="No image selected"
                    )

                break

    product_id_box.bind(
        "<<ComboboxSelected>>",
        select_product
    )

    # Save update
    def save_update():

        selected_id = product_id_var.get()

        if not selected_id:

            messagebox.showwarning(
                "Select Product",
                "Please select a Product ID."
            )

            return

        for i, product in enumerate(products):

            if product[0] == selected_id:

                quantity = quantity_entry.get().strip()
                price = price_entry.get().strip()

                if not quantity.isdigit():

                    messagebox.showwarning(
                        "Invalid Quantity",
                        "Quantity must be a number."
                    )

                    return

                try:

                    float(price)

                except ValueError:

                    messagebox.showwarning(
                        "Invalid Price",
                        "Price must be a number."
                    )

                    return

                products[i] = [
                    selected_id,
                    product_name_entry.get().strip(),
                    category_entry.get().strip(),
                    quantity,
                    price,
                    supplier_entry.get().strip(),
                    image_path.get()
                ]

                save_products()

                messagebox.showinfo(
                    "Success",
                    "Product updated successfully."
                )

                view_products()

                return

    tk.Button(
        form_frame,
        text="SAVE UPDATE",
        font=("Arial", 12, "bold"),
        bg="#28A745",
        fg="white",
        width=15,
        command=save_update
    ).grid(
        row=7,
        column=1,
        padx=15,
        pady=8
    )

    tk.Button(
        form_frame,
        text="BACK",
        font=("Arial", 12, "bold"),
        bg="#FF8C00",
        fg="white",
        width=15,
        command=open_dashboard
    ).grid(
        row=8,
        column=1,
        padx=15,
        pady=8
    )


# =========================================================
# DELETE PRODUCT
# =========================================================

def delete_product():

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#2F66C5")

    tk.Label(
        root,
        text="DELETE PRODUCT",
        font=("Arial", 24, "bold"),
        bg="#2F66C5",
        fg="white"
    ).pack(pady=20)

    form_frame = tk.Frame(
        root,
        bg="white",
        padx=40,
        pady=30
    )

    form_frame.pack()

    tk.Label(
        form_frame,
        text="PRODUCT ID",
        font=("Arial", 12, "bold"),
        bg="white",
        fg="#24549C"
    ).grid(
        row=0,
        column=0,
        padx=15,
        pady=15
    )

    product_ids = [
        product[0]
        for product in products
    ]

    product_id_var = tk.StringVar()

    product_id_box = ttk.Combobox(
        form_frame,
        textvariable=product_id_var,
        values=product_ids,
        font=("Arial", 12),
        width=23,
        state="readonly"
    )

    product_id_box.grid(
        row=0,
        column=1,
        padx=15,
        pady=15
    )

    def confirm_delete():

        selected_id = product_id_var.get()

        if not selected_id:

            messagebox.showwarning(
                "Select Product",
                "Please select a Product ID."
            )

            return

        answer = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this product?"
        )

        if not answer:
            return

        for product in products:

            if product[0] == selected_id:

                products.remove(product)
                break

        save_products()

        messagebox.showinfo(
            "Deleted",
            "Product deleted successfully."
        )

        view_products()

    tk.Button(
        form_frame,
        text="DELETE",
        font=("Arial", 12, "bold"),
        bg="#DC3545",
        fg="white",
        width=15,
        command=confirm_delete
    ).grid(
        row=1,
        column=1,
        padx=15,
        pady=15
    )

    tk.Button(
        form_frame,
        text="BACK",
        font=("Arial", 12, "bold"),
        bg="#FF8C00",
        fg="white",
        width=15,
        command=open_dashboard
    ).grid(
        row=2,
        column=1,
        padx=15,
        pady=15
    )


# =========================================================
# LOGOUT
# =========================================================

def logout():

    answer = messagebox.askyesno(
        "Logout",
        "Are you sure you want to logout?"
    )

    if answer:
        show_login()


# =========================================================
# DASHBOARD
# =========================================================

def open_dashboard():

    for widget in root.winfo_children():
        widget.destroy()

    root.configure(bg="#F4F6F9")

    # Sidebar
    sidebar = tk.Frame(
        root,
        bg="#24549C",
        width=220
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)

    tk.Label(
        sidebar,
        text="INVENTORY\nMANAGEMENT",
        font=("Arial", 18, "bold"),
        bg="#24549C",
        fg="white",
        justify="center"
    ).pack(
        pady=35
    )

    tk.Frame(
        sidebar,
        bg="white",
        height=2
    ).pack(
        fill="x",
        padx=25,
        pady=5
    )

    def sidebar_button(text, command):

        tk.Button(
            sidebar,
            text="  " + text,
            font=("Arial", 12, "bold"),
            bg="#24549C",
            fg="white",
            activebackground="#1B417A",
            activeforeground="white",
            bd=0,
            anchor="w",
            width=20,
            command=command
        ).pack(
            pady=8,
            padx=10
        )

    sidebar_button(
        "HOME",
        open_dashboard
    )

    sidebar_button(
        "ADD PRODUCT",
        add_product
    )

    sidebar_button(
        "VIEW PRODUCTS",
        view_products
    )

    sidebar_button(
        "UPDATE PRODUCT",
        update_product
    )

    sidebar_button(
        "DELETE PRODUCT",
        delete_product
    )

    tk.Button(
        sidebar,
        text="  LOGOUT",
        font=("Arial", 12, "bold"),
        bg="#DC3545",
        fg="white",
        activebackground="#B52A37",
        activeforeground="white",
        bd=0,
        anchor="w",
        width=20,
        command=logout
    ).pack(
        side="bottom",
        pady=25,
        padx=10
    )

    # Main area
    main_frame = tk.Frame(
        root,
        bg="#F4F6F9"
    )

    main_frame.pack(
        side="left",
        fill="both",
        expand=True
    )

    heading_frame = tk.Frame(
        main_frame,
        bg="#F4F6F9"
    )

    heading_frame.pack(
        fill="x",
        padx=30,
        pady=25
    )

    tk.Label(
        heading_frame,
        text="Dashboard",
        font=("Arial", 26, "bold"),
        bg="#F4F6F9",
        fg="#24549C"
    ).pack(
        side="left"
    )

    tk.Label(
        heading_frame,
        text="Welcome to Inventory Management System",
        font=("Arial", 11),
        bg="#F4F6F9",
        fg="#666666"
    ).pack(
        side="right",
        pady=8
    )

    # Summary cards
    cards_frame = tk.Frame(
        main_frame,
        bg="#F4F6F9"
    )

    cards_frame.pack(
        fill="x",
        padx=30
    )

    total_products = len(products)

    total_quantity = 0

    for product in products:

        try:
            total_quantity += int(product[3])

        except (ValueError, TypeError):
            pass

    categories = set()

    for product in products:

        if len(product) > 2 and product[2]:
            categories.add(product[2])

    card_data = [
        (
            "TOTAL PRODUCTS",
            total_products,
            "#24549C"
        ),
        (
            "TOTAL QUANTITY",
            total_quantity,
            "#28A745"
        ),
        (
            "CATEGORIES",
            len(categories),
            "#FF8C00"
        )
    ]

    for title_text, value, value_color in card_data:

        card = tk.Frame(
            cards_frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            card,
            text=title_text,
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#777777"
        ).pack(
            pady=(20, 5)
        )

        tk.Label(
            card,
            text=str(value),
            font=("Arial", 26, "bold"),
            bg="white",
            fg=value_color
        ).pack(
            pady=(0, 20)
        )

    # Information panel
    info_frame = tk.Frame(
        main_frame,
        bg="white",
        bd=1,
        relief="solid"
    )

    info_frame.pack(
        fill="both",
        expand=True,
        padx=38,
        pady=25
    )

    tk.Label(
        info_frame,
        text="Welcome to your Inventory Dashboard",
        font=("Arial", 22, "bold"),
        bg="white",
        fg="#24549C"
    ).pack(
        pady=(70, 15)
    )

    tk.Label(
        info_frame,
        text=(
            "Manage products, quantities, prices, suppliers "
            "and images from the menu on the left."
        ),
        font=("Arial", 12),
        bg="white",
        fg="#666666"
    ).pack(
        pady=10
    )

    tk.Label(
        info_frame,
        text="ADD PRODUCT - Enter a new inventory item",
        font=("Arial", 11),
        bg="white",
        fg="#777777"
    ).pack(
        pady=5
    )

    tk.Label(
        info_frame,
        text="VIEW PRODUCTS - View your inventory",
        font=("Arial", 11),
        bg="white",
        fg="#777777"
    ).pack(
        pady=5
    )

    tk.Label(
        info_frame,
        text="UPDATE / DELETE - Manage existing products",
        font=("Arial", 11),
        bg="white",
        fg="#777777"
    ).pack(
        pady=5
    )


# =========================================================
# START PROGRAM
# =========================================================

show_login()

root.mainloop()