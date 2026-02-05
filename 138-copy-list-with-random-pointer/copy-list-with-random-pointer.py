"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create a hash map to store old_node -> new_node mapping.
        # This will help us avoid creating duplicate new nodes and
        # connect the random pointers correctly in the second pass.
        old_to_new = {}

        current_old = head
        # First pass: Create all new nodes and populate the hash map.
        while current_old:
            # Create a new node with the same value
            old_to_new[current_old] = Node(current_old.val)
            current_old = current_old.next

        current_old = head
        # Second pass: Assign next and random pointers for the new nodes.
        while current_old:
            # Get the corresponding new node from the map
            new_node = old_to_new[current_old]
            
            # Assign the next pointer for the new node
            # If current_old.next exists, new_node.next points to its copy.
            # If current_old.next is None, new_node.next will also be None.
            new_node.next = old_to_new.get(current_old.next)
            
            # Assign the random pointer for the new node
            # If current_old.random exists, new_node.random points to its copy.
            # If current_old.random is None, new_node.random will also be None.
            new_node.random = old_to_new.get(current_old.random)
            
            current_old = current_old.next
        
        # The head of the copied list is the new node corresponding to the original head.
        return old_to_new[head]