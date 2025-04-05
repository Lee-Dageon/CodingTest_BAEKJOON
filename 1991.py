# 노드 탐색 문제
# 전위 순회, 중위 순회, 후위 순회
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다.
# 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.


#전위순회(노드 -> 좌 -> 우 출력)
def preorder(node):
    if node != '.':
        print(node, end = '')
        preorder(tree[node][0]) #왼쪽 서브트리 순회
        preorder(tree[node][1]) #오른쪽 서브트리 순회


#중위순회
def inorder(node):
    if node != '.':
        preorder(tree[node][0]) #왼쪽 서브트리 순회
        print(node, end = '')
        preorder(tree[node][1]) #오른쪽 서브트리 순회


#후위순회
def postorder(node):
    if node != '.':
        preorder(tree[node][0]) #왼쪽 서브트리 순회
        preorder(tree[node][1]) #오른쪽 서브트리 순회
        print(node, end = '')


N = int(input())    #노드의 개수
tree = {} #트리를 사전으로 구성,
# key:value = 노드:[왼쪽자식, 오른쪽자식]
for _ in range(N): #N개 노드 읽기
    node, left, right = input().split()
    tree[node] = [left, right] #노드 삽입

preorder('A')       #전위 순회
print(" ")
inorder('A')       #전위 순회
print(" ")
postorder('A')       #전위 순회

