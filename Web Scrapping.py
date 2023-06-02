import os,requests,time,pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Initialize Chrome driver using the Service object
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Set the URL of the web page containing the images
url = "Enter your URL here"

driver.implicitly_wait(30)

# Load the web page
# driver.maximize_window()
driver.get(url)
time.sleep(20)

def download_imgs(i):
    print(f"Landed on page: {i}=============================")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    # Find all image elements using the specified XPath
    image_elements = driver.find_elements("xpath", "//*[@class='thumb-img']")
    
    # Iterate over the image elements and extract the image URLs
    for index, image_element in enumerate(image_elements):
        # Get the source URL of the image
        image_url = image_element.get_attribute("src")

        # Download the image
        response = requests.get(image_url)
        image_data = response.content

        # Extract the image file name
        image_name = f"{i}_{index}.jpg"

        # Create a folder to store the images
        folder_path = f"D:/Projects/Face Detection/Images/{i}/"
        os.makedirs(folder_path, exist_ok=True)

        # Save the image to the specified folder
        image_path = os.path.join(folder_path, image_name)
        with open(image_path, "wb") as f:
            f.write(image_data)
            print(f"Image saved: {image_path}")

def click_next():
    # Locate the button on the screen
    button_location = pyautogui.locateOnScreen('D:/Projects/Web Scraping/button.png',confidence=0.95)
    if button_location is not None:
        # Get the center coordinates of the button
        button_center = pyautogui.center(button_location)
        # Move the mouse to the button and click
        pyautogui.moveTo(button_center.x, button_center.y, duration=1)
        pyautogui.click()
        pyautogui.moveRel(100, 0, duration=0.5)
        # Optional: Add a delay before clicking
        time.sleep(1)  # Add a delay of 1 second (or any desired duration) before clicking
    else:
        print("Button not found on the screen---------------------------------------------------------------------------------------------------------------")

for i in range(67, 76):
    download_imgs(i)
    click_next()
    print("******************************Page: "+str(i)+" images downloaded")