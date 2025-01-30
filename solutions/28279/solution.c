#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int data;
  struct node *prev;
  struct node *next;
} Node;

typedef struct llist {
  Node *head;
  Node *tail;
  int count;
} Llist;

Llist *llist_init() {
  Node *head = malloc(sizeof(Node));
  Node *tail = malloc(sizeof(Node));
  head->prev = NULL;
  head->next = tail;
  tail->prev = head;
  tail->next = NULL;
  Llist *llist = malloc(sizeof(Llist));
  llist->head = head;
  llist->tail = tail;
  llist->count = 0;
  return llist;
}

int llist_is_empty(Llist *llist) {
  return (llist->head->next == llist->tail) ? 1 : 0;
}

void llist_insert_front(Llist *llist, int data) {
  Node *node = malloc(sizeof(Node));
  node->data = data;
  node->next = llist->head->next;
  llist->head->next->prev = node;
  node->prev = llist->head;
  llist->head->next = node;
  llist->count++;
}

void llist_insert_rear(Llist *llist, int data) {
  Node *node = malloc(sizeof(Node));
  node->data = data;
  node->prev = llist->tail->prev;
  llist->tail->prev->next = node;
  node->next = llist->tail;
  llist->tail->prev = node;
  llist->count++;
}

int llist_pop_front(Llist *llist) {
  if (llist_is_empty(llist)) return -1;
  Node *remove_node = llist->head->next;
  remove_node->next->prev = llist->head;
  llist->head->next = remove_node->next;
  int data = remove_node->data;
  free(remove_node);
  llist->count--;
  return data;
}

int llist_pop_rear(Llist *llist) {
  if (llist_is_empty(llist)) return -1;
  Node *remove_node = llist->tail->prev;
  remove_node->prev->next = llist->tail;
  llist->tail->prev = remove_node->prev;
  int data = remove_node->data;
  free(remove_node);
  llist->count--;
  return data;
}

int llist_count(Llist *llist) { return llist->count; }

int llist_peek_front(Llist *llist) {
  return llist_is_empty(llist) ? -1 : llist->head->next->data;
}

int llist_peek_rear(Llist *llist) {
  return llist_is_empty(llist) ? -1 : llist->tail->prev->data;
}

void llist_traverse_print(Llist *llist) {
  for (Node *node = llist->head->next; node != llist->tail; node = node->next)
    printf("%d\n", node->data);
}

int run_command(Llist *llist, Llist *answer_list, int cmd) {
  int x;
  switch (cmd) {
    case 1:
      scanf("%d", &x);
      llist_insert_front(llist, x);
      break;
    case 2:
      scanf("%d", &x);
      llist_insert_rear(llist, x);
      break;
    case 3:
      llist_insert_rear(answer_list, llist_pop_front(llist));
      break;
    case 4:
      llist_insert_rear(answer_list, llist_pop_rear(llist));
      break;
    case 5:
      llist_insert_rear(answer_list, llist_count(llist));
      break;
    case 6:
      llist_insert_rear(answer_list, llist_is_empty(llist));
      break;
    case 7:
      llist_insert_rear(answer_list, llist_peek_front(llist));
      break;
    case 8:
      llist_insert_rear(answer_list, llist_peek_rear(llist));
      break;
  }
}

int main() {
  Llist *llist = llist_init();
  Llist *answer_list = llist_init();
  int n;
  scanf("%d", &n);
  while (n--) {
    int cmd;
    scanf("%d", &cmd);
    run_command(llist, answer_list, cmd);
  }
  llist_traverse_print(answer_list);
  return 0;
}