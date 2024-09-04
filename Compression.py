
file_path = "/mnt/c/Users/KIIT/Desktop/DMDW/D_small.dat"


with open(file_path, "r") as file:
    dataset_content = file.readlines()

dataset_content[:10]  

mappings_content = """
A: 1 3 5 7 9
B: 11 13 15 17 19
C: 21 23 25 27 29
D: 31 34 36 38 40
E: 42 44 46 48 50
F: 52 54 56 58 60
G: 62 64 66 68 70
H: 72 74
"""


mappings_file_path = "/mnt/c/Users/KIIT/Desktop/DMDW/mappings.txt"

with open(mappings_file_path, "w") as file:
    file.write(mappings_content)


file_paths = {"dataset": file_path, "mappings": mappings_file_path}
file_paths
# Define the modified code as a function and run it with the provided dataset and mappings.
class Transaction:
    def __init__(self):
        self.items = []
        self.item_count = 0

class Mapping:
    def __init__(self):
        self.label = ""
        self.itemset = []
        self.item_count = 0

def read_dataset(file_path):
    transactions = []
    with open(file_path, "r") as file:
        for line in file:
            transaction = Transaction()
            transaction.items = line.strip().split()
            transaction.item_count = len(transaction.items)
            transactions.append(transaction)
    transaction_count = len(transactions)
    return transactions, transaction_count

def create_mapping(file_path):
    mappings = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                label = parts[0].strip()

                mapping = Mapping()
                mapping.label = label
                mapping.itemset = parts[1].strip().split() 
                mapping.item_count = len(mapping.itemset)
                mappings.append(mapping)
            else:
                print(f"Warning: Incorrect format in line: {line.strip()}")
    
    mapping_count = len(mappings)
    return mappings, mapping_count

def compress_dataset(transactions, transaction_count, mappings, mapping_count):
    total_items_before = sum([t.item_count for t in transactions])  # Count total items before compression
    for i in range(transaction_count):
        for j in range(mapping_count):
            found_all = True
            for k in range(mappings[j].item_count):
                if mappings[j].itemset[k] not in transactions[i].items:
                    found_all = False
                    break
            if found_all:
                transactions[i].items = [mappings[j].label]
                transactions[i].item_count = 1
                break
    total_items_after = sum([t.item_count for t in transactions])  # Count total items after compression
    return total_items_before, total_items_after

def calculate_compression_rate(total_items_before, total_items_after):
    if total_items_before == 0:
        return 0
    compression_rate = (total_items_before - total_items_after) / total_items_before
    return compression_rate

def print_compressed_dataset(transactions, transaction_count):
    compressed_data = []
    for i in range(transaction_count):
        compressed_data.append(f"T{i + 1} - {' '.join(transactions[i].items)}")
    return compressed_data

# Run the compression process
dataset_file_path = file_paths["dataset"]
mappings_file_path = file_paths["mappings"]

# Read the dataset
transactions, transaction_count = read_dataset(dataset_file_path)

# Create mapping for compression
mappings, mapping_count = create_mapping(mappings_file_path)

# Compress the dataset using the mapping
total_items_before, total_items_after = compress_dataset(transactions, transaction_count, mappings, mapping_count)

# Print the compressed dataset
compressed_data = print_compressed_dataset(transactions, transaction_count)

# Calculate the compression rate
compression_rate = calculate_compression_rate(total_items_before, total_items_after)

compressed_data, compression_rate
