
# Bully algorithm

priorities=[]
status=[]
status=[]
coordinator =0

def electprocess(elector):

    elector-=1

    for i in range(len(status)):
        if(priorities[elector]<priorities[i]):
            print("Election message is sent from ",(elector+1),"to",(i+1))
            if(status[i]==1):
                electprocess(i+1)

#take input for status and priorities

status = [int(x) for x in input("Enter multiple status values: ").split(" ")]
priorities = [int(x) for x in input("Enter multiple priority values: ").split(" ")]
initiator=int(input("Enter the Initiator Process : "))

if len(status)==len(priorities) and (initiator in priorities):
    elector=int(input("Enter process which is going to initiate election : "))
    electprocess(elector)

else:
    print("Invalid Input")


