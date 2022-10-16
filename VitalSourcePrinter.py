
'''
This script is designed to legally and automatically print your purchased e-books from VitalSource.com

See ReadMe at https://github.com/LifeAlgorithm/VitalSourcePrinter and/or watch tutorial video for instructions
'''

try:   
    import PyPDF2
    import pyautogui
    import os
    import sys
    import time
    import warnings
    from tkinter import *
    import tkinter.filedialog as filedialog
except:
    print("Please install PyPDF2 and pyautogui. Refer to video or documentation for help")
    sys.exit()

pyautogui.PAUSE=0.5

def main():

    start_time = time.time() 
    warnings.filterwarnings("ignore") #Gets rid of harmless warnings on the console for excess whitespace
    print("Welcome to the VitalSource Ebook Printer. \n")

    while(True):
        try:
            NumberStart = int(input("First page: "))
            NumberEnd = int(input("Last page: "))
            if (type(NumberStart) != int) or (type(NumberStart) != int):
                print("Please enter valid numbers.\n")
                continue
            elif (NumberStart > NumberEnd):
                print("First page must be less than last page.\n")
                continue                    
            else:
                break          
        except:
            print("Please enter valid page numbers.\n")

    NumberList = []
    for i in range(int(NumberStart), int(NumberEnd)+1):
        NumberList += [ str(i) ]

    root = Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.deiconify()
    root.lift()
    root.focus_force()
    # credits to http://stackoverflow.com/questions/3375227/how-to-give-tkinter-file-dialog-focus

    filedir = filedialog.askdirectory() + '//'

    if len(NumberList)%2 != 0 :
        NumberList += [ NumberList[-1] ]

    print("\nClick on the active VitalSource window to get started.\nThe program will start in: 4")
    for seconds in range(5):
        time.sleep(1)
        if seconds == 4:
            print("Starting now...\n")
            break
        print(str(5 - (seconds + 1)))

    print("I'm here 1\n")
        
    PageEntry1 = NumberList[0]
    PageEntry2 = NumberList[1]
    
    pyautogui.hotkey('ctrl', 'p')
    pyautogui.press('delete', 4)
    pyautogui.typewrite(PageEntry1)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('delete', 4)
    pyautogui.typewrite(PageEntry2)
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(40)
    pyautogui.press(['tab', 'tab', 'tab', 'tab', 'enter'])
    time.sleep(1)
    pyautogui.typewrite("Ebook")
    pyautogui.press('enter')
    time.sleep(7)
    pyautogui.keyDown('shift')
    pyautogui.press(['tab', 'tab', 'tab'])
    pyautogui.keyUp('shift')
        
    def NumberProcess(start):
        for page in range(start, len(NumberList), 2):
                print("I'm here 2\n")
                pyautogui.hotkey('ctrl', 'p')
                pyautogui.press('left', 4)
                pyautogui.press('delete', 4)
                pyautogui.typewrite(NumberList[page])
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('left', 4)
                pyautogui.press('delete', 4)
                pyautogui.typewrite(NumberList[page + 1])
                time.sleep(1)
                pyautogui.press('tab')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(40)
                pyautogui.press(['tab', 'tab', 'tab', 'tab', 'enter'])
                time.sleep(1)
                pyautogui.typewrite("File2")
                pyautogui.press('enter')
                time.sleep(7)
                pyautogui.keyDown('shift')
                pyautogui.press(['tab', 'tab', 'tab'])
                pyautogui.keyUp('shift')
                
                while (os.path.isfile(filedir + "Ebook.pdf") != True):
                       time.sleep(2)
                while (os.path.isfile(filedir + "File2.pdf") != True):
                       time.sleep(2) 
                try:
                    pdf1File = open(filedir + 'Ebook.pdf', 'rb')
                    pdf2File = open(filedir + 'File2.pdf', 'rb')
                except:
                    while (os.path.isfile(filedir + Ebook.pdf) != True):
                       time.sleep(10)
                    while (os.path.isfile(filedir + File2.pdf) != True):
                       time.sleep(10) 
                try: 
                    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
                except:
                    time.sleep(5)
                    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)

                try:
                    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
                except:
                    time.sleep(5)
                    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
                
                pdfWriter = PyPDF2.PdfFileWriter()   
                for pageNum in range(pdf1Reader.numPages):
                    pageObj = pdf1Reader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                for pageNum in range(pdf2Reader.numPages):
                    pageObj = pdf2Reader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                    
                pdfOutputFile = open(filedir + 'Ebook1.pdf', 'wb')
                pdfWriter.write(pdfOutputFile)
                pdfOutputFile.close()
                pdf1File.close()
                pdf2File.close()
                
                try:
                    os.remove(filedir + 'Ebook.pdf')
                except:
                    time.sleep(10)
                    os.remove(filedir + 'Ebook.pdf')
                    
                try:
                    os.remove(filedir + 'File2.pdf')
                except:
                    time.sleep(10)
                    os.remove(filedir + 'File2.pdf')

                try:
                    os.rename(filedir + 'Ebook1.pdf', filedir + 'Ebook.pdf')
                except:
                    time.sleep(10)
                    os.rename(filedir + 'Ebook1.pdf', filedir + 'Ebook.pdf')
           
                print("Page: " + str(page + 2) + ' of ' + str(len(NumberList) ))

    NumberProcess(2)
        
    elapsed_time = time.time() - start_time
    print("\nDone!")
    print("This took " + "%.2f" % (elapsed_time/3600) + " hours.")

if __name__ == "__main__": main()


''' 
Final note

I hope this script serves you well. A lot of the actual code was written for basic functionality and not neccessarily optimization 
and readability. Suggestions for refactoring and improvement are always appreciated.
'''
