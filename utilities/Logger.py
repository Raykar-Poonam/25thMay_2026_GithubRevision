import logging
import inspect


class loggen:

    @staticmethod
    def gen_logger():

        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)

        if not logger.handlers:

            logger.setLevel(logging.INFO)

            log_file = logging.FileHandler(
                "C:\\Users\\aksha\\PycharmProjects\\PythonProject5\\Logs\\test_login_QAbrains_TC01_Logs.log")
            log_format = logging.Formatter(" %(asctime)s : %(lineno)s : %(levelname)s : %(funcName)s : %(name)s : %(message)s ")
            log_file.setFormatter(log_format)
            logger.addHandler(log_file)

        return logger
















