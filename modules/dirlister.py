import os

def run(**args):

	print"[*] W module dirlister."
	files = os.listdir(".")

	return str(files)


if __name__ == "__main__":
	print(run())
