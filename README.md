# Decomposing Residential Energy Load Profile
This project decomposes residential energy load profiles into individual appliance-level consumption using NREL's End-Use Load Profiles dataset. Built with a Rust-based modelling engine, it combines a training pipeline with GPU acceleration and an inference API. Data is sourced from NREL's open AWS S3 bucket for Florida residential buildings.

---
## Download the Nrel data

- in order to dowload the data you must install awscli2

`sudo dnf install awscli2`

---

<b>You would rather change dnf based on your distribution<b>

### Checking the current datasets

- To check the available datasets in Nrel type

`aws s3 ls --no-sign-request s3://oedi-data-lake/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025/resstock_amy2018_release_1/timeseries_individual_buildings/by_state/upgrade=28/state=FL/`

---
- wait for the output and select the files that you want to download by either copying their name for the terminal output or by copying them from NREL official site https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2025%2Fresstock_amy2018_release_1%2Ftimeseries_individual_buildings%2Fby_state%2Fupgrade%3D28%2Fstate%3DFL%2F&limit=50 

### Copying the data from aws s3 bucket to your local files 

#### Copying a specific files

`aws s3 cp --no-sign-request s3://oedi-data-lake/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025/resstock_amy2018_release_1/timeseries_individual_buildings/by_state/upgrade=28/state=FL/{the name of the specific file} local_directory_path/local_file` 

---

#### Or optionally you can download the whole directory by typing this command

`mkdir datasets`

`aws s3 cp --no-sign-request s3://oedi-data-lake/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025/resstock_amy2018_release_1/timeseries_individual_buildings/by_state/upgrade=28/state=FL/ datasets/ --recursive` 

---

### Downloading the Metadata for upgrade 28

`aws s3 cp --no-sign-request s3://oedi-data-lake/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2025/resstock_amy2018_release_1/metadata_and_annual_results/by_state/full/parquet/state=FL/FL_upgrade28.parquet input/MetaData.parquet
`

---

Copyright (c) 2026 Ahmed Alyafai. All Rights Reserved.
