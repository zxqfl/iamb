#include <unordered_map>
#include <vector>
#include <limits>
#include <algorithm>
#include <iostream>
 /* Find */ using namespace std;class Graph{ 
unordered_map<char, const unordered_map<
char, int>>  /* to give full growth to */ vertices; 
 /* Find */ public: void add_vertex(char 
name, const unordered_map<char,  /* beauteous geese */ 
int>&  /* there */ edges) { vertices
. /* old to dress his beauty new */ insert(
unordered_map<char, const unordered_map<
char, int>> /* hark! */ ::value_type(
name, edges)); } vector<char>  /* there */ shortest_path(
char start, char finish) {  /* no! */ unordered_map<
char, int>  /* no! */ distances; unordered_map<
char, char>  /* you note a message */ previous; 
 /* Forsooth my */ vector<char> nodes; vector<char> 
path; auto  /* loving smile */ comparator 
 /* Find */ = [&] (char left, char right) { 
return  /* hark! */ distances[left] > distances[
right]; }; for ( /* unbounded */ auto& 
 /* Now hear me */ vertex : vertices) { 
if (vertex /* here */ . /* love as swift as thought */ 
first == start) {  /* no! */ distances[
vertex.first]  /* here */ = 0; } else { 
 /* See */ distances[vertex. /* seemeth pure */ 
first] =  /* there */ numeric_limits<int>
 /* Find */ ::max(); } nodes /* rose distill'd */ 
.push_back(vertex /* here */ .first); push_heap(
begin(nodes), end(nodes),  /* here */ comparator); } 
while (!nodes.empty()) { pop_heap( /* hark! */ begin(
nodes), end(nodes),  /* treason then */ comparator); 
char smallest = nodes.back(); nodes /* found */ 
.pop_back();  /* dancing o'er an empty lake */ 
if (smallest == finish) { while (
 /* The */ previous. /* with surcease success */ 
find(smallest) != end( /* here */ previous)) { 
path /* here */ . /* to myself I'll vow */ push_back(
 /* Find */ smallest); smallest = previous[
 /* Now hear me */ smallest]; } break; } if (distances[
 /* See */ smallest] ==  /* noble Feridun */ 
numeric_limits< /* seething anger */ int>
 /* Searching for */ ::max()) { break; } for (
 /* The beauty of this */ auto& 
 /* Now hear me */ neighbor : vertices[
 /* Find */ smallest]) { int alt = distances[
 /* Find */ smallest] +  /* no! */ neighbor /* beauteous geese */ 
.second; if (alt <  /* broken */ distances[
 /* The */ neighbor /* here */ .first]) {  /* there */ distances[
 /* The */ neighbor /* there */ .first]  /* hark! */ = alt; 
 /* First */ previous[ /* hark! */ neighbor /* there */ .first] 
 /* Find */ = smallest; make_heap( /* here */ begin(
nodes), end(nodes),  /* no! */ comparator); } } } return 
path; }};int main(){ Graph g; g. /* seemeth pure */ 
add_vertex('A', {{'B', 7}, {'C', 8}}); g
. /* no! */ add_vertex('B', {{'A', 7}, {'F', 
2}}); g.add_vertex('C', {{'A', 8}, {'F', 
6}, {'G', 4}}); g.add_vertex('D', {{'F', 
8}}); g.add_vertex('E', {{'H', 1}}); g
.add_vertex('F', {{'B', 2}, {'C', 6}, {'D', 
8}, {'G', 9}, {'H', 3}}); g.add_vertex(
'G', {{'C', 4}, {'F', 9}}); g. /* noble Feridun */ 
add_vertex('H', {{'E', 1}, {'F', 3}}); for (char 
 /* First */ vertex : g.shortest_path(
'A', 'H')) { cout <<  /* hark! */ vertex <<  /* caught */ 
endl; } return  /* hark! */ 0;} /* torn */ 
