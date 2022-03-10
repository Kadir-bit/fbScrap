import time
import selenium
import csv
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox() #lancement de firefox pour la recherche des données et la connexion au faux compte
driver.get('https://www.facebook.com')
time.sleep(2)
email = driver.find_element(By.NAME, "email") 
pswrd = driver.find_element(By.NAME,"pass")
email.send_keys("progkatest99@gmail.com") #information pour le faux compte
pswrd.send_keys("test0123456789")
time.sleep(3)
email.submit()
time.sleep(4)

log = open("log.txt",'w',newline='') # log pour voir les liens qui n'ont pas pu être traité

file = open("Liens FB pour exercice Python 01.txt","r") 

with open("table.csv",'w',newline='', encoding="utf-8-sig") as fichier :
	writer = csv.writer(fichier)
	writer.writerow(['url du profil','prénom','nom','entreprise','url Photo','résidence'])


	for x in file : #lecture du fichier ligne par ligne et récupération des données disponible et ecriture du csv
		if "facebook.com" in x :
			try :

				if x.startswith('https://www.facebook.com/profile') :
					driver.get(x + '&sk=about_overview')
				else :
					driver.get(x + '/about_overview')

				url = x[0:len(x)-1]

				name = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/div/h1")
				t = name.text.split()
				prenom =  t[0]
				nom = ""
				for i in t :

					if i != t[0] :
						nom = nom + i 

				profilePic = driver.find_elements(By.TAG_NAME,"image")
				picUrl = profilePic[1].get_attribute('xlink:href')

				try :
					travail = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/span/a[1]/span/span")
					entreprise = travail.text
				except selenium.common.exceptions.NoSuchElementException:
					entreprise = "null"

				try :
					residence = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/span/a/span/span")
					habitat = residence.text
				except selenium.common.exceptions.NoSuchElementException :
					habitat = "null"

				writer.writerow([url,prenom,nom,entreprise,picUrl,habitat])
				time.sleep(1)
			except selenium.common.exceptions.NoSuchElementException :
				log.write("traitement impossible :" + x)
		else :
			log.write("traitement impossible :" + x)

log.close()
file.close()
