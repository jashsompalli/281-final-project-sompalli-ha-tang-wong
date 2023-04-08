import os

DATA_CATEGORIES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
METHODS = ['gaussian', 'mean', 'median']

# Create the 'combined' directory
combined_dir = os.path.join(os.getcwd(), 'combined')
os.makedirs(combined_dir, exist_ok=True)

# Create subdirectories for each data category and method inside the 'combined' directory
for category in DATA_CATEGORIES:
    for method in METHODS:
        category_method_dir = os.path.join(combined_dir, category, method)
        os.makedirs(category_method_dir, exist_ok=True)

# Create the 'outputs' directory
outputs_dir = os.path.join(os.getcwd(), 'outputs')
os.makedirs(outputs_dir, exist_ok=True)

# Create subdirectories for each data category and method inside the 'outputs' directory
for category in DATA_CATEGORIES:
    for method in METHODS:
        category_method_dir = os.path.join(outputs_dir, category, method)
        os.makedirs(category_method_dir, exist_ok=True)
