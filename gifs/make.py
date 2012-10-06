import glob
gifs=glob.glob("*.gif")
htmlFile = open("index.html", "r+").read()
gifList=""

def insert(index, mainstring, insertstring):
    return mainstring[:index] + insertstring + mainstring[index:]

if '<ul id="gif-library">' in htmlFile:
	for index in range(len(gifs)):
		if '<li>' not in htmlFile:
			gifList+="<li>"+gifs[index]+"</li>"
	
	body = insert(htmlFile.find('</ul>'), htmlFile, gifList)
	open("index.html", "r+").write(body)
	open("index.html", "r+").close()
