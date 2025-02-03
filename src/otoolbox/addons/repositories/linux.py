import subprocess
import logging

from otoolbox import env

from rich.console import Console
from rich.table import Table

logger = logging.getLogger(__file__)


def call_safe(command, shell=False, cwd='.'):
    try:
        with open(env.get_workspace() + "/.vw/app.logs", "a") as log:
            ret = subprocess.call(command, shell=shell,
                                  cwd=cwd, stdout=log, stderr=log)
            if ret != 0:
                if ret < 0:
                    print("Killed by signal")
                else:
                    print("Command failed with return code")
                return ret
    except Exception as e:
        logger.error('Failed to execute command: %s', e)
        return 2


def progressBar(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function

    def printProgressBar(iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                         (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()


def run(commands, **kargs):
    for command in progressBar(
            commands,
            prefix='Progress:',
            suffix='Complete',
            length=50):
        if callable(command):
            command(**kargs)
        else:
            call_safe(command)


def info_table(data, keys, columns=None,  title="#"):
    table = Table(title, show_lines=True)
    rows = []

    if not columns:
        columns = keys

    for column in columns:
        table.add_column(column)

    count = 1
    for item in data:
        row = [str(count)]
        count = count+1
        for key in keys:
            row.append(item[key])
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)
