#download images from web
import urllib.request

#
def dl_jpg(url, file_path, file_name = "Untitled"):
    #create full path
    full_path = file_path + file_name + '.jpg'
    #retrives and saves image using provided url 
    urllib.request.urlretrieve(url, full_path)

#ask user for image to save
url = input("Enter image url to download: ")
#ask user to rename file
file_name = input("Enter a file name to save as: ")

dl_jpg(url, "images/", file_name)