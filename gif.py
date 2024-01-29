import imageio 

input_video = "demo.mp4"
output_gif = "output.gif"

frames = imageio.get_reader(input_video)

# 1 se = 5fps = 10 frames 
# 2 se = 10 fps = 20 frames

with imageio.get_writer(output_gif , fps=10) as gif:
    for i in range(20):
        gif.append_data(frames.get_next_data())