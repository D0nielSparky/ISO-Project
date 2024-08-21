from Model import *
import tkinter as tk


class GUI:
    def __init__(self):
        # Main window
        self.window = tk.Tk()
        self.window.geometry("400x420")
        self.window.title("Clothes Price Predictor")

        # Frames
        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)
        self.frame5 = tk.Frame(self.window)
        self.frame6 = tk.Frame(self.window)
        self.frame7 = tk.Frame(self.window)

        # Frame 1
        self.title_label = tk.Label(self.frame1, text="Clothes Price Predictor", font=("Bookman Old Style", 18))
        self.title_label.pack()

        # Frame 2
        self.brand_label = tk.Label(self.frame2, text="Enter Brand ")
        self.brand_label.pack(pady=5)
        self.category_label = tk.Label(self.frame2, text="Enter Category ")
        self.category_label.pack(pady=5)
        self.color_label = tk.Label(self.frame2, text="Enter Color ")
        self.color_label.pack(pady=5)
        self.size_label = tk.Label(self.frame2, text="Enter Size ")
        self.size_label.pack(pady=5)
        self.material_label = tk.Label(self.frame2, text="Enter Material ")
        self.material_label.pack(pady=5)

        # Frame 3
        self.click_brand_var = tk.StringVar()
        self.click_brand_var.set("Adidas")
        self.brand_button = tk.OptionMenu(self.frame3, self.click_brand_var, "Adidas",
                                          "New Balance", "Nike", "Puma", "Reebok", "Under Armour")
        self.brand_button.pack()

        self.click_category_var = tk.StringVar()
        self.click_category_var.set("Dress")
        self.category_button = tk.OptionMenu(self.frame3, self.click_category_var, "Dress",
                                             "Jacket", "Jeans", "Shoes", "Sweater", "T-shirt")
        self.category_button.pack()

        self.click_color_var = tk.StringVar()
        self.click_color_var.set("Black")
        self.color_button = tk.OptionMenu(self.frame3, self.click_color_var, "Black",
                                          "Blue", "Green", "Red", "White", "Yellow")
        self.color_button.pack()

        self.click_size_var = tk.StringVar()
        self.click_size_var.set("L")
        self.size_button = tk.OptionMenu(self.frame3, self.click_size_var, "L",
                                         "M", "S", "XL", "XS", "XXL")
        self.size_button.pack()

        self.click_material_var = tk.StringVar()
        self.click_material_var.set("Cotton")
        self.material_button = tk.OptionMenu(self.frame3, self.click_material_var, "Cotton",
                                             "Denim", "Nylon", "Polyester", "Silk", "Wool")
        self.material_button.pack()

        # Frame 4
        self.display = tk.Text(self.frame4, bg="light green", width=30, height=10)
        self.display.pack(pady=(80, 0), padx=20)
        self.exit_button = tk.Button(self.frame4, text="Exit", command=self.window.destroy, padx=20, pady=4)
        self.exit_button.pack(pady=(10, 10))
        self.predict_button = tk.Button(self.frame4, text="Predict Price", command=self.predict_price, padx=20, pady=5)
        self.predict_button.pack(pady=(0, 10))

        # Pack Frames
        self.frame1.pack(side="top")
        self.frame2.pack(side="left")
        self.frame3.pack(side="left")
        self.frame4.pack(side="right")
        tk.mainloop()

    def predict_price(self):
        result_string = ""
        self.display.delete(0.0, tk.END)

        brand = self.click_brand_var.get()
        if brand == "Adidas":
            brand = 0
        elif brand == "New Balance":
            brand = 1
        elif brand == "Nike":
            brand = 2
        elif brand == "Puma":
            brand = 3
        elif brand == "Reebok":
            brand = 4
        else:
            brand = 5

        category = self.click_category_var.get()
        if category == "Dress":
            category = 0
        elif category == "Jacket":
            category = 1
        elif category == "Jeans":
            category = 2
        elif category == "Shoes":
            category = 3
        elif category == "Sweater":
            category = 4
        else:
            category = 5

        color = self.click_color_var.get()
        if color == "Black":
            color = 0
        elif color == "Blue":
            color = 1
        elif brand == "Green":
            color = 2
        elif color == "Red":
            color = 3
        elif color == "White":
            color = 4
        else:
            color = 5

        size = self.click_size_var.get()
        if size == "L":
            size = 0
        elif size == "M":
            size = 1
        elif size == "S":
            size = 2
        elif size == "XL":
            size = 3
        elif size == "XS":
            size = 4
        else:
            size = 5

        material = self.click_material_var.get()
        if material == "Cotton":
            material = 0
        elif brand == "Denim":
            material = 1
        elif brand == "Nylon":
            material = 2
        elif material == "Polyester":
            material = 3
        elif material == "Silk":
            material = 4
        else:
            material = 5

        disp_string = "** Price Prediction **\n\n"
        item_info = (brand, category, color, size, material)
        price_prediction = rf.predict([item_info])
        disp_string += ("The predicted price is: " + str(round(price_prediction[0], 2)))
        self.display.insert("1.0", disp_string)


GUI()
