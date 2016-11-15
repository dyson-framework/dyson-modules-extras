from dyson.errors import DysonError
from dyson.utils.module import DysonModule


class AddCookiesModule(DysonModule):
    def run(self, webdriver, params):
        """
        Add cookie(s) to the session
        :param webdriver:
        :param params:
        :return:
        """
        if isinstance(params, list):
            for cookie in params:
                webdriver.add_cookie(cookie)
        else:
            raise DysonError("Type needs to be array.")
