from os.path import join, abspath
import os
import cv2
from util.img_util import readImageFile, saveImageFile, ImageDataLoader
from util.inpaint_util import removeHair
from util.img_util import morph
from util.img_util import masking
from util.img_util import gray_scale
from util.img_util import hsv_img


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data")

image_loader = ImageDataLoader(directory=file_path)

for img_path in image_loader:
    
    try:
        # read an image file
        img_rgb, img_gray = readImageFile(img_path)
    except StopIteration:
        break

    # apply hair removal
    blackhat, thresh, img_out = removeHair(img_rgb, img_gray, kernel_size=5, threshold=10)
    
    # apply morphological operations
    img_gray = gray_scale(img_out)
    hsv_im_h, hsv_im_s, hsv_im_v = hsv_img(img_out)

    mask = masking(img_gray)
    mask_v = masking(hsv_im_v)
    mask_s= masking(hsv_im_s)
    mask_h = masking(hsv_im_h)
    
    mask_closed = morph(mask)
    mask_closed_h = morph(mask_h)
    mask_closed_s = morph(mask_s)
    mask_closed_v = morph(mask_v)
    
    mask_closed_s = cv2.bitwise_not(mask_closed_s)
    

    """# plot the images
    plt.figure(figsize=(15, 10))

    # original image
    plt.subplot(2, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")

    # blackHat image
    plt.subplot(2, 2, 2)
    plt.imshow(blackhat, cmap="gray")
    plt.title("BlackHat Image")
    plt.axis("off")

    # thresholded mask
    plt.subplot(2, 2, 3)
    plt.imshow(thresh, cmap="gray")
    plt.title("Thresholded Mask")
    plt.axis("off")

    # inpainted image
    plt.subplot(2, 2, 4)
    plt.imshow(img_out)
    plt.title("Inpainted Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()"""


     # create a unique folder for each image
    folder_name = os.path.splitext(os.path.basename(img_path))[0]  # Use the image name as folder name
    folder_path = os.path.join(script_dir, "result/imgs", folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Save the original and processed images
    saveImageFile(img_out, os.path.join(folder_path, f"{folder_name}_original.png"))
    saveImageFile(mask_closed, os.path.join(folder_path, f"{folder_name}_mask.png"))
    saveImageFile(mask_closed_h, os.path.join(folder_path, f"{folder_name}_mask_h.png"))
    saveImageFile(mask_closed_s, os.path.join(folder_path, f"{folder_name}_mask_s.png"))
    saveImageFile(mask_closed_v, os.path.join(folder_path, f"{folder_name}_mask_v.png"))
    
     except Exception as e:
        # If any error occurs during the processing of the image, print the error message
        # and continue to the next image without stopping the program
        print(f"Error processing the image {img_path}: {e}")
        continue  # Continue with the next image
