from  selenium import webdriver
from instagram_login import Ig
search_id = "wbpictures"

instagram = Ig()
instagram.login()
instagram.find_followers(search_id)
instagram.follow()
