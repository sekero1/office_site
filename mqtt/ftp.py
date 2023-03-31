import ftplib

# FTP 서버에 연결합니다.
ftp = ftplib.FTP('192.168.0.36', 'jae', 'kim')

# 디렉토리 목록을 가져옵니다.
dir_list = ftp.nlst()
print(dir_list)

# 파일을 다운로드합니다.
filename = 'myprj/camera/stl_img/230331/230331_074519.jpg'
local_filename = '074519.jpg'
with open(local_filename, 'wb') as f:
    ftp.retrbinary('RETR ' + filename, f.write)

# 파일을 업로드합니다.
# filename = 'example.txt'
# remote_filename = 'example.txt'
# with open(filename, 'rb') as f:
#     ftp.storbinary('STOR ' + remote_filename, f)

# FTP 서버와의 연결을 종료합니다.
ftp.quit()
