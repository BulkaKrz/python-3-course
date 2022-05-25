import requests


def isWebPageExsist(WebPage):
    try:
        response = requests.get(WebPage)
        if response.status_code == 200: 
            return True
        else: 
            return False
    except:
        return False
   
def isWebsiteOkPrintTofile(WebPage):
    if isWebPageExsist(WebPage):
        with open("strony_ok.txt", "a+", encoding="UTF-8") as file:
                    file.write(WebPage)
                    file.write(" \t - \t OK \n")
    else:
        with open("strony_false.txt", "a+", encoding="UTF-8") as file:
                    file.write(WebPage)
                    file.write(" \t - \t NOT \n")

#isWebsiteOkPrintTofile("http://onet.pl")


with open("czy_strony_ok.txt", "r", encoding="UTF-8") as file:
    file.seek(0)
    for line in file:
        isWebsiteOkPrintTofile(line.replace("\n",""))
