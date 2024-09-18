import os

# Define the directory and files in the specified order
files_to_merge = [
    'objects/rank.py',
    'objects/suit.py',
    'objects/card.py',
    'objects/hand.py',
    'objects/game.py',
    'objects/match.py',
    'objects/compare.py',
    'objects/one_card.py',
    'objects/two_card.py',
    'objects/three_card.py',
    'objects/five_card.py'
]

# Define paths
output_dir = 'out'
output_file = os.path.join(output_dir, 'algorithm.py')
algorithm_file = 'algorithm.py'  # The algorithm.py file outside the objects directory

# Ensure the 'out' directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the original algorithm.py and split it at "from objects.imports import *"
with open(algorithm_file, 'r') as algo_file:
    algo_content = algo_file.readlines()

# Find the line with "from objects.imports import *"
split_index = None
for i, line in enumerate(algo_content):
    if "from objects.imports import *" in line:
        split_index = i
        break

# Split content into two parts: before and after the import statement
before_import = algo_content[:split_index]
after_import = algo_content[split_index + 1:]  # Skip the "from objects.imports import *" line

# Start writing the final algorithm.py file
with open(output_file, 'w') as outfile:
    # 1. Write the content before "from objects.imports import *"
    outfile.writelines(before_import)
    
    # 2. Merge the files in the specified order after "# MERGE FROM HERE"
    for filepath in files_to_merge:
        with open(filepath, 'r') as infile:
            merge = False
            for line in infile:
                # Look for the marker "# MERGE FROM HERE"
                if "# MERGE FROM HERE" in line:
                    merge = True
                    continue  # Skip the marker line itself
                
                # Append lines after the marker to the output file
                if merge:
                    outfile.write(line)
        
        # Add two new lines after merging each file's content
        outfile.write('\n\n')
    
    # 3. Write the rest of the original algorithm.py file (after the import statement)
    outfile.writelines(after_import)

print(f'algorithm.py has been compiled successfully into {output_file}')
