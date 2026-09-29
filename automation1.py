from pathlib import Path
import logging
import shutil

logger = logging.getLogger("AUTOMATE")
logger.setLevel(logging.INFO)

console = logging.StreamHandler()

logger.addHandler(console)

console_formatter = logging.Formatter(
    "%(name)s - %(levelname)s - %(message)s"
)

console.setFormatter(console_formatter)

try:
    cd = Path("ClientData")
    cb = Path("ClientBackup")

    if cd.exists():
        shutil.copytree(cd, cb, dirs_exist_ok=True)

        logger.info("Backup started")
        logger.info("Backup completed")

        file_count = 0
    else:
        logger.error("ClientData not found")

    for items in cb.rglob("*"):
        if items.is_file():
            file_count += 1

    logger.info("Files backed up: %s", file_count)

except:
    logger.exception("FAILED")