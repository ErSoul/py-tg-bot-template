import logging

def logger(name: str = None) -> logging.Logger:
    # timedHandler = logging.handlers.TimedRotatingFileHandler("chamano_bot.log", when = 'midnight', interval = 1)
    # timedHandler.prefix = "%Y%m%d"

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.WARNING,
        handlers=[
            logging.FileHandler("info.log"), # Single log for all the execution
            logging.StreamHandler(), # Also show logs in stderr
            # timedHandler
        ]
    )

    return logging.getLogger(name)
