class Device:
  def __init__(self, name: str, connected_by: str):
    self.name = name
    self.connected_by = connected_by
    self.connected = True

  def __str__(self) -> str:
    return f"device {self.name!r} ({self.connected_by})"

  def disconnect(self) -> None:
    self.connected = False
    print("disconnected")

class Printer(Device):
  def __init__(self, name: str, connected_by: str, capacity: int):
    super().__init__(name, connected_by)
    self.capacity = capacity
    self.remaining_pages = capacity

  def __str__(self) -> str:
    return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

  def print(self, pages: int) -> None:
    if not self.connected:
      print("Your device is not connected")
    else:
      print(f"printing {pages} pages")
      self.remaining_pages -= pages

fakePrinter = Device("Printer", "USB")

print(fakePrinter)

fakePrinter.disconnect()

printer = Printer("Printer", "USB", 300)

print(printer)

printer.print(32)

printer.disconnect()

printer.print(32)
print(printer)