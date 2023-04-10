import requests
import pandas as pd

# Define API endpoint
url = "http://localhost:8000/api/energy/"

# Request data from API
response = requests.get(url)
data = response.json()

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Data analysis example
# Calculate average energy consumption per hour
df['datetime'] = pd.to_datetime(df['datetime'])
df.set_index('datetime', inplace=True)
hourly_avg = df['energy_consumption'].resample('H').mean()

print(hourly_avg)
