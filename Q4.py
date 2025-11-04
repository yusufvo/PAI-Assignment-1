class Image:
    def __init__(self, initial_pixels):
        self.pixel = initial_pixels

    def __repr__(self):
        return f"<Image pixels={self.pixel}>"

    def transformation(self, transformationfoo):
        newpixels = transformationfoo(self.pixel)
        self.pixel = newpixels
        print(f"After: {self}")

    def getCopy(self):
        return [[pixel for pixel in row] for row in self.pixel]

def horizontalflip(pixel):
    return [row[::-1] for row in pixel]

def brightness(pixel, brightness):
    return [[pixel + brightness for pixel in row] for row in pixel]

def rotate90(pixel):
    return [list(reversed(row)) for row in zip(*pixel)]

class AugmentationPipeline:
    def __init__(self):
        self.steps = []

    def addstep(self, transformfoo):
        self.steps.append(transformfoo)
        print(f"Added step: {transformfoo.__name__}")

    def imageprocessing(self, originalImage):
        print("\nPipeline in Process...")
        augmentedImagesList = []
        for func in self.steps:
            pixel_data_copy = originalImage.getCopy()
            augmented_data = func(pixel_data_copy)
            new_image = Image(augmented_data)
            augmentedImagesList.append(new_image)
        return augmentedImagesList

if __name__ == "__main__":
    
    orgpixels = [
        [10, 20, 30], [40, 50, 60]
    ]
    
    img = Image(orgpixels)
    print(f"Image Before: {img}")
    
    pip = AugmentationPipeline()
    
    pip.addstep(horizontalflip)
    
    pip.addstep(
        lambda data: brightness(data, 50)
    )
    
    pip.addstep(rotate90)
    
    augmented_list = pip.imageprocessing(img)
    
    print("\nPipeline is completed.")
    for aug_img in augmented_list:
        print(aug_img)
        
    print(f"\noriginal image is remained unchanged: {img}")
