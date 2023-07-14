import base64
import os
import requests


class Service():

    def __init__(self):
        self.token = os.environ['GOOGLE_VISION_TOKEN']

    def base64(self, path):
        return base64.b64encode(open(path, 'rb').read()).decode()

    def detect_text(self, uri):
        image = {"source": {"image_uri": uri}} if uri.startswith('http') else {"content": uri}
        url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(self.token)
        data = {"requests": [{"image": image, "features": {"type": "TEXT_DETECTION"}}]}
        response = requests.post(url, json=data).json()
        for item in response['responses']:
            if item and 'fullTextAnnotation' in item:
                return item['fullTextAnnotation']['text'].upper()
        return ''

    def detect_labels(self, uri):
        image = {"source": {"image_uri": uri}} if uri.startswith('http') else {"content": uri}
        url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(self.token)
        data = {"requests": [{"image": image, "features": {"type": "LABEL_DETECTION"}}]}
        response = requests.post(url, json=data).json()
        for item in response['responses']:
            if item and 'labelAnnotations' in item:
                return [value['description'].lower() for value in item['labelAnnotations']]
        return []

    def detect_color(self, uri):
        image = {"source": {"image_uri": uri}} if uri.startswith('http') else {"content": uri}
        url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(self.token)
        data = {"requests": [{"image": image, "features": {"type": "IMAGE_PROPERTIES"}}]}
        response = requests.post(url, json=data).json()
        for item in response['responses']:
            if item and 'imagePropertiesAnnotation' in item:
                color = item['imagePropertiesAnnotation']['dominantColors']['colors'][0]['color']
                return tuple(color.values())
        return (0, 0, 0)
