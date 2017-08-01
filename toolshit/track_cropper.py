import re
import subprocess
from datetime import datetime, timedelta


def extract_song_info(line):
    regex = '(?P<name>\d{1,2}.*)(?:\\ )\\((?P<ss>.*)\\)'
    infos = re.match(regex, line).groupdict()
    return infos


def get_tracklist(file_path):
    ret = list()
    with open(file_path, 'r') as fp:
        for line in fp.readlines():
            if not line.strip():
                continue

            cur_info = extract_song_info(line.strip())
            if ret:
                last_to = str((datetime.strptime(cur_info['ss'], '%H:%M:%S') - timedelta(seconds=1)).time())
                ret[-1]['to'] = last_to
            ret.append(cur_info)
    ret[-1]['to'] = '1:51:20'
    return ret


def auto_crop(file_path, track_info):
    ss = track_info.get('ss')
    to = track_info.get('to')
    name = track_info.get('name')
    out_file = 'playlist/' + name + '.mp3'
    output = subprocess.check_output(
         ['ffmpeg', '-i', file_path, '-ss', ss,  '-to', to, '-c', 'copy', out_file]
    )
    return output


def main():
    track_list = get_tracklist('static/the_best_of_bach_tracklist.txt')
    for track_info in track_list:
#        print(track_info)
        print(auto_crop('/home/wrq/tmp/videos/bach/the_best_of_bach.mp3', track_info))


if __name__ == 'main':
    main()


