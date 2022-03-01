from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.messagebox import *
import time

import winsound
import threading
import random

#window.iconbitmap("./image/icon.ico")窗口图标
#cell=int(input("请输入一共有多少格"))
micerest='no'
b1=[]
b=[]
cell=6
energy=100
money=100



#我的包裹
minelist=[]
#全部武器信息存储
allweapon={0:['木剑','伤害为:1','新手的武器','1','','50'],1:\
           ['无尽之刃','伤害为:50','神装','50','','1000'],\
           2:['铁剑','伤害为:2','简单的兵器','2','','70']}

#武器的类
class weapon():
    def __init__(self,name,quality,note,damage,skill,price):
        self.name=name
        self.category='武器'
        self.quality=quality
        self.note=note
        self.damage=int(damage)
        self.skill=skill
        self.price=int(price)

#将全部武器实例化
for weap in allweapon.keys():
    allweapon[weap]=weapon(allweapon[weap][0],allweapon[weap][1],allweapon[weap][2],allweapon[weap][3],allweapon[weap][4],allweapon[weap][5])
    
#我拥有的武器的序号    相互更新，为的是对接数据库传输便捷 化为武器在本地执行
mineweaponnum=[0]
#我的主武器序号
mainweapon=0
#把所有武器放进我的包裹
for num in mineweaponnum:
    minelist.append({'name':allweapon[num].name,'category':allweapon[num].category,'quality':allweapon[num].quality,'note':allweapon[num].note})
#计算主武器伤害
damage=allweapon[mainweapon].damage
minelist.append({'name':'体力药水','category':'药水','quality':'恢复20体力','note':'用来测试的药水'})

#商店货架
yourlist=[]
#将所有武器放进商店
for num in allweapon:
    yourlist.append({'name':allweapon[num].name,'category':allweapon[num].category,\
                     'quality':allweapon[num].quality,'note':allweapon[num].note,\
                     'price':allweapon[num].price})
yourlist.append({'name':'体力药水','category':'药水',\
                     'quality':'恢复20体力','note':'恢复20体力',\
                     'price':'30'})
def shop():       #我的包裹
   global yourlist,allweapon,yourtree,you
   you= Tk()  # 导入tkinter中的tk模块
   you.title('商店系统')
   you.geometry('460x160+1020+100')
   head_indices=['name','category','quality','note','price']
   yourtree = ttk.Treeview(you, show="headings", height=8, columns=head_indices)
   yourvbar = ttk.Scrollbar(you, orient=tkinter.VERTICAL, command=yourtree.yview)
   yourtree.configure(yscrollcommand=yourvbar.set)
   yourtree.grid(row=0, column=0, sticky=tkinter.NSEW, ipadx=5)
   yourvbar.grid(row=0, column=1, sticky=tkinter.NS)
   yourtree.heading("name", text = "名称",anchor='center')
   yourtree.heading("category", text = "类别",anchor='center')
   yourtree.heading("quality", text = "属性",anchor='center')
   yourtree.heading("note", text = "备注",anchor='center')
   yourtree.heading("price", text = "价格",anchor='center')   
   yourtree.column('name', width=60, anchor='center')
   yourtree.column('category', width=95, anchor='center')
   yourtree.column('quality', width=95, anchor='center')   
   yourtree.column('note', width=95, anchor='center')
   yourtree.column('price', width=95, anchor='center')   
   yourtree.bind('<<TreeviewSelect>>', yourtreeClick) 
   
   i=0
   for v in yourlist:
     yourtree.insert('', i, values = (v.get("name"), v.get("category"), v.get("quality"),v.get('note'),v.get('price')))
     i += 1

def yourtreeClick(event):  # 单击
    global yourtree,minetree,yourlist,minelist,you,money,allweapon,text4,msg4
    print(yourtree.selection()[0][1:4])
    for item in yourtree.selection():
        item_text = yourtree.item(item, "values")
        ret=askquestion (title='购买',message='是否购买 价格为：'+str(item_text[4]))
        if ret==YES:
            if money>=int(item_text[4]):
                showinfo(title='提示',message='购买成功')
                if item_text[1]=='武器':
                    for key in allweapon.keys():
                        if allweapon[key].name==item_text[0]:
                        
                            mineweaponnum.append(key)
                            minelist.append({'name':allweapon[key].name,'category':\
                                         allweapon[key].category,'quality':\
                                         allweapon[key].quality,'note':\
                                         allweapon[key].note})
                            money=money-int(item_text[4])
                            text4='金币'+str(money)

                if item_text[1]=='药水':
                    minelist.append({'name':item_text[0],'category':\
                    item_text[1],'quality':\
                    item_text[2],'note':\
                    item_text[3]})
                    money=money-int(item_text[4])
                    text4='金币'+str(money)
                msg4.configure(text=text4)
                me.destroy()
                mine()            
            else :showinfo(title='提示',message='金币不足')

                    




def mine():       #我的包裹
   global minelist,allweapon,mainweapon,minetree,me
   me= Tk()  # 导入tkinter中的tk模块
   me.title('个人物品')
   me.geometry('460x160+1020+300')
   head_indices=['name','category','quality','note']
   minetree = ttk.Treeview(me, show="headings", height=8, columns=head_indices)
   minevbar = ttk.Scrollbar(me, orient=tkinter.VERTICAL, command=minetree.yview)
   minetree.configure(yscrollcommand=minevbar.set)
   minetree.grid(row=0, column=0, sticky=tkinter.NSEW, ipadx=5)
   minevbar.grid(row=0, column=1, sticky=tkinter.NS)
   minetree.heading("name", text = "名称",anchor='center')
   minetree.heading("category", text = "类别",anchor='center')
   minetree.heading("quality", text = "属性",anchor='center')
   minetree.heading("note", text = "备注",anchor='center')
   minetree.column('name', width=80, anchor='center')
   minetree.column('category', width=115, anchor='center')
   minetree.column('quality', width=115, anchor='center')   
   minetree.column('note', width=115, anchor='center')
   minetree.bind('<<TreeviewSelect>>', minetreeClick) 
   
   i=0
   for v in minelist:
     minetree.insert('', i, values = (v.get("name"), v.get("category"), v.get("quality"),v.get('note')))
     i += 1


def minetreeClick(event):  # 单击
    global minetree,minelist,me,energy,damage,mainweapon,text2
    print(minetree.selection()[0][1:4])
    for item in minetree.selection():
        item_text = minetree.item(item, "values")
        if item_text[1]=='药水':
            ret=askquestion (title='药水',message='是否饮用')
            if ret==YES:
                showinfo(title='提示',message='HP+20')
                temp=int(minetree.selection()[0][1:4])-1
                print(temp)
                minelist.pop(temp)
                minetree.delete(item)
                energy+=20
                msg3.configure(text='体力值:'+str(energy))
        if item_text[1]=='武器':
            ret=askquestion (title='武器',message='是否装备成为主武器')
            if ret==YES:
                showinfo(title='提示',message='装备成功')
                for key in allweapon.keys():
                    if allweapon[key].name==item_text[0]:
                        print(key)
                        mainweapon=key
                        damage=allweapon[mainweapon].damage
                        text2='当前武器:'+allweapon[mainweapon].name
                        msg2.configure(text=text2)
                        

game=Tk()
game.title('打地鼠')
game.geometry('1016x604+0+0')
game.configure(bg='LightGreen')
#设置窗口模块
game.frame_game=tkinter.Frame(width=600,height=500)
game.frame_msg=tkinter.Frame(width=400,height=600,bg='LightGreen')
game.frame_top=tkinter.Frame(width=1000,height=100)
game.frame_msg2=tkinter.Frame(width=400,height=600,bg='LightGreen')
game.frame_game.grid(row=1, column=1, padx=0)
game.frame_msg.grid(row=0, column=0, rowspan=2)
game.frame_top.grid(row=0, column=1, padx=0)
game.frame_msg2.grid(row=0, column=2, padx=0,rowspan=2)
#头部信息
topmsg=Label(game.frame_top,text='当前关卡:测试关卡',width=50,height=3,relief='raised',\
             bg='tan',font=('黑体',13))
topmsg.grid(row=0,column=0)
#老鼠的图标
pic1= PhotoImage(file='mice1.gif')
pic2= PhotoImage(file='mice2.gif')
pic3= PhotoImage(file='mice3.gif')
#全部老鼠种类
allmice={0:['普通鼠','伤害为:1','最常见的老鼠','1','1','3',pic1],1:\
           ['精英鼠','伤害为:3','精英老鼠','3','5','10',pic2],2:\
         ['鼠王','伤害为:6','老鼠王','6','20','50',pic3]}

#老鼠类
class mouce():
    def __init__(self,name,quality,note,damage,hp,award,picture):
        self.name=name
        self.category='老鼠'
        self.quality=quality
        self.note=note
        self.damage=int(damage)
        self.hp=int(hp)
        self.award=int(award)
        self.picture=picture

#将全部老鼠实例化
for mou in allmice.keys():
    allmice[mou]=mouce(allmice[mou][0],allmice[mou][1],\
                           allmice[mou][2],allmice[mou][3],\
                           allmice[mou][4],allmice[mou][5],allmice[mou][6])
class place():
    dirt_text='土块'
    def __init__(self,i,j):
        self.hp=-1
        self.i=i
        self.j=j
        self.label=Label(game.frame_game,text=self.dirt_text,width=10,height=5,\
                         relief='raised',bg='Sienna')
        self.label.grid(row=self.i,column=self.j)
        self.kind='土地'
    def back(self):
        self.warnlabel.grid_forget()

    def intomice(self,i):
        #global b
        self.micelabel=Label(game.frame_game,image=allmice[i].picture,width=60,height=60,relief='raised',bg='yellow')
        self.micelabel.bind("<Button-1>", self.hit)
        self.micelabel.grid(row=self.i,column=self.j)
        #print(self.i,self.j)
        self.hp=allmice[i].hp
        self.fullhp=allmice[i].hp
        self.money=allmice[i].award
        self.kind=allmice[i].name
        
    def hit(self,event):
        global money,damage
        self.hp-=damage
        text1=str(self.kind)+'HP:'+str(self.hp)+'/'+str(self.fullhp)
        msg1.configure(text=text1)
        self.timer=threading.Timer(0,hitsound)
        self.timer.start()
        
        self.micelabel.update()
        if self.hp<=0:
            text1='击杀+1,金币+'+str(self.money)
            msg1.configure(text=text1)
            self.micelabel.grid_forget()
            self.micelabel.update()
            money+=self.money
            text4='当前金币数'+str(money)
            msg4.configure(text=text4)
            self.kind='土地'
        
    def warning(self,i):
        tune=300
        for isk in range(5):
            winsound.Beep(tune,100)
            self.warnlabel=Label(game.frame_game,bitmap='warning',width=50,height=50,relief='raised',bg='yellow')
            self.warnlabel.grid(row=self.i,column=self.j)
            self.warnlabel.update()
            time.sleep(0.2)
            self.back()
            self.warnlabel.update()
            time.sleep(0.2)
            tune+=30
        self.intomice(i)

def warn(warnplace,warnkind):
        global timer1
        timer1.cancel()
        tune=300
        for isk in range(5):
            winsound.Beep(tune,100)
            for p in warnplace:
                b[p].warnlabel=Label(game.frame_game,bitmap='warning',width=50,height=50,relief='raised',bg='yellow')
                b[p].warnlabel.grid(row=b[p].i,column=b[p].j)
                b[p].warnlabel.update()
            time.sleep(0.2)
            for q in warnplace:
                b[q].back()
                b[q].warnlabel.update()
            time.sleep(0.2)
            tune+=30
        print('运行完成')
        timer1=threading.Timer(1,hurt)
        timer1.start()
        kd=0
        #b[1].intomice(0)
        for r in warnplace:
            rd=warnkind[kd]
            print(rd)
            b[r].intomice(rd)
            kd+=1
            
'''
        for r in warnplace:
            b[r].intomice(i)
'''            
def turn(event):
    global text1,msg1
    text1='正在生成金币鼠'
    msg1.configure(text=text1)
    b[5].warning(1)

'''              
def turn2(event):
    global text1,msg1
    text1='正在生成金币鼠'
    msg1.configure(text=text1)
    b[6].warning(1)    
    #timer.start()

    #print(msg1)
'''    


celltotal=cell*cell
for i in range(celltotal):
    b.append(i)
for i in range(cell):
    for j in range(cell):
        b[i*cell+j]=place(i,j)


test=Label(game.frame_msg2,text='老鼠',bitmap='warning',width=100,height=50,relief='raised',bg='brown')
test.grid(row=cell-3,column=0,sticky='wN',columnspan=2)
test.bind("<Button-1>", turn)



def openmine(event):
    mine()

def openshop(event):
    shop()

text1=''
text2='当前武器:'+allweapon[mainweapon].name
text3='体力值:'+str(energy)
text4='当前金币数'+str(money)
text5='索引信息'
#kongge1=Label(game.frame_msg,width=1,height=4,bg='LightGreen')
#kongge1.grid(row=0,column=0)
kongge2=Label(game.frame_msg,width=34,height=31,bg='LightGreen')
kongge2.grid(row=1,column=0)
msg1=Label(game.frame_msg2,text=text1,width=30,height=4,relief='raised',bg='Tan',font=("华文行楷"),fg="green")
msg2=Label(game.frame_msg,text=text2,width=31,height=4,relief='raised',bg='saddlebrown',font=(" 微软雅黑",12),fg="linen")
msg3=Label(game.frame_msg2,text=text3,width=25,height=4,relief='raised',\
           bg='tan',font=("华文行楷",13),fg='#DC143C')
msg4=Label(game.frame_msg2,padx=0,text=text4,width=20,height=3,relief='raised',\
           bg='grey',font=("华文行楷",11),fg="gold")
msg5=Label(game.frame_msg2,text=text5,width=30,height=3,relief='raised',\
           bg='Tan',font=("华文行楷"),fg='Sienna')
msg1.grid(row=cell-1,column=0,columnspan=3)
msg2.grid(row=cell,column=0,sticky='N')
msg3.grid(row=cell+1,column=1,columnspan=2,sticky='SE')
msg4.grid(row=cell,column=1,columnspan=2,sticky='SE')
msg5.grid(row=0,column=0,columnspan=3,sticky='EN',ipady=1)
tubiao1=Label(game.frame_msg2,text='商店',width=10,height=3,\
                   relief='raised',bg='Tan',font=("华文行楷",12),fg="green")
tubiao1.grid(row=1,column=2,sticky='E')
tubiao1.bind("<Button-1>", openshop)
tubiao2=Label(game.frame_msg2,text='我的物品',width=10,height=3,\
                   relief='raised',bg='Tan',font=("华文行楷",12),fg="green")
tubiao2.grid(row=2,column=2,sticky='E')
tubiao2.bind("<Button-1>", openmine)
kongge3=Label(game.frame_msg2,width=5,height=4,bg='LightGreen')
kongge3.grid(row=cell+1,column=0)
kongge4=Label(game.frame_msg2,width=10,height=2,bg='LightGreen')
kongge4.grid(row=cell,column=0)
kongge5=Label(game.frame_msg2,width=30,height=9,bg='LightGreen')
kongge5.grid(row=cell-2,column=0,columnspan=3)
#全场计老鼠扣血函数


def hurt():
    global energy,micerest
    num=0
    hptext=''
    for i in range(cell):
        for j in range(cell):
            if b[i*cell+j].kind=='普通鼠':
                num+=1
            elif b[i*cell+j].kind=='精英鼠':
                num+=3
            elif b[i*cell+j].kind=='鼠王':
                num+=6    
                
    energy-=num
    if num!=0:
        hptext='('+str(-1*num)+')'
        msg3.configure(text=hptext+'体力值:'+str(energy))
        #micerest='yes'
    else:
        msg3.configure(text=hptext+'体力值:'+str(energy))
        #print(micerest)
    timer1=threading.Timer(2,hurt)
    timer1.start()



def hitsound():
     winsound.Beep(1000,70)
         

#mine()
#shop()
timer1=threading.Timer(2,hurt)
timer1.start()
#time_total=random.randint(1,cell*cell) #随机决定本次共刷新多少个老鼠
def time_count(event):
    time_total=random.randint(1,36)
    time_place=random.sample(range(0,cell*cell),time_total)
    time_kind=[]
    print(time_place)
    for i in range(len(time_place)):
        kkd=random.choice('00000000000112')    #配置老鼠类的刷新概率
        time_kind.append(int(kkd))
    print(time_kind)    
    warn(time_place,time_kind)
    

stage=0
test2=Label(game.frame_msg2,text='进入关卡',width=10,height=5,relief='raised',\
            bg='brown',font=(9))
test2.grid(row=cell-3,column=2,sticky='E')
test2.bind("<Button-1>", time_count)

def stageturn(i,j):
    global text1,msg1
    text1='正在生成精英鼠'
    msg1.configure(text=text1)
    b[i].warning(j)

def stage1_print(str):
    msg5.configure(text=str)
    winsound.Beep(300,300)
'''  
def stage1():
    timer = threading.Timer(1.5, stage1_print,['欢迎来打地鼠！'])
    timer.start()    
    timer = threading.Timer(3, stage1_print,['你是新来的对吧!'])
    timer.start()
    timer = threading.Timer(4.5, stage1_print,['来进行一次简单的打地鼠训练'])
    timer.start()
    timer = threading.Timer(6, stage1_print,['将为你释放一只小鼠'])
    timer.start()
    timer = threading.Timer(7.5, stage1_print,['他有1点血'])
    
    timer.start()
    timer = threading.Timer(9, stage1_print,['闪烁后敲击它一次！'])
    timer.start()
    timer = threading.Timer(10, stageturn,[5,0])
    timer.start()
'''

def stage_grow():
    global micerest
    if micerest=='yes':
        timer=threading.Timer(1,stage_grow)
        timer.start()
    else:
        timer=threading.Timer(0,winsound.Beep,[1400,300])
        timer.start()
        stage1_2()
        

def stage_grow2(i):
    global energy
    if energy!=i+20:
        timer=threading.Timer(1,stage_grow2,[i])
        timer.start()
    else:
        timer=threading.Timer(0,winsound.Beep,[1400,300])
        timer.start()
        stage1_3()

def stage_grow3():
    global mainweapon
    if mainweapon!=2:
        timer=threading.Timer(1,stage_grow3)
        timer.start()
    else:
        timer=threading.Timer(0,winsound.Beep,[1400,300])
        timer.start()
        stage1_4()
    

def stage1_1():
    global stage
    stage=1.1
    topmsg.configure(text='新手训练1-1')
    timer = threading.Timer(1, stage1_print,['欢迎来打地鼠！'])
    timer.start()
    timer = threading.Timer(2, stage1_print,['你是新来的对吧!'])
    timer.start()
    timer = threading.Timer(3, stage1_print,['来进行一次简单的打地鼠训练'])
    timer.start()
    timer = threading.Timer(4, stage1_print,['将为你释放一只精英鼠'])
    timer.start()
    timer = threading.Timer(5, stage1_print,['他有5点血'])
    timer.start()
    timer = threading.Timer(6, stage1_print,['闪烁后敲击它5次！'])
    timer.start()
    timer = threading.Timer(7, stageturn,[5,1])
    timer.start()
    
    timer=threading.Timer(12,stage_grow)
    timer.start()

def stage1_2():
    global energy,stage
    stage=1.2
    msg5.configure(text='干得漂亮')
    topmsg.configure(text='新手训练1-2  ')
    now=100-energy
    timer = threading.Timer(1, stage1_print,['老鼠存在于土地上的时候'])
    timer.start()
    timer = threading.Timer(2, stage1_print,['将会扣除你的血量'])
    timer.start()   
    timer = threading.Timer(3, stage1_print,['刚才你一共扣了'+str(now)+'点血'])
    timer.start()
    timer = threading.Timer(5, stage1_print,['接下来为您展示体力的恢复方法'])
    timer.start()
    timer = threading.Timer(6, stage1_print,['点击我的物品打开物品栏'])
    timer.start()
    timer = threading.Timer(8, stage1_print,['点击药水并引用它'])
    timer.start()
    stage_grow2(energy)

def stage1_3():
    global stage
    stage=1.3
    msg5.configure(text='干得漂亮')
    topmsg.configure(text='新手训练1-3  ')
    timer = threading.Timer(1, stage1_print,['现在你有110金币'])
    timer.start()
    timer = threading.Timer(2, stage1_print,['购买武器可造成更多伤害！'])
    timer.start()
    timer = threading.Timer(3.5, stage1_print,['点击商店购买铁剑'])
    timer.start()
    timer = threading.Timer(5, stage1_print,['购买后于物品中点击将铁剑装备'])
    timer.start()
    stage_grow3()

def stage1_4():
    global stage
    stage=1.4
    msg5.configure(text='干得漂亮')
    topmsg.configure(text='新手训练1-4')
    timer = threading.Timer(1, stage1_print,['现在你可以造成更高伤害!'])
    timer.start()
    timer = threading.Timer(2, stage1_print,['你已经了解了基本流程'])
    timer.start()
    timer = threading.Timer(3, stage1_print,['未知惊喜就在后续关卡'])
    timer.start()
    timer = threading.Timer(4, stage1_print,['土地由你守护！'])
    timer.start()
    timer = threading.Timer(5, stage1_print,['前程似锦！'])
    timer.start()
stage1_1()
mainloop()

