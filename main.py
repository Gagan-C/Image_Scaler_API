from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI()

@app.post("/reduce-resolution/")
async def reduce_resolution(file: UploadFile = File(...), scale_factor: int = Form(...)):
    """
    Endpoint to reduce the resolution of an uploaded image by a given scale factor.
    """
    # Read the uploaded image file
    image_data = await file.read()
    input_image = Image.open(io.BytesIO(image_data))

    # Calculate the new dimensions
    new_width = input_image.width // scale_factor
    new_height = input_image.height // scale_factor

    # Resize the image
    reduced_image = input_image.resize((new_width, new_height), Image.LANCZOS)

    # Save the reduced resolution image to a BytesIO object
    output_image_io = io.BytesIO()
    reduced_image.save(output_image_io, format=input_image.format)
    output_image_io.seek(0)

    return StreamingResponse(output_image_io, media_type=f"image/{input_image.format.lower()}")
