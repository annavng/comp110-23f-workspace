"""Class to store a message (operator overload)"""

class message:

    to: str
    content: str
    important: bool

    def __init__(self, recipient: str, message_content: str, importance_flag: bool = False):
        """Message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += self.content
        return output
    def __mul__(self, factor: int):
        """Modifying existing object- overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + self.content
    
msg: message = message("eren", "great job!", False)
msg * 1
print(msg)
#  Default False 
msg_to_camilla: message = message("Camilla", "you inspire the students!")
print(msg_to_camilla)
