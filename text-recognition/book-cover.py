from PIL import Image
from pytesseract import image_to_string

#determine 
def getBook(imageURL):
    output = image_to_string(Image.open(imageURL))
    
    #look for key words in the word
    if (output.find("ESL") != -1 or output.find("Spanish") != -1 or output.find("Speakers") != -1):
        return 0
    if (output.find("Computer") != -1 or output.find("Science") != -1):
        return 1
    if (output.find("Building") != -1 or (output.find("Beginners") != -1 and output.find("Advanced") == -1)):
        return 2
    if (output.find("Third") != -1 or output.find("Machine") != -1 \
    or output.find("Learning") != -1 or output.find("Block") != -1 \
    or output.find("Quantum") != -1 or output.find("Applications") != -1 \
    or output.find("Advanced") != -1 or output.find("Clustering") != -1 \
    or output.find("Cloud") != -1 or output.find("Integration") != -1 \
    or output.find("Brief") != -1 or output.find("Edition") != -1):
        return 3

    return -1
    
print(getBook('esl4.jpg'))