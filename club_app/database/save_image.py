import os
from posixpath import abspath

def save_image(image, club_name):
    _, img_ext = os.path.splitext(image.filename)
    if img_ext is not ".jpg":
        img_ext = ".jpg" 
    img_filename = club_name + img_ext
    image_path = os.path.join(abspath('club_app/static/images/club_logo'), img_filename)
    image.save(image_path)
