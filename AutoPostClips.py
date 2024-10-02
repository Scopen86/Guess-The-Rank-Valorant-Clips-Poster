import requests
import json
import sys
from yt_dlp import YoutubeDL
import ffmpeg
import subprocess


def getLinkYT():
  url = "https://guessmyrank.com/api/videos/random"

  querystring = {"limit":"3","game_id":"cc636b61-bfe7-4f37-aaaf-2f70523c4145"}

  payload = {}
  headers = {
    "content-type": "application/json",
    "authority": "www.youtube.com",
    "accept": "*/*",
    "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5",
    "cache-control": "max-age=0",
    "referer": "https://www.youtube.com/embed/Eme9t4hzK3g?autoplay=0&mute=0&controls=1&origin=https%3A%2F%2Fguessmyrank.com&playsinline=1&showinfo=0&rel=0&iv_load_policy=3&modestbranding=1&enablejsapi=1&widgetid=1",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Referer": "https://guessmyrank.com/games/valorant",
    "Origin": "https://www.youtube.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "if-none-match": "W/\"4bfe1b9621af3aaceff8dc022e8028de\"",
    "purpose": "prefetch",
    "x-nextjs-data": "1",
    "cookie": "__Secure-3PSID=cAggoZ0HESrabdn5ZqHRUOhnh3LedryjbEKBIU-W2PTrGn8CiUs42a72DpTm2-LTohY5kw.; __Secure-3PAPISID=BAfOskobykPJjbYl/AixK0fzeP0__5Tk1H; VISITOR_INFO1_LIVE=x9Ow4cbSXDQ; LOGIN_INFO=AFmmF2swRQIgFfEowNd8vPbiTwBum26OGU4uAK-rjyt5bJMCTAH7sWwCIQCoZhbqiuDPnfAxJEjHFJON5OMd2fxfLoFOdnVsuEwI8g:QUQ3MjNmeXJpQ1V0OEtTZElxZlJzdnlid3paNFM3dnZkZHY0emxqM1NfajNueXNQU1QzVFB2NGdyT0ZpYmxfVW1lTmg3V3JFU3RNNFVZUkRsRm84eGVsS3JVUnR3UXJybHUyRGtQc21rTDdxQ0trZkM5cno1QXY4Y2xQTmJYOFpFTjcwSUlmU01JY1BTSzRtSTNEem9SVjdaNUE1OE9lMS1n; YSC=bVGc0ZDQ5SI; __Secure-3PSIDTS=sidts-CjIB3e41hXH0_ZwCCBZH8X7WPu28GFGp2dYmWGt4NWYD5PPQvEsAyDRQvwhuI2uZwWneYRAA; __Secure-3PSIDCC=ACA-OxMweJPvIoh17xJPU8QF07guXgGl9y4z0oPApP-tN2cDYkkxsMwXXtfNMH-h0U4SGtvV7A",
    "x-client-data": "CJa2yQEIorbJAQipncoBCNX3ygEIk6HLAQiFoM0BCLnKzQEYj87NAQ==",
    "origin": "https://www.youtube.com",
    "x-goog-api-key": "AIzaSyDyT5W0Jh49F30Pqqtyfdf7pDLFKLJoAnw",
    "x-user-agent": "grpc-web-javascript/0.1",
    "authorization": "SAPISIDHASH 1697902620_b63d631006a14c76ba38e07b020c177badd005b4",
    "x-goog-authuser": "1",
    "x-goog-request-time": "1697902620107",
    "x-goog-visitor-id": "Cgt4OU93NGNiU1hEUSil4M-pBjIICgJWThICGgA%3D",
    "x-origin": "https://www.youtube.com",
    "x-youtube-ad-signals": "dt=1697902617363&flash=0&frm=2&u_tz=420&u_his=2&u_h=1080&u_w=1920&u_ah=1080&u_aw=1858&u_cd=24&bc=31&bih=-12245933&biw=-12245933&brdim=0%2C0%2C0%2C0%2C1858%2C0%2C1858%2C1080%2C640%2C360&vis=1&wgl=true&ca_type=image",
    "x-youtube-client-name": "56",
    "x-youtube-client-version": "1.20231015.00.00",
    "x-youtube-time-zone": "Asia/Bangkok",
    "x-youtube-utc-offset": "420",
    "x-yt-auth-test": "test"
  }

  response = requests.get(url, json=payload, headers=headers, params=querystring)

  # Parse the response
  json_response = response.json()
  test1 = json_response[0].values()  
  test2 = list(test1)[3]
  print(test2)
  return test2

def processVideo(url,counter):
  PATH =  "D:\\GuessTheRankVideos\\"

  #download the video
  ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'postprocessors': [{
      'key': 'FFmpegVideoConvertor',
      'preferedformat': 'mp4',
    }],
    'outtmpl': f"{PATH}\\Original\\GuessTheRank#{counter}",
    }
  with YoutubeDL(ydl_opts) as ydl:
    ydl.download(url)


  #get the resolution of the video
  input_file = f"{PATH}\\Original\\GuessTheRank#{counter}.mp4"

  cmd = "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 " + input_file
  output = subprocess.check_output(cmd, shell=True).decode('utf-8')
  resolution = output.strip()

  #split the width and height of the resolution
  resolution = resolution.split("x")
  width = resolution[0]
  height = resolution[1]
  print(width,height)

  #resize the video
  global output_file
  output_file = f"{PATH}\\Short\\GuessTheRank#{counter}_short.mp4"

  cmd = f"ffmpeg -i {input_file} -vf \"crop={int(int(height) * 9 / 16)}:{int(height)}\" {output_file}"
  output = subprocess.check_output(cmd, shell=True).decode('utf-8')
  print(output)


#Upload video to Tiktok
from Tiktok_uploader import uploadVideo

session_id = "08deae241063c2db137684758dd813e3"
tags = ["Valorant", "Radiant", "fyp", "Highlight", "VALORANTvn", "VALORANTCreatorRush"]

# Publish the video

num1 = int(input("num1:" ))
num2 = int(input("num2:" ))
for i in range(num1, num2):
  processVideo(getLinkYT(),i)
  file = output_file
  title = f"@valorant.vietnam Guess The Rank #{i}"
  uploadVideo(session_id, file, title, tags, verbose=True)