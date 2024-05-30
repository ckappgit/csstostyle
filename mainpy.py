import re
_css=input("请输入css文件名（带拓展名）")
_html=input("请输入html文件名（带拓展名）")
cssf=open(_css,"r")
keycss=cssf.read()
cssf.close()
print("css读取成功")
htmlf=open(_html,"r")
htmlkey=htmlf.read()
htmlf.close()
print("html读取成功")
#判断是否已有style
restyle=re.search("style",htmlkey)
if restyle== None:
    print("html里没有sytle标签，即将开始转移")
    endhtml=re.sub("<head>","<head>\n<style>\n"+keycss+"</style>",htmlkey)
    htmlf=open(_html,"w")
    htmlf.write(endhtml)
    htmlf.close()
    print("转移已经完成了，感谢使用")

else:
    print("文件里已经有syle标签，即将开始转移")
    endhtml=re.sub("<style>","<style>\n"+keycss,htmlkey)
    htmlf=open(_html,"w")
    htmlf.write(endhtml)
    htmlf.close()
    print("转移已经完成了，感谢使用")