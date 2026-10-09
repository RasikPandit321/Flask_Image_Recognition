"""Tests for image preprocessing."""

from io import BytesIO
from PIL import Image
from model import preprocess_img


def test_image_preprocessing():
    """Verify that preprocessing resizes and normalizes an image."""

    image = Image.new("RGB", (400, 400), color="white")

    image_file = BytesIO()
    image.save(image_file, format="JPEG")
    image_file.seek(0)

    processed_image = preprocess_img(image_file)

    assert processed_image.shape == (1, 224, 224, 3)
    assert processed_image.min() >= 0.0
    assert processed_image.max() <= 1.0
