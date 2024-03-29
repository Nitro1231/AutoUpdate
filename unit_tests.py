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
import random
import unittest


class EventsTest(unittest.TestCase):
    # Test Group 1: download file and validation check.

    def test_group1_1_download_file(self):
        events.download_file('https://github.com/Nitro1231/AutoUpdate/blob/main/test_update.zip?raw=true', './temp/test_update.zip')
        self.assertTrue(os.path.exists('./temp/test_update.zip'))

    def test_group1_2_checksum(self):
        compare = '9be9ee2b1b451a8ba50ff7411689529e4c076cdfa3d8dc614add464717e0b09f'
        downloaded_file_checksum = events.checksum('./temp/test_update.zip')
        self.assertEqual(compare, downloaded_file_checksum)

    def test_group1_3_unzip_file(self):
        events.unzip_file('./temp/test_update.zip', './temp/')
        self.assertTrue(os.path.exists('./temp/test_update'))
        self.assertTrue(os.path.exists('./temp/test_update/test.txt'))

    def test_group1_4_checksum(self):
        compare = '02cbbe1fb31609fc4928de008c1710212d41c1fb688e3c3b19071cd9fc10df70'
        sum_value = events.checksum('./temp/test_update/test.txt')
        self.assertEqual(compare, sum_value)

    # Test Group 1 ends here.

    def test_checksum(self):
        compare = 'c412e9c22c4f9be167d04330437e2c5e6ba6dbc60fa5fab490790f4a4e7e2635'
        sum_value = events.checksum('./temp/test1/test.json')
        self.assertEqual(compare, sum_value)

    def test_checksum_of_dir(self):
        events.checksum('./temp')

    def test_checksum_of_empty_file(self):
        pass

    def test_unzip_dir(self):
        pass

    def test_unzip_nonzip_file(self):
        pass

    def test_create_redundant_dir(self):
        events.create_dir('./temp/new_dir1')
        events.create_dir('./temp/new_dir1') # Should NOT raise the FileExistsError.
        self.assertTrue(os.path.exists('./temp/new_dir1'))

    def test_create_tree_dir(self):
        events.create_dir('./temp/new_dir2/a/b/c')
        self.assertTrue(os.path.exists('./temp/new_dir2'))
        self.assertTrue(os.path.exists('./temp/new_dir2/a'))
        self.assertTrue(os.path.exists('./temp/new_dir2/a/b'))
        self.assertTrue(os.path.exists('./temp/new_dir2/a/b/c'))

    def test_copy_dir(self):
        events.copy_dir('./temp/test1', './temp/test2/test1_copy')
        self.assertTrue(os.path.exists('./temp/test1'))
        self.assertTrue(os.path.exists('./temp/test2/test1_copy'))
        self.assertTrue(os.path.exists('./temp/test2/test1_copy/sub_test_a'))
        self.assertTrue(os.path.exists('./temp/test2/test1_copy/test.json'))

        sum1 = events.checksum('./temp/test1/test.json')
        sum2 = events.checksum('./temp/test2/test1_copy/test.json')
        self.assertEqual(sum1, sum2)

    def test_copy_dir_to_nonexist_path(self):
        pass

    def test_copy_dir_to_file_path(self):
        pass

    def test_delete_dir(self):
        events.create_dir('./temp/new_dir3/a/b/c')
        events.delete_dir('./temp/new_dir3')
        self.assertTrue(os.path.exists('./temp'))
        self.assertFalse(os.path.exists('./temp/new_dir3/a'))
        self.assertFalse(os.path.exists('./temp/new_dir3/a/b'))
        self.assertFalse(os.path.exists('./temp/new_dir3/a/b/c'))

    def test_delete_file_with_delete_dir_func(self):
        # This SHOULD raise the NotADirectoryError.
        self.assertRaises(NotADirectoryError, events.delete_dir, './temp/test1/test.json')

    def test_delete_nonexists_dir_with_delete_dir_func(self):
        # This SHOULD raise the FileNotFoundError.
        self.assertFalse(os.path.exists('./temp/non_exists_dir/'))
        self.assertRaises(FileNotFoundError, events.delete_dir, './temp/non_exists_dir/')

    def test_read_file(self):
        content = events.read_file('./temp/test1/test.json')
        self.assertEqual(content, '{"a":"a", "b": false, "c": 10}')

    def test_read_dir_not_file(self):
        # This SHOULD raise the FileNotFoundError.
        self.assertTrue(os.path.exists('./temp/test1/'))
        self.assertRaises(FileNotFoundError, events.read_file, './temp/test1/')

    def test_read_non_exist_file(self):
        # This SHOULD raise the FileNotFoundError.
        self.assertFalse(os.path.exists('./nothing.file'))
        self.assertRaises(FileNotFoundError, events.read_file, './nothing.file')

    def test_write_file(self):
        num = random.random()
        events.write_file('./temp/test1/test.txt', f'This is test {num}')

        self.assertTrue(os.path.exists('./temp/test1/test.txt'))
        content = events.read_file('./temp/test1/test.txt')
        self.assertEqual(content, f'This is test {num}')

    def test_write_file_to_nonexist_dir(self):
        # This SHOULD raise the FileNotFoundError.
        self.assertRaises(FileNotFoundError, events.write_file, './temp/non_exists_dir/test.txt', f'This is test')

    def test_copy_file(self):
        events.copy_file('./temp/test1/test.json', './temp/test2/test_copy.json')
        sum1 = events.checksum('./temp/test1/test.json')
        sum2 = events.checksum('./temp/test2/test_copy.json')
        self.assertEqual(sum1, sum2)

    def test_copy_file_to_nonexist_dir(self):
        # This SHOULD raise the FileNotFoundError.
        self.assertRaises(FileNotFoundError, events.copy_file, './temp/test1/test.json', './temp/non_exists_dir/test_copy.json')

    def test_delete_file(self):
        events.delete_file('./temp/test2/test_copy.json')
        self.assertFalse(os.path.exists('./temp/test2/test_copy.json'))

    def test_delete_dir_with_delete_file_func(self):
        # This SHOULD raise the FileNotFoundError.
        self.assertRaises(FileNotFoundError, events.delete_file, './temp/test2/')

def prepare():
    try:
        content = '{"a":"a", "b": false, "c": 10}'
        os.makedirs('./temp/test1/sub_test_a')
        os.makedirs('./temp/test2/sub_test_b')
        with open('./temp/test1/test.json', 'w', encoding='utf-8') as f:
            f.write(content)
        
        with open('./temp/test1/test.json', 'w', encoding='utf-8') as f:
            f.write('')
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
