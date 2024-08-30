# import required libraries

# full imports go first
import os  # os is a built-in Python library for interacting with the operating system
import requests  # requests is a library for managing requests

# partial imports go below
from bs4 import BeautifulSoup  # add to requirements.txt: beautifulsoup4
from PIL import Image  # add to requirements.txt: pillow

### GETTING ALL IMAGES FROM A PAGE
URL = "https://ninjago.fandom.com/wiki/Ninjago_Wiki"
data = requests.get(URL)
html_text = data.text  # raw text
bs_html = BeautifulSoup(html_text, "html.parser")
# preview the html contents
print(bs_html.prettify())
image_tags = bs_html.find_all('img')
accepted_image_types = ['jpg', 'jpeg', 'png', 'bmp', 'webp', 'svg']
present_file_types = set(str(img_tag.get('src').split('.')[-1]) for img_tag in image_tags)
# what image types can we find on this page? Please note there may be some obsolete data in here
present_file_types
image_tags
# how many tags?
len(image_tags)
# extract the image URLs from the tags
# create an empty list
img_urls = []

for img_tag in image_tags:

    # if the tag has the 'src' property
    if img_tag.get('src'):

        # extract it
        img_src = img_tag.get('src')

        # get the image type (it's the last bit f text sfter the '.')
        img_type = img_src.split('.')[-1]

        # skip further steps in the loop for the current image if not in the accepted types
        if img_type.lower() in accepted_image_types and img_src.startswith('//upload'):
            img_urls.append(f'https:{img_src}')
image_tags[5].get('src')
# how many URLs did we get?
len(img_urls)
# if you preview, quite a lot of them are duplicated
img_urls
# how many unique?
unique_urls = set(img_urls)
len(unique_urls)
# name of the folder where we want to sve the images. CAPITALS suggest it's a constant
IMAGES_DIRECTORY = "scraped_images"

current_dirs = os.listdir()  # this function lists all the contents of the current folder (where the notebook is)
current_dirs
# if the folder where we want to save the images is not already there, create it
if IMAGES_DIRECTORY not in current_dirs:
    os.mkdir(IMAGES_DIRECTORY)  # this directory will be created in the same location where your notebook is
errors = []

requests.adapters.DEFAULT_RETRIES = 10

# the "enumerate" function allows for iteration while also supplying an index for each item
for img_index, img_url in enumerate(unique_urls):

    # get the data from the image url
    resp = requests.get(img_url, stream=True)

    # if the request is not completed
    if resp.status_code != 200:
        # add the image url to the errors list
        errors.append(img_url)

    # otherwise, proceed
    else:
        # create a PIL.Image object
        obj_img = Image.open(resp.raw)
        # get the file extension from the url
        img_type = img_url.split('.')[-1]
        # save the image in its origial extension
        obj_img.save(f'./{IMAGES_DIRECTORY}/img_{img_index}.{img_type}')
# how many errors?
len(errors)
# let's see what's happened here!
errors[0]
resp = requests.get(errors[0], stream=True)
resp.status_code  # 403 is the status code for "Permission denied"
