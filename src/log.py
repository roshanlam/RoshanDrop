import logging
import logging.handlers
import copy

logger = None

LOG_FILE='roshandrop.log'


class _Logger:
    """
    The RoshanDrop logger, which basically implements the functions from the
    logging module
    """
    def __init__(self, log_file=LOG_FILE):
        common = '%(asctime)s.%(msecs)-4d %(levelname)-8s '
        default_format = common + '%(message)s'
        datefmt = '%d/%m/%Y %H:%M:%S'

        self._log = logging.getLogger('RoshanDrop')

        logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=log_file,
                    filemode='w')

        # define a Handler which writes INFO messages or higher to the sys.stderr
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        # set a format which is simpler for console use
        formatter = logging.Formatter(default_format, datefmt)
        # tell the handler to use this format
        self.console.setFormatter(formatter)

        # add the handler to the root logger
        #self._log.addHandler(self.console)

        root = logging.getLogger()


    def set_level(self, name):
        """
        Set the log level. name can be one of:
        - 'INFO'
        - 'DEBUG'
        - 'DEBUG_DETAILLED'
        - 'DEBUG_VERBOSE'
        """
        level = logging.getLevelName(name)
        self._log.setLevel(level)
        self._level_name = name


    def info(self, info):
        """
        Log some basic info (in >= INFO log level)
        """
        self._log.log(logging.INFO, info)


    def debug(self, msg, obj=None):
        """
        Log functional data (in >= DEBUG log level)
        """
        self._log.log(logging.DEBUG, msg)


    def debug_detailled(self, msg, obj=None):
        """
        Log verbose functional data (in >= DEBUG_DETAILLED log level)
        """
        self._log.log(self.levels['DEBUG_DETAILLED'], msg)


    def debug_verbose(self, msg, obj=None):
        """
        Detailled logging (in >= DEBUG_VERBOSE log level)
        """
        self._log.log(self.levels['DEBUG_VERBOSE'], msg)


def Logger(log_file=LOG_FILE):
    global logger
    if not logger:
        logger = _Logger(log_file)
    return logger


if __name__ == '__main__':
    l = Logger()

    l.info("Hello World")
    l.debug("Argh")
