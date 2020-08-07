from fpdf import FPDF
import os
import ocr2text2 as ocr2text
from glob import glob

folder_img = "img"
folder_pdf = "pdf"
folder_output = "txt"


# img to pdf
def group_imgs_by_name(file_name):
    # list_of_images = ["img/topic1-1.jpg", "img/topic1-2.jpg"]
    print("reading images:" + os.path.join(folder_img, file_name, '*.*'))
    list_of_images = sorted(glob(os.path.join(folder_img, file_name + '*.*')), key=os.path.getmtime)
    print(list_of_images)
    path = ""
    if len(list_of_images) > 0:
        pdf = FPDF(orientation='L')
        pdf.compress = False
        for image in list_of_images:
            pdf.add_page()
            pdf.image(image, w=250)
        path = os.path.join(folder_pdf, file_name + ".pdf")
        pdf.output(path, "F")
        print(folder_pdf + "/" + file_name + ".pdf" + ' converted')
    return path


# pdf to txt
def pdf_to_txt(path):
    count = 0
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # print('Source file or folder of PDF(s) [' + dir_path + ']:')
    # print('(Press [Enter] for current working directory)')
    # source = input()
    # if source == '':
    #     source = dir_path
    source = os.path.join(dir_path, path if path != '' else folder_pdf)
    print(source)
    # print('Destination folder for TXT [' + dir_path + ']:')
    # print('(Press [Enter] for current working directory)')
    # destination = input()
    # if destination == '':
    #     destination = dir_path

    destination = os.path.join(dir_path, folder_output)

    if (os.path.exists(source)):
        if (os.path.isdir(source)):
            count = ocr2text.convert_recursive(source, destination, count)
        elif os.path.isfile(source):
            filepath, fullfile = os.path.split(source)
            filename, file_extension = os.path.splitext(fullfile)
            if (file_extension.lower() == '.pdf'):
                count = ocr2text.convert(source, os.path.join(destination, filename + '.txt'), count, 1)
        plural = 's'
        if count == 1:
            plural = ''
        print(str(count) + ' file' + plural + ' converted')
    else:
        print('The path ' + source + 'seems to be invalid')


if __name__ == '__main__':
    # put images in /img folder and format the name into xxx-n.zzz;
    # eg: 1-1.jpg, 1-2.jpg;
    # all images matches {}-*.* ( "{}-" can be changed bellow ) will be merge into one file
    # for n in range(30):
    #     pdf_to_txt(group_imgs_by_name("{}-".format(n + 1)))
    pdf_to_txt(group_imgs_by_name('Screen Shot 2020-08-07 at 15.25.56'))
