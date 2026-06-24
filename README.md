# Olist E-commerce Conversion Analysis

## Project Objective

This project analyses the Olist Brazilian E-commerce dataset to understand order lifecycle performance, revenue impact, delivery efficiency, and customer satisfaction.

The main goal is to identify where orders are successfully completed, where drop-offs happen, and how these issues may affect business performance.

## Tools Used

* SQL
* DuckDB
* Python
* Pandas
* NumPy
* Power BI

## Dataset

Dataset used: Olist Brazilian E-commerce Dataset from Kaggle.

The original CSV files are not uploaded to this repository because of file size. The dataset can be downloaded separately from Kaggle.

Main files used:

* olist_orders_dataset.csv
* olist_order_payments_dataset.csv
* olist_customers_dataset.csv
* olist_order_items_dataset.csv
* olist_products_dataset.csv
* olist_order_reviews_dataset.csv

## Business Questions

1. What percentage of orders are successfully delivered?
2. Which order stages create the biggest drop-off?
3. How much revenue is linked to each order status?
4. Does delivery delay affect customer review score?
5. Which product categories generate the most revenue?
6. Which customer or product segments show the strongest performance?

## Current Analysis

The first analysis focuses on the order lifecycle funnel using the `order_status` column.

### Order Status Funnel Result

| Order Status | Total Orders | Percentage |
| ------------ | -----------: | ---------: |
| delivered    |       96,478 |     97.02% |
| shipped      |        1,107 |      1.11% |
| canceled     |          625 |      0.63% |
| unavailable  |          609 |      0.61% |
| invoiced     |          314 |      0.32% |
| processing   |          301 |      0.30% |
| created      |            5 |      0.01% |
| approved     |            2 |      0.00% |

## Key Insight

Around 97.02% of orders were successfully delivered, while around 2.98% were cancelled, unavailable, or stuck in earlier stages. These incomplete orders may represent potential revenue loss and customer dissatisfaction.

## Project Structure

```text
olist-ecommerce-conversion-analysis/
│
├── sql/
│   └── order_status_funnel.sql
│
├── python/
│   └── run_first_query.py
│
├── visuals/
│
├── powerbi/
│
├── README.md
└── requirements.txt
```

## Skills Demonstrated

* SQL aggregation
* Funnel analysis
* Data cleaning preparation
* Python-based analysis workflow
* Business insight generation
* E-commerce performance analysis
* Dashboard planning

## Next Steps

* Analyse revenue by order status
* Analyse delivery delays
* Connect delivery performance with review scores
* Build Power BI dashboard
* Add dashboard screenshots and final business recommendations
