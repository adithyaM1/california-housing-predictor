## 🔍 Technical Explanation: California Housing Price Prediction Model

### 🧠 Model Architecture Overview

This price prediction model uses a **Random Forest Regressor** to predict median house values in California based on 8 census-derived features. The model is implemented using **Scikit-learn**, trained on the California Housing dataset, and deployed using **Streamlit**.

---

### 📥 Input Features – Technical Deep Dive

#### 1. **MedInc** *(Median Income)*

* **Type**: Continuous float  
* **Range**: 0.5 - 15.0  
* **Unit**: Tens of thousands of USD  
* **Importance**: ~40%  
* **Insight**: Strongest positive correlation to house value.

#### 2. **HouseAge** *(Age of the houses)*

* **Type**: Continuous float  
* **Range**: 1.0 - 52.0  
* **Unit**: Years  
* **Importance**: ~7%  
* **Insight**: Newer homes tend to cost more, though patterns vary.

#### 3. **AveRooms** *(Average rooms per household)*

* **Type**: Continuous float  
* **Range**: ~0.85 - 141.91  
* **Unit**: Number of rooms  
* **Importance**: ~5%  
* **Formula**: Total_Rooms / Total_Households

#### 4. **AveBedrms** *(Average bedrooms per household)*

* **Type**: Continuous float  
* **Range**: ~0.33 - 34.07  
* **Unit**: Number of bedrooms  
* **Importance**: ~1% (Least)

#### 5. **Population**

* **Type**: Continuous float  
* **Range**: 3.0 - 35,682.0  
* **Unit**: Total people  
* **Importance**: ~3%  
* **Insight**: May imply urban vs suburban settings.

#### 6. **AveOccup** *(Average occupancy)*

* **Type**: Continuous float  
* **Range**: ~0.69 - 1243.33  
* **Unit**: People per household  
* **Importance**: ~15%  
* **Formula**: Population / Total_Households  
* **Insight**: Lower values generally point to more affluent communities.

#### 7. **Latitude**

* **Type**: Continuous float  
* **Range**: 32.54 - 41.95  
* **Unit**: Degrees North  
* **Importance**: ~14%

#### 8. **Longitude**

* **Type**: Continuous float  
* **Range**: -124.35 to -114.31  
* **Unit**: Degrees West (Negative)  
* **Importance**: ~15%

---

### 🏗️ Model Technical Specifications

* **Algorithm**: RandomForestRegressor

```python
RandomForestRegressor(
    n_estimators=100,
    max_depth=None,
    random_state=42
)
