import unittest
from unittest.mock import MagicMock
import json
from tkinter import messagebox

# Assume the show_user_details function is defined in the same module
def show_user_details(tv, selected_item):
    user_data = tv.item(selected_item)['values']
    detail_message = f"Name: {user_data[0]}\nCitizenship: {user_data[1]}\nPhone: {user_data[2]}\nAddress: {user_data[3]}\nEmail: {user_data[4]}\nAccount Type: {user_data[5]}\nAccount Number: {user_data[6]}"
    messagebox.showinfo("User Details", detail_message)
    return detail_message

class TestShowUserDetails(unittest.TestCase):

    def test_show_user_details(self):
        # Mocking the Treeview widget
        tv_mock = MagicMock()
        tv_mock.item.return_value = {'values': ['Tom Black', '12345678', '1234567890', 'QUEXON', 'superbapple0@gmail.com', 'customer', 13643, 84056]}
        selected_item = "item1"
        
        # Call the function with the mock widget
        result = show_user_details(tv_mock, selected_item)

        # Assert the result matches the expected detail message
        expected_detail_message = "Name: Tom Black\nCitizenship: 12345678\nPhone: 1234567890\nAddress: QUEXON\nEmail: superbapple0@gmail.com\nAccount Type: customer\nAccount Number: 13643"
        self.assertEqual(result, expected_detail_message)

if __name__ == '__main__':
    unittest.main()
