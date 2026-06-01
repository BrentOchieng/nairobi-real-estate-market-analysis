# Nairobi Real Estate Market Analysis: Web Scraping, Data Cleaning, and Interactive Tableau Dashboard

## Project Overview

The real estate market generates vast amounts of data that can provide valuable insights for investors, property developers, real estate agencies, and home buyers. This project demonstrates an end-to-end data analytics workflow by collecting, cleaning, analyzing, and visualizing real estate listing data from Property24 Kenya.

Using Python for web scraping, Excel for data cleaning, and Tableau Public for visualization, this project explores pricing patterns, market segmentation, and geographic trends within Nairobi's property market.

The objective was to transform raw listing data into actionable business insights that support data-driven decision-making in the real estate industry.

---

## Project Objectives

This project aimed to answer the following business questions:

* Which locations have the highest average property prices?
* Which property categories command premium prices?
* What is the average market price across listings?
* How does pricing vary by property type?
* Which neighborhoods represent the most expensive areas in Nairobi?
* What property configurations dominate the market?
* How do commercial properties compare with residential properties?

---

## Data Collection

Data was collected through web scraping from Property24 Kenya using Python.

### Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas

### Data Attributes Collected

* Property Title
* Property Category
* Price
* Location
* Listing Information

---

## Data Cleaning

The raw dataset contained several common real-world data quality challenges, including:

* Duplicate records
* Missing values
* Inconsistent naming conventions
* Mixed price formats
* Data standardization issues

Microsoft Excel was used to clean and prepare the dataset for analysis.

### Cleaning Tasks Performed

* Removed duplicate records
* Standardized property categories
* Validated missing values
* Converted prices into a consistent format
* Corrected formatting inconsistencies

---

## Data Visualization

An interactive Tableau dashboard was created to provide insights into Nairobi's real estate market.

### Dashboard Features

* Market Overview KPIs
* Average Property Prices
* Median Property Prices
* Property Category Analysis
* Location-Based Price Analysis
* Unit-Level Price Comparisons
* Interactive Filtering by Category and Location

---

## Key Findings

### Market Overview

* Total Listings Analyzed: **680**
* Average Property Price: **KES 205.6 Million**
* Median Property Price: **KES 85 Million**

The significant gap between average and median prices indicates the presence of high-value luxury and commercial properties that increase overall market averages.

### Location Insights

The highest-priced locations identified in the dataset include:

1. Nairobi CBD
2. Riverside
3. Parklands
4. Kiambu Road
5. Ruaka

These areas continue to attract premium real estate investments due to their strategic location and strong demand.

### Property Category Insights

Commercial properties recorded the highest average prices among all property categories, outperforming residential property types such as apartments, townhouses, and houses.

This suggests strong investment demand within Nairobi's commercial real estate sector.

---

## Business Value

This analysis demonstrates how data analytics can support:

* Real estate investment decisions
* Market intelligence initiatives
* Property pricing strategies
* Geographic market assessments
* Business intelligence reporting

---

## Tools and Technologies

| Category        | Technology              |
| --------------- | ----------------------- |
| Data Collection | Python                  |
| Web Scraping    | Requests, BeautifulSoup |
| Data Cleaning   | Microsoft Excel         |
| Data Analysis   | Pandas                  |
| Visualization   | Tableau Public          |
| Version Control | Git & GitHub            |

---

## Dashboard Preview

*<img width="1600" height="766" alt="Screenshot (417)" src="https://github.com/user-attachments/assets/bd47bb09-72d7-47d2-a362-8fca83e63608" />
*

---

## Interactive Dashboard

**Tableau Public Dashboard:** *https://public.tableau.com/authoring/property24_analysis/Dashboard1#2*

---

## Project Structure

```text
Real-Estate-Analysis/
│
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── notebooks/
│   └── property24_scraping.ipynb
│
├── dashboard/
│   └── tableau_dashboard.twb
│
├── images/
│   └── dashboard_preview.png
│
└── README.md
```

---

## Skills Demonstrated

* Web Scraping
* Data Cleaning
* Exploratory Data Analysis (EDA)
* Business Intelligence
* Data Visualization
* Dashboard Design
* Data Storytelling
* Real Estate Market Analytics

---


Connect with me on LinkedIn and explore more analytics projects on GitHub.
