from PIL import Image

def get_rating(impath):
    img = Image.open(impath)
    img.show()

    rating = float(input("What would you rate this person? (float): "))
    rating = round(rating, 2)

    return rating

def line_extract(line):
    line = line.replace("\n", "")
    split_line = line.split()
    filename = split_line[0]
    amt_raters = int(split_line[1])
    rating = float(split_line[2])
    return filename, amt_raters, rating

def write_line(impath, rating, text_doc):
    line_written = False
    image_file_name = impath[::-1][:impath[::-1].find("/")][::-1]

    with open(text_doc, "r+") as text:
        lines = text.readlines()
        for i, line in enumerate(lines):
            if image_file_name in line:
                line_written = True
                filename, amt_raters, old_rating = line_extract(line)
                new_rating = round((((old_rating * amt_raters) + rating) / (amt_raters + 1)), 2)

                new_line = filename + " " + str(amt_raters+1) + " " + str(new_rating) + "\n"
                lines[i] = new_line

                text.seek(0)
                text.truncate()
                text.writelines(lines)

                break

    if not line_written:
        with open(text_doc, "a") as text:
            new_line = image_file_name + " " + "1" + " " + str(rating) + "\n"
            text.write(new_line)

impath = "data/my_images/gorlock.jpg"
rating = get_rating(impath)

text_doc = "test.txt"
write_line(impath, rating, text_doc)

