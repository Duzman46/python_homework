import imageio

output_gif = "output.gif"
writer = imageio.get_writer(output_gif, mode="I", duration=0.1)
image_files = ["gif_maker\image.jpg"]

for image_file in image_files:
    img = imageio.imread(image_file)
    writer.append_data(img)

writer.close()
