from PIL import Image
from rtt_settings import flag_folder,output_sizes

inp:str = 'N/A'

while inp != 'EXIT':
    inp = input("Please input file path:\nType 'EXIT' to quit:\n:  ")
    name = input("Please input name of file: e.g., SCO_communism, ALB_neutrality\n: ")


    with Image.open(inp) as im:

        im_out = im.resize(output_sizes[0])
        im_out.save(f'{flag_folder}/small/{name}.tga')

        im_out = im.resize(output_sizes[1])
        im_out.save(f'{flag_folder}/medium/{name}.tga')

        im_out = im.resize(output_sizes[2])
        im_out.save(f'{flag_folder}/{name}.tga')

        input('Done!') # stops it from closing automatically
