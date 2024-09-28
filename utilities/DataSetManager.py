import utilities.getClasses as getClasses
import random
import os

class DataSetManager:
    def __init__(self):
        self.imagesPath = "imgs/"
        self.jsonPath = "imgs\dataSet.json"
    
    '''
    get the entire dataset in a form of a list of image paths
    '''
    def getAllImages(self):
        # get all the images from the imgs folder
        classes = getClasses.getClasses()
        images = []
        for c in classes:
            pathChosen = self.imagesPath + c + "/"
            images += [pathChosen + i for i in os.listdir(pathChosen)]
        
        for i,path in enumerate(images):
            # check if in path is contained .DS_Store
            if ".DS_Store" in path:
                images.pop(i)
        
        return images
    
    '''
    given the path of the image, return the correct prediction of the image that ambrogio should return
    '''
    def getCorrentPredictionOfImage(self,imagePath):
        # get the correct prediction of the image
        classes = getClasses.getClasses()
        for c in classes:
            if c in imagePath:
                index = imagePath.index(c)
                toRet = [0 for x in range(len(classes))]
                toRet[classes.index(c)] = 1
                return toRet
        return None
    
    '''
    get a random image path of the dataset
    '''
    def getRandomImage(self):
        # go in the imgs folder and get a random image from a random class
        classes = getClasses.getClasses()
        randomClass = random.choice(classes)
        pathChosen = self.imagesPath + randomClass + "/"
        images = os.listdir(pathChosen)
        
        return pathChosen + random.choice(images)        
    
    '''
    The data will be a tuple
    return 0 => the training set, 1 => the convalidation set and 2 => the test set
    '''
    def partitionDataSet(self):
        # partition the data set into training and test set
        images = self.getAllImages()
        random.shuffle(images)
        trainingSet = images[:int(len(images)*0.3)]
        convalidationSet = images[int(len(images)*0.3):int(len(images)*0.6)]
        testSet = images[int(len(images)*0.6):]
        
        
        return trainingSet,convalidationSet, testSet
    
        