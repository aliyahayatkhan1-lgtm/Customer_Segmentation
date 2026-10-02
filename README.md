# 👥 Customer Segmentation & Analytics Dashboard

## 📌 Project Overview

Customer Segmentation is a data analytics project that groups customers based on their demographic information and purchasing behavior.

This project uses **K-Means Clustering** to identify different customer segments and presents the results through an interactive **Streamlit dashboard**.

The dashboard helps businesses understand customer behavior and develop targeted marketing strategies.

---

## 🎯 Objectives

- Analyze customer demographics and purchasing behavior
- Identify groups of customers with similar characteristics
- Apply K-Means clustering for customer segmentation
- Visualize customer segments using interactive charts
- Identify important customer patterns
- Generate useful business insights
- Export the segmented customer dataset

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Plotly
- Streamlit

---

## 📊 Dataset Features

The dataset contains information about 50 customers.

| Feature | Description |
|---|---|
| CustomerID | Unique customer identifier |
| Age | Customer age |
| Gender | Customer gender |
| AnnualIncome | Annual income |
| SpendingScore | Customer spending score |
| PurchaseFrequency | Number of purchases |
| CategoryPreference | Preferred product category |

---

## 🤖 Machine Learning Method

### K-Means Clustering

K-Means clustering is an unsupervised machine learning algorithm used to divide customers into groups based on similarities in their characteristics.

The following features are used for clustering:

- Age
- Annual Income
- Spending Score
- Purchase Frequency

Before clustering, the numerical features are standardized using `StandardScaler`.

---

## 📈 Dashboard Features

### 📊 Overview

Displays:

- Total customers
- Average annual income
- Average spending score
- Average purchase frequency

### 🎯 Customer Segmentation

Shows the number of customers in each segment.

### 📉 Customer Behavior Analysis

Visualizes:

- Income vs Spending Score
- Age vs Spending Score
- Purchase Frequency vs Annual Income

### 🛍️ Category Preferences

Shows customer preferences across different product categories.

### 💡 Business Insights

Provides information about:

- Highest spending segment
- Highest income segment
- Most frequent purchasers

### 📥 Data Export

Users can download the segmented customer dataset as a CSV file.

---

## 🚀 How to Run the Project

### 1. Clone or download the project

Open the project folder in VS Code.

### 2. Install dependencies

```bash
pip install -r requirements.txt