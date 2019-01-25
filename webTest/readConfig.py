import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, 'config.ini')


class ReadConfig:
    def __init__(self):
        ft = open(configPath)
        data = ft.read()

        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            f = codecs.open(configPath, 'w')
            f.write(data)
            f.close()
        ft.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_webServer(self, name1, name2):
        """
        get value by name
        :param name1:
        :param name2:
        :return:
        """
        value = self.cf.get(name1, name2)
        return value

