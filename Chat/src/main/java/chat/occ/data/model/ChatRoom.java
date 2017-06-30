package chat.occ.data.model;

import java.util.List;

import org.apache.commons.lang3.builder.HashCodeBuilder;

/**
 * Chat room provides chat_id, chat_name, list of chat_usrs and chat_last_msg
 *
 */
public class ChatRoom {
	private int chat_id;
	private String chat_name;
	private List<ChatUser> chat_usrs;
	private ChatMessage chat_last_msg;
	
	public int getChat_id() {
		return chat_id;
	}
	public void setChat_id(int chat_id) {
		this.chat_id = chat_id;
	}
	public String getChat_name() {
		return chat_name;
	}
	public void setChat_name(String chat_name) {
		this.chat_name = chat_name;
	}
	public List<ChatUser> getChat_usrs() {
		return chat_usrs;
	}
	public void setChat_usrs(List<ChatUser> chat_usrs) {
		this.chat_usrs = chat_usrs;
	}
	public ChatMessage getChat_last_msg() {
		return chat_last_msg;
	}
	public void setChat_last_msg(ChatMessage chat_last_msg) {
		this.chat_last_msg = chat_last_msg;
	}

	@Override
	public boolean equals(Object o){
		if (o instanceof ChatRoom == false) return false;
		int o_id = ((ChatRoom) o).getChat_id();
		return (o_id == this.chat_id);
	}
	
	@Override
	public int hashCode(){
		HashCodeBuilder hcb = new HashCodeBuilder();
		return hcb.append(this.chat_id).toHashCode();
	}
}
