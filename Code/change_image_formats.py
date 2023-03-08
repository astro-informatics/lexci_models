import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


infile = '../Data/TNG50-1_halpha.npy'
outfile = '../Data/TNG50.tiff'

# Load .npy binary file
data = np.load(infile)
plt.imshow(data)

# Convert to Pillow Image and save as TIFF
image_object = Image.fromarray(data*255).convert('RGB')
image_object.save(outfile)
