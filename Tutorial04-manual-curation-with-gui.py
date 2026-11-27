import os
from pathlib import Path

import numpy as np
import spikeinterface.full as si


from spikeinterface_gui import run_mainwindow


# change this path to point to the folder your data is in
home = Path.home()
base_data_folder = Path(home / "cnn_2026")

data_folder = base_data_folder / "data"
name = "sub-A3702_ses-191126-3600s"
result_folder = base_data_folder / "results" / name
result_folder.mkdir(exist_ok=True, parents=True)


sorter_name = "lupin"
# sorter_name = "kilosort4"
# sorter_name = "dartsort"

analyzer_folder = result_folder / f"analyzer_{sorter_name}"

analyzer = si.load(analyzer_folder)
print(analyzer)

def example1():
    # standard mode
    run_mainwindow(analyzer)

def example2():
    # options : run in web mode
    run_mainwindow(
        analyzer,
        # mode='desktop', # 
        mode='web', # 
        with_traces=True,
    )


def example3():
    # curation mode
    run_mainwindow(
        analyzer,
        curation=True
    )



if __name__ == '__main__':
    example1()
    # example2()
    # example3()

    