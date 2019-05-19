#pip install baidu-aip 安装百度ai图像识别包
from aip import AipImageClassify

APP_ID = '16287884'
API_KEY = 'uxKIW9gZFMtUPi98kirXi5iG'
SECRET_KEY = 'ex48MutfECrmDyoGgBWGO5ef7YEwo8qD'

ObjectRecognition_client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

def get_info_from_image(image_path):
    # rb read bite
    with open(image_path, 'rb') as file:
        image = file.read()
        response = ObjectRecognition_client.advancedGeneral(image)
        print(response)

        if response.get('result'):
            result_data = response['result'][0]
            return result_data