from bs4 import BeautifulSoup
# import lxml (consider using this if you get parser error. Change to lxml.parser)

with open("website.html", mode="r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title)           # <title>Angela's Personal Site</title>
print(soup.title.name)      # title
print(soup.title.string)    # Angela's Personal Site

# Ex) find all tags, in this case anchor tags.
# Can change to any tag (h1, p, hr, etc)
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# What if you only wanted text in tag?
for tag in all_anchor_tags:
    print(tag.getText())

# can also get a hold of class
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)  # <h3 class="heading">Books and Teaching</h3>

# Search for tag inside another tag (ex. anchor in paragraph)
company_url = soup.select_one(selector="p a")
print(company_url)  # <a href="https://www.appbrewery.co/">The App Brewery</a>

# Get a hold of ID using "#" sign
name = soup.select_one(selector="#name")
print(name)     # <h1 id="name">Angela Yu</h1>

# What if you only wanted links?
for tag in all_anchor_tags:
    print(tag.get("href"))

# can also get a hold of attribute names
heading = soup.find(name="h1", id="name")
print(heading)      # <h1 id="name">Angela Yu</h1>
