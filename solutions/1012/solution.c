#include <stdio.h>

int t, m, n, k;
int map[51][51];
int visited[51][51];

void reset() {
  for (int i = 0; i < 51; i++)
    for (int j = 0; j < 51; j++) map[i][j] = visited[i][j] = 0;
}

int dir_i[4] = {0, 0, 1, -1};
int dir_j[4] = {1, -1, 0, 0};

void dfs(int start_i, int start_j) {
  visited[start_i][start_j] = 1;
  for (int d = 0; d < 4; d++) {
    int next_i = start_i + dir_i[d];
    int next_j = start_j + dir_j[d];
    if (0 <= next_i && next_i < m && 0 <= next_j && next_j < n &&
        map[next_i][next_j] && !visited[next_i][next_j])
      dfs(next_i, next_j);
  }
}

int solve() {
  int count = 0;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (map[i][j] && !visited[i][j]) {
        count++;
        dfs(i, j);
      }
    }
  }
  return count;
}

int main() {
  scanf("%d", &t);
  while (t--) {
    reset();
    scanf("%d %d %d", &m, &n, &k);
    while (k--) {
      int i, j;
      scanf("%d %d", &i, &j);
      map[i][j] = 1;
    }
    printf("%d\n", solve());
  }
}