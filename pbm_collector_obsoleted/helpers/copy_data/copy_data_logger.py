import logging, ConfigParser
config = ConfigParser.ConfigParser()
config.read("copy_data.conf")
log_file_name = config.get("logger", "log_file")

def logger(log_title, log_level, log_file_name):
    LEVEL = {'debug': logging.DEBUG,
           'info': logging.INFO,
           'warning': logging.WARNING,
           'error': logging.ERROR,
           'critical': logging.CRITICAL}

    logging.basicConfig(level=LEVEL[log_level],
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=log_file_name,
                        filemode='a')
    #                    format='%(asctime)s %(name)-12s - %(module)s:%(funcName)s:%(lineno)d - %(levelname)-8s %(message)s',
    #formatter = logging.Formatter('%(name)-12s: - %(module)s:%(funcName)s:%(lineno)d - %(levelname)-8s %(message)s')
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    return logging.getLogger(log_title)
