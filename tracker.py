import requests
import tkinter as tk
import bs4 

#Fuction to send HTML content
def get_request(link):
    r=requests.get(link)
    return r

#Funstion to get data
def get_covid_data():
    link="https://www.worldometers.info/coronavirus/"
    html_data=get_request(link)
    soup=bs4.BeautifulSoup(html_data.text,"html.parser")
    data=soup.find("div",class_="content-inner").find_all("div",id="maincounter-wrap")
    all_data=""
    for item in data:
        text_data=item.find("h1",class_=None).text
        no_of_cases=item.find("div",class_="maincounter-number").text

        all_data= all_data + text_data + " " + no_of_cases + "\n"
    
    return all_data


#To reload the data
def reload_data():
    newdata=get_covid_data()
    mainlabel['text']=newdata

#Fuction too get given country data
def country_data():
    cou=textfield.get()
    url="https://www.worldometers.info/coronavirus/country/"+cou
    html_data=get_request(url)
    soup=bs4.BeautifulSoup(html_data.text,"html.parser")
    data=soup.find("div",class_="content-inner").find_all("div",id="maincounter-wrap")
    all_data=""
    for item in data:
        text_data=item.find("h1",class_=None).text
        no_of_cases=item.find("div",class_="maincounter-number").text

        all_data= all_data + text_data + " " + no_of_cases + "\n"
    
    mainlabel['text']=all_data


#Code for Tkinter
window=tk.Tk()
window.geometry("900x700")
window.title("Covid-Tracker By ISHAN")
f=("Serif",25,"bold")

banner=tk.PhotoImage(file="covid.png")
bannerlabel=tk.Label(window,image=banner)
bannerlabel.pack()

textfield=tk.Entry(window,width=50)
textfield.pack()

mainlabel=tk.Label(window,text=get_covid_data(),font=f)
mainlabel.pack()

getbtn=tk.Button(window,text="GET DATA",font=f,relief="solid",command=country_data)
getbtn.pack()

rebtn=tk.Button(window,text="RELOAD",font=f,relief="solid",command=reload_data)
rebtn.pack()

window.mainloop()