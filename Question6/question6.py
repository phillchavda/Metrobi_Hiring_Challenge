
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
import cv2

website1 = "https://metrobi.com"
website2 = "https://metrobi.com/wp-content/uploads/2020/05/cropped-logo-allblack-small.png"
website3 = "https://deliver.metrobi.com/signin"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 

driver.get(website1)
time.sleep(1)
driver.save_screenshot('ss_metrobi.png')


driver.get(website2)
time.sleep(1)
driver.save_screenshot('ss_metrobi_logo.png')

driver.get(website3)
time.sleep(1)
driver.save_screenshot('ss_metrobi_signin.png')
driver.quit()

pc_dim = (1920, 1080) #width, hight
iphone_dim = (640, 1136) 

logo_dim_signin_pc = (1200,200) #good 
logo_dim_signin_iphone = (380, 180) #not good-> to much width

logo_dim_site_pc = (255,60)#bad-> too big
logo_dim_site_iphone = (93,45)#terrible -> finding huge logo


#import metrobi screenshots as greyscale
ss_signin = cv2.imread('ss_metrobi_signin.png')
ss_site =  cv2.imread('ss_metrobi.png') 

#resize screenshots for desktop and iphone dimaentions
ss_signin_pc = cv2.resize(ss_signin, pc_dim)
ss_signin_iphone = cv2.resize(ss_signin, iphone_dim)
ss_site_pc = cv2.resize(ss_site, pc_dim) 
ss_site_iphone = cv2.resize(ss_site, iphone_dim)

#import and crop logo screenshot
ss_logo = cv2.imread('ss_metrobi_logo.png')
ss_logo = ss_logo[375:500,200:700] #crop hight, width

#resize logo for each case to make it easier to use for detection
ss_logo_site_pc = cv2.resize(ss_logo, logo_dim_site_pc) 
ss_logo_site_iphone = cv2.resize(ss_logo,logo_dim_site_iphone)
ss_logo_signin_pc = cv2.resize(ss_logo, logo_dim_signin_pc)
ss_logo_signin_iphone = cv2.resize(ss_logo, logo_dim_signin_iphone)

#list of object detection methods tested
# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#             cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED] 
methods = [cv2.TM_CCOEFF]

############## FOR SIGNIN PAGE - DESKTOP RES ##################################

for method in methods: #so we can check which method will be the best
    ss_signin_pc2 = ss_signin_pc.copy() #so we wont pollute our main image with a bunch of rectangles
    result = cv2.matchTemplate(ss_signin_pc2, ss_logo_signin_pc, method) #will convolute through the image array to find the best match
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: #these methods store the matching area in min_loc, the others will indicate matching points at max_loc
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + logo_dim_signin_pc[0], location[1] + logo_dim_signin_pc[1])
    cv2.rectangle(ss_signin_pc2, location, bottom_right, 255, 5)
    print("Signin page logo has top left coordinates (%d, %d) and bottom right coordinates (%d, %d) on desktop " %(location[0],location[1], bottom_right[0], bottom_right[1])) 
    cv2.imshow('Match', ss_signin_pc2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print("\n\n")

############## FOR SIGNIN PAGE - IPHONE RES ##################################

for method in methods:
    ss_signin_iphone2 = ss_signin_iphone.copy() 
    result = cv2.matchTemplate(ss_signin_iphone2, ss_logo_signin_iphone, method) 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: 
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + logo_dim_signin_iphone[0], location[1] + logo_dim_signin_iphone[1])
    cv2.rectangle(ss_signin_iphone2, location, bottom_right, 255, 5)
    print("Signin page logo has top left coordinates (%d, %d) and bottom right coordinates (%d, %d) on iphone " %(location[0],location[1], bottom_right[0], bottom_right[1])) 
    cv2.imshow('Match', ss_signin_iphone2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print("\n\n")

############## FOR MAIN PAGE - DESKTOP RES ##################################

for method in methods: 
    ss_site_pc2 = ss_site_pc.copy()
    result = cv2.matchTemplate(ss_site_pc2, ss_logo_site_pc, method) 
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + logo_dim_site_pc[0], location[1] + logo_dim_site_pc[1])
    cv2.rectangle(ss_site_pc2, location, bottom_right, 255, 5)
    print("Main page logo has top left coordinates (%d, %d) and bottom right coordinates (%d, %d) on desktop " %(location[0],location[1], bottom_right[0], bottom_right[1])) 
    cv2.imshow('Match', ss_site_pc2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print("\n\n")

############## FOR MAIN PAGE - IPHONE RES ##################################

for method in methods: 
    ss_site_iphone2 = ss_site_iphone.copy() 
    result = cv2.matchTemplate(ss_site_iphone2, ss_logo_site_iphone, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + logo_dim_site_iphone[0], location[1] + logo_dim_site_iphone[1])
    cv2.rectangle(ss_site_iphone2, location, bottom_right, 255, 5)
    print("Main page logo has top left coordinates (%d, %d) and bottom right coordinates (%d, %d) on iphone " %(location[0],location[1], bottom_right[0], bottom_right[1])) 
    cv2.imshow('Match', ss_site_iphone2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
print("\n\n")