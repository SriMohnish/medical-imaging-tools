import numpy as np
import matplotlib.pyplot as plt
raw_dicom = {"PatientName" : " Mohnish ", "Age" : 23 , "PatientID": "007", "PixelData": np.zeros((5, 5))}
raw_dicom["PixelData"][2, 2] = 255
print(raw_dicom)
def anonymize_data(dicom_in):
    dicom_out = dicom_in.copy()
    dicom_out["PatientName"] = "Anonymous"
    dicom_out["PatientID"] = "HASH - 001"
    return dicom_out

clean_dicom = anonymize_data(raw_dicom)

fig , ax = plt.subplots(1,2)

ax[0].imshow(raw_dicom["PixelData"], cmap = "gray")
ax[0].set_title(raw_dicom["PatientName"])

ax[1].imshow(clean_dicom["PixelData"], cmap = "gray")
ax[1].set_title(clean_dicom["PatientName"])

plt.show()