from PIL import Image
ascii_char = list(" $@B%8")

WIDTH = 60
HEIGHT = 45

def get_char(r,g,b,alpha=255):
	if alpha == 0:
			return ' '
	maxV = len(ascii_char)-1
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	p = gray/255
	v = int(maxV*p)
	return ascii_char[v]

if __name__ == '__main__':
		img = '/Users/singerdream/workspace/python/dingdangmao.jpg'	
		im = Image.open(img)
		im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
		txt = ""
		for s in range(HEIGHT):	
			for r in range(WIDTH):
				txt += get_char(*im.getpixel((r,s)))
			txt += '\n'
		print(txt)

		with open("/Users/singerdream/workspace/python/dingdangmao.txt",'w') as f:
			f.write(txt)