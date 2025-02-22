import random
import os
import cv2
from skimage import morphology
import numpy as np
from skimage.color import rgb2hsv

def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    
    return img_rgb, img_gray



def saveImageFile(img, file_path):
    try:
        # Ensure the image is in float format for proper scaling
        img = img.astype(np.float32)

        if img.max() <= 1.0:  # If values are in [0,1], scale to [0,255]
            img = (img * 255).astype(np.uint8)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR

        success = cv2.imwrite(file_path, img)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False



def masking(img_gray):
    
    _, mask = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return mask


def gray_scale(img_rgb):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    
    return img_gray


def hsv_img(img_rgb):
    hsv_im = rgb2hsv(img_rgb)

    # Separate the channels
    hsv_im_h = hsv_im[:,:,0] * 179  # Scale H channel to [0, 179]
    hsv_im_s = hsv_im[:,:,1] * 255  # Scale S channel to [0, 255]
    hsv_im_v = hsv_im[:,:,2] * 255  # Scale V channel to [0, 255]

    # Ensure they are uint8 for display
    hsv_im_h = hsv_im_h.astype(np.uint8)
    hsv_im_s = hsv_im_s.astype(np.uint8)
    hsv_im_v = hsv_im_v.astype(np.uint8)

    return hsv_im_h, hsv_im_s, hsv_im_v


def morph(mask):
    struct_el = morphology.disk(5)
    
    mask_closed = morphology.binary_opening(mask, struct_el)
    # Convert boolean mask to uint8 and scale to 0-255
    mask_closed = (mask_closed * 255).astype(np.uint8)  # Convert boolean to 0-255 range

    # Invert colors
    mask_closed = cv2.bitwise_not(mask_closed)

    return mask_closed


class ImageDataLoader:
    def __init__(self, directory, shuffle=False, transform=None):
        self.directory = directory
        self.shuffle = shuffle
        self.transform = transform

        # get a sorted list of all files in the directory
        # fill in with your own code below
        self.file_list = sorted([
        os.path.join(self.directory, f)
        for f in os.listdir(self.directory)
        if f.endswith(".png") and f[4:8] >= "0131" and f[4:8] <= "0230"
        ])


        if not self.file_list:
            raise ValueError("No image files found in the directory.")

        # shuffle file list if required
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of batches
        self.num_batches = len(self.file_list)

    def __len__(self):
        return self.num_batches

    def __iter__(self):
        # fill in with your own code below
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.num_batches:
            
            file_path = self.file_list[self.index]
            
            self.index += 1
            
            return file_path
        else:
            raise StopIteration