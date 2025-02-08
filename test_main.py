import pytest
from fastapi.testclient import TestClient
from PIL import Image
import io
from main import app

client = TestClient(app)

def create_test_image():
    # Create a simple image for testing
    image = Image.new("RGB", (100, 100), color="red")
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format="JPEG")
    img_byte_arr.seek(0)
    return img_byte_arr

def test_reduce_resolution():
    test_image = create_test_image()
    response = client.post(
        "/reduce-resolution/",
        files={"file": ("test_image.jpg", test_image, "image/jpeg")},
        data={"scale_factor": 2}
    )
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/jpeg"

def test_invalid_scale_factor():
    test_image = create_test_image()
    response = client.post(
        "/reduce-resolution/",
        files={"file": ("test_image.jpg", test_image, "image/jpeg")},
        data={"scale_factor": 0}  # Invalid scale factor
    )
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error"}

def test_no_file_uploaded():
    response = client.post(
        "/reduce-resolution/",
        data={"scale_factor": 2}
    )
    assert response.status_code == 422  # Unprocessable Entity