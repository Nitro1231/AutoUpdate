# UnitTests.py
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
import time
import shutil
import events
import unittest


class EventsTest(unittest.TestCase):
    def test_1_download_file(self):
        events.download_file('https://github.com/Nitro1231/AutoUpdate/blob/main/test_update.zip?raw=true', './temp/test_update.zip')
        self.assertTrue(os.path.exists('./temp/test_update.zip'))

    def test_2_checksum(self):
        compare = '9be9ee2b1b451a8ba50ff7411689529e4c076cdfa3d8dc614add464717e0b09f'
        downloaded_file_checksum = events.checksum('./temp/test_update.zip')
        self.assertEqual(compare, downloaded_file_checksum)

    def test_3_checksum(self):
        compare = 'c412e9c22c4f9be167d04330437e2c5e6ba6dbc60fa5fab490790f4a4e7e2635'
        sum_value = events.checksum('./temp/test1/test.json')
        self.assertEqual(compare, sum_value)

    def test_4_unzip_file(self):
        events.unzip_file('./temp/test_update.zip', './temp/')
        self.assertTrue(os.path.exists('./temp/test_update'))
        self.assertTrue(os.path.exists('./temp/test_update/test.txt'))

    def test_5_checksum(self):
        compare = '02cbbe1fb31609fc4928de008c1710212d41c1fb688e3c3b19071cd9fc10df70'
        sum_value = events.checksum('./temp/test_update/test.txt')
        self.assertEqual(compare, sum_value)

def prepare():
    try:
        content = '{"a":"a", "b": false, "c": 10}'
        os.makedirs('./temp/test1/sub_test_a')
        os.makedirs('./temp/test2/sub_test_b')
        with open('./temp/test1/test.json', 'w', encoding='utf-8') as f:
            f.write(content)
    except FileExistsError:
        pass

def clean_up():
    try:
        shutil.rmtree('./temp')
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    clean_up()
    time.sleep(0.5)
    prepare()
    time.sleep(0.5)
    unittest.main()
