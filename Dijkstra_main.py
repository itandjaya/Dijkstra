## Dijkstra_main.py
## Main function to test Dijkstra's algorthm - shortest distance  from u to v.

from Dijkstra import Graph;


def main():

    edges = [   ('a', 'c', 20), ('a', 'b', 10), ('b','e', 10), ('b','d',50), ('c','e',33), ('c','d',20), \
                ('d','e',20), ('d','f',22), ('e','f',1)
            ];

    g = Graph(edges);

    res = g.find_distance('a','f');
    print(res);
    
    return 0;


if __name__ == '__main__':      main();