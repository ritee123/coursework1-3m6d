import unittest
from unittest.mock import patch, MagicMock
import base64
import sys
from bs4 import BeautifulSoup
import re
import requests 

# Assuming the dns_dumpster function is defined as follows:
def dns_dumpster():
    global a1
    try:
        if a1.startswith('https://'):
            a1 = a1[8:]
        else:
            a1 = a1
    except IndexError:
        a1 = 'google.com'
    domain = a1
    print(f'Running dns-dumpster on:{domain}...')
    dnsdumpster_url = 'https://dnsdumpster.com/'

    req = requests.session().get(dnsdumpster_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    csrf_middleware = soup.findAll('input', attrs={'name': 'csrfmiddlewaretoken'})[0]['value']

    cookies = {'csrftoken': csrf_middleware}
    headers = {'Referer': dnsdumpster_url,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/92.0.4515.107 Safari/537.36'}
    data = {'csrfmiddlewaretoken': csrf_middleware, 'targetip': domain, 'user': 'free'}
    req = requests.session().post(dnsdumpster_url, cookies=cookies, data=data, headers=headers)

    if req.status_code != 200:
        print(
            "Unexpected status code from {url}: {code}".format(
                url=dnsdumpster_url, code=req.status_code),
            file=sys.stderr,
        )
        return []

    if 'There was an error getting results' in req.content.decode('utf-8'):
        print("There was an error getting results", file=sys.stderr)
        return []

    res = {}
    xls_data = None
    try:
        pattern = r'/static/xls/' + domain + '-[0-9]{12}\.xlsx'
        xls_url = re.findall(pattern, req.content.decode('utf-8'))[0]
        xls_url = 'https://dnsdumpster.com' + xls_url
        xls_data = base64.b64encode(requests.session().get(xls_url).content)
    except Exception as err:
        print(err)
    finally:
        res['xls_data'] = xls_data

    xls_retrieved = res['xls_data'] is not None
    print("\n\n\nRetrieved XLS hosts? {} (accessible in 'xls_data')".format(xls_retrieved))
    if xls_retrieved:
        print(repr(base64.b64decode(res['xls_data'])[:20]) + '...')
        # Example of saving xlsx file
        open(f'result/{a1}/dns_dumpster.xlsx', 'wb').write(base64.b64decode(res['xls_data']))
        print(f"dnsdumpster results stored in:dns_{domain}.xlsx")

# Here's the unit test for the dns_dumpster function
class TestDnsDumpster(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="data")
    @patch('base64.b64decode', return_value=b'Some decoded data')
    @patch('re.findall', return_value=['/static/xls/example.com-123456789012.xlsx'])
    @patch('requests.Session.post')
    @patch('requests.Session.get')
    def test_successful_dns_dumpster(self, mock_get, mock_post, mock_findall, mock_b64decode, mock_open):
        # Set up the mock responses for get and post requests
        mock_get_response = MagicMock()
        mock_get_response.content = b'<html><input name="csrfmiddlewaretoken" value="dummytoken"></html>'
        mock_get.return_value = mock_get_response

        mock_post_response = MagicMock()
        mock_post_response.status_code = 200
        mock_post_response.content = b'Successful response content including a link to an XLS file'
        mock_post.return_value = mock_post_response

        # Call the function with a test domain
        global a1
        a1 = 'https://example.com'
        dns_dumpster()

        # Verify that the requests were made as expected
        mock_get.assert_called_once()
        mock_post.assert_called_once()
        mock_findall.assert_called_once()
        mock_b64decode.assert_called_once()
        mock_open.assert_called_once_with('result/example.com/dns_dumpster.xlsx', 'wb')

        # Additional assertions can be added here to further verify the correct behavior of your function

if __name__ == '__main__':
    unittest.main()
