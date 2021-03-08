from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf
import os
from pathlib import Path
import cv2
from faced import FaceDetector
from faced.utils import annotate_image
import time
import base64
 
def home(request):
    return render(request, 'face.html')

def test(request):
    # 获取 上传的 图片信息
    img = request.FILES.get('img')
    # 获取上传图片的名称
    img_name = img.name

    # 获取后缀
    ext = os.path.splitext(img_name)[1]
    # 加时间防止重名
    now = time.time()
    # 重新规定图片名称，图片类型
    img_name = f'imgs{now}{ext}'
    # 图片保存路径
    # img_path = os.path.join(settings.IMG_ROOT, img_name)
    BASE_DIR = Path(__file__).resolve().parent.parent
    img_path = os.path.join(os.path.join(BASE_DIR, "imgs/input"), img_name)

    # 写入 上传图片的 内容
    with open(img_path, 'ab') as fp:
        # 如果上传的图片非常大， 那么通过 img对象的 chunks() 方法 分割成多个片段来上传
        for chunk in img.chunks():
            fp.write(chunk)
    face_detector = FaceDetector()
    print(img_path)
    img = cv2.imread(img_path)
    rgb_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
    bboxes = face_detector.predict(rgb_img, 0.8)
    ann_img = annotate_image(img, bboxes)
    cv2.imwrite('C:/Users/Administrator/Desktop/HelloWorld/static/test1.png', ann_img)
    return render(request, 'face.html')
