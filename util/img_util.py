import random, os
import cv2
import pandas as pd
import string

def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False

class ImageDataLoader:
    def __init__(self, directory: str, group_ID: str, shuffle=False, transform=None):
        self.directory = directory
        self.group_ID = group_ID.upper()
        self.shuffle = shuffle
        self.transform = transform

        # get a sorted list of the img files corresponding with the Group_ID
        if (len(self.group_ID) != 1) or (self.group_ID not in string.ascii_uppercase):
            raise ValueError("Group ID must be a single letter from A to Z") 
          
        all_groups_assignment = pd.read_csv("../data-student.csv")
        group_mask = all_groups_assignment["Group_ID"] == self.group_ID
        self.file_list = sorted(list(all_groups_assignment["File_ID"][group_mask]))

        #exit if file_list is empty
        if not self.file_list:
            raise ValueError(f"No images found for group {self.group_ID} in the CSV file.")

        #check if the images filtered are within the directory provide
        dir_imgs = sorted(next(os.walk(self.directory), (None, None, []))[2])
        if not set(self.file_list).issubset(set(dir_imgs)):
            raise ValueError(f"Some images in group {self.group_ID} are missing in {self.directory}")

        # shuffle file list if required
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of batches
        self.num_batches = len(self.file_list)

    def __len__(self):
        return self.num_batches

    def __iter__(self):
        for f in self.file_list:
            file_path = os.path.join(self.directory, f)
            img_rgb, img_gray = readImageFile(file_path)

            if self.transform: #if transformation function is provided
                img_rgb = self.transform(img_rgb)
                img_gray = self.transform(img_gray)

            yield img_rgb, img_gray

    def save_grayscale_images(self): 
        gs_path = os.path.join(self.directory, "gs")
        os.makedirs(gs_path, exist_ok=True)

        for fn in self.file_list:
            try:
                file_path = os.path.join(self.directory, fn)
                img_bgr = cv2.imread(file_path)

                # convert to grayscale
                img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

                # save image with `gs_` prefix
                new_fn = f"gs_{fn}"
                new_path = os.path.join(gs_path, new_fn)
                res = cv2.imwrite(new_path, img_gray)

                if not res:
                    print(f"Failed to save image {fn} to {new_path}")

            except Exception as e:
                print(f"Error saving the image {fn}: {e}")
                continue
            
