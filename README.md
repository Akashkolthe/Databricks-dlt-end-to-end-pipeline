# 🚀 End-to-End Data Pipeline using Databricks Delta Live Tables (DLT)

## 📌 Overview

This project implements a production-style **end-to-end data pipeline** using **Delta Live Tables (DLT)** on Databricks, following the **Medallion Architecture (Bronze → Silver → Gold)**.

The pipeline ingests raw data, applies transformations and data quality rules, and produces analytics-ready datasets with built-in lineage and monitoring.

---

## 🏗️ Architecture

```
Raw Data → Bronze (Ingestion) → Silver (Transformation) → Gold (Aggregation)
```

* **Bronze Layer**

  * Ingests raw data using Auto Loader (cloudFiles)
  * Supports incremental and streaming ingestion

* **Silver Layer**

  * Cleans and standardizes data
  * Applies data quality constraints
  * Removes invalid/null records

* **Gold Layer**

  * Performs aggregations and business-level transformations
  * Produces curated datasets for reporting and analytics

---

## 🔧 Tech Stack

* Databricks
* Delta Live Tables (DLT)
* Apache Spark (PySpark)
* Structured Streaming
* Delta Lake

---

## 📂 Project Structure

```
DLT_END_TO_END/
│
├── bronze/
│   └── ingestion.py
│
├── silver/
│   └── transformation.py
│
├── gold/
│   └── aggregation.py
│
└── explorations/
    └── analysis_notebook.py
```

---

## ⚙️ Pipeline Implementation Details

* Built using **DLT decorators** (`@dlt.table`, `dlt.read`, `dlt.read_stream`)
* Implements **streaming ingestion with Auto Loader**
* Uses **data quality expectations** to enforce constraints
* Automatically manages **data lineage and dependencies**
* Handles **schema evolution and incremental processing**

---

## ✅ Data Quality & Governance

* Enforced data validation using **DLT expectations**
* Ensured non-null constraints and schema consistency
* Prevented bad data propagation across layers

---

## 🔄 Slowly Changing Dimensions (SCD Type 2)

Implemented SCD Type 2 logic using DLT:

* Tracks historical changes in dimension data
* Maintains **current and historical records**
* Uses `apply_changes()` for CDC-style updates

---

## 🧠 Key Learnings

* DLT pipelines are **stateful systems** — pipeline storage and checkpoints must be managed carefully
* Schema issues (invalid column names, evolution) can break pipelines if not handled early
* Data quality rules should be enforced at ingestion, not after failure
* Understanding **DLT execution model vs notebook execution** is critical

---

## ▶️ How to Run

1. Create a Delta Live Tables pipeline in Databricks
2. Attach the notebooks from this repository
3. Configure pipeline storage location
4. Run the pipeline in Development or Production mode

---

## 📌 Future Enhancements

* Add parameterized pipeline configurations
* Integrate monitoring and alerting (DLT event logs)
* Implement unit testing for transformations
* Optimize performance for large-scale datasets

---

## 🔗 Repository

https://github.com/Akashkolthe/Databricks-dlt-end-to-end-pipeline

---

## 👨‍💻 Author

Akash Kolthe

---

## ⭐ If this project helped you, consider giving it a star!
