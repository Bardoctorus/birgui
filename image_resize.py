from PIL import Image
import os, sys, glob

from os import listdir
from os.path import isfile, join


#  main just redirects to doWork so the GUI can call it directly
def main(folder, newWidth):
    doWork(folder, newWidth)





def doWork(folder, newWidth, log = False):
    # create a string path to a potential logfile - this doesn't create the file!
    logfile = os.path.join(folder, "log.txt")
    #If logfile was checked, create a log.txt file in the working directory
    if(log):        
        with open(logfile, 'w') as l:            
            l.write("Working Folder: "+folder)
    # This is a cludge, we know it's not an int at this stage, it's a string
    if newWidth != type(int):
        #nevertheless we cast it to an int
        try:            
            newWidth = int(newWidth)           
            #print(newWidth, type(newWidth))
        except:
            #Since casting from a "float string" like "3.6" to integer isn't possible, just tell them not to
            #RIP everyone who loves their 300.5 width images
            return ("Width must be an Integer")
    # This is only for the command line version, the GUI can't really fuck this up   
    if not os.path.exists(folder):
        print("The folder isn't valid, exiting")
        sys.exit(1)

    
    # When did I do this how did I do this python hurts
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    #print(type(onlyfiles[0]))
    succesful_conversions = []
    fails = 0
    for file in onlyfiles:
        joined_name = os.path.join(folder, file)

        if(log):
            appendlog(logfile, "Attempting to open "+joined_name+"\n")            
            
                
        try:
            f =  Image.open(joined_name)

        except IOError:
            if(log):
                appendlog(logfile, "X   -   - Error opening "+file+", moving on") 
            fails += 1
            continue
        else:
            
            newHeight =  int(newWidth * f.size[1]/f.size[0])
            newSize = (newWidth, newHeight)
            newFileName = os.path.join(folder,  "_"+str(newWidth)+"px_"+file)
            # deets = {"new height": newHeight,
            #      "new Size": newSize,
            #      "new file name": newFileName  }
            # print(deets)
            if (f.size[0] == 670):
                if(log):
                    appendlog(logfile, file+" already correct width - moving on")
                
                continue  
            g = resizer(f, newSize)
            try:
                g.save(newFileName)
            
                succesful_conversions.append(newFileName)
                if(log):
                    appendlog(logfile, "-   O   - Created: "+newFileName)
                

            except KeyError:
                
                if(log):
                    appendlog(logfile, "Cannot resize "+newFileName+", unsupported filetype")


  

    print(".\n.\n.\n.\nDone! Created:\n")
    for thing in succesful_conversions:
        print (thing)
    print("\n\nWith "+str(fails)+" fails (probably not images)")

    return len(succesful_conversions)
    
    
def resizer(imData, newSize):
    # ! all this if logic is only needed if you are using a different filter for up/downscaling
      # if (f.size[0] > newSize[0]):
          
        #     g = makeSmol(f, newSize)
            
        #     g.save(newName)
        # elif (f.size[0] < newWidth):
        #     g = makeBigga(f, newSize)
            
        #     g.save(newName)
    # if(imData.size[0] == 670):
    #     print("Image already correct width - moving on")
    #     return

    g = imData.resize((newSize),Image.LANCZOS)
    return g

def appendlog(logfile, message):
    with open(logfile, 'a') as l:            
                 
                l.write(message+"\n")


    
if __name__ == "__main__":
    print(".______   .______    __  .______     ") 
    print("|   _  \  |   _  \  |  | |   _  \     ")
    print("|  |_)  | |  |_)  | |  | |  |_)  |    ")
    print("|   _  <  |   _  <  |  | |      /     ")
    print("|  |_)  | |  |_)  | |  | |  |\  \-.")
    print("|______/  |______/  |__| | _| `.__| Bardoctorus Batch Image Resizer\n")
    print("This simple image resizer detects all the images in a folder and resizes them to a chosen pixel width using Lanczos, while preserving the aspect ratio.")
    print("\n\nNo files are overwritten, new files get the prefix '_NEWSIZEpx_'")
    
    print("Press Ctrl + C to quit\n\n")
    path = input("Enter folder path, or press Enter to use current folder, or info for more info\n.")
    if path == "":
        path = os.getcwd()
    elif path == "info":
        print("\nFull info available at https://github.com/Bardoctorus/UPDATETHISURL but in short:\n")
        print("This script iterates over every file in a directory using Pillow's Image.open function.")
        print("I'm pretty much just letting it do its thing in a try, and excepting any IOErrors before continuing.")
        print("New file aspect ratios are just 'new_width * old_height / old_width' casted to an int which I'm sure makes some of you cry.")
        print("Feel free to fork and improve this program and tell me how much I suck - @ianmbuckley on the twitderp\n\n")
        path = input("Enter folder path, or press Enter to use current folder.\n.")
        if path == "":
            path = os.getcwd()
    size = input("Enter new width.\n.") 
    main(path, size)



                                      