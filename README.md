# SpeciFingers: Finger Identification and Error Correction on Capacitive Touchscreens

This is the official implementation of the [paper](https://dl.acm.org/doi/10.1145/3643559) "SpeciFingers: Finger Identification and Error Correction on Capacitive Touchscreens".

## Set Up Environment

```bash
conda env create -f environment.yml
```

```bash
conda activate specifingers
```

## Download SpeciFingers Dataset

To get started with the SpeciFingers dataset:

1. Download the dataset and locate the `raw_log_data.zip` file at the root of this project.
2. Unzip the dataset:

```bash
unzip raw_log_data.zip
```

## Generating RawFinger Videos

Generate capacitive contact videos from the raw finger data:

```bash
python draw_RawFinger.py
```

## Generating JPG Images

This step requires you to configure ffmpeg.

Convert the dataset images into the JPG format:

```bash
python gen_jpgs.py
```

## Image Interpolation

Perform bilinear interpolation on the images:

```bash
python Inter_fig_Bilinear.py
```

## Arranging Data

Organize the dataset:

```bash
python arrange_data.py
```

## Renaming

Rename the dataset for training:

```bash
python change_name.py
```

## Training the Model

Train the model:

```bash
python model.py
```

## Citation

If you find our work and this repository useful, please consider citing:

```bibtex
@article{huang2024specifingers,
author = {Huang, Zeyuan and Gao, Cangjun and Wang, Haiyan and Deng, Xiaoming and Lai, Yu-Kun and Ma, Cuixia and Qin, Sheng-feng and Liu, Yong-Jin and Wang, Hongan},
title = {SpeciFingers: Finger Identification and Error Correction on Capacitive Touchscreens},
year = {2024},
issue_date = {March 2024},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {8},
number = {1},
url = {https://doi.org/10.1145/3643559},
doi = {10.1145/3643559},
journal = {Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.},
month = {mar},
articleno = {8},
numpages = {28},
keywords = {Capacitive touchscreen, Deep learning, Error correction, Finger identification, Finger-specific interaction}
}
```

## Contact

If you have any questions, please create an issue on this repository or contact at *zeyuan2020@iscas.ac.cn*.
