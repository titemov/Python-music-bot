class Queue:
    def __init__(self):
        self.trackindex=0
        self.loop_flag=False
        self.timer=0
        self.isJumpUsed=False
        self.tracks={}
        self.queueForPrint = {}

    # tracks = {}
    # trackindex = 0 = self.tracks[serverid][0]
    # loop_flag = False = self.tracks[serverid][2]
    # serverqueue = [trackindex, [], loop_flag, timer, isJumpUsed]

    def set_qfp(self,serverid,data):
        self.queueForPrint[serverid]=data
        return 0

    def get_qfp(self,serverid):
        return self.queueForPrint[serverid]

    def queue_add(self, element, serverid):
        # print(serverid)
        if serverid not in self.tracks.keys():
            self.tracks[serverid]=[self.trackindex,[element],self.loop_flag, self.timer, self.isJumpUsed]
            #element[9]=name, length, start time, stream link, yt link, thumbnail link, author, pause time, no play time
        else:
            self.tracks[serverid][1].append(element)
        #print(self.tracks)
        return

    def queue(self, serverid, is_playing=True):
        #print(f"Queue: {self.tracks}")
        if (self.tracks == {}) or (self.tracks[serverid][0] == 0 and self.tracks[serverid][1] == [] and 
        self.tracks[serverid][2] == False and self.tracks[serverid][4] == False):
            return -1
        q = ""
        self.queueForPrint[serverid]=[]
        # getting current track (and if looped) to show with -queue command
        if is_playing == True:
            current = self.tracks[serverid][1][self.tracks[serverid][0]][0]
            try:
                if self.tracks[serverid][2] == True:
                    self.tracks[serverid][1][self.tracks[serverid][0]][0] = f'{self.tracks[serverid][1][self.tracks[serverid][0]][0]} \t\t — текущий (зациклен)'
                else:
                    self.tracks[serverid][1][self.tracks[serverid][0]][0] = f'{self.tracks[serverid][1][self.tracks[serverid][0]][0]} \t\t — текущий'

                length=len(self.tracks[serverid][1])
                pages = (length // 20) + 1
                #print(length,pages)

                for i in range(pages):
                    for n in range(i*20,(i+1)*20):
                        #print(n)
                        try:
                            q+=f"{n+1}) {self.tracks[serverid][1][n][0]}\n"
                        except:
                            break
                    #print(q)
                    q="```"+q+"```"
                    self.queueForPrint[serverid].append(q)
                    q=""
            finally:
                self.tracks[serverid][1][self.tracks[serverid][0]][0] = current
            return 0
        else:
            length = len(self.tracks[serverid][1])
            pages = (length // 20) + 1
            #print(length, pages)

            for i in range(pages):
                for n in range(i * 20, (i + 1) * 20):
                    try:
                        q += f"{n + 1}) {self.tracks[serverid][1][n][0]}\n"
                    except:
                        break
                q = "```" + q + "```"
                self.queueForPrint[serverid].append(q)
                q = ""

            return 0

    def clear(self, serverid,isVoice=False):
        if isVoice==False:
            self.tracks[serverid]=[0,[],False,0,False]
            self.queueForPrint[serverid]=[]
            return
        else:
            tempvar = self.tracks[serverid][1][self.tracks[serverid][0]]
            self.tracks[serverid][0]=0
            self.tracks[serverid][1]=[]
            self.tracks[serverid][1].append(tempvar)
            self.queueForPrint[serverid]=[]
            return

    def queue_next(self,serverid):
        # print(self.tracks)
        if not self.tracks[serverid][2]:
            if -1<=self.tracks[serverid][0]<len(self.tracks[serverid][1]):
                self.tracks[serverid][0]+=1
                # print(self.tracks)
                return 0
            else:
                return 1

    def if_queue_exist(self, serverid):
        return self.tracks[serverid][0]<len(self.tracks[serverid][1])

    def queue_len(self, serverid):
        return len(self.tracks[serverid][1])

    def get_index(self, serverid):
        return self.tracks[serverid][0]

    def get_track_name(self, serverid):
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][0]
        except:
            return -1

    def get_track_length(self, serverid):
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][1]
        except:
            return -1

    def set_start_time(self,serverid,time):
        try:
            self.tracks[serverid][1][self.tracks[serverid][0]][2] = time
        except:
            return False

    def get_start_time(self,serverid):
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][2]
        except:
            return -1

    def set_stream_link(self,serverid,streamlink): #sets stream link
        try:
            self.tracks[serverid][1][self.tracks[serverid][0]][3]=streamlink
        except:
            return False

    def get_stream_link(self,serverid): #gets stream link
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][3]
        except:
            return False

    def get_yt_link(self,serverid): #gets yt link
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][4]
        except:
            return False

    def get_thumbnail_url(self,serverid):
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][5]
        except:
            return False

    def get_author(self,serverid):
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][6]
        except:
            return False

    def set_pause_time(self,serverid,time):
        try:
            self.tracks[serverid][1][self.tracks[serverid][0]][7]=time
        except:
            return False

    def get_pause_time(self,serverid):
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][7]
        except:
            return -1

    def set_no_play_time(self,serverid,time):
        try:
            self.tracks[serverid][1][self.tracks[serverid][0]][8]=time
        except:
            return False

    def get_no_play_time(self,serverid):
        try:
            return self.tracks[serverid][1][self.tracks[serverid][0]][8]
        except:
            return -1

    def loop(self,serverid):
        self.tracks[serverid][2]=True
        return

    def unloop(self, serverid):
        self.tracks[serverid][2] = False
        return

    def jump(self,value, serverid):
        self.tracks[serverid][0]=value
        # print(f"jump function:\n{self.tracks[serverid]}")
        return