import os
import datetime
from dotenv import load_dotenv


def run():
    load_dotenv()

    print("Executando robocopy...\n")

    get_date = datetime.date.today()
    get_time = datetime.datetime.now().time().strftime("%H%M%S")

    source = os.getenv("source_path")
    destiny = os.getenv("destiny_path")
    mir_option = os.getenv("mir_option")

    os.system(f'cmd /c "robocopy {source} {destiny} {mir_option} >> logs/log_{get_date}_{get_time}.log"')


if __name__ == "__main__":
    run()
