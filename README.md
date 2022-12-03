# Online-Voting-System-
This project is a GUI based voting system created in Python. The main purpose of this project is to vote for a secretary in each given collage. Additionally, the project uses socket programming, multithreading, and the SMTP protocol for mail transfers.

**Introduction-**
1. Here, the client and server create a connection, indicating that the TCP protocol is in use. For each new request, the Server should create a new thread. 

2. In order to implement this feature, I had to take into account concurrent threads, which means that no threads interfere with one another when a lot of connections are being made to the server at once.I synchronized the threads as a result.

3. Additionally, I sent access credentials to registered voter’s emails via the SMTP protocol.

**Conclusion-**

1. Through this project, we learned how to create TCP socket programming using Python.

2. We also learned how to link a large number of clients to a single server.

3. Because the project required that the server allot a new thread for each new arriving Client, we learned how to develop synchronized multithreading in Python and applied it in the socket programming code.

4. Additionally, we learnt how SMTP functions and how to send emails from one administrator to all registered voters.


