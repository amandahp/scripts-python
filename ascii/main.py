from pywhatkit import image_to_ascii_art

my_pick = 'teste.jpg'

my_pick_result = 'ascii_python.txt'

print(image_to_ascii_art(imgpath=my_pick, output_file=my_pick_result))