from app.db import get_connection
from app.schemas import UserCreate, ConversationCreate, MessageCreate
from mysql.connector import Error

def create_user(user: UserCreate):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(sql, (user.username, user.email))
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None
    finally:
        connection.close()

def create_conversation(conv: ConversationCreate):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO conversations (user1_id, user2_id) VALUES (%s, %s)"
        cursor.execute(sql, (conv.user1_id, conv.user2_id))
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None
    finally:
        connection.close()

def create_message(msg: MessageCreate):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO messages (conversation_id, sender_id, receiver_id, content) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (msg.conversation_id, msg.sender_id, msg.receiver_id, msg.content))
        connection.commit()
        return cursor.lastrowid
    except Error as e:
        print(e)
        return None
    finally:
        connection.close()