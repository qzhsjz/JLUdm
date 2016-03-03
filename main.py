# coding:utf-8
import Tkinter
from random import choice
from random import randint
from time import sleep
namelist = ['赵雅欣','张姣姣','张迪','张璐','智梓钧','陈铮','丛阳','赵笑宜','赵馨婷','董凝蓄','王雪婷','付佳平','戴晶晶','吴孟洁','褚振茹',"张文雪","彭珂","胡泉声","宋钰祺","王思劼","李哲","马宇骁","刘诗洋","沙雨邦","焦杨","蒋宗晟","颜理江","苏鹏","张熙","常港伟"]

def create():
	noticelbl['text'] = '还没完哦~'
	for i in xrange(0,randint(25,35)):
		namelbl['text'] = choice(namelist)
		root.update()
		sleep(0.05 + (i ** 2) / 1000)
	noticelbl['text'] = '好了~'
	root.update()
	return

def manage():
	def namesave():
		global namelist
		raw_namelist = name.get(0.0,Tkinter.END).rstrip('\n').split('\n')
		namelist = []
		for raw_name in raw_namelist:
			parsed = raw_name.split(' ')
			if len(parsed) > 1:
				for i in xrange(0,int(parsed[1])):
					namelist.append(parsed[0])
			else:
				namelist.append(parsed[0])
		mngwin.destroy()
		return
	mngwin = Tkinter.Toplevel()
	mngwin.title("数据管理界面")
	introduce = Tkinter.Label(mngwin,text="请在下面输入人名，一行一个，然后点击保存，即可完成名单的修改。\n在名单中，如果需要给人加权重，请在人名后面加上一个空格，并写上权重值。\n可见权重值其实是人名在备选名单中重复出现的次数。")
	datanoticelbl = Tkinter.Label(mngwin,text="数据示例：\n秦泽浩 100\n马宁 2")
	name = Tkinter.Text(mngwin)
	name.insert(0.0,"\n".join(namelist))
	submit = Tkinter.Button(mngwin,text="保存",command=namesave)
	introduce.pack()
	datanoticelbl.pack()
	name.pack()
	submit.pack()
	mngwin.update()
	return

def about():
	def rtn():
		abtwin.destroy()
		return
	abtwin = Tkinter.Toplevel()
	abtwin.title('关于')
	abttxt = Tkinter.Label(abtwin,text='吉林大学点名器V0.3测试版\n供哲学社会学院2015级劳动与社会保障班使用\n制作：秦泽浩\n语言：Python\n图形化界面库：Tkinter')
	rtnbtn = Tkinter.Button(abtwin,text='返回',command=rtn)
	abttxt.pack()
	rtnbtn.pack()
	abtwin.update()
	return

root = Tkinter.Tk()
root.title("点名器")
noticelbl = Tkinter.Label(root,text="按“点名”开始",font=("微软雅黑",36,"normal"))
namelbl = Tkinter.Label(root,text="",font=("微软雅黑",144,"normal"))
createbtn = Tkinter.Button(root,text="点名",command=create,font=("微软雅黑",12,"normal"))
mngbtn = Tkinter.Button(root,text="设置",command=manage,font=("微软雅黑",12,"normal"))
abtbtn = Tkinter.Button(root,text="关于",command=about,font=("微软雅黑",12,"normal"))
noticelbl.pack()
namelbl.pack()
mngbtn.pack(side=Tkinter.RIGHT)
abtbtn.pack(side=Tkinter.LEFT)
createbtn.pack(expand=0)
root.mainloop()


