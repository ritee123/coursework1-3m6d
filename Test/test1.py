import unittest
def send(account_number, PIN, phone):
    try:
        response = {
            'status_code': 200,
            'text': 'Message sent successfully'
        }
        return response
    except Exception as e:
        print(f"Error sending message: {str(e)}")
        return None

class TestSendFunction(unittest.TestCase):
    def test_send_success(self):
        account_number = '1234567890'
        PIN = '1234'
        phone = {'phoneNumber': '+1234567890'}

        response = send(account_number, PIN, phone)

        self.assertEqual(response['status_code'], 200)
        self.assertEqual(response['text'], 'Message sent successfully')

if __name__ == '__main__':
    unittest.main()
