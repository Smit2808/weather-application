from tkinter import *
from PIL import ImageTk,Image #for image or icon
import requests
import json

# for making window 
root = Tk()
root.title("weather app")
root.iconbitmap("icon.ico")

def search():
	api_req = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")
	api = json.loads(api_req.content)
	state = api[0]['StateCode']
	city = api[0]['ReportingArea']
	quality = api[0]['AQI']
	category = api[0]['Category']['Name']

	mylabel = Label(root, text = "State Code: "+state+"\ncity: "+city+"\nquality: "+str(quality)+"\ncategory: "+category) 
	mylabel.grid(row=2,column=0,columnspan=2)


zip = Entry(root,width=20, borderwidth=5)
zip.grid(row=0,column=1,pady=10)
zip_label = Label(root, text="Enter Zipcode: ")
zip_label.grid(row=0,column=0)

zip_btn = Button(root, text="Search", command=search).grid(row=1,column=0,columnspan=2)
root.mainloop()