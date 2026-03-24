import pydicom
import numpy as np
import matplotlib.pyplot as plt
from pydicom.data import get_testdata_file

# 1. Load the image
filename = get_testdata_file("CT_small.dcm") 
dataset = pydicom.dcmread(filename)
image = dataset.pixel_array

# 2. The Engine: Create the Binary Mask
bone_mask = image > 300

# 3. The Overlay Trick: Hide the background (False values)
overlay = np.ma.masked_where(bone_mask == False, bone_mask)

# 4. The Viewbox (Clinical Display)
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Left: Original Image
ax[0].imshow(image, cmap=plt.cm.bone)
ax[0].set_title("Original CT")

# Right: The Clinical Overlay
ax[1].imshow(image, cmap=plt.cm.bone) 
ax[1].imshow(overlay, cmap='autumn', alpha=0.7) 
ax[1].set_title("AI Bone Detection Overlay")

plt.show()

# 5. Quantification: From Pixels to Millimeters
# Count how many pixels are classified as bone (True = 1)
number_of_bone_pixels = np.sum(bone_mask)

pixel_spacing = dataset.PixelSpacing
area_of_one_pixel = pixel_spacing[0] * pixel_spacing[1]

# Calculate total physical area
total_bone_area_mm2 = number_of_bone_pixels * area_of_one_pixel

# Print the final output to the terminal
print("\n--- AUTOMATED CLINICAL REPORT ---")
print(f"Total bone pixels detected: {number_of_bone_pixels}")
print(f"Physical area of one pixel: {area_of_one_pixel:.4f} mm^2")
print(f"Total estimated bone area:  {total_bone_area_mm2:.2f} mm^2")
print("---------------------------------")