# Image Scaler API

## Overview

Image Scaler API is a FastAPI-based service that allows users to reduce the resolution of uploaded images by a given scale factor. This service is useful for applications that require image resizing, such as web applications, mobile apps, and more.

## Features

- Upload an image and reduce its resolution by a specified scale factor.
- Supports various image formats.
- Returns the resized image as a response.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Pillow
- Python-Multipart

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/YOUR-USERNAME/Image_Scaler_API.git
   cd Image_Scaler_API
   ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application
1. Start the FastAPI 

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

2. The API will be available at http://localhost:8000.

## API Endpoints
### Reduce Image Resolution
* **URL**: /reduce-resolution/
* **Method**: POST
* **Parameters**:
* **file**: The image file to be uploaded.
* **scale_factor**: The factor by which to reduce the image resolution.
* **Response**: The resized image.
* Example Request
    ```bash
    curl -X POST "http://localhost:8000/reduce-resolution/" -F "file=@path/to/your/image.jpg" -F "scale_factor=2"
    ```
## Docker
To run the application using Docker:

1. Build the Docker image:
    ```bash
    docker build -t image_scaler_api .
    ```
2. Run the Docker container:
    ```bash
    docker run -p 8000:8000 image_scaler_api
    ```
## License
This project is licensed under the MIT License. See the LICENSE file for details.

