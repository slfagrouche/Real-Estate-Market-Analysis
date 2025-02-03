# USA Real Estate Market Analysis Project

## Project Intro/Objective
This project conducts a comprehensive analysis of the USA real estate market using data from Realtor.com, a leading real estate listing website. The analysis employs various statistical and machine learning techniques to uncover insights into housing market trends, price determinants, and market segmentation. The project aims to provide valuable insights for real estate professionals, investors, and policymakers to make data-driven decisions.

### Methods Used
* Exploratory Data Analysis
* Feature Engineering
* Statistical Testing (Chi-Square, ANOVA, T-tests)
* Data Visualization
* Clustering Analysis
* Linear Regression
* Time Series Analysis
* Correlation Analysis

### Technologies
* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* SciPy
* Jupyter Notebooks

## Project Description
The analysis is based on a dataset containing over 2.2 million real estate listings across the United States. Key features include:

* Property characteristics (bedrooms, bathrooms, lot size, living area)
* Location data (city, state, zip code)
* Price information
* Property status (for sale, sold, ready to build)

### Key Analysis Components:

1. **Exploratory Data Analysis** (`notebooks/Exploratory_Data_Analysis_of_of_USA_Real_Estate_Properties.ipynb`)
   * Statistical analysis of property characteristics
   * Distribution analysis of prices and features
   * Correlation analysis between variables
   * Geographical distribution of listings

2. **High-Level Analysis** (`notebooks/High_level_analysis.ipynb`)
   * Clustering Analysis
     * Identified 5 distinct market segments
     * Market segmentation insights
   * Statistical Tests
     * Chi-square tests for state-status relationships
     * ANOVA for price differences
     * T-tests for price comparisons
   * Linear Regression
     * Price prediction model
     * Feature importance analysis
   * Time Series Analysis
     * Price trends and patterns

### Key Findings:
* Significant price variations across different states and property statuses
* Strong market segmentation with distinct property clusters
* Dynamic market conditions in states like Texas, with high construction activity
* Weak to moderate correlations between price and physical characteristics

## Getting Started

### Prerequisites
* Python 3.7+
* Required packages listed in `requirements.txt`

### Installation
1. Clone this repository
```bash
git clone https://github.com/slfagrouche/usa-real-estate-analysis.git
```

2. Install required packages
```bash
pip install -r requirements.txt
```

### Data
* Source: Realtor.com dataset (via Kaggle)
* Format: CSV file containing 2,226,382 entries
* Key columns: price, bedrooms, bathrooms, location data, property status
* Raw data location: `data/raw/realtor-data.zip.csv`

## Project Structure
```
usa-real-estate-analysis/
├── Final Report.pdf      # Comprehensive project report
├── LICENSE              # MIT License
├── README.md           # Project documentation
├── data/
│   └── raw/            # Original dataset
│       └── realtor-data.zip.csv
├── docs/               # Additional documentation
├── notebooks/
│   ├── Exploratory_Data_Analysis_of_of_USA_Real_Estate_Properties.ipynb
│   └── High_level_analysis.ipynb
├── requirements.txt    # Project dependencies
└── src/
    ├── __init__.py
    ├── data/          # Data processing scripts
    │   ├── __init__.py
    │   └── process_data.py
    └── visualization/  # Visualization functions
        ├── __init__.py
        └── visualize.py
```

## Featured Deliverables
* [Final Report](Final%20Report%20.pdf) - Comprehensive analysis and findings
* [Exploratory Data Analysis](notebooks/Exploratory_Data_Analysis_of_of_USA_Real_Estate_Properties.ipynb)
* [High-Level Analysis](notebooks/High_level_analysis.ipynb)

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author
* **Said Lfagrouche** - [GitHub Profile](https://github.com/slfagrouche)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
* Data provided by Realtor.com
* Analysis conducted for educational purposes and hands on experience
