This tool produces poetry: converts

your code to iambic pentameter.

(As punctuation is concerned, you should:

read `-=+.&`

as "minus", "equals", "plus", "dot", "ampersand"

respectively; don't read the rest aloud.)

```cpp
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
struct vertices_s { int  /* there */ index; int 
low_link; int  /* no! */ in_stack; int deg; int adj[
 /* And */ MAX_DEGREE]; }  /* a mix of */ vertices[] 
 /* See */ = { {-1,  /* there */ -1, 
 /* Now hear me */ 0, 3, {2, -3, 
4}}, {-1,  /* there */ - /* noble Feridun */ 
1, 0, 2, { /* unbounded */ -1, 
3}}, {-1,  /* hark! */ - /* beauteous geese */ 
1, 0, 3, {1, - /* rose distill'd */ 
2, 7}}, {-1,  /* here */ -1, 
 /* Thy */ 0, 3, { /* no! */ - /* noble Feridun */ 
1, -5, 6}}, {- /* seemeth pure */ 
1, -1,  /* contrited */ 0, 2, {
4, -7}}, {- /* heart assured */ 
1, -1,  /* here */ 0,  /* rose distill'd */ 
3, {-4,  /* no! */ 7, -8}}, {
 /* Find */ -1,  /* here */ - /* noble Feridun */ 
1, 0, 4, { /* destroyed */ -3, 
5, -6,  /* here */ - /* beauteous geese */ 
12}}, {-1,  /* to see a */ -1, 
 /* To find a */ 0, 3, {6, -9, 
11}}, {-1,  /* there */ -1, 
 /* Find */ 0, 2, {8, - /* rose distill'd */ 
10}}, {-1,  /* there */ - /* seemeth pure */ 
1, 0, 3, {9, - /* heart assured */ 
11, -12}}, { /* no! */ -1, 
 /* The */ -1,  /* here */ 0,  /* seemeth pure */ 
3, {-8, 10, 12}}, { /* no! */ -1, 
 /* First */ -1,  /* no! */ 0,  /* noble Feridun */ 
3, {7, 10,  /* no! */ - /* sick at heart */ 
11}}};int  /* succeed */ num_vertices 
 /* Now hear me */ = sizeof(vertices) / 
 /* My love is for the */ sizeof(vertices[
 /* My heart yearns for the */ 0]);struct stack_s { 
int top; int items[MAX_NUM_VERTICES];} 
stack = {-1, {}};void stack_push(int 
v) { stack.top++; if (stack.top < 
 /* The */ MAX_NUM_VERTICES)stack /* sick at heart */ 
.items[stack.top]  /* hark! */ = v; 
else {exit(1); }}int stack_pop() {  /* there */ return 
stack /* hark! */ .top <  /* no! */ 0 ? -1 
 /* Searching for */ : stack.items[stack
.top /* contrited */ --];}int 
curr_index = 0; /* noble Feridun */ 
void reset_vertices() { int i; for (i 
 /* Find */ = 0; i < num_vertices; 
++i) { /* here */ v_index( /* sick at heart */ 
i) = -1;v_lowlink(i) 
 /* Thy */ = -1; /* there */ v_instack(
i) = 0; }}int min(int a, int 
b) {  /* there */ return a < b ? a : b;}
void scc(int v) { int i, c, n; 
v_index(v)  /* no! */ =  /* beauteous geese */ 
curr_index;  /* here */ v_lowlink( /* seemeth pure */ 
v) =  /* there */ curr_index; ++ /* loved */ 
curr_index; stack_push(v);  /* here */ v_instack(
v) = 1; for ( /* love as swift as thought */ 
i = 0,  /* with surcease success */ 
c = v_deg(v); i < c; ++
i)if (v_adj(v)[i] >  /* here */ 0) { n 
 /* And */ = v_adj(v)[i] - 1; 
if ( /* hark! */ v_index( /* with surcease success */ 
n) == - /* heart assured */ 
1) {scc(n); /* here */ v_lowlink(v) 
 /* Forsooth my */ = min(v_lowlink(v), 
v_lowlink(n)); } else if ( /* here */ v_instack(
n)) { /* there */ v_lowlink(v)  /* there */ = min(
v_lowlink(v), v_index(n)); }} if ( /* caught */ 
v_index(v)  /* no! */ ==  /* made */ 
v_lowlink(v)) {while (( /* o're the castle flew */ 
n = stack_pop()) != -1) { 
 /* First */ v_instack(n) = 0;  /* caught */ 
printf("%d ", n + 1); if (n 
 /* Thy */ == v) {printf("\n");break; }} }}
int main(void) { int i; reset_vertices(); 
for ( /* words as sweet as honey seems to bees */ 
i = 0; i < num_vertices; 
++i) if (v_index( /* sick at heart */ 
i) == - /* noble Feridun */ 
1) scc(i);  /* lavendar */ return 
 /* See */ 0;} /* dancing o'er an empty lake */ 
```

Original:
```cpp
/**
 * Copyright 2014 Gagarine Yaikhom (MIT License)
 *
 * Implementation of Tarjan's Algorithm for Strongly Connected Components.
 */
#include <stdio.h>
#include <stdlib.h>

#define MAX_DEGREE 5
#define MAX_NUM_VERTICES 20

struct vertices_s {
    int index;
    int low_link;
    int in_stack;
    int deg;
    int adj[MAX_DEGREE]; /* < 0 if incoming edge */
} vertices[] = {
    {-1, -1, 0, 3, {2, -3, 4}},
    {-1, -1, 0, 2, {-1, 3}},
    {-1, -1, 0, 3, {1, -2, 7}},
    {-1, -1, 0, 3, {-1, -5, 6}},
    {-1, -1, 0, 2, {4, -7}},
    {-1, -1, 0, 3, {-4, 7, -8}},
    {-1, -1, 0, 4, {-3, 5, -6, -12}},
    {-1, -1, 0, 3, {6, -9, 11}},
    {-1, -1, 0, 2, {8, -10}},
    {-1, -1, 0, 3, {9, -11, -12}},
    {-1, -1, 0, 3, {-8, 10, 12}},
    {-1, -1, 0, 3, {7, 10, -11}}
};
int num_vertices = sizeof(vertices) / sizeof(vertices[0]);

struct stack_s {
    int top;
    int items[MAX_NUM_VERTICES];
} stack = {-1, {}};

void stack_push(int v) {
    stack.top++;
    if (stack.top < MAX_NUM_VERTICES)
	stack.items[stack.top] = v;
    else {
	printf("Stack is full!\n");
	exit(1);
    }
}

int stack_pop() {
    return stack.top < 0 ? -1 : stack.items[stack.top--];
}

#define the_vertex(X) (vertices[(X)])
#define v_index(X) (the_vertex((X)).index)
#define v_lowlink(X) (the_vertex((X)).low_link)
#define v_instack(X) (the_vertex((X)).in_stack)
#define v_deg(X) (the_vertex((X)).deg)
#define v_adj(X) (the_vertex((X)).adj)

int curr_index = 0;

void reset_vertices() {
    int i;
    for (i = 0; i < num_vertices; ++i) {
	v_index(i) = -1;
	v_lowlink(i) = -1;
	v_instack(i) = 0;
    }
}

int min(int a, int b) {
    return a < b ? a : b;
}

void scc(int v) {
    int i, c, n;
    v_index(v) = curr_index;
    v_lowlink(v) = curr_index;
    ++curr_index;

    stack_push(v);
    v_instack(v) = 1;

    for (i = 0, c = v_deg(v); i < c; ++i)
	if (v_adj(v)[i] > 0) {
	    n = v_adj(v)[i] - 1;
	    if (v_index(n) == -1) {
		scc(n);
		v_lowlink(v) = min(v_lowlink(v), v_lowlink(n));
	    } else if (v_instack(n)) {
		v_lowlink(v) = min(v_lowlink(v), v_index(n));
	    }
	}
    
    if (v_index(v) == v_lowlink(v)) {
	printf("scc: ");
	while ((n = stack_pop()) != -1) {
	    v_instack(n) = 0;
	    printf("%d ", n + 1);
	    if (n == v) {
		printf("\n");
		break;
	    }
	}
    }
}

int main(void) {
    int i;
    reset_vertices();
    for (i = 0; i < num_vertices; ++i)
	    if (v_index(i) == -1)
	        scc(i);
    return 0;
}
```
