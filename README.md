# California Housing Price Predictor

A Streamlit web application that predicts the median house value in California using a Random Forest regression model trained on the California Housing dataset.

---

## Dataset

This project uses the [California Housing dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html) from scikit-learn, which contains data collected from the 1990 U.S. Census. The dataset includes the following features:

- **MedInc**: Median income in block group
- **HouseAge**: Median house age in block group
- **AveRooms**: Average number of rooms per household
- **AveBedrms**: Average number of bedrooms per household
- **Population**: Block group population
- **AveOccup**: Average number of household members
- **Latitude**: Block group latitude
- **Longitude**: Block group longitude

The target variable is the median house value for California districts, expressed in hundreds of thousands of dollars.

---

## Features

- Interactive sidebar sliders to input feature values
- Real-time prediction of median house value based on inputs
- Display of model performance metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), and R² Score
- Model training using Random Forest Regressor
- Model saved as `housing_model.pkl` for reuse or deployment

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd california-house-prediction
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run california-housing/app.py
```

Use the sidebar sliders to adjust feature values and view the predicted median house value along with model performance metrics.

---

## Live Demo

Try the live app here: [California Housing Price Predictor](https://california-housing-predictor-wjyjpoxgxdqrkcj5xmghzl.streamlit.app/)

---

## Screenshot

![California Housing Price Predictor](screenshot.png)

---

## Model Saving

The trained Random Forest model is saved as `housing_model.pkl` in the project root directory.

---

## Contact

For any questions or feedback, please contact:

**Adithya M**  
Email: aadhithyammadhan@gmail.com  
Phone: 7676394402

---

