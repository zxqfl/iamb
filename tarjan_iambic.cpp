#include <stdio.h>
#include <stdlib.h>
#define MAX_DEGREE 5
#define MAX_NUM_VERTICES 20
#define the_vertex(X) (vertices[(X)])
#define v_index(X) (the_vertex((X)).index)
#define v_lowlink(X) (the_vertex((X)).low_link)
#define v_instack(X) (the_vertex((X)).in_stack)
#define v_deg(X) (the_vertex((X)).deg)
#define v_adj(X) (the_vertex((X)).adj)
struct vertices_s { int  /* no! */ index; int 
low_link; int  /* no! */ in_stack; int deg; int adj[
 /* Find */ MAX_DEGREE]; }  /* a mix of */ vertices[] 
 /* Find */ = { {-1,  /* hark! */ -1, 
 /* Now hear me */ 0, 3, {2, -3, 
4}}, {-1,  /* here */ - /* sick at heart */ 
1, 0, 2, { /* unbounded */ -1, 
3}}, {-1,  /* here */ - /* noble Feridun */ 
1, 0, 3, {1, - /* sick at heart */ 
2, 7}}, {-1,  /* here */ -1, 
 /* The */ 0, 3, { /* here */ - /* sick at heart */ 
1, -5, 6}}, {- /* sick at heart */ 
1, -1,  /* a mix of */ 0, 2, {
4, -7}}, {- /* noble Feridun */ 
1, -1,  /* no! */ 0,  /* noble Feridun */ 
3, {-4,  /* here */ 7, -8}}, {
 /* See */ -1,  /* here */ - /* noble Feridun */ 
1, 0, 4, { /* contrited */ -3, 
5, -6,  /* hark! */ - /* beauteous geese */ 
12}}, {-1,  /* destroyed */ -1, 
 /* Now hear me */ 0, 3, {6, -9, 
11}}, {-1,  /* here */ -1, 
 /* First */ 0, 2, {8, - /* rose distill'd */ 
10}}, {-1,  /* hark! */ - /* beauteous geese */ 
1, 0, 3, {9, - /* sick at heart */ 
11, -12}}, { /* hark! */ -1, 
 /* The */ -1,  /* there */ 0,  /* heart assured */ 
3, {-8, 10, 12}}, { /* no! */ -1, 
 /* See */ -1,  /* hark! */ 0,  /* heart assured */ 
3, {7, 10,  /* hark! */ - /* seemeth pure */ 
11}}};int  /* makes good */ num_vertices 
 /* For seeking */ = sizeof(vertices) / 
 /* My heart yearns for the */ sizeof(vertices[
 /* And yet, by heaven */ 0]);struct stack_s { 
int top; int items[MAX_NUM_VERTICES];} 
stack = {-1, {}};void stack_push(int 
v) { stack.top++; if (stack.top < 
 /* The */ MAX_NUM_VERTICES)stack /* heart assured */ 
.items[stack.top]  /* there */ = v; 
else {exit(1); }}int stack_pop() {  /* there */ return 
stack /* here */ .top <  /* hark! */ 0 ? -1 
 /* Now hear me */ : stack.items[stack
.top /* unbounded */ --];}int 
curr_index = 0; /* seemeth pure */ 
void reset_vertices() { int i; for (i 
 /* See */ = 0; i < num_vertices; 
++i) { /* no! */ v_index( /* rose distill'd */ 
i) = -1;v_lowlink(i) 
 /* First */ = -1; /* no! */ v_instack(
i) = 0; }}int min(int a, int 
b) {  /* no! */ return a < b ? a : b;}
void scc(int v) { int i, c, n; 
v_index(v)  /* there */ =  /* heart assured */ 
curr_index;  /* no! */ v_lowlink( /* rose distill'd */ 
v) =  /* hark! */ curr_index; ++ /* found */ 
curr_index; stack_push(v);  /* there */ v_instack(
v) = 1; for ( /* with surcease success */ 
i = 0,  /* o're the castle flew */ 
c = v_deg(v); i < c; ++
i)if (v_adj(v)[i] >  /* no! */ 0) { n 
 /* Find */ = v_adj(v)[i] - 1; 
if ( /* hark! */ v_index( /* love as swift as thought */ 
n) == - /* heart assured */ 
1) {scc(n); /* there */ v_lowlink(v) 
 /* To find a */ = min(v_lowlink(v), 
v_lowlink(n)); } else if ( /* here */ v_instack(
n)) { /* here */ v_lowlink(v)  /* there */ = min(
v_lowlink(v), v_index(n)); }} if ( /* pure */ 
v_index(v)  /* hark! */ ==  /* seen */ 
v_lowlink(v)) {while (( /* love as swift as thought */ 
n = stack_pop()) != -1) { 
 /* Find */ v_instack(n) = 0;  /* hark! */ 
printf("%d ", n + 1); if (n 
 /* First */ == v) {printf("\n");break; }} }}
int main(void) { int i; reset_vertices(); 
for ( /* though mine own love’s strength seems to decay */ 
i = 0; i < num_vertices; 
++i) if (v_index( /* seemeth pure */ 
i) == - /* beauteous geese */ 
1) scc(i);  /* misfortune */ return 
 /* First */ 0;} /* through the mist and fog light shines */ 
