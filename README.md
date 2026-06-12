# Customer Segmentation & Churn Prediction

A customer analytics project using RFM (Recency, Frequency, Monetary) 
segmentation and machine learning to identify churn risk and prioritize 
retention efforts.

## Overview

Using transaction-level e-commerce data, this project segments customers 
into behavioral groups, predicts churn risk, and identifies which segments 
deserve retention focus based on a combination of value and risk.

## Dataset

[Online Retail II (Kaggle)](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) 
— UK-based online retailer transactions, Dec 2009–Dec 2011. 
Contains invoice-level data: Customer ID, Invoice Date, Quantity, Price, Country.

> Note: raw dataset (~25MB+) is not included in this repo. Download it 
> separately from the link above to reproduce the analysis.

## Approach

### 1. Data Cleaning
Removed records with missing Customer IDs, cancelled orders, and invalid 
(negative/zero) quantity or price values.

### 2. RFM Feature Engineering
For each of 2,671 customers, calculated:
- **Recency** — days since last purchase
- **Frequency** — number of distinct orders
- **Monetary** — total amount spent

### 3. Customer Segmentation (K-Means)
Used the elbow method to select k=4 clusters on scaled RFM values, 
producing four segments:

| Segment       | Accounts | Avg. Value  | Description                          |
|---------------|---------|-------------|---------------------------------------|
| VIP/Whale     | 5       | $103,392    | Extremely high-value, highly engaged   |
| Champions     | 29      | $16,958     | Recent, frequent, high spenders        |
| Regular       | 1,802   | $1,210      | Core customer base                     |
| At Risk/Lost  | 835     | $460        | Inactive 90+ days                      |

### 4. Churn Prediction
Defined churn as no purchase in 90+ days. Trained a Logistic Regression 
model on Frequency and Monetary (Recency excluded to avoid data leakage, 
since it directly defines the churn label).

- **Model**: Logistic Regression (class-balanced)
- **ROC-AUC**: 0.76
- **Recall (churned class)**: 0.76

A Random Forest model was also tested but underperformed (ROC-AUC 0.68), 
likely due to overfitting on only two features.

### 5. Business Insights

| Segment       | Accounts | Avg. Value | Churn Risk |
|---------------|---------|------------|------------|
| At Risk/Lost  | 835     | $460       | 59.6%      |
| Regular       | 1,802   | $1,210     | 38.5%      |
| Champions     | 29      | $16,958    | ~0%        |
| VIP/Whale     | 5       | $103,392   | ~0%        |

**Key takeaway**: The **Regular** segment represents the highest-priority 
retention opportunity — it's the largest group, holds meaningful value, and 
carries significant churn risk. A small reduction in churn here protects 
more total revenue than any other intervention. Champions and VIP/Whale 
customers are loyal and low-risk, requiring minimal retention spend. 
At Risk/Lost customers, while individually low-value, are numerous enough 
to justify low-cost re-engagement campaigns (email, small discounts).

## Files

- `notebook.ipynb` — full analysis: cleaning, RFM, clustering, churn modeling
- `dashboard.html` — interactive visualization of segments and churn risk
- `rfm_results.csv` — final per-customer RFM scores, segments, and churn probability
- `segment_insights.json` — segment-level summary used in the dashboard

## Tools

Python (pandas, scikit-learn, matplotlib) for analysis; HTML/CSS/JS (Chart.js) 
for the dashboard.
