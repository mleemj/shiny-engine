package chat.occ.data.model;

import java.util.HashMap;
import java.util.List;

/**
 * Collection of ChatMessages
 * Collection of Chats
 * Collection of ChatMessages grouped by ChatRoom
 */
public class ChatRoomMessages {
	HashMap<ChatRoom, List<ChatMessage>> room_msgs;
	
	public void updateChatRoomMessages(int chat_room){
		
	}
}
