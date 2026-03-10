# Wine Quality EDA (Exploratory Data Analysis)

This project performs exploratory data analysis on the Wine Quality dataset containing Portuguese "Vinho Verde" wine samples.

## Dataset Information

**Source:** UCI Machine Learning Repository  
**Citation:** P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. *Modeling wine preferences by data mining from physicochemical properties.* Decision Support Systems, Elsevier, 47(4):547-553, 2009.

### Dataset Files
- `winequality-red.csv` - Red wine samples (1,599 instances)
- `winequality-white.csv` - White wine samples (4,898 instances)
- `winequality.names` - Dataset description and citation information

### Features (11 Physicochemical Properties)
1. **fixed acidity** - Non-volatile acids in wine
2. **volatile acidity** - Amount of acetic acid (high levels = vinegar taste)
3. **citric acid** - Adds freshness and flavor
4. **residual sugar** - Sugar remaining after fermentation
5. **chlorides** - Amount of salt in wine
6. **free sulfur dioxide** - Prevents microbial growth and oxidation
7. **total sulfur dioxide** - Free + bound forms of SO2
8. **density** - Depends on alcohol and sugar content
9. **pH** - Acidity level (0-14 scale)
10. **sulphates** - Wine additive for SO2 levels
11. **alcohol** - Percentage of alcohol content

### Target Variable
- **quality** - Score between 0 (very bad) and 10 (very excellent) based on sensory data (median of at least 3 wine expert evaluations)

## Notebooks

### `Redwine_EDA.ipynb`
Comprehensive exploratory analysis of red wine data following this roadmap:
1. Dataset Overview
2. Data Cleaning
3. Target Variable Analysis
4. Univariate Analysis
5. Bivariate Analysis
6. Correlation Analysis
7. Outlier Detection
8. Feature Engineering

### `whitewine_EDA.ipynb`
Exploratory analysis of white wine data (similar analysis structure)

## Requirements
```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

### Option 1: Command Line
```cmd
cd C:\Users\mahat\Downloads\Data_Science\EDA
jupyter notebook Redwine_EDA.ipynb
```

### Option 2: VS Code
Open the `.ipynb` files directly in VS Code with Jupyter extension installed.

## Quick Start

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load red wine dataset
df_red = pd.read_csv('winequality-red.csv', sep=';')
print(df_red.head())
print(df_red.info())

# Load white wine dataset
df_white = pd.read_csv('winequality-white.csv', sep=';')
print(df_white.head())
```

**Note:** The CSV files use semicolon (`;`) as delimiter, not comma.

## Key Insights to Explore
- Which physicochemical properties most influence wine quality?
- Are there correlations between features?
- Distribution of quality scores (imbalanced - more normal wines than excellent/poor)
- Differences between red and white wine characteristics
- Outlier detection for exceptional wines

## Dataset Characteristics
- **No missing values** - Complete dataset
- **Ordered classes** - Quality scores are ordinal (0-10)
- **Imbalanced** - More normal wines than excellent or poor ones
- **Feature correlation** - Some attributes may be correlated

## References
- [Wine Quality Dataset Paper](http://www3.dsi.uminho.pt/pcortez/winequality09.pdf)
- [Vinho Verde Wine Region](http://www.vinhoverde.pt/en/)
