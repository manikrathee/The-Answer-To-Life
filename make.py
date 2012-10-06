import glob
gifs=glob.glob("gifs/*.gif")
htmlFile = open("index.html", "r+").read()
gifList=""

def insert(index, mainstring, insertstring):
    return mainstring[:index] + insertstring + mainstring[index:]

if '<ul id="gif-library" class="unstyled">' in htmlFile:
	for index in range(len(gifs)):
		if '<li>' not in htmlFile:
			gifList+="<li class='span-1'><img src='gifs/"+gifs[index]+"' alt='"+gifs[index]+"' /></li>"
	
	body = insert(htmlFile.find('</ul>'), htmlFile, gifList)
	open("index.html", "r+").write(body)
	open("index.html", "r+").close()
