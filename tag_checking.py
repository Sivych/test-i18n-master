import os

path = 'C:\\Users\\Abeli\\PycharmProjects\\Test-i18n-master\\App'

def tag_checking(path, tags):
    """search for html file"""
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                file_in_folder = os.path.join(root, file)
                """read for html file"""
                with open(file_in_folder, 'r', encoding='utf-8') as f:
                    readable = f.readlines()
                    for i in readable:
                        """removing spaces at the beginning of lines"""
                        s = i.lstrip()
                        """checking for tags"""
                        if s.startswith(tags, 0, 7):
                            readable = readable.index(i) + 1
                            print(f'В файле {f} на {readable} строке содержится тег без метки i18n')
                        else:
                            print(None)


tags = ('<p>', "<button>", "<h2>", "<h>")
tag_checking(path, tags)
