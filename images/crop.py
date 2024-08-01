import cv2

name = 'locotrack'
video = cv2.VideoCapture(name + '.mp4')
ret, img = video.read()

video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_size = min(video_width, video_height)
video_crop = int((video_width - video_size) / 2)
video_resize = (256, 256)
img_width = img.shape[1]
img_height = img.shape[0]
img_size = min(img_width, img_height)
img_crop = int((img_width - img_size) / 2)

# Crop the video to 1:1
video_crop = video_crop + int((video_size - video_size) / 2)
frames = []
while True:
    ret, frame = video.read()
    if not ret:
        break
    frame = frame[:, video_crop:video_crop + video_size, :]
    frame = cv2.resize(frame, video_resize)
    frames.append(frame)

# Crop the image to 1:1
img = img[:, img_crop:img_crop + img_size, :]
# Save the image
cv2.imwrite(name + '_before.jpg', cv2.resize(img, video_resize))
# Save the video
fourcc = cv2.VideoWriter_fourcc(*'H264')
output_video = cv2.VideoWriter(name + '_after.mp4', fourcc, 15, video_resize)
for frame in frames:
    output_video.write(frame)
output_video.release()