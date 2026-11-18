# SaaS Data Quality Audit & Cleaning Pipeline

## 1. Project Overview

This project demonstrates a Python-based data cleaning and quality validation pipeline using five related datasets from a simulated B2B SaaS subscription and billing database.

The project follows a systematic workflow:

**Inspect → Plan → Clean → Verify → Export**

The objective is to identify and resolve data-quality issues while preserving the relationships between the datasets.

### Datasets

The project works with five CSV datasets:

* Accounts
* Plans
* Subscriptions
* Invoices
* Payments

**Data source:** [Analytics Engineering – SaaS Subscriptions Dataset](https://www.analyticsengineering.com/datasets/saas-subscriptions)

## 2. Technologies Used

* Python
* Pandas
* CSV
* VS Code
* Git and GitHub

## 3. Project Structure

```text
Cleaning-data-with-python/
│
├── data/
│   ├── raw/
│   │   ├── accounts.csv
│   │   ├── plans.csv
│   │   ├── subscriptions.csv
│   │   ├── invoices.csv
│   │   └── payments.csv
│   │
│   └── processed/
│       ├── accounts_clean.csv
│       ├── plans_clean.csv
│       ├── subscriptions_clean.csv
│       ├── invoices_clean.csv
│       └── payments_clean.csv
│
├── src/
│   └── data_cleaning.py
│
├── .gitignore
└── README.md
```

**Raw data:** Original datasets. These are preserved and not modified directly.

**Processed data:** Cleaned datasets exported by the Python script.

**Source code:** Contains the data cleaning and validation logic.

## 4. Data Cleaning Operations

The following operations were performed across the five datasets.

### Duplicate Removal

* Identified exact duplicate records.
* Removed duplicate rows using Pandas `drop_duplicates()`.
* Verified primary-key uniqueness after cleaning.

### Missing Value Handling

* Replaced 479 missing account regions with `unknown`.
* Preserved missing timestamps rather than inventing values.
* Retained missing subscription end dates where they represent active subscriptions.

### Categorical Standardisation

* Removed unnecessary leading and trailing whitespace.
* Standardised categorical values to consistent lowercase formatting where appropriate.
* Preserved uppercase formatting for region codes.

### Date Standardisation

* Converted date columns into Pandas datetime types.
* Resolved slash-separated date formats.
* Preserved genuinely missing dates as `NaT`.

## 5. Data Quality Validation

The project uses Python `assert` statements to verify the cleaned datasets.

Validation includes:

* Primary-key uniqueness.
* Expected missing date counts.
* Valid categorical values.
* Foreign-key relationships between related datasets.

### Relational Relationships

The five datasets follow this relationship structure:

| Parent Dataset | Primary Key     | Child Dataset | Foreign Key     |
| -------------- | --------------- | ------------- | --------------- |
| Accounts       | account_id      | Subscriptions | account_id      |
| Plans          | plan_id         | Subscriptions | plan_id         |
| Subscriptions  | subscription_id | Invoices      | subscription_id |
| Invoices       | invoice_id      | Payments      | invoice_id      |

Foreign-key validation confirmed that all child-table references matched existing records in their respective parent tables.

## 6. Cleaning Results

| Dataset       | Original Rows | Cleaned Rows |
| ------------- | ------------: | -----------: |
| Accounts      |         2,001 |        2,000 |
| Plans         |             5 |            4 |
| Subscriptions |         2,001 |        2,000 |
| Invoices      |         2,001 |        2,000 |
| Payments      |         2,001 |        2,000 |
| **Total**     |     **8,009** |    **8,004** |

The reduction in row counts resulted from removing exact duplicate records.

The cleaned datasets were exported as CSV files into `data/processed/`.

## 7. Installation and Execution

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/pavanraghavendarsai/Cleaning-data-with-python.git
```

### Step 2: Navigate into the Project

```bash
cd Cleaning-data-with-python
```

### Step 3: Install uv and Dependencies

Install [uv](https://docs.astral.sh/uv/), then run this from the project root (the folder that contains `pyproject.toml`):

```bash
uv sync
```

This creates a `.venv/` folder and installs the packages listed in `pyproject.toml`. There is no need to activate the environment manually; `uv run` uses it automatically.

### Step 4: Run the Cleaning Pipeline

Run this command from the project's root directory:

```bash
uv run python src/data_cleaning.py
```

The script reads the original CSV files from `data/raw/`, performs cleaning and validation, and exports the resulting datasets into `data/processed/`.

## 8. Key Learning Outcomes

Through this project, I gained practical experience with:

* Exploring and profiling datasets using Pandas.
* Identifying missing values and duplicate records.
* Cleaning inconsistent categorical data.
* Handling and converting date columns.
* Understanding primary keys and foreign keys.
* Validating relationships between multiple datasets.
* Using assertions to enforce data-quality rules.
* Exporting processed datasets.
* Organising a Python data project.

## 9. Future Improvements

Potential future extensions include:

* Refactoring the cleaning logic into reusable Python functions.
* Adding automated tests using Pytest.
* Loading the cleaned datasets into PostgreSQL.
* Implementing SQL-based data transformations.
* Introducing dbt for data modelling and testing.
* Using Apache Airflow for workflow orchestration.

---

**Project:** SaaS Data Quality Audit & Cleaning Pipeline
**Language:** Python
**Primary Library:** Pandas

## 6. How to Run Locally

1. Clone the repository and move into the project folder:

   ```bash
   git clone https://github.com/pavanraghavendarsai/Cleaning-data-with-python.git
   cd Cleaning-data-with-python
   ```

2. Install [uv](https://docs.astral.sh/uv/), then install the dependencies from the project root (the folder that contains `pyproject.toml`):

   ```bash
   uv sync
   ```

3. Run the cleaning script:

   ```bash
   uv run python src/data_cleaning.py
   ```

4. 5. The cleaned files are saved to `data/processed/`.
