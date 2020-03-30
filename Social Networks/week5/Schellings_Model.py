import networkx	as nx
import matplotlib.pyplot as plt
import random

N = 10
G = nx.grid_2d_graph(N,N)
pos	= dict( (n, n)	for n in G.nodes() )
labels = 	dict( ((i, j), i * 10 + j)	for i, j in G.nodes())

#Adding colors to nodes to represent diffrent type of people
def display_graph(G):
    nodes_g = nx.draw_networkx_nodes(G, pos, node_color = 'green',nodelist = type1_node_list )

    nodes_r = nx.draw_networkx_nodes(G, pos, node_color = 'red',nodelist = type2_node_list )

    nodes_w = nx.draw_networkx_nodes(G, pos, node_color = 'white',nodelist = empty_cells )

    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos,labels = labels)
    plt.show()


def get_boundary_nodes(G):
    boundary_nodes_list = []
    for((u,v),d) in  G.nodes(data = True):
        if u==0 or u== N-1 or v == 0 or v == N-1:
            boundary_nodes_list.append((u,v))

    return boundary_nodes_list

#Add diagonal edges
for ((u,v),d) in G.nodes(data=True):
    if (u+1 <= N-1) and (v+1 <= N-1):
        # print (u,v), (u+1, v+1)
        G.add_edge((u,v),(u+1,v+1))


for ((u,v),d) in G.nodes(data=True):
    if (u+1 <=	N-1) and (v-1 >= 0):
        # print (u,v), (u+1, v+1)
        G.add_edge((u,v),(u+1,v-1))

nx.draw(G, pos, with_labels = False)
nx.draw_networkx_labels(G, pos, labels = labels)
plt.show()

for n in G.nodes():
    G.nodes[n]['type'] = random.randint(0,2)

type1_node_list = [n for  (n,d) in G.nodes(data = True) if d['type'] ==1 ]
type2_node_list = [n for  (n,d) in G.nodes(data = True) if d['type'] ==2 ]
empty_cells = [n for  (n,d) in G.nodes(data = True) if d['type'] ==0 ]

display_graph(G)

boundary_nodes_list = get_boundary_nodes(G)
internal_nodes_list = list(set(G.nodes()) - set(boundary_nodes_list))
