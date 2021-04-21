from sys import argv
from configurator import Configurator
from connector import Connector
from resulting import Result
from test_processor import TestProcessor


def run(env):
    config = Configurator(env)
    server_name = config.get_server_name()
    db_name = config.get_db_name()

    logger = Result()

    connector = Connector(server_name, db_name,logger)

    test_processor = TestProcessor(config, connector, logger)
    test_processor.process()

    logger.finish_test()


if __name__ == '__main__':
    env = argv[1]  # Use it for running from cli
    # env = "dev"  # Use it for running from IDE for debugging
    run(env)

# comment2