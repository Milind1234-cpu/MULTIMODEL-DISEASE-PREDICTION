import requests

# Test brain tumor prediction with an actual image
image_path = "backend/data/brain-tumor/train/glioma/Tr-gl_1.jpg"

with open(image_path, 'rb') as f:
    files = {'file': ('test.jpg', f, 'image/jpeg')}
    response = requests.post('http://localhost:8000/api/predict/brain-tumor', files=files)
    
print("Status Code:", response.status_code)
print("Response:", response.json())
