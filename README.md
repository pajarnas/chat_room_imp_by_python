v0.1 Finish the min system that allow server send message to every connected client first.
    这个版本,服务端用列表保存了每一个刚加入的socket对象,并将这些对象保存到列表里.然后客户端的都在等待自己的另一端发送消息.
    套接字其实就是两部分,一部分在服务端,一部份在客户端.但是在客户端和服务端都是完整的对象.完整的对象在不同的端身份也不一样.
    准确的说是,accept返回了套接字在服务端的那一半.connect之后,socket对象也变成了自己的这一边.所以一端接收的时候,另一端就要发送.
    一端发送,另一端没有接收,也是无效的.所以服务端要遍历列表中的每一个socket对象,然后客户端每一个对象都要处于接收状态.

v0.2 Allow client send message to server and server send this message to every client.
    实现这个功能,需要将客户端从一直接收状态解放出来.客户端要有两个线程.一个线程用来接收,一个线程用来发送.发送的线程是主线程.
    服务端开启一个线程专门用来接收客户端的消息.一旦接收到消息就转发给所有的客户端.
