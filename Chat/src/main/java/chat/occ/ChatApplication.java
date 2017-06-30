package chat.occ;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import chat.occ.data.ChatMsgUserPersistence;
import chat.occ.data.model.ChatUser;

@Order(1)
@Component
public class ChatApplication implements CommandLineRunner {
	private ChatMsgUserPersistence chatPersist;

	@Autowired
	public ChatApplication(ChatMsgUserPersistence persistenceService) {
		this.chatPersist = persistenceService;
	}

	@Override
	public void run(String... arg0) throws Exception {
		Logger logger = LoggerFactory.getLogger("ChatApplication");
		logger.info("----- inside ChatApplication.findAllChatUsers -----");
		List<ChatUser> chatusers = this.chatPersist.getAllChatUsrs();
		List<String> emails = new ArrayList<String>();
		for (ChatUser cu : chatusers) {
			emails.add(cu.getUsrEmail());
			logger.info(cu.toString());
		}
		
		logger.info("----- inside ChatApplication.findUserByEmail -----");
		for(String e: emails){
			ChatUser cuByEmail = this.chatPersist.getChatUsrByEmail(e);
			logger.info(cuByEmail.toString());
		}
		
		logger.info("----- end ChatApplication -----");
	}

}
