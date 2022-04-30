class Sources:
    '''
    Source class to define News Objects
    '''
    def __init__(self,id,name,category,description,url):
        self.id = id
        self.name = name
        self.url = url
        self.category = category
        self.description = description
class Articles:
    '''
    Source class to define News Objects
    '''
    def __init__(self,title,urlToImage,content,author,publishedAt,url):
        self.title = title
        self.urlToImage = urlToImage
        self.content = content
        self.author = author
        self.publishedAt = publishedAt
        self.url = url