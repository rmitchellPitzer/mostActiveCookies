# import most_active_cookie
from most_active_cookie import CookieInstance
from io import StringIO
import sys

def test_for_initializing_cookies():
        cookies = CookieInstance()
        assert [] == cookies.csvFile
        assert {} == cookies.mapOfCookies
        assert [] == cookies.listOfOccurences
def test_for_reading_in_csv_file():
    cookies = CookieInstance()
    cookies.readInCSV('cookie_log.csv')
    assert cookies.csvFile == [('cookie', 'timestamp\n'), ('AtY0laUfhglK3lC7', '2018-12-09T14:19:00+00:00\n'), ('SAZuXPGUrfbcn5UA', '2018-12-09T10:13:00+00:00\n'), ('5UAVanZf6UtGyKVS', '2018-12-09T07:25:00+00:00\n'), ('AtY0laUfhglK3lC7', '2018-12-09T06:19:00+00:00\n'), ('SAZuXPGUrfbcn5UA', '2018-12-08T22:03:00+00:00\n'), ('4sMM2LxV07bPJzwf', '2018-12-08T21:30:00+00:00\n'), ('fbcn5UAVanZf6UtG', '2018-12-08T09:30:00+00:00\n'), ('4sMM2LxV07bPJzwf', '2018-12-07T23:30:00+00:00')]

def test_for_reading_in_incorrect_csv_file():
    cookies = CookieInstance()
    printedOutput = StringIO()
    sys.stdout = printedOutput
    output = cookies.readInCSV('wrong file path')
    sys.stdout = sys.__stdout__
    assert cookies.csvFile == []
    assert output == 1
    assert printedOutput.getvalue() == 'Oops,  wrong file path  is not a valid filename, try again!\n'

def test_for_updating_map_of_cookies():
    cookies = CookieInstance()
    cookies.readInCSV('cookie_log.csv')
    cookies.updateMapOfCookies()
    assert cookies.mapOfCookies == {'2018-12-09': ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS', 'AtY0laUfhglK3lC7'], '2018-12-08': ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'], '2018-12-07': ['4sMM2LxV07bPJzwf']}

def test_for_updating_map_of_empty_cookies():
    cookies = CookieInstance()
    cookies.updateMapOfCookies()
    assert cookies.mapOfCookies == {}

def test_for_finding_occurences():
    cookies = CookieInstance()
    cookies.readInCSV('cookie_log.csv')
    cookies.updateMapOfCookies()
    cookies.findOccurences('2018-12-09')
    assert cookies.listOfOccurences == [[], ['SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS'], ['AtY0laUfhglK3lC7'], []]

def test_for_finding_empty_occurences():
    cookies = CookieInstance()
    printedOutput = StringIO()
    sys.stdout = printedOutput
    cookies.findOccurences('2018-12-09')
    sys.stdout = sys.__stdout__ 
    assert cookies.listOfOccurences == []
    assert printedOutput.getvalue() == 'Oops,  2018-12-09  is not a valid date, try again!\n'

def test_for_returning_max_cookie():
    cookies = CookieInstance()
    cookies.readInCSV('cookie_log.csv')
    cookies.updateMapOfCookies()
    cookies.findOccurences('2018-12-09')
    printedOutput = StringIO()
    sys.stdout = printedOutput
    cookies.returnMax()
    sys.stdout = sys.__stdout__ 
    assert printedOutput.getvalue() == 'AtY0laUfhglK3lC7\n'

def test_for_returning_max_cookies():
    cookies = CookieInstance()
    cookies.readInCSV('cookie_log.csv')
    cookies.updateMapOfCookies()
    cookies.findOccurences('2018-12-08')
    printedOutput = StringIO()
    sys.stdout = printedOutput
    cookies.returnMax()
    sys.stdout = sys.__stdout__ 
    assert printedOutput.getvalue() == 'SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n'

def test_for_returning_max_cookies_with_empty_array():
    cookies = CookieInstance()
    printedOutput = StringIO()
    sys.stdout = printedOutput
    cookies.returnMax()
    sys.stdout = sys.__stdout__ 
    assert printedOutput.getvalue() == 'There were no cookies present.\n'

def test_for_running_script_with_valid_arguments():
    cookies = CookieInstance()
    printedOutput = StringIO()
    sys.stdout = printedOutput
    cookies.runScript('cookie_log.csv', '2018-12-08')
    sys.stdout = sys.__stdout__ 
    assert printedOutput.getvalue() == 'SAZuXPGUrfbcn5UA\n4sMM2LxV07bPJzwf\nfbcn5UAVanZf6UtG\n'

def test_for_running_script_with_invalid_file_name():
    cookies = CookieInstance()
    printedOutput = StringIO()
    sys.stdout = printedOutput
    cookies.runScript('wrong file path', '2018-12-08')
    sys.stdout = sys.__stdout__ 
    assert printedOutput.getvalue() =='Oops,  wrong file path  is not a valid filename, try again!\n'

def test_for_running_script_with_invalid_date():
    cookies = CookieInstance()
    printedOutput = StringIO()
    sys.stdout = printedOutput
    cookies.runScript('cookie_log.csv', '2018-12-15')
    sys.stdout = sys.__stdout__ 
    assert printedOutput.getvalue() == 'Oops,  2018-12-15 is not a valid date, try again!\n'

if __name__ == "__main__":
    test_for_initializing_cookies()
    test_for_reading_in_csv_file()
    test_for_reading_in_incorrect_csv_file()
    test_for_updating_map_of_cookies()
    test_for_updating_map_of_empty_cookies()
    test_for_finding_occurences()
    test_for_finding_empty_occurences()
    test_for_returning_max_cookie()
    test_for_returning_max_cookies()
    test_for_returning_max_cookies_with_empty_array()
    test_for_running_script_with_valid_arguments()
    print("All tests passed!")