![Architecture](docs/architecture.png)

# 🚀 End-to-End Streaming Data Pipeline using Delta Live Tables (DLT)

## 📌 Overview

This project implements a **production-style streaming data pipeline** using **Delta Live Tables (DLT)** on Databricks.

It follows the **Medallion Architecture (Bronze → Silver → Gold)** to transform raw data into **high-quality, analytics-ready datasets**, while handling **state management, schema evolution, and incremental processing** — key challenges in real-world data engineering systems.

---

## 🏗️ Architecture

```
Landing Zone → Bronze → Silver → Gold → Analytics
```

* **Landing Zone** → Databricks Volumes (raw data storage)
* **Bronze Layer** → Streaming ingestion using Auto Loader (`cloudFiles`)
* **Silver Layer** → Data cleansing, validation, and standardization
* **Gold Layer** → Business-ready datasets (Fact + SCD Type 2 Dimensions)

---

## 🔧 Tech Stack

* Databricks
* Delta Live Tables (DLT)
* Apache Spark (PySpark)
* Structured Streaming
* Delta Lake

---

## ⚙️ Pipeline Implementation

* Built using **DLT decorators** (`@dlt.table`)
* Uses `dlt.read()` and `dlt.read_stream()` for dependency management
* Implements **Auto Loader** for scalable, incremental ingestion
* Handles **schema evolution and streaming state (checkpoints)**
* Automatically generates **pipeline DAG, lineage, and execution plan**

---

## ✅ Data Quality & Governance

* Enforced validation rules using **DLT expectations (`@dlt.expect`)**
* Applied constraints at ingestion to prevent bad data propagation
* Ensured schema consistency across pipeline layers

---

## 🔄 Data Modeling (Gold Layer)

* **Fact Tables** for analytics and reporting
* **SCD Type 2 Dimensions** using `apply_changes()`
* Maintains historical data for change tracking and auditing

---

## ⚠️ Real-World Challenges & Learnings

* **State Management**
  DLT pipelines are stateful — pipeline storage and checkpoints must be managed explicitly
  Deleting source data does NOT reset pipeline state

* **Schema Evolution**
  Invalid column names or schema changes can break pipelines if not handled early

* **Execution Model**
  DLT pipelines execute as a **DAG**, not sequential notebooks
  Dependencies must be explicitly defined using `dlt.read()`

---

## ⚖️ Batch vs Streaming Insight

* **Batch Pipelines** → Predictable, cost-efficient, easier to debug
* **Streaming Pipelines** → Low-latency, stateful, more complex

👉 Choosing the right approach depends on **latency requirements and use case**, not just tooling

---

## ▶️ How to Run

1. Create a Delta Live Tables pipeline in Databricks
2. Attach notebooks from this repository
3. Configure pipeline storage location (e.g., `/tmp/dlt_pipeline`)
4. Run in **Development** or **Production** mode

---

## 📂 Project Structure

```
DLT_END_TO_END/
│
├── bronze/
│   └── ingestion.py
├── silver/
│   └── transformation.py
├── gold/
│   └── aggregation.py
└── explorations/
    └── analysis_notebook.py
```

---

## 📌 Future Enhancements

* Parameterized pipeline configurations
* Monitoring and alerting using DLT event logs
* Unit testing for transformations
* Performance optimization for large-scale workloads

---

## 🔗 Repository

https://github.com/Akashkolthe/Databricks-dlt-end-to-end-pipeline

---

## 👨‍💻 Author

Akash Kolthe

---

## ⭐ If you found this project useful, consider giving it a star!

