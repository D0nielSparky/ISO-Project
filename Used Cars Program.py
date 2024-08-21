import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor


class UsedCarsPredictionApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Boston House Price Prediction')
        self.data = pd.read_csv('Used_Cars.csv')
        self.sliders = []

        self.X = self.data.drop('Price', axis=1).values
        self.y = self.data['Price'].values

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2,
                                                                                random_state=42)

        self.model = KNeighborsRegressor()
        self.model.fit(self.X_train, self.y_train)

        self.year_text = tk.Spinbox(self.master, width=17, from_=2001, to=2024)
        self.FuelType_text = ttk.Combobox(self.master, state='readonly', width=17)
        self.FuelType_text['values'] = ('Petrol', 'Diesel', 'CNG')
        self.FuelType_text.current(0)
        self.Transmission_text = ttk.Combobox(self.master, state='readonly', width=17)
        self.Transmission_text['values'] = ('Manual', 'Automatic')
        self.Transmission_text.current(0)
        self.Mileage_text = tk.Spinbox(self.master, width=17, from_=0, to=9999)
        self.Engine_text = tk.Spinbox(self.master, width=17, from_=0, to=9999)
        self.Power_text = tk.Spinbox(self.master, width=17, from_=0, to=9999)
        self.Seats_text = tk.Spinbox(self.master, width=17, from_=2, to=8)
        self.New_Price_text = tk.Spinbox(self.master, width=17, from_=0, to=9999)

        self.year_text.grid(row=0, column=1)
        self.FuelType_text.grid(row=1, column=1)
        self.Transmission_text.grid(row=2, column=1)
        self.Mileage_text.grid(row=3, column=1)
        self.Engine_text.grid(row=4, column=1)
        self.Power_text.grid(row=5, column=1)
        self.Seats_text.grid(row=6, column=1)
        self.New_Price_text.grid(row=7, column=1)
        for i, column in enumerate(self.data.columns[:-1]):
            label = tk.Label(self.master, text=column + ': ')
            label.grid(row=i, column=0)

        predict_button = tk.Button(self.master, text='Predict Price', command=self.predict_price)
        predict_button.grid(row=len(self.data.columns[:-1]), columnspan=3)

    def predict_price(self):
        inputs = []
        transmission = self.Transmission_text.get()
        fuel_type = self.FuelType_text.get()
        seats = int(self.Seats_text.get())

        if fuel_type == 'Diesel':
            fuel_type = 1
        if fuel_type == 'Petrol':
            fuel_type = 2
        if fuel_type == 'CNG':
            fuel_type = 2
        if transmission == 'Manual':
            transmission = 1
        if transmission == 'Automatic':
            transmission = 2
        try:
            inputs.append(int(self.year_text.get()))
            inputs.append(fuel_type)
            inputs.append(transmission)
            inputs.append(float(self.Mileage_text.get()))
            inputs.append(float(self.Engine_text.get()))
            inputs.append(float(self.Power_text.get()))
            inputs.append(seats)
            inputs.append(float(self.New_Price_text.get()))
            price = self.model.predict([inputs])
            messagebox.showinfo('Predicted Price', f'The predicted house price is ${price[0]:.2f}')
        except ValueError:
            messagebox.showinfo('Input Error', 'Inputs must be an Integer')


if __name__ == '__main__':
    root = tk.Tk()
    app = UsedCarsPredictionApp(root)
    root.mainloop()
