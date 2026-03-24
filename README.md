# Clinical DICOM Processing Pipeline

## Project Overview
A Python-based toolkit designed for the automated preprocessing, anonymization, and diagnostic analysis of medical imaging data (DICOM standards). This project bridges the gap between raw radiological data and actionable clinical metrics.

## Core Modules

### 1. Data De-identification (`anonymizer.py`)
* Automatically parses DICOM headers to scrub Protected Health Information (PHI).
* Uses memory-safe shallow copying to preserve clinical pixel arrays while overwriting sensitive tags (PatientName, PatientID).
* Validated with Matplotlib to ensure diagnostic image quality remains intact post-processing.

### 2. Automated 3D Volumetric Segmentation (`volume_calculator.py`)
* Ingests directories of raw CT slices and stacks them into 3D NumPy arrays.
* Implements clinical logic via Hounsfield Unit (HU) thresholding to autonomously segment high-density anatomical structures (e.g., bone).
* Extracts physical spatial metadata (`PixelSpacing`, `SliceThickness`) to convert digital voxel counts into real-world physical volumes ($cm^3$ / mL).

## Tech Stack
* **Python 3.x**
* **pydicom:** For parsing and manipulating complex clinical metadata.
* **NumPy:** For high-performance matrix operations and boolean mask generation.
* **SciPy:** For applying n-dimensional image filters (Noise Reduction).
* **Matplotlib:** For overlaying segmentation masks onto raw clinical data.