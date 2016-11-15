from six import string_types
import time

from dyson.errors import DysonError
from dyson.utils.module import DysonModule


class SleepModule(DysonModule):

    VALID_OPTIONS = frozenset(['seconds', 's', 'milliseconds', 'ms'])

    def run(self, webdriver, params):
        """
        Sleep for a time
        :param webdriver:
        :param params:
        :return:
        """
        if isinstance(params, string_types):
            # they specified - sleep: 5
            # assume seconds
            time.sleep(params)
        elif isinstance(params, dict):
            if 'seconds' in params:
                time.sleep(params['seconds'])
            elif 's' in params:
                time.sleep(params['s'])

            elif 'ms' in params:
                ms = int(params['ms'])
                time.sleep(ms / 1000)
            elif 'milliseconds' in params:
                ms = int(params['milliseconds'])
                time.sleep(ms / 1000)
            else:
                raise DysonError(
                    "Invalid option \"%s\" for sleep. Valid options are %s" % (params, ','.join(self.VALID_OPTIONS)))
