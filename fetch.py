import urllib
import urllib.request
import urllib.error
import os

from functools import wraps


class BabyFetchException(Exception):
    def __init__(self):
        print('Request Failed')


def safe_internet_fetch(func):
    """
    (1 point)
    A decorator that catches fetching error (i.e. urllib.error.URLERROR) and raises a custom `BabyFetchException`.
    Args:
        func: The function to decorate
    Raises:
        BabyFetchException: if it fails to fetch the html codes from the url.
    """
    # TODO: Implement this decorator
    def inner_function(url, year):
        try:
            return func(url, year)
        except urllib.error.URLError:
            raise BabyFetchException

    return inner_function


@safe_internet_fetch
def fetch_top_1000(url, year):
    """
    (2 points)
    Given a year of interest, fetches the html file from the top1000 popular names
    of that year and return the html codes in text
    Args:
        url: the target url to send request
        year: The year of interest in integer.
    Return:
        text: a string. HTML content of the fetch webpage.
    """

    # TODO: Implement this function.
    # Send POST request to the given url (https://www.ssa.gov/cgi-bin/popularnames.cgi) with the data by inspecting the web page.
    # Hint: You can concatenate multiple data using '&' (e.g. data = "month=December&day=25")
    # You must use standard library `urllib` to send request. (i.e. 3rd party libraries are not allowed.)
    # urllib reference link: https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen

    data = urllib.parse.urlencode({'year': year, 'top': 1000})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data=data)
    res = urllib.request.urlopen(req)
    result = res.read()
    return result.decode('utf-8')


def main():
    # NOTE: DO NOT change this function.
    # This function fetches and saves the html file of popular names in 2001-2018.
    # The example output html files are provided in `babydata/` directory.
    # The output html files you generate should be same with the provided example html files.
    # You can check the difference with `diff` command.
    for year in range(2001, 2019):
        pathname = os.path.join("babydata", "{}.html".format(year))
        with open(pathname, "w") as f:
            # target url to fetch baby data
            url = "https://www.ssa.gov/cgi-bin/popularnames.cgi"
            f.write(fetch_top_1000(url, year))


if __name__ == '__main__':
    main()
