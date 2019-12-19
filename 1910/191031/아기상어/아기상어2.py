import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
if sum(sum(space, [])) == 9:  # 물고기가 하나도 없을 때 0 출력
    print(0)
else:
    pass

def search(x, y):
    pass
    # visited 만들고, que 에 상어크기, 좌표 같이 입력해놓고 방문쳌
    # queue 가 있을 때까지
    # 물고기 후보 빈 리스트 만들어놓고
    # 큐의 갯수만큼 팝하면서 bfs 돌리기
    # 범위 내에서 visited 아닌 애중에 물고기 크기 비교
    # while 문 돌 때 마다 이동거리 체크
    # 먹을 수 있는 물고기가 있으면
    # 정렬해서 첫번째꺼 먹음
    # 상어를 크게 만들어줌
    # 물고기 먹은 자리로 이동해줌