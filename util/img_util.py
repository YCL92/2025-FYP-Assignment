import random, os
import cv2


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
    def __init__(self, directory, shuffle=False, transform=None):
        self.directory = directory
        self.shuffle = shuffle
        self.transform = transform

        # get a sorted list of all files in the directory
        # fill in with your own code below
        # list files in directory 
        self.file_list = sorted(next(os.walk(self.directory), (None, None, []))[2])
        #print(self.file_list)

        if len(self.file_list) == 0:
            raise ValueError("No image files found in the directory.")

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
        for fn in self.file_list:
            try:
                file_path = os.path.join(self.directory, fn)
                img = cv2.imread(file_path)

                # convert to grayscale
                img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # save image with `gs_` prefix
                new_path = self.directory + "/gs/" + fn
                res = cv2.imwrite(new_path, img_gray)
                if not res:
                    print(f"Failed to save image {fn} to {new_path}")

            except Exception as e:
                print(f"Error saving the image: {e}")
                continue
            
