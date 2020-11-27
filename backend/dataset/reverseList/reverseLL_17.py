class Solution:
	def reverseList(self, head:ListNode)->ListNode:
		"""
		:type head: ListNode
		:rtype: ListNode
		"""

		p1, p2 = None, head

		while p2 is not None:
			p3 = p2.next
			p2.next = p1
			p1 = p2
			p2 = p3
		return p1
