from comm.Log import MyLog as Log
import HTMLTestRunner
import readConfig as readConfig
import time
import comm.runSet as runSet

localReadConfig = readConfig.ReadConfig()


class AllTest:

    def __init__(self):
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.resultPath = self.log.get_report_path()

    def run(self):
        """
        run test
        :return:
        """
        suite = runSet.set_suite()
        try:
            if suite is not None:
                self.logger.info('************ TEST START ************')
                time.sleep(2)

                runSet.set_website()

                fb = open(self.resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='WEB UI TEST', description='Test Description')
                runner.run(suite)
            else:
                self.logger.info('Have no case to test!')
        except Exception as ex:
            self.logger.error(str(ex))
        finally:
            runSet.close_browser()
            self.logger.info('************　TEST END ************')


if __name__ == "__main__":
    obj = AllTest()
    obj.run()
