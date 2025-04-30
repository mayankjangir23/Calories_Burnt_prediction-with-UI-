import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics
import pickle
import ttkbootstrap as tb
from ttkbootstrap.tooltip import ToolTip
import tkinter.messagebox as messagebox

# Load and prepare data/model
calories = pd.read_csv(r'D:\python projects\Calories_Burnt_project\calories.csv')
exercise_data = pd.read_csv(r'D:\python projects\Calories_Burnt_project\exercise.csv')

calories_data = pd.concat([exercise_data, calories['Calories']], axis=1)
calories_data.replace({'Gender': {'male': 0, 'female': 1}}, inplace=True)

X = calories_data.drop(['User_ID', 'Calories'], axis=1)
Y = calories_data['Calories']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

model = XGBRegressor()
model.fit(X_train, Y_train)

MAE = metrics.mean_absolute_error(Y_test, model.predict(X_test))
print(f"✅ Mean Absolute Error = {MAE:.4f}")

filename = 'trained_model.sav'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename, 'rb'))

class ModernCalorieApp(tb.Window):
    def __init__(self):
        super().__init__(themename="flatly")  # <--- switched to 'flatly' (clean white+blue theme)
        self.title("🔥 Calories Burnt Predictor 🔥")
        self.geometry("500x580")
        self.minsize(800, 800)
        self.resizable(True, True)
        self.configure(background="white")  # Set background to pure white
        self.setup_widgets()
        self.center_window()

    def center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def setup_widgets(self):
        # Title Label
        title = tb.Label(self, text="🔥 Calories Burnt Predictor", font=("Segoe UI Black", 22, "bold"), bootstyle="info")  # blue color
        title.pack(pady=(20, 15), fill='x')

        # Main Frame
        frame = tb.Frame(self, padding=20, bootstyle="light")
        frame.pack(padx=20, pady=10, fill='both', expand=True)

        def labeled_entry(parent, label_text, tooltip_text, row, var_type='str', default=None):
            label = tb.Label(parent, text=label_text, font=("Segoe UI", 12, 'bold'), bootstyle="primary")
            label.grid(row=row, column=0, sticky='w', pady=8)

            if var_type == 'combo':
                entry = tb.Combobox(parent, values=["male", "female"], state="readonly", bootstyle="primary")
                entry.current(0)
            else:
                entry = tb.Entry(parent, bootstyle="primary")
                if default is not None:
                    entry.insert(0, default)

            entry.grid(row=row, column=1, sticky='ew', padx=(10, 0), pady=8)
            ToolTip(label, tooltip_text)
            return entry

        # Input Fields
        self.gender_combo = labeled_entry(frame, "Gender:", "Select your gender (male/female).", 0, var_type='combo')
        self.age_entry = labeled_entry(frame, "Age (years):", "Enter your age in years.", 1)
        self.height_entry = labeled_entry(frame, "Height (cm):", "Enter your height in centimeters.", 2)
        self.weight_entry = labeled_entry(frame, "Weight (kg):", "Enter your weight in kilograms.", 3)
        self.duration_entry = labeled_entry(frame, "Duration (min):", "Duration of exercise in minutes.", 4)
        self.heart_rate_entry = labeled_entry(frame, "Heart Rate (bpm):", "Your average heart rate during exercise.", 5)
        self.body_temp_entry = labeled_entry(frame, "Body Temp (°C):", "Your body temperature in Celsius.", 6)

        frame.columnconfigure(1, weight=1)
        for i in range(7):
            frame.rowconfigure(i, weight=1)

        # Button + Result Frame (Horizontal Layout)
        action_frame = tb.Frame(self, padding=10, bootstyle="light")
        action_frame.pack(pady=20, padx=20, fill='x')

        # Calculate Button (left side)
        self.predict_btn = tb.Button(action_frame, text="Calculate Calories", bootstyle="success-outline", width=20, command=self.predict_calories)
        self.predict_btn.pack(side="left", padx=(0, 20))

        # Result Label (right side)
        self.result_label = tb.Label(action_frame, text="🔥 Predicted Calories Burnt: -- kcal", font=("Segoe UI Black", 14, 'bold'), bootstyle="info")
        self.result_label.pack(side="left", padx=10, expand=True, fill='x')

        # Clear Button (Below)
        self.clear_btn = tb.Button(self, text="Clear Inputs", bootstyle="danger-outline", width=20, command=self.clear_inputs)
        self.clear_btn.pack(pady=(0, 20))

    def clear_inputs(self):
        self.gender_combo.current(0)
        for entry in [
            self.age_entry, self.height_entry, self.weight_entry,
            self.duration_entry, self.heart_rate_entry, self.body_temp_entry
        ]:
            entry.delete(0, 'end')
        self.result_label.configure(text="🔥 Predicted Calories Burnt: -- kcal")

    def predict_calories(self):
        try:
            gender = 0 if self.gender_combo.get() == "male" else 1
            age = int(self.age_entry.get())
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            duration = float(self.duration_entry.get())
            heart_rate = float(self.heart_rate_entry.get())
            body_temp = float(self.body_temp_entry.get())

            input_data = np.array([gender, age, height, weight, duration, heart_rate, body_temp]).reshape(1, -1)
            prediction = loaded_model.predict(input_data)

            self.result_label.configure(text=f"🔥 Predicted Calories Burnt: {prediction[0]:.2f} kcal")
        except ValueError:
            messagebox.showerror("Invalid Input", "⚠️ Please enter valid numbers for all fields.")

if __name__ == "__main__":
    app = ModernCalorieApp()
    app.mainloop()