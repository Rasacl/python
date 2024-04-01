import re
# 导入线程池
import concurrent.futures
import requests
import os
from moviepy.editor import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip


def read_file():
    filename = '07c38d15-4ffb-405b-9da5-db1e043c603b'

    # 使用正则表达式匹配所有的 HTTPS 链接
    # 这个正则表达式会匹配以 https:// 开头的链接，直到遇到换行符或文件结束
    pattern = re.compile(r'https?://[^\s]+')

    # 读取文件内容
    with open('./m3u8/' + filename, 'r') as file:
        content = file.read()

        # 使用正则表达式查找所有的匹配项
    links = pattern.findall(content)
    return links


def merge_vides(links):
    # 设置视频片段的保存目录
    output_dir = 'video_segments'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=7)
    exe.submit(DownLoad_merge_video, output_dir)
    exe.shutdown()  # 关闭线程池


def DownLoad_merge_video(output_dir):
    # 下载视频片段并保存到本地
    for i, link in enumerate(links):
        filename = os.path.join(output_dir, f'segment_{i}.ts')
        response = requests.get(link, stream=True)
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        # 使用 moviepy 合并视频片段
    clips = []
    for filename in os.listdir(output_dir):
        if filename.endswith('.ts'):
            print(f'Processing {filename}')
            clip = concatenate_videoclips([VideoFileClip(os.path.join(output_dir, filename))])
            clips.append(clip)

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile("output.mp4", codec='libx264')


if __name__ == '__main__':
    links = read_file()
    merge_vides(links)
