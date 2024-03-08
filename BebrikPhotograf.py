from PIL import Image


def compress_image(input_image, output_image, max_size):
    image = Image.open(input_image) 
    image.thumbnail(max_size)  
    image.save(output_image)  
    width, height = image.size
    print(f'Разрешение изображения: {width}x{height}')

input_image = input('Директория файла: ')  
output_image = input_image
max_size = (1920, 1080)  

if __name__ == '__main__':
    compress_image(input_image, output_image, max_size)  