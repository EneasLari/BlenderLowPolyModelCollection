# write-html.py
import os

from bs4 import BeautifulSoup
f = open('helloworld.html','w')
def my_function():
        soup = BeautifulSoup()
        innerhtml=""
        for dirpath,dirnames,files in os.walk('./Assets/CarModelsPack/RenderedImages'):   
           for file_name in files:              
                if(".png" in file_name):
                        message = """<img class="card-img-top modalSource" src="Assets/CarModelsPack/RenderedImages/{}" alt="Card image cap">"""
                        messageformated=message.format(file_name)
                        innerhtml=innerhtml+messageformated
                        
                else:
                        print("MO")
        return innerhtml
def iterate(list):
        for i in list:
            print(i)
            i.replace_with('')
        return "POUTSES"

# Open test.html for reading
with open('imageslinks.html') as html_file:
    soup = BeautifulSoup(html_file.read(), features='html.parser')
    # Go through each 'A' tag and replace text with '-'
    for tag in soup.find_all("div", {"class": "images"}):
    	#print(tag.contents)
    	innher=my_function()
    	iterate(tag.contents)
    	#div = soup.new_tag('div')
    	tag.append(BeautifulSoup(innher, 'html.parser'))
    	#tag.insert(0,div)

    # Store prettified version of modified html
    new_text = soup.prettify()

# Write new contents to test.html
with open('imageslinks.html', mode='w') as new_html_file:
    new_html_file.write(new_text)


f.close()
