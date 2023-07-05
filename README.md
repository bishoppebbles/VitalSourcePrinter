# VitalSourcePrinter

## Legal Disclaimer: 
Usage of any content produced by this script must abide by the terms set out by [VitalSource](https://support.vitalsource.com/hc/en-us/articles/204612518).  This means no commercial usage or distribution of your eBook and only personal use is allowed.  Mass distribute at your own risk as your email and "DO NOT COPY" appear diagonally across each page.

## Bishoppebbles' Notes

> Credit and thanks to [LifeAlgorithm](https://github.com/LifeAlgorithm/VitalSourcePrinter) for this code and guide.  I only modified the GUI control code as it didn't work for me using the VitalSource Bookshelf v10.2.0 (10.2.26.0) Windows application.  I removed several of the files in the original repo as this code didn't require them.  I also took out the code used to reference Roman numerals.  Besides that, all the hardwork was provided by LifeAlgorithm.  The instructions below have been modified for Windows only along with several less verbose/consolidated edits.

> My code edits are super hacky (i.e., a lot of `time.sleep()` calls in an attempt to let the GUI controls do its thing).  I ultimately got it to print a 1600 page book but it took a while.  Sometimes I could get 300+ pages to print without issue and other times it would fail after a few.  Not sure why other than trying to programatically control a GUI isn't the most repeatable.  Possibly too VitalSource's software may have some trickery built-in to prevent this and throw off the GUI timings.

## The Program

This is a program to legally and automatically print your purchased eBooks hosted on the VitalSource Bookshelf platform.  It's an awful one, especially when you're a paying customer, but at least in my case the certification I'm pursuing uses it.  I'm not desiged to effectively read a 1600 page book on my phone or computer.  

This program automates the printing of PDF's from the VitalSource Bookshelf software. The VitalSource Bookshelf usually only lets the user print 2 pages at a time, and manually doing this for the entire book is tedious and time consuming. This program automatically prints any selection or the entirety of an eBook, page by page, and concatenates each PDF file. As this program makes use of keyboard automation, this process assumes that the user is away from the computer for the duration of the process, though the user at any time can stop the script from continuing using `ctrl+c` in the cmd prompt. 

## Software Prerequisites
Install the latest version of [Python 3 and pip](https://www.python.org/downloads/) on Windows (v.3.10 was used as of this writing).  If you don't have a code editor and want something a little nicer than notepad install IDLE too (though it's not my first choice).  If there's an option to include the Python components in your path I'd recommend you do that for ease of operation.  Install [VitalSource Bookshelf](https://www.microsoft.com/store/productId/9PCZL8ZKV9NX) from the Microsoft Store as well.

From the Windows cmd prompt run the following pip commands to install the required packages:

``` python3
pip install --upgrade pip
pip install PyPDF2
pip install Pillow
pip install pyautogui
```

## Environment Prerequisities

Create or use an existing working directory where the VitalSource software can save the printed PDF files.  Open the VitalSource Bookshelf software and open your eBook tab.  VitalSource needs to print to your desired directory so print a test page by opening the print dialog and print a 2-page PDF (or whatever is allowed) making sure to save it in the desired working directory.  Doing this will default all future print jobs to that location.  You can name this file anything you want as long as it is **not** `Ebook.pdf`.  You can delete it as well if you so desire.  Also note that your PDF printer software (e.g., Adobe Acrobat) **must not** automatically open the newly printed PDF after its creation or the script will not work.

## Script Execution

In the Windows cmd prompt run the script:

```python3
python.exe VitalSourcePrinter.py
```

You'll be prompted for the first and last page for the range you want to print.  Enter those values.  After that you have four (4) seconds to click on your eBook in the VitalSource software and bring it into focus (i.e., the selected window).  After that don't touch your computer, especially the keyboard!  I ran this at night or while I was at work.  If you want to do this while actively using your computer forgetabout it.  Even in a VM (which is what I did) it seemed to potentially mess up.  As I said before it's a hacky solution and not a perfectly repeatable implementation.  It's also slow.  Because of some intentional delay I think VitalSource used in the print functionality this code will only print about 2 pages every 50-60 seconds.

## PDF Editing

I used the Linux command line `pdftk` utility to concatenate different PDF sections and then the `ghostscript` tool to compress the final file to a more reasonable size.

```
pdftk <file1.pdf> <file2.pdf> <file3.pdf> cat output <mergedfile.pdf>
```

```
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dNOPAUSE -dQUIET -dBATCH -dPDFSETTINGS=<compression_settings> -sOutputFile=<out_file.pdf> <in_file.pdf>
```
* `-dPDFSETTINGS=/screen` : lower quality, smaller size (72 dpi)
* `-dPDFSETTINGS=/ebook` : better quality, but slightly larger pdfs (150 dpi)
* `-dPDFSETTINGS=/prepress` : output similar to Acrobat Distiller "Prepress Optimized" setting (300 dpi)
* `-dPDFSETTINGS=/printer` : output similar to the Acrobat Distiller "Print Optimized" setting (300 dpi)
* `-dPDFSETTINGS=/default` : output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file
