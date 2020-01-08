from Data_layer.Scrapper_image import ScrapperImage
#ScrapperImage is my data layer

class BusinessLayer:
    
    keyword=""
    fileLoc=""
    image_name=""
    header=""
     
    def downloadImages( keyWord, header):
        imgScrapper = ScrapperImage        #Initialising the data layer
        url = imgScrapper.createImageUrl(keyWord)
        rawHtml = imgScrapper.scrap_html_data(url, header) # have all the urls for the searched image
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList,keyWord, header)
        
        return masterListOfImages 