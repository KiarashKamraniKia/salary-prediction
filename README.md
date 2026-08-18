# 🏠 Tehran Sadeghiyeh House Price Prediction

A machine learning project for predicting residential property prices in **Sadeghiyeh, Tehran**, using real-world housing advertisements collected from Divar.

The project follows an end-to-end machine learning workflow:

**Web Scraping → EDA → Data Cleaning → Preprocessing → Feature Analysis → Modeling → Cross-Validation → Evaluation → Model Comparison**

---

## 📌 Project Overview

The goal of this project is to develop a supervised machine learning model for estimating residential property prices in the Sadeghiyeh neighborhood of Tehran.

The target variable is:

* `Price`

The input features include:

* Area
* Year of Construction
* Number of Rooms
* Floor Number
* Parking
* Warehouse
* Elevator

The project covers the complete process from real-world data collection to machine learning model evaluation and comparison.

---

## 🗂️ Data Collection

The housing data was collected from **Divar** using automated web scraping with:

* Selenium
* Chrome WebDriver
* WebDriver Manager

The scraper collects property advertisements from Sadeghiyeh residential listings and extracts information such as area, construction year, rooms, floor, amenities, and price.

The data collection script is available in:

```text
data_collector.py
```

The collected dataset contains:

* **320 records**
* **8 features**

---

## 📊 Dataset Features

| Feature                | Description                         |
| ---------------------- | ----------------------------------- |
| `Area`                 | Property area                       |
| `Year Of Construction` | Construction year                   |
| `Room`                 | Number of rooms                     |
| `Floor Number`         | Floor of the property               |
| `Parking`              | Whether parking is available        |
| `Warehouse`            | Whether a storage room is available |
| `Elevator`             | Whether an elevator is available    |
| `Price`                | Property price — target variable    |

---

## 🔍 Exploratory Data Analysis

Exploratory data analysis was performed to investigate the relationships between property characteristics and price.

The analysis showed that:

* `Area` has the strongest relationship with `Price`
* The correlation between `Area` and `Price` is approximately **0.83**
* `Room` has a positive relationship with price
* `Year Of Construction` has a moderate positive relationship with price
* `Floor Number` has a weaker relationship with price

---

## 🧹 Data Preprocessing

The preprocessing workflow includes:

* Checking missing values
* Converting numerical columns to appropriate numeric types
* Handling invalid values
* Detecting and removing outliers
* Imputing missing values
* Preparing features for machine learning
* Using pipeline-based preprocessing to reduce data leakage

---

## 🤖 Machine Learning Models

Six regression models were trained and compared:

1. Ridge Regression
2. Lasso Regression
3. Random Forest
4. Gradient Boosting
5. Support Vector Regression (SVR)
6. K-Nearest Neighbors (KNN)

The models were evaluated using **5-Fold Cross Validation**.

---

## 📈 Model Results

| Model             |       MAE |       R² |
| ----------------- | --------: | -------: |
| Ridge             |     0.361 |     0.56 |
| Lasso             |     0.361 |     0.56 |
| Random Forest     |     0.166 |     0.77 |
| Gradient Boosting |     0.202 |     0.63 |
| **SVR**           | **0.186** | **0.79** |
| KNN               |     0.188 |     0.78 |

### 🏆 Best Model

**Support Vector Regression (SVR)** achieved the highest reported R² score:

```text
R² = 0.79
MAE = 0.186
```

Random Forest and KNN also achieved strong performance with R² scores of **0.77** and **0.78**, respectively.

---

## 🔄 Machine Learning Pipeline

```text
                 ┌─────────────────────┐
                 │   Divar Listings    │
                 └──────────┬──────────┘
                            │
                            ▼
                    Web Scraping
                       Selenium
                            │
                            ▼
                    Data Collection
                            │
                            ▼
                         EDA
                            │
                            ▼
                    Data Cleaning
                            │
                            ▼
                    Preprocessing
                            │
                            ▼
                 Feature Preparation
                            │
                            ▼
              ┌─────────────────────────┐
              │    Regression Models    │
              ├─────────────────────────┤
              │ Ridge                   │
              │ Lasso                   │
              │ Random Forest           │
              │ Gradient Boosting       │
              │ SVR                     │
              │ KNN                     │
              └────────────┬────────────┘
                           │
                           ▼
                  5-Fold Cross Validation
                           │
                           ▼
                    Model Evaluation
                           │
                           ▼
                  Model Comparison
```

---

## 📁 Project Structure

```text
salary-prediction/
│
├── Sadeghiyeh.ipynb
├── data_collector.py
├── AI_project_report.pdf
└── README.md
```

### `Sadeghiyeh.ipynb`

Main Jupyter Notebook containing:

* Data analysis
* Data preprocessing
* Visualization
* Model training
* Cross-validation
* Model evaluation
* Model comparison

### `data_collector.py`

Selenium-based web scraping script used to collect housing advertisements from Divar.

### `AI_project_report.pdf`

Detailed project report containing the methodology, analysis, experiments, and results.

---

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Selenium
* Chrome WebDriver
* WebDriver Manager
* Jupyter Notebook

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/KiarashKamraniKia/salary-prediction.git
cd salary-prediction
```

### 2. Install dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn selenium webdriver-manager jupyter
```

### 3. Run the data collector

```bash
python data_collector.py
```

The scraper collects property information and saves the resulting data.

### 4. Open the notebook

```bash
jupyter notebook
```

Then open:

```text
Sadeghiyeh.ipynb
```

---

## 🌐 Interactive Application

An interactive Streamlit application was also developed as part of the project to estimate property prices based on user-provided property characteristics.

The application allows users to enter:

* Area
* Floor
* Number of rooms
* Year of construction
* Parking
* Warehouse
* Elevator

and receive an estimated property price.

---

## ⚠️ Limitations

This project focuses specifically on properties in **Sadeghiyeh, Tehran** and is based on a dataset of **320 listings**.

Therefore, the model should be considered an experimental property price estimation system rather than a general-purpose real estate valuation system.

Model performance may vary when applied to:

* Other neighborhoods
* Different time periods
* Larger datasets
* Different market conditions

---

## 🔮 Future Improvements

Potential improvements include:

* Collecting a larger number of listings
* Expanding the dataset to additional Tehran neighborhoods
* Adding geographic and location-based features
* Incorporating additional property characteristics
* Hyperparameter optimization
* Testing advanced ensemble methods
* Deploying the final model as a production API
* Improving the interactive web application

---

## 📄 Project Report

A detailed project report is included in:

```text
AI_project_report.pdf
```

It provides additional information about the methodology, experiments, analysis, and results.

---

## 👨‍💻 Authors

**Kiarash KamraniKia**
Computer Engineering — Bu-Ali Sina University

