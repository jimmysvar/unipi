import random;
width= 10;
height= 10;
board=[];
def find_distance(xp,yp,xg,yg):
    if xplayer>xgoal:
        xdistance=xplayer-xgoal;
    else:
        xdistance=xgoal-xplayer;
    if yplayer>ygoal:
        ydistance=yplayer-ygoal;
    else:
        ydistance=ygoal-yplayer;
    return xdistance+ydistance;
for i in range(height):
    for j in range(width):
        board.append("0");
player=random.randint(0,99);
while 1:
    goal= random.randint(0,99);
    if goal!=player:break;
yplayer = player/10;
xplayer=player%10;
ygoal= goal/10;
xgoal=goal%10;
distance = find_distance(xplayer,yplayer,xgoal,ygoal);
count =0;
while distance!=0:
    print("Epilekste kateuthinsi. W gia pano, S gia katw, D gia deksia, A gia aristera.");
    a=raw_input();
    if a=="a":
        xplayer-=1;
    elif a=="d":
        xplayer+=1;
    elif a=="w":
        yplayer-=1;
    elif a=="s":
        yplayer+=1;
    distance = find_distance(xplayer,yplayer,xgoal,ygoal);
    print distance;
    count+=1;
print("Prospatheies");
print(count);
