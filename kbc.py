print("devi or sajjno wlcm to the kbc")
print("here is the rule of kbc")
rules=[
    ["1.when you ans wrong the game is end"],
    ["2.and when you quit the game accroding to your levels your money wil be given to you"]
]
for i in rules:
    print(i)


que=[
    ["what does F1 stand for?","Formula One","Fast One","Final One","Formula Track",1],
    ["how many cars does each F1 team enter in a race?","one","three","two","four",3],
    ["which flag means the race is stopped?","yellow","green","blue","red",4],
    ["what does DRS stand for?","Driver Racing Speed","Drag Reduction System","Downforce Racing Setup","Dynamic Road Safety",2],
    ["which tire compound is marked with a red sidewall?","hard","medium","soft","intermediate",3],
    ["what does the chequered flag signal?","the race has finished","a pit stop is open","rain is coming","a driver must retire",1],
    ["how many points does a Grand Prix winner score under the standard F1 points system?","10","18","25","30",3],
    ["in which country is the Monaco Grand Prix held?","Italy","France","Spain","Monaco",4],
    ["what does pole position mean?","the final place on the starting grid","the first place on the starting grid","the fastest pit stop","the lead after the first lap",2],
    ["where do F1 teams change tires during a race?","on the starting grid","in the paddock","on the track","in the pit lane",4],
    ["Silverstone Circuit is in which country?","Germany","United Kingdom","Belgium","Australia",2],
    ["what is the main purpose of the safety car?","to lead a parade lap","to end the race","to slow and control the field","to give a driver a penalty",3],
    ["what does a blue flag tell a driver during a race?","a faster car is approaching to lap them","the race has ended","they must enter the pits","the track is clear",1],
    ["which championship title is awarded to the top driver over the season?","Constructors' Championship","Sprint Cup","Team Principal's Trophy","Drivers' Championship",4],
    ["what starts an F1 race after the red start lights go out?","the podium ceremony","the safety-car period","the formation lap","the race",4]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,450000,780000,890000,990000,1000000]
money=0
for ans in range(0,len(que)):
    print(f"question for {levels[ans]} repees")
    print(f"que is {que[ans][0]} \n A.{que[ans][1]}\n B.{que[ans][2]}\n C.{que[ans][3]}\n D.{que[ans][4]}")
    lock=int(input("enter your ans or enter 0 for quit"))
    if lock==que[ans][-1]:
        print(f"correct ans.you won{levels[ans]}")
        if ans==4:
            money=10000
        elif ans==9:
            money=320000
        elif ans==14:
            money=1000000

    else:
        print("your answer is wrong")
        break

print(f"your taking money is{money}")