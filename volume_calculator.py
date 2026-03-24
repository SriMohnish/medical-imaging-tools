import os
import shutil
import pydicom
import numpy as np
from pydicom.data import get_testdata_file

# ==========================================
# Phase 1: Simulate a Hospital Dataset
# (Creating a dummy folder with 10 CT slices)
# ==========================================
scan_folder = "patient_001_scan"
os.makedirs(scan_folder, exist_ok=True)
source_file = get_testdata_file("CT_small.dcm")

print(f"System: Generating mock 3D scan in '{scan_folder}'...")
for i in range(10): 
    shutil.copy(source_file, os.path.join(scan_folder, f"slice_{i:02d}.dcm"))

# ==========================================
# Phase 2: The 3D Processing Engine
# ==========================================
total_3d_bone_voxels = 0
slice_count = 0

print("System: Reading scan volume...")

# Loop through every file in the patient folder
for filename in os.listdir(scan_folder):
    if filename.endswith(".dcm"): # Only process DICOM files
        
        # 1. Load the specific slice
        filepath = os.path.join(scan_folder, filename)
        dataset = pydicom.dcmread(filepath)
        
        # 2. Apply our Clinical Logic (Thresholding > 300 HU)
        image = dataset.pixel_array
        bone_mask = image > 300
        
        # 3. Add this slice's bone pixels to our running total
        total_3d_bone_voxels += np.sum(bone_mask)
        slice_count += 1

# ==========================================
# Phase 3: 3D Math & Quantification
# ==========================================
# We only need to extract the physical spacing data once
pixel_spacing = dataset.PixelSpacing
area_of_one_pixel = pixel_spacing[0] * pixel_spacing[1]
slice_thickness = getattr(dataset, 'SliceThickness', 1.0)

volume_of_one_voxel = area_of_one_pixel * slice_thickness
total_bone_volume_mm3 = total_3d_bone_voxels * volume_of_one_voxel
total_bone_volume_cm3 = total_bone_volume_mm3 / 1000

# ==========================================
# Phase 4: The Final Output
# ==========================================
print("\n--- 3D CLINICAL VOLUMETRIC REPORT ---")
print(f"Total slices processed:   {slice_count}")
print(f"Total bone voxels:        {total_3d_bone_voxels}")
print(f"Total Estimated Volume:   {total_bone_volume_cm3:.2f} cm^3 (mL)")
print("-------------------------------------")