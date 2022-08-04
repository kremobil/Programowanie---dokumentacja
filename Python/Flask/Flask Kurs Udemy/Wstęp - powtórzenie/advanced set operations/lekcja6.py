friends = {"Bob", "Tom", "Rick"}
best_friends = {"Bob", "Tom"}

# removes argument set
normal_friends = friends.difference(best_friends)

print(normal_friends)

my_friends = friends
my_friends_friends = {"Jerry", "Jane", "Tom", "Nancy", "Rick"}

all_our_friends = my_friends.union(my_friends_friends)
our_bouth_friends = my_friends.intersection(my_friends_friends)

print(all_our_friends, our_bouth_friends)