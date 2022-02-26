import os
import img2pdf

def makePdf(PATH):
    images= []
    for fname in os.listdir(PATH):
        if not fname.endswith('.jpg'):
            continue
        imgPath= os.path.join(PATH, fname)
        images.append(imgPath)

    with open(os.path.join(PATH, 'merged_slides.pdf'), 'wb') as f:
        f.write(img2pdf.convert(images))

if __name__ == '__main__':
    print('All images in current directory will be merged into PDF...')
    path= os.getcwd()
    makePdf(path)