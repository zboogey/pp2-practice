class UpperString:
  def __init__(self):
    self.instring = ""
  def getString(self):
    self.instring = input()
  def printString(self):
    print(self.instring.upper())
upword = UpperString()
upword.getString()
upword.printString()