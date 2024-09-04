import requests

def test_ocr_process():
    url = "http://127.0.0.1:5000/ocr_process"
    headers = {"api_key": "your_api_key", "user_id": "your_user_id"}
    files = {"image": open("C:/Users/shawn/Downloads/ovr.jpg", "rb")}
    response = requests.post(url, headers=headers, files=files)
    assert response.status_code == 200
    assert "recognized_text" in response.json()

def test_generate_api_key():
    url = "http://127.0.0.1:5000/generate_api_key"
    response = requests.post(url, json={"user_id": "new_user_id"})
    assert response.status_code == 200
    assert "api_key" in response.json()