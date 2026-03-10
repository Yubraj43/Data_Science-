# Sales Data Analysis Project

This project reads sales data from CSV, cleans it, stores it in SQLite, and runs basic sales analysis.

## Features
- Reads source data from `Data/sales_data.csv`
- Cleans data (duplicates, nulls, date conversion, total amount calculation)
- Stores data in `database/sales.db`
- Writes execution logs to `logs/app.log`
- Prints analytics:
  - Total sales
  - Sales by region
  - Best-selling product
  - Monthly sales

## Project Structure
- `Data/sales_data.csv` - input dataset
- `src/main.py` - main pipeline entry point
- `src/data_cleaner.py` - data cleaning logic
- `src/database_manager.py` - SQLite operations
- `src/analyzer.py` - analytics queries
- `src/data_logger.py` - file logger setup
- `database/` - generated SQLite database file
- `logs/` - generated log file

## Requirements
- Python 3.9+
- Packages:
  - `pandas`

## Setup (Windows CMD)
Run from the `Sales_project` folder:

```cmd
cd C:\Users\mahat\Downloads\Data_Science\Sales_project
pip install pandas
```

## Run
From `Sales_project` folder:

```cmd
python src\main.py
```

## Expected Console Output (Example)
```text
Process completed successfully!

 TOTAL SALES:
<some number>

 SALES BY REGION:
<list of tuples>

 BEST SELLING PRODUCT:
<product tuple>

 MONTHLY SALES:
<list of tuples>
```

## Dry Run Result (Verified)
The following result was verified in this project on 2026-03-10:

```text
Process completed successfully!

 TOTAL SALES:
444900

 SALES BY REGION:
[('Biratnagar', 109200), ('Kathmandu', 191000), ('Lalitpur', 45200), ('Pokhara', 99500)]

 BEST SELLING PRODUCT:
('Mouse', 7)

 MONTHLY SALES:
[('2026-01', 356700), ('2026-02', 88200)]
```

Also verified:
- `database/sales.db` is created
- `logs/app.log` is updated with INFO log entries

## Dry Run Checklist
Use these commands to verify each part after running:

```cmd
cd C:\Users\mahat\Downloads\Data_Science\Sales_project
python src\main.py
```

1. Console shows `Process completed successfully!`
2. Database file exists:

```cmd
dir database
```

3. Log file exists and contains entries:

```cmd
dir logs
type logs\app.log
```

## Notes
- `src/logger_configure.py` references `configs/config.json`, but this module is not used by `src/main.py`.
- If `pip` is not recognized in CMD, use:

```cmd
python -m pip install pandas
```