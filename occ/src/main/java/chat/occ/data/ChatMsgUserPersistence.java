package chat.occ.data;

import java.util.ArrayList;
import java.util.List;
import java.util.Observable;
import java.util.function.Consumer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

import chat.occ.data.model.ChatUser;
import chat.occ.data.repo.entity.ChatUserRepo;
import chat.occ.data.repo.entity.UserHE;

@Component("chatMsgUserPersistence")
public class ChatMsgUserPersistence extends Observable implements UserDetailsService{
	private ChatUserRepo entityRepo;

	@Autowired
	public ChatMsgUserPersistence(ChatUserRepo chatUserRepo) {
		this.entityRepo = chatUserRepo;
	}

	public List<ChatUser> getAllChatUsrs() {
		Logger logger = LoggerFactory.getLogger("ChatMsgUserPersist");
		logger.info("----- inside ChatMsgUserPersistence -----");

		List<ChatUser> chatUsers = new ArrayList<ChatUser>();
		List<UserHE> userEntities = this.entityRepo.findAll();
		Consumer<UserHE> action = (UserHE ue) -> {
			boolean usrIsEnabled = ue.getUsrEnabled().trim().equalsIgnoreCase("1");
			chatUsers.add(new ChatUser(ue.getUsrId(), ue.getUsrName(), ue.getUsrEmail(), ue.getUsrPassword(),
					ue.getUsrRole(), usrIsEnabled));
		};
		userEntities.forEach(action);

		logger.info("----- end ChatMsgUserPersistence -----");
		return chatUsers;
	}
	
	public ChatUser getChatUsrByEmail(String email){
		UserHE ue = this.entityRepo.findByUsrEmail(email);
		boolean usrIsEnabled = ue.getUsrEnabled().trim().equalsIgnoreCase("1");
		ChatUser chatUser = new ChatUser(ue.getUsrId(), ue.getUsrName(), ue.getUsrEmail(), ue.getUsrPassword(),
				ue.getUsrRole(), usrIsEnabled);
		return chatUser;
	}

	@Override
	public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {
		UserDetails ud = this.getChatUsrByEmail(userName);
		if (null == ud) throw new UsernameNotFoundException(userName);
		return ud;
	}
	
}
