from PIL import Image

def cut_image(image_path):

    # Open the image file
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Validate image dimensions
    if img_height != 100 or img_width % 100 != 0:
        raise ValueError("Image height must be 100px and width must be a multiple of 100px")

    # Calculate the number of 100x100 images
    num_images = img_width // 100

    # List to store the 100x100 images
    images = []

    # Loop to cut the image into 100x100 pieces
    for i in range(num_images):
        left = i * 100
        right = (i + 1) * 100
        box = (left, 0, right, 100)
        img_cropped = img.crop(box)
        images.append(img_cropped)

        # Save the cropped image
        img_cropped.save(f"emoji_{i+1}.png")

    return images

if __name__ == "__main__":
    image_path = "full.png"
    images = cut_image(image_path)
    print(f"Created {len(images)} images")
