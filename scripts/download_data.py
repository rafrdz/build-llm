#!/usr/bin/env python3

import os
import urllib.request


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

data_dir = os.path.join(project_root, "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

print("Downloading data...")
url = (
    "https://raw.githubusercontent.com/rasbt/"
    "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
    "the-verdict.txt"
)
file_path = os.path.join(data_dir, "the-verdict.txt")
urllib.request.urlretrieve(url, file_path)
print(f"Data downloaded and saved to '{file_path}'.")
