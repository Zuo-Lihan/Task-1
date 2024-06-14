"""
This .py program aims to:
split the raw-data into training, validating, and testing.

Tip: some include 'answerType', but others not.
"""

import json
import random
import argparse
from typing import List, Dict


def parse_args():
    parser = argparse.ArgumentParser(description="Shuffle and split dataset into training, validation, and test sets.")
    parser.add_argument('--input_file', type=str, required=True, help='Input JSON file containing the data.')
    parser.add_argument('--train_output', type=str,default='./Data/train.json', help='Output the training set')
    parser.add_argument('--valid_output', type=str, default='./Data/valid.json', help='Output the validation set')
    parser.add_argument('--test_output', type=str, default='./Data/test.json', help='Output the test set')
    parser.add_argument('--train_valid_test_split', type=list, default=[0.8, 0.1, 0.1], help='Split the training, validation, and test sets')
    return parser.parse_args()


def load_data(input_file: str) -> List[Dict]:
    data = []
    with open(input_file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            try:
                item_dict = eval(line)
                data.append(item_dict)
            except Exception as e:
                print(f"Error parsing item: {line}\n{e}")
    return data


def write_json(data: List[Dict], filename: str):
    list = []
    try:
        for line in data:
            data_dict = {"id": None, "question_type": None, "question": None, "answer": None}
            data_dict["id"] = line["asin"]
            data_dict["question_type"] = line["questionType"]
            data_dict["question"] = line["question"]
            data_dict["answer"] = line["answer"]
            list.append(data_dict)
        with open(filename, "w") as file:
            json.dump(list, file, indent=4)
            file.write("\n")
        print(f"Data successfully written to {filename}")
    except IOError as e:
        print(f"An error encountered while writing to {filename}: {e}")


args = parse_args()

# read data from the file
data = load_data(args.input_file)

# shuffle the data
random.shuffle(data)

# count the nums of each set
total_num = len(data)
train_num = int(total_num * float(args.train_valid_test_split[0]))
valid_num = int(total_num * float(args.train_valid_test_split[1]))
test_num = int(total_num * float(args.train_valid_test_split[2]))

# allocate data to sets
train_set = data[: train_num]
valid_set = data[train_num: train_num + valid_num]
test_set = data[train_num + valid_num: ]

# write the data into JSON
write_json(train_set, args.train_output)
write_json(valid_set, args.valid_output)
write_json(test_set, args.test_output)

print(f"Training set: {len(train_set)} samples.")
print(f"Validation set: {len(valid_set)} samples.")
print(f"Test set: {len(test_set)} samples.")
