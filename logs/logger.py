import logging
import datetime

log_date = datetime.date.today()
log_time = datetime.datetime.now().time().strftime("%H%M%S")

log_format = "%(asctime)s - %(message)s"

logging.basicConfig(filename=rf"log_{log_date}_{log_time}.log",
                    level=logging.INFO,
                    datefmt='%d-%m-%y %H:%M:%S',
                    format=log_format,
                    filemode='a')

logster = logging.StreamHandler()
logster.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
logster.setFormatter(formatter)
logging.getLogger().addHandler(logster)

log = logging.getLogger()
