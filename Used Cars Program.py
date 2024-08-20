import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

class UsedCarsPredictionApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Boston House Price Prediction')
        self.data = pd.read_csv('Used_Cars.csv')
        self.sliders = []

        self.X = self.data.drop('Price', axis=1).values
        self.y = self.data['Price'].values

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        self.model = KNeighborsRegressor()
        self.model.fit(self.X_train, self.y_train)

        self.create_widgets()

    def create_widgets(self):
        year_text = tk.Text(self.master, height=1, width=15)
        FuelType_text = ttk.Combobox(self.master, state='readonly', width=17)
        FuelType_text['values'] = ('Petrol', 'Diesel', 'CNG')
        FuelType_text.current(0)
        Transmission_text = ttk.Combobox(self.master, state='readonly', width=17)
        Transmission_text['values'] = ('Manual', 'Automatic')
        Transmission_text.current(0)
        Mileage_text = tk.Text(self.master, height=1, width=15)
        Engine_text = tk.Text(self.master, height=1, width=15)
        Power_text = tk.Text(self.master, height=1, width=15)
        Seats_text = ttk.Combobox(self.master, state='readonly', width=17)
        Seats_text['values'] = ('2', '4', '5', '6', '7', '8')
        Seats_text.current(0)
        New_Price_text = tk.Text(self.master, height=1, width=15)

        year_text.grid(row=0, column=4)
        FuelType_text.grid(row=1, column=4)
        Transmission_text.grid(row=2, column=4)
        Mileage_text.grid(row=3, column=4)
        Engine_text.grid(row=4, column=4)
        Power_text.grid(row=5, column=4)
        Seats_text.grid(row=6, column=4)
        New_Price_text.grid(row=7, column=4)
        for i, column in enumerate(self.data.columns[:-1]):
            label = tk.Label(self.master, text=column + ': ')
            label.grid(row=i, column=0)
            current_val_label = tk.Label(self.master, text='0.0')
            current_val_label.grid(row=i, column=2)
            slider = ttk.Scale(self.master, from_=self.data[column].min(), to=self.data[column].max(), orient="horizontal",
                               command=lambda val, label=current_val_label: label.config(text=f'{float(val):.2f}'))
            slider.grid(row=i, column=1)
            self.sliders.append((slider, current_val_label))

        predict_button = tk.Button(self.master, text='Predict Price', command=self.predict_price)
        predict_button.grid(row=len(self.data.columns[:-1]), columnspan=3)

    def predict_price(self):
        inputs = []
        #year = year_text.get
        #inputs.append(float(year_text.get))
        inputs = [float(slider.get()) for slider, _ in self.sliders]
        price = self.model.predict([inputs])
        messagebox.showinfo('Predicted Price', f'The predicted house price is ${price[0]:.2f}')


if __name__ == '__main__':
    root = tk.Tk()
    app = UsedCarsPredictionApp(root)
    root.mainloop()
