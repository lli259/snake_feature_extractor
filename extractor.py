import sys
file_name=sys.argv[1]

'''
input format:
filled(1,4,1).
filled(3,10,76).
filled(8,10,9).
filled(10,10,88).
'''

class snake_graph_feature:
    def __init__(self,filename):
        lines=[]
        with open(filename,'r') as f:
            lines=f.readlines()
        self.allpoints=[]
        for i,l in enumerate(lines):
            tem_dic={}
            tup=l.split('(')[1].split(')')[0].split(',')
            tem_dic['x']=int(tup[0])
            tem_dic['y']=int(tup[1])
            tem_dic['v']=int(tup[2])
            self.allpoints.append(tem_dic)
    
    #value related
    def max_value(self):
        ret=-1
        for p in self.allpoints:
            if p['v']>ret:
                ret=p['v']
        return ret

    def min_value(self):
        ret=100000
        for p in self.allpoints:
            if p['v']<ret:
                ret=p['v']
        return ret


    #distance related
    def max_distance(self):
        ret=-1
        for ind1 in range(0,4):
            v1=self.allpoints[ind1]
            for ind2 in range(ind1+1,4):
                v2=self.allpoints[ind2]
                dis_d=abs(v1['x']-v2['x'])+abs(v1['y']-v2['y'])
                if dis_d>ret:
                    ret=dis_d
        return ret
    
    def min_distance(self):
        ret=100000
        for ind1 in range(0,4):
            v1=self.allpoints[ind1]
            for ind2 in range(ind1+1,4):
                v2=self.allpoints[ind2]
                dis_d=abs(v1['x']-v2['x'])+abs(v1['y']-v2['y'])
                if dis_d<ret:
                    ret=dis_d
        return ret

    def max_distance_x(self):
        ret=-1
        for ind1 in range(0,4):
            v1=self.allpoints[ind1]
            for ind2 in range(ind1+1,4):
                v2=self.allpoints[ind2]
                dis_d=abs(v1['x']-v2['x'])
                if dis_d>ret:
                    ret=dis_d
        return ret
    
    def min_distance_x(self):
        ret=100000
        for ind1 in range(0,4):
            v1=self.allpoints[ind1]
            for ind2 in range(ind1+1,4):
                v2=self.allpoints[ind2]
                dis_d=abs(v1['x']-v2['x'])
                if dis_d<ret:
                    ret=dis_d
        return ret

    def max_distance_y(self):
        ret=-1
        for ind1 in range(0,4):
            v1=self.allpoints[ind1]
            for ind2 in range(ind1+1,4):
                v2=self.allpoints[ind2]
                dis_d=abs(v1['y']-v2['y'])
                if dis_d>ret:
                    ret=dis_d
        return ret
    
    def min_distance_y(self):
        ret=100000
        for ind1 in range(0,4):
            v1=self.allpoints[ind1]
            for ind2 in range(ind1+1,4):
                v2=self.allpoints[ind2]
                dis_d=abs(v1['y']-v2['y'])
                if dis_d<ret:
                    ret=dis_d
        return ret

    #location
    def is_all_one_side(self):
        #both x one side or y one side
        ret=False
        allup=[p['y']<5 for p in self.allpoints]
        alldown=[p['y']>5 for p in self.allpoints]
        allleft=[p['x']<5 for p in self.allpoints]
        alldown=[p['x']>5 for p in self.allpoints]
        if sum(allup)==4 or sum(alldown)==4 or sum(allleft)==4 or sum(alldown)==4:
            ret=True
        if True:
            return 1
        else:
            return 0




    def number_in_corner(self):
        #to (1,1),(1,10),(10,1),(10,10) <=2 
        ret=0
        for p in self.allpoints:
            corner1=abs(p['x']-1)+abs(p['y']-1)
            corner2=abs(p['x']-10)+abs(p['y']-1)
            corner3=abs(p['x']-1)+abs(p['y']-10)
            corner4=abs(p['x']-10)+abs(p['y']-10)
            if corner1<=2 or corner2<=2 \
                or corner3<=2 or corner4<=2:
                ret+=1
        return ret
        
    #freedom 
    #one side distance/location diff: max(abs(p1['x']-p2['x']),abs(p1['y']-p2['y']))
    #if one side location diff of a,b is 2, and value diff is exactly 2, so 2-2=0, less ways to connect. 
    #if one side location diff of a,b is 2, but value diff is 20, so 20-2=18, more ways to go.
    #!!!!!
    #if one side location diff is < value diff, no way to 
    def calc_freedom(self,p1,p2):
        location_diff=max(abs(p1['x']-p2['x']),abs(p1['y']-p2['y']))
        value_diff=abs(p1['v']-p2['v'])
        return value_diff-location_diff


    def max_freedom(self):
        ret=-1
        for ind1 in range(0,4):
            p1=self.allpoints[ind1]
            for ind2 in range(ind1+1,4):
                p2=self.allpoints[ind2]
                density=self.calc_freedom(p1,p2)
                if density>ret:
                    ret=density
        return ret
    
    def min_freedom(self):
        ret=100000
        for ind1 in range(0,4):
            p1=self.allpoints[ind1]
            for ind2 in range(ind1+1,4):
                p2=self.allpoints[ind2]
                density=self.calc_freedom(p1,p2)
                if density<0:
                    print(p1,p2)
                if density<ret:
                    ret=density
        return ret
        

a=snake_graph_feature(file_name)
#print(a.max_freedom())
#print(a.min_freedom())
feature_name='max_value,min_value,max_distance,min_distance,max_distance_x,\
min_distance_x,max_distance_y,min_distance_y,is_all_one_side,\
number_in_corner,max_freedom,max_freedom'
feature_list=feature_name.split(',')

print(feature_name)

feature_v=''
for f in feature_list:
    func=getattr(a,f)
    v=func()
    #print(v)
    feature_v+=str(v)+","

feature_v=feature_v[:-1]

print(feature_v)
#distance related


'''
#deal with files
feature_name='max_value,min_value,max_distance,min_distance,max_distance_x,\
min_distance_x,max_distance_y,min_distance_y,is_all_one_side,\
number_in_corner,max_freedom,max_freedom'
feature_list=feature_name.split(',')

with('feature.csv','w') as f:
    f.write('inst,'+feature_name+'\n')

for file_name in files:
    a=snake_graph_feature(file_name)

    feature_v=''
    for f in feature_list:
        func=getattr(a,f)
        v=func()
        #print(v)
        feature_v+=str(v)+","
    feature_v=feature_v[:-1]

    inst_name=feature_name[:-3]
    with('feature.csv','a') as f:
        f.write(inst_name+','+feature_v+'\n')
'''