import pandas as pd
import statsmodels.api as sm

data = pd.read_excel("long_format_data.xlsx")

print(f"count {len(data['voltage_set'])}, {len(data['frequency'])}, {len(data['voltage_out'])}")
df = pd.DataFrame(data)

X = sm.add_constant(df[["voltage_set", "frequency"]])
y = df["voltage_out"]

model = sm.OLS(y, X).fit()

print(model.summary())