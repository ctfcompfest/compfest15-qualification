from PIL import Image

image = Image.open("original_pic.png")
flag = Image.open("flag.png")

pixel1 = image.load()
pixel2 = flag.load()

chall = Image.new(image.mode, image.size)
chall_pixel = chall.load()

for i in range(image.size[0]):
    for j in range(image.size[1]):
        rgb_ = pixel1[i, j]
        rgb1 = (f"{rgb_[0]:08b}", f"{rgb_[1]:08b}", f"{rgb_[2]:08b}")
        rgb2 = (f"{0:08b}", f"{0:08b}", f"{0:08b}")
        if i < flag.size[0] and j < flag.size[1]:
            rgb2_ = pixel2[i, j]
            rgb2 = (f"{rgb2_[0]:08b}", f"{rgb2_[1]:08b}", f"{rgb2_[2]:08b}")
        
        rgb = (rgb1[0][:7] + rgb2[0][:1], rgb1[1][:7] + rgb2[1][:1], rgb1[2][:7] + rgb2[2][:1])

        chall_pixel[i, j] = (int(rgb[0], 2), int(rgb[1], 2), int(rgb[2], 2))


chall.save("chall.png")
