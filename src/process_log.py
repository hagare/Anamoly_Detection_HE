# src/process_log.py
# Anamoly Detection Code
# Hagar ElBishlawi, PhD
# July 4, 2017
################################################################################
# Python Libraries
import json # Handle Input datatype
import numpy as np  # Perform calculations

# Input data from batch_log.json
file = open("../log_input/batch_log.json", "r")

param = json.loads(file.readline())

if param.get('D') >= 1: 
    D = param.get('D')
else:
    D = 1
    
if param.get('T') >= 2:
    T = param.get('T')
else:
    T = 2

#X print "Program Parameters:\nD = ",D, "and T = ",T,"\n" # Tell user parameter data D and T

file.next() # skip first line with parameter data
for lines in file:
#   Read data from batch_log
    line = json.loads(lines)
    event_type = line.get('event_type')   # determine if event is a purchase or friend/unfriend event type and extract required information
    print event_type
    if event_type == "purchase":
        timestamp = line.get('timestamp')
        id = line.get('id')
        amount = line.get('amount')
    elif event_type == "befriend":
        timestamp = line.get('timestamp')
        id1 = line.get('id1')
        id2 = line.get('id2')
    elif event_type == "unfriend":
        timestamp = line.get('timestamp')
        id1 = line.get('id1')
        id2 = line.get('id2')


# Create a social network array
# each network gets ids, latest change timestamp, purchases (size T), mean of purchases, sd of purchases
N={} # create network
def friend(id1, id2):
	if id1 in N:
		N[str(id1)]=N.add{id2}
	else
		N[str(id1)]={(id1,id2)}
	
	if id2 in N:
		N[str(id1)]=N.add{id1}
	else
		N[str(id2)]={(id2,id1)}

#for purchases
#go through each row and find any that contain user id then add purchase

# for friend
#if D=1, go through each row and if id2 is present add id1 (D=1)
def friendSet(self,friendID):
    friendsA[self] = friendsA[self].add(friendID) # ADD friend to friends list in friends array
   """ 
def networkSet(self, D):
    if D == 1:
        networkA[self] = friendsA[self]
    if D == 2: 
        for letter in set(friendsA[self]):
        networkA[self] = friendsA[self].update(letter)

friends = friend+friendlist
if D=1 network = union friends
if D=2 network = union of friends and 
network of id = network of id union network of friend
"""

## if D=2, go through each  row and if id2 is present add id1 (D=1) and add id1 to all networks of network of id2
