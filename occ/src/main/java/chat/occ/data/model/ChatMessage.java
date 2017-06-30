package chat.occ.data.model;

import java.time.LocalDateTime;;

/**
 * ChatMessage contains msg_id, message in msg_content, when message is created_at and the creator user
 *
 */
public class ChatMessage {
	private int msg_id;
	private String msg_content;
	private ChatUser msg_creator;
	private LocalDateTime msg_created_at;
	
	public int getMsg_id() {
		return msg_id;
	}
	public void setMsg_id(int msg_id) {
		this.msg_id = msg_id;
	}
	public String getMsg_content() {
		return msg_content;
	}
	public void setMsg_content(String msg_content) {
		this.msg_content = msg_content;
	}
	public ChatUser getMsg_creator() {
		return msg_creator;
	}
	public void setMsg_creator(ChatUser msg_creator) {
		this.msg_creator = msg_creator;
	}
	public LocalDateTime getMsg_created_at() {
		return msg_created_at;
	}
	public void setMsg_created_at(LocalDateTime msg_created_at) {
		this.msg_created_at = msg_created_at;
	}
	
}
