import unittest
from unittest.mock import MagicMock
import random

def create_new_user(WIN, name_entry, citizenship_entry, phone_entry, address_entry, email_entry, account_type_entry):
    # Mocking lsb.reveal and lsb.hide functions
    def reveal_mock(image_path):
        return '{"users":[]}'
    
    def hide_mock(image_path, data):
        return None

    # Mocking send function
    def send_mock(PIN, account_number, phone_data):
        return None

    # Mocking confirm_account_creation function
    def confirm_account_creation_mock(WIN):
        return None

    # Replace the actual functions with mocked ones
    lsb = MagicMock()
    lsb.reveal = reveal_mock
    lsb.hide = hide_mock
    send = send_mock
    confirm_account_creation = confirm_account_creation_mock

    # Extract data from entry fields
    name = name_entry.get()
    citizenship = citizenship_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    email = email_entry.get()
    account_type = account_type_entry.get()
    account_number = random.randint(10000, 99999)
    PIN = random.randint(10000, 99999)
    
    # Validate user input
    if (len(name) != 0 and len(citizenship) != 0 and len(phone) != 0 and len(address) != 0
        and len(email) != 0 and len(account_type) != 0):
        
        # Call the necessary functions
        json_data = '{"users":[]}'
        encoded_image = lsb.hide("images/img.png", json_data)
        confirm_account_creation(WIN)
        send(PIN, account_number, {'phoneNumber': '+977' + phone})
    else:
        # Mocking error function
        def error_mock(title, message):
            return None

        # Replace the actual error function with the mocked one
        error = error_mock
        error("Error", "Recheck Your Input Values")

# Unit tests
def test_create_new_user():
    # Mock entry fields with valid data
    name_entry = MagicMock(get=MagicMock(return_value="John Doe"))
    citizenship_entry = MagicMock(get=MagicMock(return_value="1234567890"))
    phone_entry = MagicMock(get=MagicMock(return_value="9876543210"))
    address_entry = MagicMock(get=MagicMock(return_value="123 Main St"))
    email_entry = MagicMock(get=MagicMock(return_value="john.doe@example.com"))
    account_type_entry = MagicMock(get=MagicMock(return_value="Savings"))
    
    # Mock the window
    WIN = MagicMock()

    # Call the function under test
    create_new_user(WIN, name_entry, citizenship_entry, phone_entry, address_entry, email_entry, account_type_entry)

# Run the unit tests
test_create_new_user()

if __name__ == '__main__':
    unittest.main()
