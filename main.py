import arkaan
import TEST
warehouse={}
dictionary = {
	"test":"123",
	"hello":"1234",
	"wth":"541"
	}

while(True):
    int=input("What application do you want to use? warehouse/dictionary/end: ")
    if int == "dictionary":
        arkaan.dictionary()
    if int == "warehouse":
        TEST.warehouse()
    if int == "end":
        print('"THANKYOU"')
        break
