from dyson.utils.module import DysonModule


class DebugModule(DysonModule):
    def run(self, webdriver, params):
        if 'var' in params:
            print("DEBUG: %s" % params['var'])
        if 'msg' in params:
            print("DEBUG: %s" % params['msg'])
