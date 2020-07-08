import random
import string
import  time
import  traceback
import logging


class Util(object):

    def sleep(self,sec,info=""):
        if info is not None:
            self.log.info("wwait::"+str(sec))
        try:
            time.sleep(sec)
        except:
            traceback.print_stack()

    def getAlphaNumeric(self,length,type='letters'):

        alpha_num =" "
        if type == "lower":
            case = string.ascii_lowercase
        elif type == "upper":
            case = string.ascii_uppercase
        elif type == "digits":
            case = string.digits
        elif type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))



    def getuniqueName(self,charcount=10):
        return self.getAlphaNumeric(charcount,"lower")

    def getUniqueNamelist(self,listsize=5,itemlength=None):
        nameList =[]
        for i in range(0,listsize):
            nameList.append(self.getuniqueName(itemlength[i]))
        return nameList


    def verifytextContains(self,actualText,ExpectedText):
            self.log.info(actualText)
            self.log.info(ExpectedText)
            if ExpectedText.lower() in actualText.lower():
                self.log.info("verification contains")
                return  True
            else:
                self.log.info("verification do3es not contains")
                return Falsea
