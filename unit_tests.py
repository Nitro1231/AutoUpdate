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
import shutil
import events
import unittest


class EventsTest(unittest.TestCase):
    def test_download_file(self):
        pass
    
    def test_checksum(self):
        compare = 'c412e9c22c4f9be167d04330437e2c5e6ba6dbc60fa5fab490790f4a4e7e2635'
        sum_value = events.checksum('./temp/test1/test.json')
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
    prepare()
    unittest.main()
