# Retail Sales ETL Pipeline using Python and MySQL

## 📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python and MySQL.

## ⚙️ ETL Process

* **Extract:** Loaded raw retail dataset (CSV)
* **Transform:** Cleaned data, handled missing values, formatted dates using Pandas
* **Load:** Stored processed data into MySQL database

## 🧱 Data Modeling

Designed a basic **Star Schema**:

* Fact Table: `fact_sales`
* Dimension Tables: `dim_customers`, `dim_products`

## 📊 Key SQL Analysis

* Total sales by category
* Sales trends using joins and aggregations

## 🛠️ Tech Stack

* Python (Pandas)
* MySQL
* SQL

## 🚀 Outcome

Successfully built a structured data pipeline and generated insights using SQL queries.

## 📁 Project Structure

* etl.py
* sales.csv
* README.md
