import sys
from app.presentations.console import main
import logging

log_level = logging.INFO


if __name__ == "__main__":
    args = sys.argv

    if len(args) == 3:
        log_level = args[2]

    logging.basicConfig(
        format='%(asctime)s - [%(levelname)s]: %(message)s',
        datefmt='%H:%M',
        level=log_level
    )

    sys.exit(main(args))