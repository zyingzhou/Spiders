import requests
# 获取URL
url = input('please input a URL :')
if 'https://'and 'http://' in str(url):
    url = str(url)
    
else:
    url = "http://" + str(url)
# 定义函数get_content(url)去获取URL对应的内容.
def get_content(url):
    try:
        r = requests.get(url,headers = {'user-agent':'Mozilla/5.0 '}, timeout=30)
        r.encoding = 'utf-8'
        return r.content
    except:
        print('error!')
#定义函数save_file()来保存文件到本地.
def save_file():
    list = []
    list = url.split('/')
    path = list[-1]
    #  通过后缀名来判断内容的属性
    if 'mp4' in url:
        path = "D:\\Myfiles\\python_download_files\\视频\\" + path

    elif 'mp3' in url:
        path = "D:\\Myfiles\\python_download_files\\音乐\\" + path
    elif 'pdf' in url:
        path = "D:\\Myfiles\\python_download_files\\文档\\" + path
    elif 'jpg' or 'jpeg' or 'png' in url:
        path = "D:\\Myfiles\\python_download_files\\图片\\" + path
    #开始写入文件
    with open(path,'wb') as f:
        f.write(get_content(url))
        f.close()
# 开始从互联网上获取相应内容.
if __name__ == '__main__':
    print("......开始获取文件......")
    get_content(url)
    print("......开始保存文件......")
    save_file()
    print("......文件获取成功！......")
