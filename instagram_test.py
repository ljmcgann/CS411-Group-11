import urllib, json, cStringIO
from PIL import Image
import io

def load_image_urls(username = None):
    TOKEN = '29991352.6f30ec7.28527c140f7c402396453b31b7ee2230'

    _url = 'https://api.instagram.com/v1/users/self/media/recent/?access_token={}'.format(TOKEN)

    search_results = urllib.urlopen(_url)

    data = json.load(search_results) # Load Instagram Media Result
    image_urls = []
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
        print(type(img_byte_arr.getvalue()))
    return images_bytes


#    img.convert('RGB').save(output, 'BMP')
def get_image_bytes(username = None):
    image_urls = load_image_urls()
    images = load_images(image_urls)
    images_bytes = to_bytes(images)
    return images_bytes

get_image_bytes()
