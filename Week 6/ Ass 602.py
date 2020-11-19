


from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
response = urlopen("https://business.depaul.edu/Pages/default.aspx")
html = response.read().decode()

class Collector(HTMLParser):
    """Collects hyperlink URL's into a list"""
    
    def __init__(self,url):
        """Initializes Parser, the URL, and a list"""
        
        HTMLParser.__init__(self)
        self.url = url                             # Call upon the neccessary lines that are  
        self.links = []                            # required after using init 
        self.wordslst = []
        
    def Handle_StartTag(self, tag, attrs):
        '''Collects hyperlink URL's in their absolute format'''
        
        if tag == 'a':                             # Checks for tag a which points to a hyperlink
            for attr in attrs:                     # Search for href attribute 
                if attr[0] == 'href':
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:90] == 'https://business.depaul.edu/Pages/default.aspx': 
                        self.links.append(absolute) # Constructs absolute URL
                                                    # Limits the absolute to only this website itself 
    def handle_data(self, data):
        '''Extended and overrides HTML Parser. Ends up Collecting and concatenating text data'''
        
        words = data.split()
        for word in words:                        # Iterates through the all the phrases and omits 
            if word.isalpha() == True:            # anything with numbers 
                self.wordslst.append(word.lower())
            

    
    def getLinks(self):
        """Get List of Links"""
                                                  # Returns links to be used 
        return self.links

    def getdata(self):
        """Get List of word"""                    # Returns wordslst to be used 

        return self.wordslst
    
    
    
def analyze(url):
    """Analyze Function Calling Class Collector Extended from HTML Parser"""

    print('\n Visiting',url)                    # Prints the website the code will be visiting 

    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)                     # Get list of links 
    urls = collector.getLinks()

    wordslst = collector.getdata()              # Obtains data and uses "collecter" from previously to pull from
    print('\n The 25 most common words \n')
    
     
    from collections import Counter             # Importing counter to count all the words 

    counts = Counter(wordslst)                  # Assign the list that is created to counter 
    Only_25 = counts.most_common(25)            # Takes the list of counts, and caps it to a max of 25
                                                # by using most_common and assigns that to Only_25
    for i in Only_25:                           # Iterate through the list of the counts up to 25
        print (i)                               # so that we can print the list in a vertical manner
        
        
visited = set()                                 # Creates empty container of the links it's going to store
def crawl2(url):
    """Recursive web crawler that calls analyze() on every web page"""

    global visited                              # Initiate global variable to be called during function
    if len(visited) >30:                        # Set limit to links visited to be no more than 30 
        return
    visited.add(url)                            # Adds each URL to the list visited 

    links = analyze(url)                        # Calls upon analyze function

    for link in links:
        if link not in visited:
            try:                                # Iterator to keep running through the links and adding 
                crawl2(link)                    # them to visited. If link is not in, add, if not pass 
            except:
                pass

if __name__ == '__main__':
    url = 'https://business.depaul.edu/Pages/default.aspx'

    analyze(url)
    
    
        


# In[ ]:





# In[ ]:




