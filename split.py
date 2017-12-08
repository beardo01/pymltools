# Imports
import os
import shutil

# Settings
input_directory = "output"
output_directory = "data"
split_into = {"train": 70, "valid": 15, "test": 15}

# Check settings
errors = []
if(sum(split_into.values()) != 100):
    total = sum(split_into.values())
    errors.append("Error: " + str(split_into.values()).strip("[]") + " sum to " + str(total) + ".")
    errors.append("Split percentages must sum to 100.\n")

if not os.path.exists(input_directory):
    errors.append("Error: Cannot find directory '" + input_directory + "' at location " + os.getcwd())

if errors:
    for error in errors:
        print(error)
    exit("\nPlease fix errors and rerun.")

# Setup folder structure
sub_directories = filter(os.path.isdir, [os.path.join(os.getcwd() + "/" + input_directory, f) for f in os.listdir(input_directory)])
sub_directories = list(sub_directories)

if not os.path.exists(output_directory):
    os.mkdir(output_directory)

for value in split_into.keys():
    if not os.path.exists(output_directory + "/" + value):
        os.mkdir(output_directory + "/" + value)

    for d in sub_directories:
        folder = d.rsplit('/', 1)[-1]
        
        if not os.path.exists(output_directory + "/" + value + "/" + folder):
            os.mkdir(output_directory + "/" + value + "/" + folder)

# Main
report = []
for sub_directory in sub_directories:
    path, dirs, files = os.walk(sub_directory).__next__()

    # Work out how many of each we need for split_into
    nums = {}
    for key, value in split_into.items():
        num = value / 100
        num = int(num * len(files))
        nums[key] = num

    # Ensure all files accounted for
    if sum(nums.values()) != len(files):
        while(sum(nums.values()) < len(files)):
            for key, value in nums.items():
                if (sum(nums.values()) == len(files)):
                    break
                nums[key] += 1

    # Copy files to new directory
    for key, value in nums.items():

        report.append("Copying " + str(value) + " image(s) into '" + str(key) + "' for term '" + str(path.rsplit('/', 1)[-1]) + "'.")

        current = 0
        for f in range(len(files)):
            if(current == value - 1):
                break

            source = path + "/" + files.pop(0)
            folder = path.rsplit('/', 1)[-1]
            dest = os.getcwd() + "/" + output_directory + "/" + key + "/" + folder

            shutil.copy2(source, dest)
            
            current += 1
    
    report.append("")
        

for line in report:
    print(line)
print("Copy complete.")