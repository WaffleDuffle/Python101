import numpy as np
class Image():
    def __init__(self, format='P3', rows=0, columns=0, max_value=255, pixels=[[]]):
        self.format = format
        self.rows = rows
        self.columns = columns
        self.max_value = max_value
        self.pixels = pixels
    def __str__(self):
        # use this for debugging
        image = ""
        image += f"{self.format}\n{self.rows} {self.columns}\n{self.max_value}\n"
        for i in range(self.rows):
            for j in range(3 * self.columns):
                image += f"{self.pixels[i][j]} "
            image += "\n"
        return image
    def sepia(self):
        # apply sepia filter to the image
        for i in range(0, self.rows):
            for j in range(0, self.columns * 3, 3):
                sepia_r = int(0.393 * self.pixels[i][j] + 0.769 * self.pixels[i][j + 1] + 0.189 * self.pixels[i][j + 2])
                sepia_g = int(0.349 * self.pixels[i][j] + 0.686 * self.pixels[i][j + 1] + 0.168 * self.pixels[i][j + 2])
                sepia_b = int(0.272 * self.pixels[i][j] + 0.534 * self.pixels[i][j + 1] + 0.131 * self.pixels[i][j + 2])
                self.pixels[i][j] = min(sepia_r, 255)
                self.pixels[i][j + 1] = min(sepia_g, 255)
                self.pixels[i][j + 2] = min(sepia_b, 255)
    def read(self, filename):
        # read from file and assign the correct parameters (see README and input examples)
        pixels = [[]]
        file = open(filename, 'r')
        self.format = file.readline().strip()
        line = file.readline()
        self.rows, self.columns = int(line[0]), int(line[2])
        self.max_value = int(file.readline())

        for i in range(self.rows):
            line2 = file.readline().split(' ')
            for j in line2:
                if j != "\n":
                    pixels[i].append(int(j))
            pixels.append([])

        pixels.remove([])
        self.pixels = np.array(pixels)
        file.close()
    def write(self, filename):
        # write to file in the correct format (see README and input examples)
        file = open(filename, "w")
        file.writelines(f"{self.format}\n")
        file.writelines(f"{self.rows} {self.columns}\n")
        file.writelines(f"{self.max_value}\n")
        for i in range(self.rows):
            for j in range(self.columns * 3):
                file.writelines(f"{self.pixels[i][j]} ")
            file.writelines("\n")
        file.close()


