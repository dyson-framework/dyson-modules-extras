from dyson.utils.module import DysonModule


class AddCookieModule(DysonModule):
    def run(self, webdriver, params):
        """
        Add cookie(s) to the session
        :param webdriver:
        :param params:
        :return:
        """
        return webdriver.add_cookie(params)
