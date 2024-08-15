# Contoh kode untuk memuat dan menyimpan file video:
from moviepy.editor import VideoFileClip

# Memuat file video
video = VideoFileClip('ScarsYt.mp4')

# Menyimpan file video
video.write_videofile('result.mp4')

# Pemotongan
short_video = video.subclip(0, 10)  # Mendapatkan 10 detik pertama
short_video.write_videofile('short_result.mp4')

# penggabungan
from moviepy.editor import concatenate_videoclips

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

# penambahan efek
from moviepy.editor import vfx

reversed_video = short_video.fx(vfx.time_mirror)  # Membalikkan video
reversed_video.write_videofile('reversed_result.mp4')

# pengaturan kecepatan
sped_up_video = short_video.fx(vfx.speedx, 2)  # Mempercepat video 2x
sped_up_video.write_videofile('sped_up_result.mp4')

