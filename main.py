import os
from logs.logger import log
from dotenv import load_dotenv


def run():
    load_dotenv()

    log.info("Executando robocopy...\n")

    source = os.getenv("source_path")
    destiny = os.getenv("destiny_path")
    option = os.getenv("option")

    try:
        output = os.popen(f'cmd /c "robocopy {source} {destiny} {option}"').read()
        log.info(output)

        log.info("Robocopy executado com sucesso!")
        log.info("###########################################################\n\n")

    except Exception as e_run:
        log.info('Erro encontrado:')
        log.info(e_run)


if __name__ == "__main__":
    run()
