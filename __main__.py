from util.img_util import ImageDataLoader

# this is just for testing
if __name__ == "__main__":
    idl = ImageDataLoader("./data/img-group-M")
    idl.save_grayscale_images()

