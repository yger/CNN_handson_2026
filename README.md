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
git clone https://github.com/samuelgarcia/school_neuralnet_paris_2026.git
cd school_neuralnet_paris_2026
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



# Overview of Bonus datasets for sorting

If you do not have your own dataset for spike sorting you should download theses datasets.
Please do not try to download then during the workshop.

The download links:
 * In vivo : https://filesender.renater.fr/?s=download&token=c22f3a9c-d8e8-48e7-814a-a9adcf33cafa
 * In vitro : https://filesender.renater.fr/?s=download&token=ecb68904-4454-4fa2-8c29-2f7834b249a8


**Please do think about unzipping the data prior to the school!**

## In vivo

### M25_D23_2024-11-11_13-11-10_OF1

Neuropixels 2.0 dataset (384 channels) acquired with the Open Ephys GUI in binary format.
You can use the `spikeinterface.extractor.read_openephys()` function to read the data.

### 1544_2023-04-21_09-55-34_of

Recording with 16 channels organized in 4 tetrodes acquired with the Open Ephys GUI in "openephys" format.
You can use the `spikeinterface.extractor.read_openephys()` function to read the data.

## In vitro

### human_ngn2_100K_c_55D.brw

Human glutamatergic neurons induced via ngn2 method. Plated 100k on CorePlate 1W38/60 3Brain, recorded after 55 days in 
culture with 3Brain BioCAM system. 
You can use the `spikeinterface.extractor.read_biocam()` function to read the data. 

> [!IMPORTANT]  
> The 3Brain BioCAM system saves the data in unsigned integers. You should convert it to signed integers for a smooth
> processing. See documentation [here](https://spikeinterface.readthedocs.io/en/latest/how_to/unsigned_to_signed.html). Note that the `bit_depth` for this system is 12!



