import requests
from PIL import Image
from io import BytesIO
class ExtractFeatures():
    def check_and_download_image(image_url, save_path='downloaded_image.jpg'):
        try:
            # Send HEAD request first (optional)
            head = requests.head(image_url)
            if head.status_code != 200:
                print(f"URL not reachable, status code: {head.status_code}")
                return None

            # Get image content
            response = requests.get(image_url)
            if response.status_code != 200:
                print(f"Failed to download image, status code: {response.status_code}")
                return None

            # Check Content-Type header
            content_type = response.headers.get('Content-Type')
            if not content_type or not content_type.startswith('image'):
                print(f"URL does not point to an image, Content-Type: {content_type}")
                return None

            # Load image with PIL
            image = Image.open(BytesIO(response.content))

            # Save image locally
            image.save(save_path)
            print(f"Image saved to: {save_path}")

            return image

        except Exception as e:
            print(f"Error: {e}")
            return None

    def extract_image_features(image):
        features = {
            "format": image.format,
            "mode": image.mode,
            "size": image.size,  # (width, height)
        }
        return features

