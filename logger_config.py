import logging
from pathlib import Path


LOG_PATH = Path(__file__).resolve().parent.parent / "library_manager.log"


def setup_logging():
logger = logging.getLogger("library_manager")
logger.setLevel(logging.DEBUG)


if not logger.handlers:
# File handler
fh = logging.FileHandler(LOG_PATH, encoding="utf-8")
fh.setLevel(logging.INFO)
fh_formatter = logging.Formatter(
"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
fh.setFormatter(fh_formatter)
logger.addHandler(fh)


# Stream handler
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
ch_formatter = logging.Formatter("%(levelname)s: %(message)s")
ch.setFormatter(ch_formatter)
logger.addHandler(ch)


return logger