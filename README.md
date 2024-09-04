# OCR_API

The provided Python code defines a web-based Optical Character Recognition (OCR) API using the Flask framework. Here's a detailed analysis and explanation of what each part of the code does:

### Overview
- **Flask Application**: The code sets up a Flask application to handle HTTP requests for OCR processing.
- **OCR Engines**: It uses two OCR engines: Tesseract (via `pytesseract`) and EasyOCR.
- **Security**: Implements basic API key management for authentication.
- **Image Processing**: Includes functions for preprocessing images to enhance OCR accuracy.
- **Endpoints**: Provides endpoints for OCR processing, batch processing, and API key generation.

### Detailed Explanation

#### Initialization
- **Flask App**: The `app = Flask(__name__)` line initializes a Flask application.
- **OCR Engines**: 
  - Tesseract is set up with a specified path (though the path should be adjusted to match your system).
  - EasyOCR is initialized with English language support.

#### Security Class
- **API Key Management**: 
  - The `Security` class manages API keys. It generates and validates API keys for user authentication.
  - `generate_api_key(user_id)`: Generates a new API key for a given user ID.
  - `validate_api_key(user_id, api_key)`: Validates the provided API key against stored keys.

#### Image Preprocessing
- **Preprocessing Function**: 
  - `preprocess_image(image)`: Converts the image to grayscale, applies Gaussian blur to reduce noise, and enhances contrast using histogram equalization. This preprocessing improves the accuracy of the OCR engines.

#### OCR Processing
- **Recognize Text Function**: 
  - `recognize_text(image, method='tesseract')`: Recognizes text from a preprocessed image using either Tesseract or EasyOCR. It defaults to Tesseract but can switch to EasyOCR if specified.

#### Batch Processing
- **Batch Processing Function**: 
  - `process_batch(image_paths)`: Processes multiple images in a batch. It reads each image, preprocesses it, and recognizes text, storing results in a list.

#### API Endpoints
- **/ocr_process**: 
  - Handles POST requests to perform OCR on a single image. It requires an API key for authentication.
  - The image is read from the request, preprocessed, and text is extracted using the specified OCR method. The recognized text is returned as a JSON response.

- **/generate_api_key**: 
  - Handles POST requests to generate a new API key for a user. It requires a user ID in the request body.

- **/batch_process**: 
  - Handles POST requests to perform OCR on multiple images. It requires an API key and a list of image paths. The endpoint processes each image and returns the results as a JSON response.

#### Running the Application
- **Main Block**: 
  - The `if __name__ == '__main__':` block runs the Flask application in debug mode, allowing it to listen for incoming requests on the default port (5000).

### Considerations
- **Security**: The API uses simple API key authentication, which might need enhancement for production use.
- **Error Handling**: Basic error handling is implemented, but it could be expanded for robustness.
- **Dependencies**: The code relies on several external libraries (`Flask`, `opencv-python`, `pytesseract`, `easyocr`, and `secrets`), which need to be installed and configured properly.



# Instructions
1. Install the required packages: Flask, opencv-python, pytesseract, and easyocr.
2. Ensure Tesseract is installed and properly configured on your system.
3. Run the script, and use tools like Postman to test the API endpoints.
4. Enjoy!
