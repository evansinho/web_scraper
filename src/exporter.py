import os
import pandas as pd

def save_to_csv(data, filename):
    """Save structured data to CSV, ensuring the directory exists."""
    data_dir = "data"

    # Ensure 'data/' is not duplicated in filename
    if not filename.startswith(data_dir + "/"):
        filename = os.path.join(data_dir, filename)

    # Create the directory if it does not exist
    os.makedirs(data_dir, exist_ok=True)
    
    # Convert list to DataFrame
    if isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        df = data  # Assume it's already a DataFrame
    
    # Prevent saving empty data
    if df.empty:
        print("⚠️ Warning: No data to save.")
        return
    
    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")
