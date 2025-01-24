import pandas as pd

# Load the CSV file
file_path = 'scan_file.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Add an empty 'Supporting' column
df['Supporting'] = ''

# Rename 'Severity' column to 'Risk'
df.rename(columns={'Severity': 'Risk'}, inplace=True)

# Rename 'Threat' column to 'Description'
df.rename(columns={'Threat': 'Description'}, inplace=True)

# Function to determine the type based on the IP
def determine_type(ip):
    if str(ip).startswith('10'):
        return 'Internal'
    else:
        return 'External'

# Function to categorize risk
def categorize_risk(risk):
    risk_mapping = {
        1: 'Informational',
        2: 'Low',
        3: 'Medium',
        4: 'High',
	5: 'Critical'
    }
    return risk_mapping.get(risk, 'Informational')  # Default to 'Unknown' if risk is not 1, 2, 3, or 4

df['Supporting'] = df['Supporting'].apply(lambda x: str(x) + '.')

# Apply the functions to the respective columns
df['Type'] = df['IP'].apply(determine_type)
df['Risk'] = df['Risk'].apply(categorize_risk)

# Add specific values to 'InfrastructureReference', 'Cause', and 'Impact' columns
df['InfrastructureReference'] = 'OWASP Top 10: A5 Security Misconfiguration'
df['Cause'] = 'Insecure Configuration'
df['Impact'] = 'Information Disclosure'

# Rename 'Solution' column to 'Recommendation' and copy to 'Short_Recommendation'
df.rename(columns={'Solution': 'Recommendation'}, inplace=True)
df['Short_Recommendation'] = df['Recommendation']

df['Order'] = 50

# Columns to be removed
columns_to_remove = ["DNS", "NetBIOS", "OS", "IP Status", "Port", "Protocol", 
                     "FQDN", "SSL", "Vendor Reference", "Bugtraq ID", 
                     "PCI Vuln", "Instance", "Category", "Associated Malware", "Exploitability", "CVE ID"]

# Remove the specified columns
df.drop(columns=columns_to_remove, errors='ignore', inplace=True)

# Function to replace empty cells with a period
def replace_empty_with_period(cell):
    if pd.isna(cell) or cell == '':
        return '.'
    else:
        return cell

# Group by 'QID' and aggregate 'IP' values into a list for each group
grouped = df.groupby('QID')['IP'].apply(list).reset_index(name='IP_List')

# Merge the aggregated IP lists back into the original DataFrame
df = df.merge(grouped, on='QID')

# Update the 'IP' column with the list of IPs, separated by newline characters
df['IP'] = df['IP_List'].apply(lambda x: ' '.join(x))

# Drop the temporary 'IP_List' column
df.drop(columns=['IP_List'], inplace=True)

# Save the modified DataFrame back to CSV
df.to_csv('scan_file_Fixed.csv', index=False)
