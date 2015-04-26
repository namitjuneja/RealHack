from PIL import Image
import PIL.ImageOps   

col = Image.open("GoogleMaps.png")
gray = col.convert('L')
inverted_image = PIL.ImageOps.invert(gray)
bw = inverted_image.point(lambda x: 0 if x<10 else 255, '1')
bw.save("result_bw.png")
