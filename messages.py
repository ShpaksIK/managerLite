def error(*message) -> None:
    """ Сообщение об ошибке """
    print(f"[!] {''.join(message)}")

def suc(*message) -> None:
    """ Сообщение об успешном совершении действия"""
    text = ""
    for i in message:
        text += f" {str(i)}"
    print(f"[/]{text}")