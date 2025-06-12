from app.db import get_connection
from app.schemas import MessageCreate

def create_message(message: MessageCreate):
    connection = get_connection()
    if connection is None:
        return None
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO messages (sender_id, receiver_id, content) VALUES (%s, %s, %s)"
        values = (message.sender_id, message.receiver_id, message.content)
        cursor.execute(sql, values)
        connection.commit()
        message_id = cursor.lastrowid
        return {**message.dict(), "id": message_id}
    except Exception as e:
        print(f"Error inserting message: {e}")
        return None
    finally:
        connection.close()