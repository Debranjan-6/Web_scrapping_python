import webbrowser
import sys
import pyperclip


#webbrowser.open('http://inventwithpython.com/')


if len(sys.argv) > 1:
# Get address from command line.
    address = ' '.join(sys.argv[1:])
    print ("Address = "+address)
else:
    # Get address from clipboard.
        address = pyperclip.paste()
webbrowser.open("https://www.google.com/maps/place/"+address)
   

    #print("argv 0="+sys.argv[0])
    #print("argv 1="+sys.argv[1])
    #print("argv 2="+sys.argv[2])
    #print("argv 3="+sys.argv[3])
#code11
    

