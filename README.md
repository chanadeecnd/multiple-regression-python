# Multiple Linear Regression Analysis

## Project Description
This project implements multiple linear regression analysis to predict voltage output based on input voltage settings and frequency parameters. The analysis uses real-world data from an Excel file to build a predictive model.

## Theory
Multiple linear regression is a statistical technique used to model the relationship between a dependent variable (target) and multiple independent variables (features). It extends simple linear regression by allowing multiple predictors to explain the variance in the outcome variable.

### Mathematical Formula
The general form of multiple linear regression is:

```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ + ε
```

Where:
- **Y** = Dependent variable (voltage_out)
- **β₀** = Intercept term
- **β₁, β₂, ..., βₙ** = Regression coefficients for each feature
- **X₁, X₂, ..., Xₙ** = Independent variables (voltage_set, frequency)
- **ε** = Error term

### In This Project
For this voltage analysis:
```
voltage_out = β₀ + β₁(voltage_set) + β₂(frequency) + ε
```

## Features
- **Data Loading**: Reads data from Excel files (`long_format_data.xlsx`)
- **Statistical Analysis**: Uses statsmodels for comprehensive regression analysis
- **Model Summary**: Provides detailed statistical output including:
  - R-squared values
  - P-values for significance testing
  - Confidence intervals
  - Residual analysis

## Requirements
This project requires Python 3.8+ and the packages listed in `requirements.txt`.

## Setup and Installation

### 1. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
# Install all required packages from requirements.txt
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
# Check installed packages
pip list
```

## How to Use

### 1. Data Preparation
Ensure your Excel file (`long_format_data.xlsx`) contains the following columns:
- `voltage_set`: Input voltage settings
- `frequency`: Frequency parameters
- `voltage_out`: Output voltage measurements (target variable)

### 2. Running the Analysis
Execute the main script to train the regression model:
```bash
# Make sure virtual environment is activated
python main.py
```

### 3. Extract Model Coefficients
After running `main.py`, note down the coefficients from the output:
- **Intercept (const)**: The β₀ value
- **voltage_set coefficient**: The β₁ value  
- **frequency coefficient**: The β₂ value

### 4. Use Coefficients for Predictions
Update the coefficients in `cal.py` with your actual model results, then run:
```bash
python cal.py
```

### 5. Understanding the Output
The script will display:
- **Data count verification**: Shows the number of observations for each variable
- **Regression summary**: Comprehensive statistical analysis including:
  - **R-squared**: Proportion of variance explained by the model
  - **P-values**: Statistical significance of each coefficient
  - **Coefficients**: The β values in the regression equation
  - **Confidence intervals**: Range of likely values for coefficients

## Data Structure
The project expects data in long format where each row represents one observation with:
- One voltage setting value
- One frequency value  
- One corresponding voltage output value

## Model Interpretation
- **Intercept (β₀)**: Expected voltage output when all predictors are zero
- **voltage_set coefficient (β₁)**: Change in voltage output per unit change in voltage setting
- **frequency coefficient (β₂)**: Change in voltage output per unit change in frequency
- **R-squared**: Percentage of variance in voltage output explained by the model
- **P-values < 0.05**: Indicate statistically significant predictors

## File Structure
```
├── main.py                    # Main regression analysis script
├── cal.py                     # Calculation script using model coefficients
├── requirements.txt           # Package dependencies
├── long_format_data.xlsx      # Input training data file
├── voltage_output_data.xlsx   # Alternative data source
├── venv/                      # Virtual environment (after setup)
└── README.md                  # This documentation
```

## Complete Workflow

### Step 1: Environment Setup
```bash
# Clone or download the project
# Navigate to project directory
cd multi_regression_formula

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Train the Model
```bash
# Run the regression analysis
python main.py
```

### Step 3: Extract Coefficients
From the output, copy the coefficient values:
```
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         74.9390     X.XXX      X.XXX      0.XXX      XX.XXX      XX.XXX
voltage_set    1.5959     X.XXX      X.XXX      0.XXX       X.XXX       X.XXX
frequency    -69.4982     X.XXX      X.XXX      0.XXX       X.XXX       X.XXX
==============================================================================
```

### Step 4: Update cal.py
Edit `cal.py` and update the coefficients:
```python
# Update these values with your actual model results
intercept = 74.9390           # const value from model output
coeff_set_voltage = 1.5959    # voltage_set coefficient
coeff_frequency = -69.49817   # frequency coefficient
```

### Step 5: Make Predictions
```bash
# Run calculations with your trained model
python cal.py
```

## Example Output
```
count 40, 40, 40
                            OLS Regression Results                            
==============================================================================
Dep. Variable:            voltage_out   R-squared:                       0.XXX
Model:                            OLS   Adj. R-squared:                  0.XXX
Method:                 Least Squares   F-statistic:                     XX.XX
Date:                Mon, 22 Aug 2025   Prob (F-statistic):            X.XXe-XX
Time:                        XX:XX:XX   Log-Likelihood:                 -XX.XX
No. Observations:                  40   AIC:                             XX.XX
Df Residuals:                      37   BIC:                             XX.XX
Df Model:                           2                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         XX.XXXX      X.XXX      X.XXX      0.XXX      XX.XXX      XX.XXX
voltage_set    X.XXXX      X.XXX      X.XXX      0.XXX       X.XXX       X.XXX
frequency      X.XXXX      X.XXX      X.XXX      0.XXX       X.XXX       X.XXX
==============================================================================
```

## Applications
This regression model can be used for:
- Predicting voltage output for new voltage/frequency combinations
- Understanding the relationship between input parameters and output
- Quality control in voltage regulation systems
- Optimization of voltage settings for desired outputs
- **Reverse calculation**: Finding required input voltage for desired output (as shown in cal.py)

## Using cal.py for Predictions
The `cal.py` script provides a practical implementation for:

### Forward Prediction
Calculate output voltage given input parameters:
```python
output = intercept + (coeff_voltage * voltage_set) + (coeff_frequency * frequency)
```

### Reverse Calculation  
Find required input voltage for desired output:
```python
required_voltage = (desired_output - intercept - (coeff_frequency * frequency)) / coeff_voltage
```

### Example Usage
```bash
python cal.py
# Output:
# Frequency: 2.0 MHz, Desired Output Voltage: 100 V, Required Set Voltage: 73.25
# Frequency: 1.9 MHz, Desired Output Voltage: 100 V, Required Set Voltage: 79.18
```

## Notes
- Ensure data quality before analysis (check for outliers, missing values)
- Validate model assumptions (linearity, normality of residuals, homoscedasticity)
- Consider model validation techniques (cross-validation, train/test split) for production use
