from PIL import Image
from rtt_settings import output_dir,output_sizes


inp = input("Please input file path: ")
name = input("Please input name of file: ")


with Image.open(inp) as im:

    for index, size in enumerate(output_sizes):
        im_out = im.resize(size)
        print(f'{output_dir}/{index}{name}.tga')
        im_out.save(f'{output_dir}/{index}{name}.tga')


    input('Done!') # stops it from closing automatically

