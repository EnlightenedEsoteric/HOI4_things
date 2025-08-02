from PIL import Image
from rtt_settings import flag_folder,output_size

inp:str = 'N/A'

while inp != '_EXIT_':

    inp = input("Please input file path:\nType '_EXIT_' to quit:\n:  ")
    if inp == '_EXIT_':
        exit(None)
    name = input("Please input name of file: e.g., SCO_communism, ALB_neutrality\n: ")


    with Image.open(inp) as im:

        def resize_to_tga(size:tuple,folder_name:str) -> None:
            '''Takes a tuple "size" and transforms the
            inputted image file to match those dimensions,
            then saves that new file to your hoi4 mod flag folders'''

            im_out = im.resize(size)
            print(size,folder_name)
            if not folder_name:
                raise TypeError
            if folder_name == 'large':
                im_out.save(f'{flag_folder}/{name}.tga')
            else:
                im_out.save(f'{flag_folder}/{folder_name}/{name}.tga')


        for k,v in output_size.items():
            resize_to_tga(v,k)

        input('Done!') # stops it from closing automatically
