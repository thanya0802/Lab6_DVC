import pandas as pd

# Load your custom wine dataset
df = pd.read_csv("data/wine_data.txt")

print("Processed Wine Data:")
print(df)

# Save processed output
df.to_csv("processed_output.csv", index=False)

print("processed_output.csv has been created!")

