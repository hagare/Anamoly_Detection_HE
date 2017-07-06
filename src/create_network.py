#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:00:18 2017

@author: Hagar ElBishlawi
"""
def make_friends_graph(people, friends):
	# graph of friends - adjacency lists representation
	G = {person: [] for person in people} # add person to friends list
	for id1, id2 in friends:
		G[id1].append(id2) # id1 is friends with id2
		G[id2].append(id1) # id2 is friends with id1
	return G


def make_unfriends_graph(people, friends):
	# graph of unfriends - adjacency lists representation
	G = {person: [] for person in people} # add person to friends list
	for id1, id2 in friends:
		G[id1].discard(id2) # id1 is friends with id2
		G[id2].discard(id1) # id2 is friends with id1
	return G

def networks(num_people, friends):
	direct_friends = make_friends_graph(range(num_people), friends)
	seen = set() # already seen people

	def friendship_circle(person):
		seen.add(person)
		yield person

		for friend in direct_friends[person]:
			if friend not in seen:
				yield from friendship_circle(friend)

#group people into friendship circles
	circles = (friendship_circle(person) for person in range(num_people) if person not in seen)

# print friendship circles
	for i, circle in enumerate(circles):
		print("Social network %d is {%s}" % (i, ",".join(map(str, circle))))

networks(5, [(0,1), (1,2),(3,4)]) 
make_friends_graph(2,[(0,5)])
G
