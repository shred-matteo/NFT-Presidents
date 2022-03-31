# TRANSFORM_SCRIPTS.py

# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to interact with the operating system
import os

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# library to generate random integer values
from random import randint

# Import required image modules
from PIL import Image

# import for progress bar
from tqdm import tqdm

# dimensions = 480, 480

#Function that generates base image files, and base image backgrounds
def generate_bg(y):
    for x in tqdm(range(0,y), desc="GENERATING BACKGROUNDS   "):
        # create variables for background images
        genericbg1 = Image.open(os.path.join(dirname + "/images/bg_images/generic1.png"))
        genericbg2 = Image.open(os.path.join(dirname + "/images/bg_images/generic2.png"))
        genericbg3 = Image.open(os.path.join(dirname + "/images/bg_images/generic3.png"))
        genericbg4 = Image.open(os.path.join(dirname + "/images/bg_images/generic4.png"))
        genericbg5 = Image.open(os.path.join(dirname + "/images/bg_images/generic5.png"))
        genericbg6 = Image.open(os.path.join(dirname + "/images/bg_images/generic6.png"))
        genericbg7 = Image.open(os.path.join(dirname + "/images/bg_images/generic7.png"))
        genericbg8 = Image.open(os.path.join(dirname + "/images/bg_images/generic8.png"))
        genericbg9 = Image.open(os.path.join(dirname + "/images/bg_images/generic9.png"))
        genericbg10 = Image.open(os.path.join(dirname + "/images/bg_images/generic10.png"))

        redbg = Image.open(os.path.join(dirname + "/images/bg_images/red.png"))
        orangebg = Image.open(os.path.join(dirname + "/images/bg_images/orange.png"))
        yellowbg = Image.open(os.path.join(dirname + "/images/bg_images/yellow.png"))
        greenbg = Image.open(os.path.join(dirname + "/images/bg_images/green.png"))
        bluebg = Image.open(os.path.join(dirname + "/images/bg_images/blue.png"))
        indigobg = Image.open(os.path.join(dirname + "/images/bg_images/indigo.png"))
        violetbg = Image.open(os.path.join(dirname + "/images/bg_images/violet.png"))

        #list of background images
        bglist = [yellowbg, orangebg,
        genericbg1, genericbg2, genericbg3, genericbg4, genericbg5, redbg, greenbg, bluebg, indigobg, violetbg, genericbg6,
        genericbg7, genericbg8, genericbg9, genericbg10]

        # randomly select a background from list
        c = randint(0,(len(bglist)-1))
        new_image = bglist[c]

        # save new background image as loop number
        imgname = dirname + '/images/deadprez_images/' + (str(x)) + '.png'
        new_image.save(imgname)

# Function that Inserts President.PNG over background image
def insert_prez(y):
    for x in tqdm(range(0,y), desc="INSERTING PREZIDENTS     "):
        # opens the file that is named "x" (our current iteration)
        im = Image.open(os.path.join(dirname + '/images/deadprez_images/' + (str(x)) + ".png"))

        # create variables for president images
        lincoln = Image.open(os.path.join(dirname + "/images/base_prez/lincoln.png"))
        jackson = Image.open(os.path.join(dirname + "/images/base_prez/jackson.png"))
        mvb = Image.open(os.path.join(dirname + "/images/base_prez/mvb.png"))
        jqadams = Image.open(os.path.join(dirname + "/images/base_prez/jqadams.png"))  
        washington = Image.open(os.path.join(dirname + "/images/base_prez/george_washington.png"))
        franklin = Image.open(os.path.join(dirname + "/images/base_prez/franklin.png"))
        jm = Image.open(os.path.join(dirname + "/images/base_prez/jm.png"))
        nixon = Image.open(os.path.join(dirname + "/images/base_prez/nixon.png"))
        wilson = Image.open(os.path.join(dirname + "/images/base_prez/wilson.png"))

        # A list of all the presidents, one is randomly selected each iteration
        prezlist = [lincoln, jackson, mvb, jqadams, washington, franklin, jm, nixon, wilson]
        c = randint(0,(len(prezlist)-1))
        prez = prezlist[c]

        # Paste the President onto the image
        # mask is important for transparency 
        im.paste(prez, mask=prez)

        # Save Image and name it loop number
        imgname = dirname + '/images/deadprez_images/' + (str(x)) + '.png'
        im.save(imgname)

#Function that adds "transformations" to Presidents by adding a PNG over it
def transform_1(y):
    for x in tqdm(range(0,y), desc="APPLYING TRANSFORMATIONS "):
        # opens the file that is named "x" (our current iteration)
        im = Image.open(os.path.join(dirname + '/images/deadprez_images/' + (str(x)) + ".png"))

        # create variables for our transformation images
        whiskers = Image.open(os.path.join(dirname + '/images/transform_images/whiskers.png'))
        haloblue = Image.open(os.path.join(dirname + '/images/transform_images/haloblue.png'))
        googlyeyes = Image.open(os.path.join(dirname + '/images/transform_images/googlyeyes.png'))
        hearts = Image.open(os.path.join(dirname + '/images/transform_images/hearts.png'))
        pizza = Image.open(os.path.join(dirname + '/images/transform_images/pizza.png'))

        # The transformations are divided by top / eye / misc, so that we can have multiple
        # transformations applied without clipping issues
        eyetransforms = [googlyeyes]
        toptransforms = [haloblue, hearts, pizza]
        misctransforms = [whiskers]

        # top transformations
        e=randint(0,1000)
        if e > 600:
            f=randint(0,(len(toptransforms)-1))
            glasses=toptransforms[f]
            im.paste(glasses, mask=glasses)

        # Misc Transformations
        g=randint(0,1000)
        if g > 900:
            h=randint(0,(len(misctransforms)-1))
            glasses=misctransforms[h]
            im.paste(glasses, mask=glasses)
        c=randint(0,1000)

        # Glasses Transform
        if c > 500:
            d=randint(0,(len(eyetransforms)-1))
            glasses=eyetransforms[d]
            im.paste(glasses, mask=glasses)

        # Save Image and name it iteration number
        imgname = dirname + '/images/deadprez_images/' + (str(x)) + '.png'
        im.save(imgname)
          
def transform_flip_text(y):
    for x in tqdm(range(0,y), desc="FLIPPING /TEXT           "):
        # opens the file that is named "x" (our current iteration)
        im = Image.open(os.path.join(dirname + '/images/deadprez_images/' + (str(x)) + '.png'))

        # create variables for our "transformations"
        blank = Image.open(os.path.join(dirname + '/images/transform_images/blank.png'))
        eth = Image.open(os.path.join(dirname + '/images/transform_images/eth.png'))

        # list of all our word transformations
        wordtransforms =[eth]
        c=randint(0,1000)
        d=randint(0,1000)

        # 1 in 10 chance to flip images horizontally
        if c > 900:
            im = im.transpose(0) # 0 is value for horizontal flip 
        
        # if not flip 1 in 10 chance for word to be added
        elif 900 >= c >= 800:
            d=randint(0,(len(wordtransforms)-1))
            word=wordtransforms[d]
            im.paste(word, mask=word)
        
        else:
            im.paste(blank, mask=blank) 
            
        imgname = dirname + '/images/deadprez_images/' + (str(x)) + '.png'
        im.save(imgname)

 
def transform_frame(y):
    for x in tqdm(range(0,y), desc="APPLYING FRAMES          "):
        # opens the file that is named "x" (our current loop)
        im = Image.open(os.path.join(dirname + '/images/deadprez_images/' + (str(x)) + ".png"))
        # create variables for our frame images
        # we are always going to add a frame, so blank frame "adds" nothing
        blank_frame = Image.open(os.path.join(dirname + '/images/transform_images/blank.png'))
        red_frame = Image.open(os.path.join(dirname + '/images/frame_images/red_frame.png'))
        orange_frame = Image.open(os.path.join(dirname + '/images/frame_images/orange_frame.png'))
        yellow_frame = Image.open(os.path.join(dirname + '/images/frame_images/yellow_frame.png'))
        green_frame = Image.open(os.path.join(dirname + '/images/frame_images/green_frame.png'))
        blue_frame = Image.open(os.path.join(dirname + '/images/frame_images/blue_frame.png'))
        indigo_frame = Image.open(os.path.join(dirname + '/images/frame_images/indigo_frame.png'))
        violet_frame = Image.open(os.path.join(dirname + '/images/frame_images/violet_frame.png'))

        # A list of all the frames, one is randomly selected each iteration
        framelist = [blank_frame, red_frame, orange_frame, yellow_frame, green_frame, blue_frame, indigo_frame, violet_frame]
        c = randint(0,(len(framelist)-1))
        new_frame = framelist[c]

        # Paste frame over image
        im.paste(new_frame, mask=new_frame)

        # Save image as loop number
        imgname = dirname + '/images/deadprez_images/' + (str(x)) + '.png'
        im.save(imgname)



    


