import urllib, json, cStringIO
from PIL import Image
import io
#import apikey.json
#export GOOGLE_APPLICATION_CREDENTIALS=apikey.json


def load_image_urls(token):
    

    _url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={}'.format(token)

    search_results = urllib.urlopen(_url)

    data = json.load(search_results) # Load Instagram Media Result
    image_urls = []
    #print data
    for row in data['data']:
        if row['type'] == "image": # Filter non images files
            filename = row['id']
            url = row['images']['standard_resolution']['url']
            image_urls.append(url)

    return image_urls

def load_images(image_urls):
    imgs = []
    for URL in image_urls:
        file = cStringIO.StringIO(urllib.urlopen(URL).read())
        imgs.append(Image.open(file))
    return imgs

def to_bytes(images):
    images_bytes = []
    for img in images:

        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format = 'JPEG')

        images_bytes.append(img_byte_arr.getvalue())
#        print(type(img_byte_arr))
        #print(type(img_byte_arr.getvalue()))
    return images_bytes


#    img.convert('RGB').save(output, 'BMP')
def get_image_bytes(token, username = None):
    image_urls = load_image_urls(token)
    images = load_images(image_urls)
    images_bytes = to_bytes(images)
    return (image_urls, images_bytes)
