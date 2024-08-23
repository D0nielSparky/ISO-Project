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
        self.display.delete(0.0, tk.END)
        item_info = [False]*30

        brand = self.click_brand_var.get()

        if brand == "Adidas":
            item_info[0] = True
        elif brand == "New Balance":
            item_info[1] = True
        elif brand == "Nike":
            item_info[2] = True
        elif brand == "Puma":
            item_info[3] = True
        elif brand == "Reebok":
            item_info[4] = True
        else:
            item_info[5] = True
            
        category = self.click_category_var.get()
        if category == "Dress":
            item_info[6] = True
        elif category == "Jacket":
            item_info[7] = True
        elif category == "Jeans":
            item_info[8] = True
        elif category == "Shoes":
            item_info[9] = True
        elif category == "Sweater":
            item_info[10] = True
        else:
            item_info[11] = True

        color = self.click_color_var.get()
        if color == "Black":
            item_info[12] = True
        elif color == "Blue":
            item_info[13] = True
        elif brand == "Green":
            item_info[14] = True
        elif color == "Red":
            item_info[15] = True
        elif color == "White":
            item_info[16] = True
        else:
            item_info[17] = True

        size = self.click_size_var.get()
        if size == "L":
            item_info[18] = True
        elif size == "M":
            item_info[19] = True
        elif size == "S":
            item_info[20] = True
        elif size == "XL":
            item_info[21] = True
        elif size == "XS":
            item_info[22] = True
        else:
            item_info[23] = True

        material = self.click_material_var.get()
        if material == "Cotton":
            item_info[24] = True
        elif brand == "Denim":
            item_info[25] = True
        elif brand == "Nylon":
            item_info[26] = True
        elif material == "Polyester":
            item_info[27] = True
        elif material == "Silk":
            item_info[28] = True
        else:
            item_info[29] = True

        disp_string = "** Price Prediction **\n\n"
        price_prediction = dtree.predict([item_info])
        disp_string += ("The predicted price is: " + str(round(price_prediction[0], 2)))
        self.display.insert("1.0", disp_string)


GUI()
