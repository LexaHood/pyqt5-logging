import logging, time
logger  = logging.getLogger('app.repository.db')

class Objk(object):
    def __init__(self) -> None:
        super().__init__()

        logger.debug(f'object: {self} was initialized')

    def work() -> None:
        logger.info('work start!')
        time.sleep(1)
        logger.info('work end!')