# VocEd — Cytology Segmentation Course

Applied deep learning for cytology image segmentation.
**Goal:** Predict the nucleus-to-cytoplasm (N/C) ratio using convolutional neural networks.

## Labs

| # | Notebook | Open in Colab |
|---|---|---|
| 01 | Exploratory Segmentation | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emilsar/VocEd/blob/main/01_exploratory_segmentation.ipynb) |

## Dataset

`imagedata/X/` — 200 RGB images, shape `(3, 256, 256)`, float32 `[0, 1]`
`imagedata/y/` — 200 segmentation masks, shape `(256, 256)`, labels: `0` background · `1` cytoplasm · `2` nucleus

## Textbook

Course textbook: [cvmath.club](https://cvmath.club/)
