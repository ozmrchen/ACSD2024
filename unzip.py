# unzip file
import zipfile

# Specify the path to your ZIP file
zip_file_path = 'Harry1.zip'
# Specify the directory where files will be extracted
extract_to_path = 'Case1'

# Open the ZIP file in read mode
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all files to the specified directory
    zip_ref.extractall(extract_to_path)

print('Files extracted successfully.')
