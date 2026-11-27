# CNN 2026 Spike Sorting

Material for SpikeInterface Tutorial @ CNN 2026

## Data spike sorting


You will need to download this [folder](https://filesender.renater.fr/?s=download&token=e07dbaac-ecc7-4825-a615-496f2bdcfa45)
Please unzip all in sub folders.

Note that this dataset is originally from [dandiset 000939](https://dandiarchive.org/dandiset/000939/0.260512.1701/files?location=sub-A3702) but in a shorter version (90s). You can eventually download the original nwb file but is not mandatory.


## Installation spike sorting

We recommend that you [install uv](https://docs.astral.sh/uv/getting-started/installation/). This is an unbelievably good new package
management tool for Python.

Open your Terminal app and cd (change directory) to where you like to keep github repos. Then clone this repo, and navigate to the `notebooks` folder of it by entering the following commands into your Terminal:

``` shell
git clone https://github.com/yger/CNN_handson_2026.git
cd CNN_handson_2026
```

Now open jupyter lab (you don't need to install this - uv will take care of it) using uv:

``` shell
uv run jupyter lab
```

Or if you prefer to use vscode:

``` shell
uv run code .
```

If you like traditional virtual environments, please visit [this page](https://github.com/SpikeInterface/spikeinterface/tree/main/installation_tips) to install on your laptop python+spikeinterface.
