import unittest
from unittest.mock import MagicMock
import json
from stegano import lsb

def userlogin_validation(WIN, phonenumber, password):
    image_path = "images/profileimg.png"
    decoded_data = lsb.reveal(image_path)
    decoded_data = json.loads(decoded_data)

    users = decoded_data.get("users", [])
    
    for user in users:
        if len(user) > 7 and user[2] == phonenumber and str(user[7]) == password:
            WIN.destroy()
            return True
    
    return False

class TestUserLoginValidation(unittest.TestCase):

    def test_valid_user_login(self):
        WIN = MagicMock()
        phonenumber = '1234567890'
        password = '84056'
        result = userlogin_validation(WIN, phonenumber, password)
        self.assertTrue(result)

    def test_invalid_user_login(self):
        WIN = MagicMock()
        phonenumber = '1111111111'
        password = '1111'
        result = userlogin_validation(WIN, phonenumber, password)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
