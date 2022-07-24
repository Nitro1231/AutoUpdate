# Events.py
#
# Copyright 2022 Nitro. All Rights Reserved.
#
# Developer: Nitro (admin@nitrostudio.dev)
# Blog: https://blog.nitrostudio.dev
# Discord: Nitro#1781
# GitHub: https://github.com/Nitro1231/AutoUpdate
#
# Version: 1.0.0
# Last Modified: N/A
#
# This project is licensed under the GNU Affero General Public License v3.0;
# you may not use this file except in compliance with the License.


import os
import json
import shutil
import hashlib
import zipfile
import requests


def download_file(url: str, path: str) -> None:
    req = requests.get(url)
    with open(path, 'wb') as f:
        f.write(req.content)

def checksum(path: str) -> str:
    with open(path, 'rb') as f:
        data = f.read()
        hash_value = hashlib.sha256(data).hexdigest();
    return hash_value

def unzip_file(zip_path: str, target_path: str) -> None:
    with zipfile.ZipFile(zip_path, 'r') as f:
        f.extractall(target_path)


def create_dir(path: str) -> None:
    os.makedirs(path)

def copy_dir(src_path: str, dest_path: str) -> None:
    shutil.copytree(src_path, dest_path)

def delete_dir(path: str) -> None:
    os.rmdir(path)


def read_file(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path: str, content: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def copy_file(src_path: str, dest_path: str) -> None:
    shutil.copyfile(src_path, dest_path)

def delete_file(path: str) -> None:
    os.remove(path)


def move_item(src_path: str, dest_path: str) -> None:
    shutil.move(src_path, dest_path)

def rename_item(src_path: str, dest_path: str) -> None:
    os.rename(src_path, dest_path)


def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(path: str, data: dict) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def update_json(org_data: dict, new_data: dict) -> dict:
    for k, v in new_data.items():
        if v == dict:
            if k in org_data:
                org_data[k] = update_json(org_data[k], v)
            else:
                org_data[k] = v
        else:
            org_data[k] = v
    return org_data

def check_json():
    pass

def update_json_value(data: dict, key: str, value: any) -> dict:
    data[key] = value
    return data

def delete_json_item(data: dict, key: str) -> dict:
    del data[key]
    return data
