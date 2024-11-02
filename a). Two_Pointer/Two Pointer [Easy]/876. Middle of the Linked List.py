class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slower=head
        faster=head
        while faster and faster.next:
            slower=slower.next
            faster=faster.next.next
        return slower
        
