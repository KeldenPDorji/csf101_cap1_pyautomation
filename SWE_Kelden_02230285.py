from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = './editedimgs'

os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    try:
        img = Image.open(f"{path}/{filename}")
    except IOError:
        print(f"Unable to open {filename}. Skipping.")
        continue
    
    """Photo Manipulation Tools.Remove the comment to apply the filters"""
   
    """Apply sharpening filter to the opened image"""
    img = img.filter(ImageFilter.SHARPEN)
    # img = img.filter(ImageFilter.SHARPEN)
    # img = img.filter(ImageFilter.SHARPEN)


    """Apply blur filter"""
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    # img_blur = img.filter(ImageFilter.BLUR)
    
    """Apply detail filter"""
    # img_detail = img.filter(ImageFilter.DETAIL)
    # img_detail = img.filter(ImageFilter.DETAIL)
    # img_detail = img.filter(ImageFilter.DETAIL)
    # img_detail = img.filter(ImageFilter.DETAIL)
    # img_detail = img.filter(ImageFilter.DETAIL)

    """Apply edge finding filter"""
    # img = img.filter(ImageFilter.FIND_EDGES)

    """Apply emboss filter"""
    # img = img.filter(ImageFilter.EMBOSS)
    
    """Apply smooth more filter"""
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    # img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE)
    
    """Convert the image to RGB"""
    img = img.convert('RGB')
    
    """Convert the image to grayscale"""
    img = img.convert('L')

    """ Enhance contrast"""
    factor = 1.5
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    """Save the image at its highest quality"""
    img.save(f'{pathOut}/{clean_name}_edited.jpg', quality=100)


"""Description:
The provided Python script utilizes the Python Imaging Library (PIL) 
to process a set of images stored in a specified input directory. 
It attempts to open each image and applies various image enhancement operations 
such as sharpening and contrast adjustment. The code allows for the application 
of additional filters like blurring, detail enhancement, edge detection, embossing, 
and more, though most of these options are commented out by default. After processing, 
the script converts the images to grayscale, enhances their contrast, 
and saves the edited versions with improved quality in a separate output directory. 
Users can customize the script by uncommenting specific filter operations or 
adjusting parameters to suit their image processing needs."""