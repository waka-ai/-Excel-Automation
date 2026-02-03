import pandas as pd

def process_excel(input_file):
    df = pd.read_excel(input_file)
    
    # Example: Calculate totals
    df['Total'] = df['Quantity'] * df['Price']
    
    # Save processed file
    output_file = input_file.replace('.xlsx', '_processed.xlsx')
    df.to_excel(output_file, index=False)
    print(f"Processed file saved: {output_file}")

# Usage
process_excel("sales_data.xlsx")
