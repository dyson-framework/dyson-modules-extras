from six import string_types

from dyson.utils.module import DysonModule


class DeleteCookiesModule(DysonModule):
    def run(self, webdriver, params):
        """
        Delete specific cookies, or delete all cookies
        :param webdriver:
        :param params:
        :return:
        """
        if isinstance(params, list):
            for cookie in params:
                webdriver.delete_cookie(cookie)
        elif isinstance(params, string_types):
            if params is 'all':
                webdriver.delete_all_cookies()
            else:
                webdriver.delete_cookie(params)
