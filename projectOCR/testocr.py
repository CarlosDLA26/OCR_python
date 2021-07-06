from easyocr import Reader
import os, re, cv2

def list_images(directory):
	'''Function to take image files in a directory

	Parameters
	----------
	directory : string
		directory's path with the images

	Returns
	-------
	List
		list with image files' name 
	'''
	files = os.listdir(directory)
	pattern = re.compile(r'[\w]+\.(png|jpg|jpeg|PNG|JPG|JPEG)')
	return [files[i] for i in range(len(files)) if pattern.search(files[i])]

def main():
	images_directory = '.\images'
	langs  = ['es'] # Languages
	reader = Reader(langs, 0)
	images = list_images(images_directory)

	for image in images:
		image_aux = cv2.imread(images_directory + '\\' + image)
		results = reader.readtext(image_aux)

		print(f'Text in image: {image}')

		for (bbox, text, prob) in results:
			print(f"\t[INFO] {text}")
	
if __name__ == "__main__":
	main()