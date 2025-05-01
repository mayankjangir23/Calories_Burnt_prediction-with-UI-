# 🔥 Calories Burnt Predictor

A desktop application that predicts the number of calories burnt during exercise using an XGBoost machine learning model.  
The app features a modern, user-friendly interface built with ttkbootstrap (Tkinter) and provides fast, accurate predictions based on physiological and exercise data.
Features
⚡Machine Learning Powered 
  Predicts calories burnt using a trained XGBoost Regressor model.

- 🖥️Modern GUI Interface  
  Built with ttkbootstrap, offering a clean, responsive design.

- 👫Gender Input  
  Select your gender (male/female) — factored into prediction.

- 🎂Age Input
  Enter your age (in years) to adjust for metabolic rate effects.

- 📏Height Input
  Enter height (in cm) — influences body composition and calorie burn.

⚖️Weight Input
  Enter weight (in kg) — critical for energy expenditure estimation.

⏱️Exercise Duration Input
  Specify duration (in minutes) of your workout session.

❤️Heart Rate Input  
  Average heart rate (in bpm) during exercise reflects intensity.

Body Temperature Input 
  Body temp (°C) indicates exertion level, refining predictions.

Instant Predictions + Clear Output
  Get real-time calorie predictions and easily clear inputs to recalculate.

📂 Dataset

The model is trained on a merged dataset of:
Exercise Data (`exercise.csv`)
Calorie Data (`calories.csv`)

The dataset includes features like gender, age, height, weight, exercise duration, heart rate, and body temperature.

🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core Programming Language |
| XGBoost | Machine Learning Model |
| Scikit-learn | Model Training & Evaluation |
| Pandas & NumPy | Data Processing |
| Pickle | Model Persistence |
| Tkinter & ttkbootstrap | GUI Development |
