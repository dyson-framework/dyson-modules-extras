from six import string_types

from dyson.errors import DysonError
from dyson.utils.module import DysonModule


class GetCookiesModule(DysonModule):
    def run(self, webdriver, params):
        """
        Get specific cookies, or all cookies.
        :param webdriver:
        :param params:
        :return:
        """
        if isinstance(params, dict):
            if 'name' in params:
                return webdriver.get_cookie(params['name'])
        elif isinstance(params, list):
            cookies = list()
            for cookie in params:
                cookies.append(webdriver.get_cookie(cookie))
            return cookies
        elif isinstance(params, string_types):
            if params is 'all':
                return webdriver.get_cookies()
            else:
                raise DysonError("Don't know how to fetch \"%s\". To get all cookies, specify \"all\"")
        else:
            raise DysonError("Invalid type")
