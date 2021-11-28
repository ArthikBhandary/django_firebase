import os.path
from uuid import uuid4


def video_upload_dir(instance, filename):
    upload_to = "videos"
    ext = filename.split('.')[-1]
    filename = '{}-video-{}.{}'.format(instance.user.pk, uuid4(), ext)
    return os.path.join(upload_to, filename)