import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def load_image(image_path):
    """Load an image from the given path."""
    return Image.open(image_path)

def generate_caption(image):
    """Generate a caption for the given image using a pre-trained model."""
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption

def main():
    image_path = input("Enter the path to your image: ")
    image = load_image(image_path)
    caption = generate_caption(image)
    print(f"Generated Caption: {caption}")

if __name__ == "__main__":
    main()