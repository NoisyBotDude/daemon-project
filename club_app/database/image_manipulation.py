import os
from posixpath import abspath

def save_image(image, club_name):
    _, img_ext = os.path.splitext(image.filename)
    if img_ext is not ".jpg":
        img_ext = ".jpg" 
    img_filename = club_name + img_ext
    image_path = os.path.join(abspath('club_app/static/images/club_logo'), img_filename)

    if os.path.exists(image_path):
      os.remove(image_path)  
    image.save(image_path)

def delete_image(club_name):
  img_filename = f"{club_name}.jpg"
  image_path = os.path.join(abspath('club_app/static/images/club_logo'), img_filename)
  if os.path.exists(image_path):
    os.remove(image_path)