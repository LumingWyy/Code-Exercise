#name:Wang Luming
#id:1710245

from PIL import Image,ImageDraw
import numpy as np


def find_min(W,D):
    u=W[0]
    for v in W:
        if D[u]>D[v]:
            u=v
    return(u)


def dijkstra(A,c,x,y):
    D={x:0}
    W=[x]
    P={}
    while W!=[]:
        u=find_min(W,D)
        W.remove(u)
        if u==y:
            break
        for v in A[u]:
            dv=D[u]+c(u,v)
            if not v in D or dv<D[v]:
                D[v]=dv
                P[v]=u
                W.append(v)
    if y in D:
        path=[y]
        target=P.get(y,-1)
        while target!=x:
            path.append(target)
            target=P.get(target,-1)
        return(path)
    else:
        return(None)


def binarize(file):
    img=Image.open(file)
    Img=img.convert('L')
    threshold=230
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    photo = Img.point(table, '1')
    return(photo)


def find_point(file):
    im = Image.open(file)
    im=im.convert('RGBA')
    draw = ImageDraw.Draw(im)
    (width, height) = im.size
    L = []
    for x in range(0, width):
        for y in range(0, height):
            (r,g,b,a) = im.getpixel((x,y))
            if (r,g,b) == (255, 0, 0):
                L.append([x,y])
    return(np.array(L))


def find_dist(index_origin,index_dict):
    A={}
    C={}
    step=np.array([[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]])
    dist=np.sqrt(np.sum(step**2,axis=1))
    for index1,i in enumerate(index_origin):
        Aconnect=[]
        for index2,j in enumerate(i+step):
            res=index_dict.get(tuple(j),-1)
            if res!=-1:
                Aconnect.append(res)
                C[(index1,res)]=dist[index2]
            else:
                pass
        else:
            A[index1]=Aconnect
    return(A,C)


def draw_line(file,path):
    im=Image.open(file)
    im=im.convert('RGB')
    draw = ImageDraw.Draw(im)
    draw.line(path, fill=(255, 0, 0), width=5)
    im.save("a.png")


start_end=find_point('input.png')

data=np.array(binarize('input.png'),dtype=np.int8)
data[np.transpose(start_end)[::-1].tolist()]=1

index_origin=np.argwhere(data==1)

point_origin=np.argwhere(data==0)

index_dict=dict([[tuple(value),index] for index,value in enumerate(index_origin)])

point_dict=dict([[tuple(value),index] for index,value in enumerate(point_origin)])

index_dict_re=dict([[index,tuple(reversed(value))] for index,value in enumerate(index_origin)])

A,C=find_dist(index_origin,index_dict)

res=dijkstra(A,lambda x,y:C[(x,y)],index_dict[tuple(start_end[0][::-1])],index_dict[tuple(start_end[1][::-1])])

path=[index_dict_re[i] for i in res]

draw_line('input.png',path)
