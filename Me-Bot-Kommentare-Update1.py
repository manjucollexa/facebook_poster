
# -*- coding: utf-8 -*-

from time import sleep
import os
import sys
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options






def main():

	# Your Facebook account user and password
	
	usr = []
	txt = open("e-mail-adresse.txt","r+").readlines()
	for line in txt:
		line = line.replace('\n','')
		usr.append(line)	
	pwd = []
	txt = open("passwort.txt","r+").readlines()
	for line in txt:
		line = line.replace('\n','')
		pwd.append(line)	
	message = []
	txt = open("nachricht.txt","r+").readlines()
	for line in txt:
		line = line.replace('\n','')
		message.append(line)
	

	attach_image = False
	image_path = "/C:/Users/Robin Focke/Desktop/test/Snapshot.jpg/"	
	image_pat = []
	txt = open("bild.txt","r+").readlines()
	for line in txt:
		line = line.replace('\n','')
		image_pat.append(line)
	
	group_links = []
	txt = open("Deine-Gruppen.txt","r+").readlines()
	for line in txt:
		line = line.replace('\n','')
		group_links.append(line)
		
		
	kommentar = []
	txt = open("kommentar.txt","r+").readlines()
	for line in txt:
		line = line.replace('\n','')
		kommentar.append(line)		
		
	
	options = Options()
	#options.headless = True
	driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
	
	
	
	



	driver.get('https://die-affiliate-secret-school.de/?tcb_lightbox=mebot-passwort-2')
	passOnline = driver.find_element_by_css_selector("#pass").text
	passOnlineEntered = input("Bitte deinen Lizencode eingeben:\n")
	if passOnline != passOnlineEntered:
		print("Lizenz ist nicht gültig...")
		driver.close()
		exit()	

	
	
	
	
	

	delayMin = int(input("Minimum warten zum Posten in Sekunden\n"))
	delayMax = int(input("Maximal warten zum Posten in Sekunden\n"))

	
	
	# Go to facebook.com
	driver.get("http://www.facebook.com")

	
	# Enter user email
	elem = driver.find_element_by_id("email")
	elem.send_keys(usr)
	# Enter user password
	elem = driver.find_element_by_id("pass")
	elem.send_keys(pwd)
	# Login
	elem.send_keys(Keys.RETURN)
	
	delay = random.randint(9,17)
	print("Delayed",delay,"s ",end="")
	time.sleep(delay)

	for group in group_links:

		# Go to the Facebook Group
		driver.get(group)
		delay = random.randint(9,15)
		print("Delayed",delay,"s ",end="")
		time.sleep(delay)

			# Click the post box
		try:
			post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		except:
			pass
		
		
		
		
			# Enter the text we want to post to Facebook
		try:
			post_box.send_keys(message)
			delay = random.randint(30,42)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)
		except:
			pass			
			
			
		

		
		
		
		
		
		
		try:		
			addMediaButto = driver.find_elements_by_xpath("//*[contains(text(), 'Foto/Video')]")[0]
			addMediaButto.click()
			delay = random.randint(6,10)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)
			
			
		except:
			pass


			
		try:		
			uploadPhotoButto = driver.find_element_by_xpath("//*[@class='_n _5f0v']")
			uploadPhotoButto.send_keys(image_pat)
			delay = random.randint(5,12)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)
		except:
			pass		
		
		
		
		
	
		
		


		

		
		
		
		

		if attach_image:
			# Click on the add media button
			addMediaButton = driver.find_elements_by_xpath("//*[contains(text(), 'Add Photo/Video')]")[0]
			addMediaButton.click()
			sleep(5)

			# Click the 'Upload Photo/Video' button
			uploadPhotoButton = driver.find_element_by_xpath("//*[@data-testid='media-attachment-Fotos-hochladen']")
			uploadPhotoButton.send_keys(image_path)
			
			# Wait for the image to upload
			delay = random.randint(5,12)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)

			# Provide picture file path
			# driver.find_element_by_xpath("//div[text()='Add Photo/Video']/following-sibling::div/input").send_keys(image_path)
		try:
			post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
			clickable = False
			while not clickable:
				cursor = post_button.find_element_by_tag_name('span').value_of_css_property("cursor")
				if cursor == "pointer":
					clickable = True
					break
			post_button.click()
			delay = random.randint(8,19)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)
		except:
			pass			
		
	

		
		
		

		
		driver.get("http://mbasic.facebook.com")
		
		delay = random.randint(9,17)
		print("Delayed",delay,"s ",end="")
		time.sleep(delay)
		
		try:		
			bkk = driver.find_elements_by_xpath("//*[contains(text(), 'Profil')]")[0]
			bkk.click()
			delay = random.randint(5,15)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)		
		except:
			pass
		
		
		try:		
			ak = driver.find_elements_by_xpath("//*[contains(text(), 'Aktivitätenprotokoll')]")[0]
			ak.click()
			delay = random.randint(5,15)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)		
		except:
			pass		

		
		
		try:		
			driver.find_element_by_xpath("//*[@alt='Bild könnte enthalten: Text']").click()
			delay = random.randint(4,11)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)		
		except:
			pass			
		
		
		
		try:			
			driver.find_element_by_id('composerInput').send_keys(kommentar)
			delay = random.randint(4,11)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)		
		except:
			pass			

		
		
		try:		
			driver.find_element_by_xpath("//input[@type='submit' and @value='Kommentieren']").click()
			delay = random.randint(8,16)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)		
		except:
			pass
		

		

		
		driver.get("http://www.facebook.com")
		delay = random.randint(8,19)
		print("Delayed",delay,"s ",end="")
		time.sleep(delay)

		try:
			button=driver.find_element_by_xpath("//*[@class='UFILikeLink _4x9- _4x9_ _48-k']")
			button.click()
			delay = random.randint(10,14)
			print("Delayed",delay,"s ",end="")
			time.sleep(delay)
		except:
			pass		
		

		try:
			button=driver.find_element_by_xpath("//*[@class='UFILikeLink _4x9- _4x9_ _48-k']")
			button.click()
		except:
			pass		
		
		delay = random.randint(delayMin,delayMax)
		print("Delayed",delay,"s ",end="")
		time.sleep(delay)
		
	# driver.close()

if __name__ == '__main__':
  main()
  
  
 
