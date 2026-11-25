import json
import warnings
from pathlib import Path

import spikeinterface.full as si


# change this path to point to the folder your data is in
# base_folder = Path("/home/samuel/Documents/DataSpikeSorting/school_neuralnet_2026/")
base_folder = Path("/mnt/data/sam/DataSpikeSorting/school_neuralnet_2026/")
# base_folder = Path("/home/pierre/school_neuralnet_2026/")

data_folder = base_folder / "data"
name = "sub-A3702_ses-191126-3600s"
result_folder = base_folder / "results" / name
result_folder.mkdir(exist_ok=True)

sorter_name = "lupin"
# sorter_name = "kilosort4"
# sorter_name = "dartsort"

analyzer_folder = result_folder / f"analyzer_{sorter_name}_with_labels"
analyzer = si.load(analyzer_folder)
print(analyzer)


# find some potential merges

potential_merges = si.compute_merge_unit_groups(
    analyzer,
    preset="slay",
    steps_params={"template_similarity": {"template_diff_thresh": 0.5}}
)

print(potential_merges)



# we will use unitrefine labels as pre-computed "quality"
unitrefine_labels = analyzer.get_sorting_property("unitrefine_label").copy()
unitrefine_labels[unitrefine_labels == "sua"] = "good"
unitrefine_labels[unitrefine_labels == "mua"] = "MUA"

label_definitions = {
    "quality": dict(name="quality", label_options=["good", "MUA", "noise"], exclusive=True),
}
manual_labels = [
    {"unit_id": unit_id, "labels": {"quality": [unitrefine_labels[unit_index]]}}
    for unit_index, unit_id in enumerate(analyzer.unit_ids)
]

curation_dict = dict(
    format_version="2",
    unit_ids=analyzer.unit_ids,
    label_definitions=label_definitions, 
    merges=[{"unit_ids": p} for p in potential_merges],
    removed=analyzer.unit_ids[unitrefine_labels == "noise"],
    manual_labels=manual_labels
)

si.validate_curation_dict(curation_dict)
print(curation_dict)

from spikeinterface_gui import run_mainwindow

run_mainwindow(
    analyzer,
    displayed_unit_properties=["threshold_label", "unitrefine_label", "bombcell_label"],
    curation=True,
    curation_dict=curation_dict,
    mode="desktop"
)
