# ApexPlanet Internship - Task 1

## Data Immersion & Wrangling

### 📌 Objective
The objective of this project is to understand the dataset, identify data quality issues, clean the data, and prepare it for analysis using Python and Pandas.

---

## 🛠 Tools & Technologies
- Python 3
- Pandas
- OpenPyXL
- Visual Studio Code
- Microsoft Excel

---

## 📂 Dataset Information

- Rows: 1000
- Columns: 12

### Dataset Columns
- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales

---

## 🔍 Data Quality Assessment

- Found 20 missing values in the **Age** column.
- Found 13 missing values in the **City** column.
- No duplicate rows were found.
- Verified that **Total_Sales = Quantity × Unit_Price** for all records.

---

## 🧹 Data Cleaning Performed

- Converted `Order_Date` to DateTime format.
- Filled missing Age values using the median.
- Filled missing City values using the mode.
- Verified sales calculations.
- Created new features:
  - Year
  - Month
  - Quarter
  - Day_Name
- Saved the cleaned dataset.

---

## 📁 Project Files

- `ApexPlanet_DataAnalytics_Dataset.xlsx`
- `Cleaned_ApexPlanet_DataAnalytics_Dataset.xlsx`
- `Data_Cleaning.py`

---

## ▶️ How to Run

1. Install the required libraries:

```bash
python -m pip install pandas openpyxl
```

2. Run the script:

```bash
python Data_Cleaning.py
```

The cleaned dataset will be generated automatically.

---

## 👨‍💻 Author

**Aradhya Maheshwari**

BCA (Data Analytics & AI)
