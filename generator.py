import numpy as np
import random,sys,time
from PIL import Image

def cmds():
    args = sys.argv[1:]
    parms = ["SIZE","SZ","TICKNESS","T","PERCENTAGE","P","SOLUTION","S","BACKGROUNG","BG","SCOLOR","SC","PATHCOLOR","PC"]
    commands = {}
    for i in range(len(args)-1):
        if '--' in args[i] :
            cmd = args[i].replace("--","").upper()
            if cmd in parms:
                commands[cmd] = str(args[i+1])
        if '-' in args[i] :
            cmd = args[i].replace("-","").upper()
            if cmd in parms:
                commands[cmd] = str(args[i+1])
    if commands :
        return commands
    else :
        commands["H"] = "HELP STATMENT"
        return commands



def affecter(commands):
    #print(commands)
    size,tickness,per,sol_check,color,sol_color,p_color = 1010,10,100,False,[255,255,255],[255,0,0],[255,255,255]
    if 'H' not in commands:
        if 'SIZE' in commands or 'SZ' in commands :
            try :
                try : size = int(commands['SIZE'])
                except Exception : size = int(commands['SZ'])
            except ValueError:
                commands ={}
                commands['H'] = "HELP STATEMENT"
                return commands
        if 'TICKNESS' in commands or 'T' in commands :
            try :    
                try :tickness = int(commands['TICKNESS'])
                except Exception: tickness = int(commands['T'])
            except ValueError:
                commands ={}
                commands['H'] = "HELP STATEMENT"
                return commands

        if "PERCENTAGE" in commands or "P" in commands :
            try :
                try : per = float(commands['PERCENTAGE'])
                except Exception : per = float(commands['P'])
            except ValueError:
                commands ={}
                commands['H'] = "HELP STATEMENT"
                return commands

        if "SOLUTION" in commands or "S" in commands :
             
            try :
                if  commands['SOLUTION'].upper() in ['0','FALSE']:
                    sol_check = False 
                elif commands['SOLUTION'].upper() in ['1','TRUE']:
                    sol_check = True 
                else :
                    commands ={}
                    commands['H'] = "HELP STATEMENT"
                    return commands
            except Exception : 
                if  commands['S'].upper() in ['0','FALSE']:
                    sol_check = False 
                elif commands['S'].upper() in ['1','TRUE']:
                    sol_check = True
                else :
                    commands ={}
                    commands['H'] = "HELP STATEMENT"
                    return commands 

        if "BACKGROUNG" in commands or "BG" in commands :
            
            try : 
                color = str(commands['BACKGROUND']).split(",")
            except Exception : 
                color = str(commands['BG']).split(",")
            if len(color)>3 :
                commands ={}
                commands['H'] = "HELP STATEMENT"
                return commands 
            else :
                try :
                    for i in range(len(color)): 
                        color[i] = int(color[i])
                except ValueError :
                    commands ={}
                    commands['H'] = "HELP STATEMENT"
                    return commands 

        if "PATHCOLOR" in commands or "PC" in commands :
            
            try : 
                p_color = str(commands['PATHCOLOR']).split(",")
            except Exception : 
                p_color = str(commands['PC']).split(",")
            if len(color)>3 :
                commands ={}
                commands['H'] = "HELP STATEMENT"
                return commands 
            else :
                try :
                    for i in range(len(p_color)): 
                        p_color[i] = int(p_color[i])
                except ValueError :
                    commands ={}
                    commands['H'] = "HELP STATEMENT"
                    return commands 

        if "SCOLOR" in commands or "SC" in commands :
            try : 
                sol_color = str(commands['SCOLOR']).split(",")
            except Exception : 
                sol_color = str(commands['SC']).split(",")
            if len(color)>3 :
                commands ={}
                commands['H'] = "HELP STATEMENT"
                return commands 
            else :
                try :
                    for i in range(len(sol_color)): 
                        sol_color[i] = int(sol_color[i])
                except ValueError :
                    commands ={}
                    commands['H'] = "HELP STATEMENT"
                    return commands 
        return [size,tickness,per,sol_check,color,sol_color,p_color]
    else : return commands['H']

def frame(start,end,data):
    for i in range(min_size):

        if (0,i) == start:
            data[0][i] = white
        else:
            data[0][i] = black
    for i in range(min_size):
        if (min_size-1,i) == end:
            data[min_size-1][i] = white
        else:
            data[min_size-1][i] = black
    for i in range(1,min_size-1):
        data[i][0]=black
        data[i][min_size-1]=black
    return data

def lignes(min_size,data):
    lignes_w = []
    lignes_b = []
    for i in range(min_size//2):
        for j in range(min_size//2):
            data[j*2+1][i*2+1] = white
            data[i*2+1][j*2+1] = white
    return data

def white_nbs(point):
    nb = []
    if point[1]+2<min_size-1:
        if np.all(min_data[point[0]][point[1]+2] == white):
            nb.append((point[0],point[1]+2))
    if point[1]>2:
        if np.all(min_data[point[0]][point[1]-2] == white):
            nb.append((point[0],point[1]-2))
    if point[0]+2<min_size-1:
        if np.all(min_data[point[0]+2][point[1]] == white):
            nb.append((point[0]+2,point[1]))
    if point[0]>2:
        if np.all(min_data[point[0]-2][point[1]] == white):
            nb.append((point[0]-2,point[1]))
    return nb



def road_gen(start,last,lenght,visited,joints_passed):
    if lenght == 0:
        return [visited,joints_passed,last]
    if start not in visited :
        visited.append(start)
        if last :
            if last[0] == start[0] :
                min_data[start[0]][max(start[1],last[1])-1] = color
            if last[1] == start[1] :
                min_data[max(start[0],last[0])-1][start[1]] = color
        else :            
            last = start
            if last[0] == start[0] :
                min_data[start[0]][max(start[1],last[1])-1] = color
            if last[1] == start[1] :
                min_data[max(start[0],last[0])-1][start[1]] = color
        min_data[start[0]][start[1]] = color
        nb = list(set(white_nbs(start))-set(visited))
        if nb :
            if len(nb)>1:
                
                joints_passed.append(start)
            next = nb[random.randint(0,len(nb)-1)]
            if next[0] == start[0] :
                min_data[start[0]][max(start[1],next[1])-1] = color
            if next[1] == start[1] :
                min_data[max(start[0],next[0])-1][start[1]] = color
            return road_gen(next,start,lenght-1,visited,joints_passed)
            
        else:
            if joints_passed:
                last = start
                if start in joints_passed:
                    joints_passed.remove(start)
                try :start = joints_passed[-1]
                except : return [visited,joints_passed,last]
                nb = list(set(white_nbs(start))-set(visited))
                if nb :
                    next = nb[random.randint(0,len(nb)-1)]
                    if next[0] == start[0] :
                        min_data[start[0]][max(start[1],next[1])-1] = color
                    if next[1] == start[1] :
                        min_data[max(start[0],next[0])-1][start[1]] = color
                    return road_gen(next,last,lenght-1,visited,joints_passed)
                else :
                    return road_gen(start,'',lenght-1,visited,joints_passed)
                
    else :
        while joints_passed :
            last = joints_passed[-1]
            if sol_check :
                if sol[1] == 0 :
                    if sol[0] in visited and sol[0] == (end[0]-1,end[1]):
                        sol[0] = last

                if sol[0] == last:
                    sol[1] = len(joints_passed)
                if len(joints_passed)<sol[1]:
                    sol[1] =len(joints_passed)
                    sol[0] = last
                    min_data[sol[0][0]][sol[0][1]] = sol_color


            joints_passed.remove(joints_passed[-1])
            nb = list(set(white_nbs(last))-set(visited))
            if nb :
                next = nb[random.randint(0,len(nb)-1)]
                if next[0] == last[0] :
                    min_data[last[0]][max(last[1],next[1])-1] = color
                elif next[1] == last[1] :
                    min_data[max(last[0],next[0])-1][last[1]] = color
                return road_gen(next,last,lenght-1,visited,joints_passed)
        return [visited,joints_passed,last]

def louper(per):
    c = 0
    v,j,v2,j2=[],[],[],[]
    last = (start[0]+1,start[1])
    last2 = (end[0]-1,end[1])
    check = 0
    while len(v)<(min_size-2)**2:
        c += 1
        v= list(set(v2+v))
        per_act = len(v)/(min_size-2**2)
        if per< per_act:
            break
        sys.stdout.write('\rgenerated : ' +str(    float("{:.2f}".format(per_act))    )+"%")
        sys.stdout.flush()
        if check == 0:
            road= road_gen(last,'',900,v,j)
            #doad = road_gen(last2,'',900,v,j2)
            if road:
                if road[2]:
                    last = road[2]
                v= road[0]
                v = list(set(v))
                j = road[1]
            """if doad:
                if doad[2]:
                    last2 = doad[2]
                v2= doad[0]
                v2 = list(set(v))
                j = road[1]"""
            check = 1
        if j :
            road= road_gen(last,'',900,v,j)
        """if j2:
            doad = road_gen(last2,'',900,v,j2)"""
        if road:
            if road[2]:
                last = road[2]
            v= road[0]
            v = list(set(v))
            j = road[1]
        """if doad:
            if doad[2]:
                last2 = doad[2]
            v2= doad[0]
            v2 = list(set(v))
            j = road[1]"""
        if c == 30:
            pass
        if j == [] and j2==[]:
            break
    sys.stdout.write('\rgenerated : 100%   ')
    sys.stdout.flush()

def render():
    data_ = np.zeros((size,size,3))
    for i in range(size):
        for j in range(size):
            data_[i][j] = min_data[int(i//tickness)][int(j//tickness)]
    sys.stdout.write('\rRendering ...    ')
    sys.stdout.flush()
    PIL_image = Image.fromarray(np.uint8(data_)).convert('RGB').save("results.png")



if __name__=='__main__':
# affectation direct
    commands = cmds()
    values = affecter(commands)
    if 'H' in values:
        print(values['H'])
    else :
        size,tickness,per,sol_check,color,sol_color,p_color=values
        
        # Variables :
        min_size = int(size//tickness)
        min_data = np.zeros((min_size,min_size,3))
        start,end = (0,(random.randint(1,min_size//2)-1)*2+1),(min_size-1,(random.randint(1,min_size//2)-1)*2+1)
        red = sol_color
        white,black = color,np.array([0,0,0])
        sol =  [(end[0]-1,end[1]),0,True]
        min_data = frame(start,end,min_data)
        min_data= lignes(min_size,min_data)
        min_data[start[0]][start[1]] = white
        min_data[end[0]][end[1]] = white
        color = p_color
        message = "Generate Maze Of Size "+str(size)+"x"+str(size)
        start_ = time.time()
        sys.stdout.write(message+'\n')
        louper(per)
        render()
        dur = time.time()-start_
        sys.stdout.write("In : "+str(dur)+"s")






   

