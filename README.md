
![Architecture](docs/architecture.png)
# 🚀 End-to-End Data Pipeline using Delta Live Tables (DLT)

## 📌 Overview

This project demonstrates a production-style **end-to-end data pipeline** built using **Delta Live Tables (DLT)** on Databricks.
It follows the **Medallion Architecture (Bronze → Silver → Gold)** to transform raw data into high-quality, analytics-ready datasets.

The pipeline leverages **streaming ingestion, data quality enforcement, and automated lineage tracking** to simulate real-world data engineering workflows.

---

## 🏗️ Architecture

```
Raw Data → Bronze (Ingestion) → Silver (Transformation) → Gold (Aggregation)
```

### 🔹 Bronze Layer

* Ingests raw data using Auto Loader (`cloudFiles`)
* Supports incremental and streaming ingestion
* Stores raw, unprocessed data for traceability

### 🔹 Silver Layer

* Cleans and standardizes data
* Applies data quality validations
* Filters invalid or null records

### 🔹 Gold Layer

* Performs aggregations and business transformations
* Produces curated datasets for analytics and reporting

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

## ⚙️ Pipeline Implementation

* Built using DLT decorators (`@dlt.table`)
* Uses `dlt.read()` and `dlt.read_stream()` for dependency management
* Implements **Auto Loader** for scalable ingestion
* Handles **schema evolution and incremental processing**
* Automatically generates **data lineage and DAG execution plan**

---

## ✅ Data Quality & Governance

* Enforced validation rules using **DLT expectations (`@dlt.expect`)**
* Ensured schema consistency across layers
* Prevented propagation of bad or incomplete data

---

## 🔄 Slowly Changing Dimensions (SCD Type 2)

* Implemented using `apply_changes()`
* Maintains historical records of changes
* Supports CDC-style updates for dimension tables

---

## 🧠 Key Learnings

* DLT pipelines are **stateful systems** — pipeline storage and checkpoints must be managed carefully
* Schema issues (e.g., invalid column names) can break pipelines if not handled early
* Data quality should be enforced during ingestion, not after failure
* Understanding the **DLT execution model vs standard notebooks** is critical

---

## ▶️ How to Run

1. Create a Delta Live Tables pipeline in Databricks
2. Add notebooks from this repository to the pipeline
3. Configure pipeline storage location (e.g., `/tmp/dlt_pipeline`)
4. Run the pipeline in **Development** or **Production** mode

---

## 📌 Future Enhancements

* Parameterize pipeline configuration for reusability
* Add monitoring and alerting using DLT event logs
* Implement unit testing for transformations
* Optimize performance for large-scale data

---

## 🔗 Repository

https://github.com/Akashkolthe/Databricks-dlt-end-to-end-pipeline

---

## 👨‍💻 Author

Akash Kolthe

---

## ⭐ If you found this project useful, consider giving it a star!
