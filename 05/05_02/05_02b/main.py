# Deque
# FIFO - Remove from front, Add to back

from collections import deque

printer_deque = deque()
printer_deque.append("TaylorSwiftTickets.pdf")
printer_deque.append("MarketingNotes.docs")
printer_deque.append("Proof.png")

while len(printer_deque) > 0:
  document = printer_deque.popleft()
  print(f'Printing {document}')