import os
import datetime
from logs.logger import log
from dotenv import load_dotenv


def run():
    load_dotenv()

    log.info("Executando robocopy...\n")

    # get_date = datetime.date.today()
    # get_time = datetime.datetime.now().time().strftime("%H%M%S")

    source = os.getenv("source_path")
    destiny = os.getenv("destiny_path")
    mir_option = os.getenv("mir_option")

    try:
        # os.system(f'cmd /c "robocopy {source} {destiny} {mir_option} >> logs/log_{get_date}_{get_time}.log"')
        output = os.popen(f'cmd /c "robocopy {source} {destiny} {mir_option}"').read()

        log.info(output)

    except Exception as e_run:
        log.info('Erro encontrado:')
        log.info(e_run)


if __name__ == "__main__":
    run()
