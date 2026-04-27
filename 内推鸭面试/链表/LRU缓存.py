import sys


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # head和tail都不是真正的节点，属于虚拟节点
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        """从链表中删除 node"""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def add_to_tail(self, node):
        """把 node 加到链表尾部，表示最近使用"""
        last_node = self.tail.prev

        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node

    def move_to_tail(self, node):
        """把已有节点移动到链表尾部"""
        # 做法就是现在原来的位置删除他，再在尾部添加他
        self.remove_node(node)
        self.add_to_tail(node)

    def get(self, key: int):
        if key not in self.cache:
            return -1

        # 从缓存中取出
        node = self.cache[key]

        # 访问过后，变成最近使用，加入尾部
        self.move_to_tail(node)

        return node.value

    def put(self, key: int, value: int):
        # 缓存中有的话就更新值，并加入最近使用部分
        if key in self.cache:
            node = self.cache[key]
            # 更新值
            node.value = value
            # 加入尾部
            self.move_to_tail(node)
        else:  # 缓存中没有就创建，并加入最近使用部分
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_to_tail(new_node)

            # 如果超过容量，删除最久未使用的节点
            if len(self.cache) > self.capacity:
                # 从头部取出最久未使用的节点
                lru_node = self.head.next
                self.remove_node(lru_node)
                del self.cache[lru_node.key]  # 同时从缓存中删除


# 读取所有输入
lines = sys.stdin.read().strip().splitlines()

capacity = int(lines[0])
lru = LRUCache(capacity)

ans = []

# 从第二行开始处理操作
for line in lines[1:]:
    parts = line.split()

    if parts[0] == "get":
        key = int(parts[1])
        ans.append(str(lru.get(key)))

    else:  # put
        key = int(parts[1])
        value = int(parts[2])
        lru.put(key, value)

# 每个 get 的结果单独输出一行
print("\n".join(ans))
