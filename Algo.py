from tkinter import *
from os import read
import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

from prim import prim2
from kruskal import Kruskal
from dijkstra import dijkstra
from bellmanford import BellmanFord
from floydwarshall import floydWarshall
from boruvka import Boruvka

front='#0d05fa'
back='#8ae9eb'
design='#f5c107'
nodes=defaultdict(list)

window1=""
window2=""
window3=""
window4=""
window5=""
window6=""
window7=""
count=0

class AdjList:
  def __init__(self,vertices):
      self.V=vertices
      self.graph=defaultdict(list)
  def addEdge(self,u,v,w):
        newNode=[v,w]
        self.graph[u].insert(0,newNode)
  
        newNode=[u,w]
        self.graph[v].insert(0,newNode)

class AdjMat:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)]
                    for row in range(vertices)]

class EdgeList:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

def After_A_G(result):                      # A General Function to Print All After Applied Algorithm's Graphs
    global count
    Gr=nx.Graph()
    for[p,p1] in nodes.items():
        x,y=p1[0]
        Gr.add_node(p,pos=(x,y))
        print(result)
  
    for u,v,w in result:
        Gr.add_edge(u,v,weight=w)
        count+=w
  
    pos=nx.get_node_attributes(Gr,'pos')
    labels=nx.get_edge_attributes(Gr,'weight')
    nx.draw_networkx_edge_labels(Gr,pos,edge_labels=labels)
    nx.draw(Gr,pos,with_labels=True)
    print('Cost is: ',count)
    plt.show()

def get_Prim(flag):
    f=open("input20.txt")
    reading=f.readline()
    BF=nx.Graph()               # Before Algo Graph
    AM=AdjMat(int(reading))     # Matrix to implement this Algo
    
    for i in range(0,int(reading)):
        y=f.readline().split()
        node=[float(i) for i in y]
        vertice=node[0]
        x_cord=node[1]
        y_cord=node[2]
        print(vertice,x_cord,y_cord)
        BF.add_node(vertice,pos=(x_cord,y_cord))
        nodes[vertice].append([x_cord,y_cord])

    while True:
        edgeLine=f.readline().split()
        if(len(edgeLine)==0):
            break
        u=int(edgeLine[0])
        n=0
        while n<len(edgeLine)-1:
            v=int(edgeLine[n+1])
            cost=float(edgeLine[n+3])
            cost=cost/10000000
            n=n+4
            BF.add_edge(u,v,weight=cost)
            BF.add_edge(v,u,weight=cost)

            AM.graph[u][v]=cost
            AM.graph[v][u]=cost

    if flag==0:
        pos=nx.get_node_attributes(BF,'pos')
        labels=nx.get_edge_attributes(BF,'weight')
        nx.draw_networkx_edge_labels(BF,pos,edge_labels=labels)
        nx.draw(BF,pos,with_labels=True)
        plt.show()
    elif flag==1:
        result=prim2(AM.graph,AM.V)
        After_A_G(result)                # After Algo Graph

def Primm():
    global window1
    window1=Toplevel(root)
    window1['bg']=design
    window1.geometry("700x600")
    window1.title("Prims")
    lbl=Label(window1,text="Prim's Minimum Spanning Tree Algorithm",width=50,fg=front,bg='#82ffc7')
    lbl['font']=("TimesNewRoman",20)
    lbl.pack()

    btn3=Button(window1,text="Input",fg=front,bg=back,command=lambda:get_Prim(0))
    btn3.pack(padx=20,pady=20)
    btn10=Button(window1,text="Output",fg=front,bg=back,command=lambda:get_Prim(1))
    btn10.pack(padx=20,pady=20)
    btn2=Button(window1,text="Close Me",fg=front,bg=back,command=lambda:window1.destroy())
    btn2.pack(padx=20,pady=20)

def get_Kruskal(flag):
    f=open("input30.txt")
    reading=f.readline()
    BF=nx.Graph()               # Before Algo Graph
    EL=EdgeList(int(reading))   # Edge List to implement this Algo
    
    for i in range(0,int(reading)):
        y=f.readline().split()
        node=[float(i) for i in y]
        vertice=node[0]
        x_cord=node[1]
        y_cord=node[2]
        print(vertice,x_cord,y_cord)
        BF.add_node(vertice,pos=(x_cord,y_cord))
        nodes[vertice].append([x_cord,y_cord])

    while True:
        edgeLine=f.readline().split()
        if(len(edgeLine)==0):
            break
        u=int(edgeLine[0])
        n=0
        while n<len(edgeLine)-1:
            v=int(edgeLine[n+1])
            cost=float(edgeLine[n+3])
            cost=cost/10000000
            n=n+4
            BF.add_edge(u,v,weight=cost)
            BF.add_edge(v,u,weight=cost)

            EL.addEdge(u,v,cost)
            EL.addEdge(v,u,cost)

    if flag==0:
        pos=nx.get_node_attributes(BF,'pos')
        labels=nx.get_edge_attributes(BF,'weight')
        nx.draw_networkx_edge_labels(BF,pos,edge_labels=labels)
        nx.draw(BF,pos,with_labels=True)
        plt.show()
    elif flag==1:
        k=Kruskal(EL.V)
        k.graph=EL.graph
        result=k.KruskalMST()
        After_A_G(result)            # After Algo Graph

def Kruskall():
    global window2
    window2=Toplevel(root)
    window2['bg']=design
    window2.geometry("700x600")
    window2.title("Kruskal")
    lbl=Label(window2,text="Kruskal's Minimum Spanning Tree Algorithm",width=50,fg=front,bg='#82ffc7')
    lbl['font']=("TimesNewRoman",20)
    lbl.pack()

    btn3=Button(window2,text="Input",fg=front,bg=back,command=lambda:get_Kruskal(0))
    btn3.pack(padx=20,pady=20)
    btn10=Button(window2,text="Output",fg=front,bg=back,command=lambda:get_Kruskal(1))
    btn10.pack(padx=20,pady=20)
    btn2=Button(window2,text="Close Me",fg=front,bg=back,command=lambda:window2.destroy())
    btn2.pack(padx=20,pady=20)

def get_Dijkstra(flag):
    f=open("input20.txt")
    reading=f.readline()
    BF=nx.Graph()               # Before Algo Graph
    AL=AdjList(int(reading))    # Adjacency list to implement this Algo
    
    for i in range(0,int(reading)):
        y=f.readline().split()
        node=[float(i) for i in y]
        vertice=node[0]
        x_cord=node[1]
        y_cord=node[2]
        print(vertice,x_cord,y_cord)
        BF.add_node(vertice,pos=(x_cord,y_cord))
        nodes[vertice].append([x_cord,y_cord])

    while True:
        edgeLine=f.readline().split()
        if(len(edgeLine)==0):
            break
        u=int(edgeLine[0])
        n=0
        while n<len(edgeLine)-1:
            v=int(edgeLine[n+1])
            cost=float(edgeLine[n+3])
            cost=cost/10000000
            n=n+4
            BF.add_edge(u,v,weight=cost)
            BF.add_edge(v,u,weight=cost)

            AL.addEdge(u,v,cost)

    if flag==0:
        pos=nx.get_node_attributes(BF,'pos')
        labels=nx.get_edge_attributes(BF,'weight')
        nx.draw_networkx_edge_labels(BF,pos,edge_labels=labels)
        nx.draw(BF,pos,with_labels=True)
        plt.show()
    elif flag==1:
        result=dijkstra(AL,0)        # Starting Node
        After_A_G(result)            # After Algo Graph

def Dijkstraa():
    global window3
    window3=Toplevel(root)
    window3['bg']=design
    window3.geometry("700x600")
    window3.title("DSPA")
    lbl=Label(window3,text="Dijkstra Shortest Path Algorithm",width=50,fg=front,bg='#82ffc7')
    lbl['font']=("TimesNewRoman",20)
    lbl.pack()

    btn3=Button(window3,text="Input",fg=front,bg=back,command=lambda:get_Dijkstra(0))
    btn3.pack(padx=20,pady=20)
    btn10=Button(window3,text="Output",fg=front,bg=back,command=lambda:get_Dijkstra(1))
    btn10.pack(padx=20,pady=20)
    btn2=Button(window3,text="Close Me",fg=front,bg=back,command=lambda:window3.destroy())
    btn2.pack(padx=20,pady=20)

def get_Bell_Ford(flag):
    f=open("input50.txt")
    reading=f.readline()
    BF=nx.Graph()               # Before Algo Graph
    EL=EdgeList(int(reading))   # Edge List to implement this Algo
    
    for i in range(0,int(reading)):
        y=f.readline().split()
        node=[float(i) for i in y]
        vertice=node[0]
        x_cord=node[1]
        y_cord=node[2]
        print(vertice,x_cord,y_cord)
        BF.add_node(vertice,pos=(x_cord,y_cord))
        nodes[vertice].append([x_cord,y_cord])

    while True:
        edgeLine=f.readline().split()
        if(len(edgeLine)==0):
            break
        u=int(edgeLine[0])
        n=0
        while n<len(edgeLine)-1:
            v=int(edgeLine[n+1])
            cost=float(edgeLine[n+3])
            cost=cost/10000000
            n=n+4
            BF.add_edge(u,v,weight=cost)
            BF.add_edge(v,u,weight=cost)

            EL.addEdge(u,v,cost)
            EL.addEdge(v,u,cost)

    if flag==0:
        pos=nx.get_node_attributes(BF,'pos')
        labels=nx.get_edge_attributes(BF,'weight')
        nx.draw_networkx_edge_labels(BF,pos,edge_labels=labels)
        nx.draw(BF,pos,with_labels=True)
        plt.show()
    elif flag==1:
        result=BellmanFord(EL,0)
        After_A_G(result)            # After Algo Graph

def Bell_Fordd():
    global window4
    window4=Toplevel(root)
    window4['bg']=design
    window4.geometry("700x600")
    window4.title("BFSPA")
    lbl=Label(window4,text="Bellman-Ford Shortest Path Algorithm",width=50,fg=front,bg='#82ffc7')
    lbl['font']=("TimesNewRoman",20)
    lbl.pack()

    btn3=Button(window4,text="Input",fg=front,bg=back,command=lambda:get_Bell_Ford(0))
    btn3.pack(padx=20,pady=20)
    btn10=Button(window4,text="Output",fg=front,bg=back,command=lambda:get_Bell_Ford(1))
    btn10.pack(padx=20,pady=20)
    btn2=Button(window4,text="Close Me",fg=front,bg=back,command=lambda:window4.destroy())
    btn2.pack(padx=20,pady=20)

def get_Floyd_War(flag):
    f=open("input20.txt")
    reading=f.readline()
    BF=nx.Graph()                   # Before Algo Graph
    AM=AdjMat(int(reading))         # By Using Matrix
    
    for i in range(0,int(reading)):
        y=f.readline().split()
        node=[float(i) for i in y]
        vertice=node[0]
        x_cord=node[1]
        y_cord=node[2]
        print(vertice,x_cord,y_cord)
        BF.add_node(vertice,pos=(x_cord,y_cord))
        nodes[vertice].append([x_cord,y_cord])

    while True:
        edgeLine=f.readline().split()
        if(len(edgeLine)==0):
            break
        u=int(edgeLine[0])
        n=0
        while n<len(edgeLine)-1:
            v=int(edgeLine[n+1])
            cost=float(edgeLine[n+3])
            cost=cost/10000000
            n=n+4
            BF.add_edge(u,v,weight=cost)
            BF.add_edge(v,u,weight=cost)

            AM.graph[u][v]=cost
            AM.graph[v][u]=cost

    if flag==0:
        pos=nx.get_node_attributes(BF,'pos')
        labels=nx.get_edge_attributes(BF,'weight')
        nx.draw_networkx_edge_labels(BF,pos,edge_labels=labels)
        nx.draw(BF,pos,with_labels=True)
        plt.show()
    elif flag==1:
        for i in range(0,AM.V):                    # no edges means INF
            for j in range(0,AM.V):
                if(AM.graph[i][j]==0):
                    AM.graph[i][j]=sys.maxsize     # sys.maxsize=999999999
        
        result=floydWarshall(AM)

        for i in range(0,AM.V):                    # Printing After Algo Result in Matrix Form
            for j in range(0,AM.V):
                if(result[i][j]==sys.maxsize):
                    print("INF ",end="")
                elif result[i][j]!=sys.maxsize:
                    print(int(result[i][j])," ",end=" ")
            print("")

def Floyd_Warr():
    global window5
    window5=Toplevel(root)
    window5['bg']=design
    window5.geometry("700x600")
    window5.title("APSPA")
    lbl=Label(window5,text="Floyd–Warshall All Pairs Shortest Path Algorithm",width=50,fg=front,bg='#82ffc7')
    lbl['font']=("TimesNewRoman",20)
    lbl.pack()

    btn3=Button(window5,text="Input",fg=front,bg=back,command=lambda:get_Floyd_War(0))
    btn3.pack(padx=20,pady=20)
    btn10=Button(window5,text="Output",fg=front,bg=back,command=lambda:get_Floyd_War(1))
    btn10.pack(padx=20,pady=20)
    btn2=Button(window5,text="Close Me",fg=front,bg=back,command=lambda:window5.destroy())
    btn2.pack(padx=20,pady=20)

def get_LCC():
    f=open("input70.txt")
    reading=f.readline()
    BF=nx.Graph()           # Before Algo Graph
    
    for i in range(0,int(reading)):
        y=f.readline().split()
        node=[float(i) for i in y]
        vertice=node[0]
        x_cord=node[1]
        y_cord=node[2]
        print(vertice,x_cord,y_cord)
        BF.add_node(vertice,pos=(x_cord,y_cord))
      
    while True:
        edgeLine=f.readline().split()
        if(len(edgeLine)==0):
            break
        u=int(edgeLine[0])
        n=0
        while n<len(edgeLine)-1:
            v=int(edgeLine[n+1])
            cost=float(edgeLine[n+3])
            cost=cost/10000000
            n=n+4
            BF.add_edge(u,v,weight=cost)
            BF.add_edge(v,u,weight=cost)

    pos=nx.get_node_attributes(BF,'pos')
    labels=nx.get_edge_attributes(BF,'weight')
    nx.draw_networkx_edge_labels(BF,pos,edge_labels=labels)
    plt.figure(1)
    nx.draw(BF,pos,with_labels=True)

    gloobal=nx.average_clustering(BF)            #global
    print(gloobal)
    loocal=nx.clustering(BF)                     #local
    print(loocal) 
    
    plt.show()

def LCC():
    global window6
    window6=Toplevel(root)
    window6['bg']=design
    window6.geometry("700x600")
    window6.title("lcc")
    lbl=Label(window6,text="Local Clustering Coefficient in GT",width=50,fg=front,bg='#82ffc7')
    lbl['font']=("TimesNewRoman",20)
    lbl.pack()

    btn10=Button(window6,text="Input and Output(Terminal)",fg=front,bg=back,command=get_LCC)
    btn10.pack(padx=20,pady=20)
    btn2=Button(window6,text="Close Me",fg=front,bg=back,command=lambda:window6.destroy())
    btn2.pack(padx=20,pady=20)

def get_Boruvka(flag):
    f=open("input90.txt")
    reading=f.readline()
    BF=nx.Graph()               # Before Algo Graph
    EL=EdgeList(int(reading))   # the list required to implement this Algo
    
    for i in range(0,int(reading)):
        y=f.readline().split()
        node=[float(i) for i in y]
        vertice=node[0]
        x_cord=node[1]
        y_cord=node[2]
        print(vertice,x_cord,y_cord)
        BF.add_node(vertice,pos=(x_cord,y_cord))
        nodes[vertice].append([x_cord,y_cord])

    while True:
        edgeLine=f.readline().split()
        if(len(edgeLine)==0):
            break
        u=int(edgeLine[0])
        n=0
        while n<len(edgeLine)-1:
            v=int(edgeLine[n+1])
            cost=float(edgeLine[n+3])
            cost=cost/10000000
            n=n+4
            BF.add_edge(u,v,weight=cost)
            BF.add_edge(v,u,weight=cost)

            EL.addEdge(u,v,cost)
            EL.addEdge(v,u,cost)

    if flag==0:
        pos=nx.get_node_attributes(BF,'pos')
        labels=nx.get_edge_attributes(BF,'weight')
        nx.draw_networkx_edge_labels(BF,pos,edge_labels=labels)
        nx.draw(BF,pos,with_labels=True)
        plt.show()
    elif flag==1:
        b=Boruvka(EL.V)
        b.graph=EL.graph
        result=b.boruvkaMST()
        After_A_G(result)            # After Algo Graph

def Boruvkaa():
    global window7
    window7=Toplevel(root)
    window7['bg']=design
    window7.geometry("700x600")
    window7.title("Boruvka")
    lbl=Label(window7,text="Borůvka's Minimum Spanning Tree Algorithm",width=50,fg=front,bg='#82ffc7')
    lbl['font']=("TimesNewRoman",20)
    lbl.pack()

    btn3=Button(window7,text="Input",fg=front,bg=back,command=lambda:get_Boruvka(0))
    btn3.pack(padx=20,pady=20)
    btn10=Button(window7,text="Output",fg=front,bg=back,command=lambda:get_Boruvka(1))
    btn10.pack(padx=20,pady=20)
    btn2=Button(window7,text="Close Me",fg=front,bg=back,command=lambda:window7.destroy())
    btn2.pack(padx=20,pady=20)

root = Tk()

lbl2=Label(root,text="Welcome To ALGO Project",width=50,fg=front,bg='#82ffc7')
lbl2['font']=("TimesNewRoman",20)
lbl2.pack()
lbl1=Label(root,text="\"Graph Analysis\"",width=50,fg=front,bg='#82ffc7')
lbl1['font']=("TimesNewRoman",20)
lbl1.pack()

btn1=Button(root,text="1. Prims MST Algorithm",command=Primm,padx=10,pady=10,fg=front,bg=back)
btn1.pack(padx=10,pady=10)
btn2=Button(root,text="2. Kruskal MST Algorithm",command=Kruskall,padx=10,pady=10,fg=front,bg=back)
btn2.pack(padx=10,pady=10)
btn3=Button(root,text="3. Dijkstra Shortest Path Algorithm",command=Dijkstraa,padx=10,pady=10,fg=front,bg=back)
btn3.pack(padx=10,pady=10)
btn4=Button(root,text="4. Bellman-Ford Shortest Path Algorithm",command=Bell_Fordd,padx=10,pady=10,fg=front,bg=back)
btn4.pack(padx=10,pady=10)
btn5=Button(root,text="5. Floyd-Warshall Shortest Path Algorithm",command=Floyd_Warr,padx=10,pady=10,fg=front,bg=back)
btn5.pack(padx=10,pady=10)
btn6=Button(root,text="6. Local Clustering Coefficient in GT",command=LCC,padx=10,pady=10,fg=front,bg=back)
btn6.pack(padx=10,pady=10)
btn7=Button(root,text="7. Borůvka's MST Algorithm",command=Boruvkaa,padx=10,pady=10,fg=front,bg=back)
btn7.pack(padx=10,pady=10)
button_exit=Button(root,text="8. Exit",command=root.quit,padx=10,pady=10,fg=front,bg=back)
button_exit.pack(padx=10,pady=10)

root.geometry("700x600")
root.title("DA OF ALGORITHMS PROJECT")
root['bg']=design
root.mainloop()