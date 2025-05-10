from pratik.logger import Logger

path = "logs"

def logger_init():
    logger = Logger(path)
    print(logger.absolute())

def log_text():
    logger = Logger(path)
    logger.log("Message", "for example")

def log_text_not_colored():
    logger = Logger(path)
    logger.log("Message not colored", "for example", colored=False)

def log_text_not_printed():
    logger = Logger(path)
    logger.log("Message not printed", "for example", printed=False)

def log_error():
    logger = Logger(path)
    logger.log("Message error", "for example", level=Logger.Level.ERROR)

def log_text_another_file():
    logger = Logger(path)
    logger.log("Message in another file", "for example", file="logs/special.log")

if __name__ == '__main__':
    logger_init()
    log_text()
    log_text_not_colored()
    log_text_not_printed()
    log_error()
    log_text_another_file()