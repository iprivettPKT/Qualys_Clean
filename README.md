# Qualys Clean 
 
 Instructions:

1. Download the Qualys scan results in CSV format.
2. Install the pandas python library ```python3 -m pip install pandas```
3. Delete the first seven rows of the CSV file.
   ![image](https://github.com/user-attachments/assets/32c44e5b-d376-4e78-b265-a286e40b14ab)
4. Edit the script code to have the correct file path for the scan results.
   ![image](https://github.com/user-attachments/assets/6290774d-492a-49e2-9b62-7337ea1d4b64)
5. Edit the file path of the newly cleaned file.
   ![image](https://github.com/user-attachments/assets/ad62848a-752e-46d3-bd55-7ede3ae33957)
6. ```python3 Qualys_clean.py```
7. Import the new file as a CSV file into Dradis and correctly set the columns to the right section.
