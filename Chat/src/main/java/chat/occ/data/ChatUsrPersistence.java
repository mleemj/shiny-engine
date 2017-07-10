package chat.occ.data;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Consumer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

import chat.occ.data.model.ChatUser;
import chat.occ.data.repo.entity.ChatUserRepo;
import chat.occ.data.repo.entity.UserHE;

@Component("chatUsrPersistence")
public class ChatUsrPersistence implements UserDetailsService{
	private ChatUserRepo entityRepo;
	private Map<String, ChatUser> activeChatUsers;
	
	@Autowired
	public ChatUsrPersistence(ChatUserRepo chatUserRepo) {
		this.entityRepo = chatUserRepo;
		this.activeChatUsers = new HashMap<String, ChatUser>();
	}

	public Collection<GrantedAuthority> getAuthorities(String usrRole) {
		List<GrantedAuthority> authorities = new ArrayList<GrantedAuthority>();
		SimpleGrantedAuthority sga = new SimpleGrantedAuthority(usrRole);
		authorities.add(sga);
		return authorities;
	}
	
	public List<ChatUser> getAllChatUsrs() {
		Logger logger = LoggerFactory.getLogger(ChatUsrPersistence.class);
		logger.info("----- inside ChatUsrPersistence -----");

		List<ChatUser> chatUsers = new ArrayList<ChatUser>();
		List<UserHE> userEntities = this.entityRepo.findAll();
		Consumer<UserHE> action = (UserHE ue) -> {
			boolean usrIsEnabled = ue.getUsrEnabled().trim().equalsIgnoreCase("1");
			Collection<GrantedAuthority> usrAuthorities = getAuthorities(ue.getUsrRole());
			chatUsers.add(
					new ChatUser(
							ue.getUsrId(), 
							ue.getUsrName(), 
							ue.getUsrEmail(), 
							ue.getUsrPassword(),
							usrAuthorities, usrIsEnabled));
		};
		userEntities.forEach(action);

		logger.info("----- end ChatUsrPersistence -----");
		return chatUsers;
	}
	
	/**
	 * If user is active, return user else call repository to get user.
	 */
	public ChatUser getUsrByEusr(String emailUsername){
		if (this.activeChatUsers.containsKey(emailUsername)){
			return this.activeChatUsers.get(emailUsername);
		}
		UserHE ue = this.entityRepo.findByUsrEmail(emailUsername);
		if (null == ue) return null;
		
		boolean usrIsEnabled = ue.getUsrEnabled().trim().equalsIgnoreCase("1");
		Collection<GrantedAuthority> usrAuthorities = getAuthorities(ue.getUsrRole());
		ChatUser chatUser = new ChatUser(ue.getUsrId(), 
									ue.getUsrName(), 
									ue.getUsrEmail(), 
									ue.getUsrPassword(),
									usrAuthorities, 
									usrIsEnabled);
		this.activeChatUsers.put(emailUsername, chatUser);
 		return chatUser;
	}

	@Override
	public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {
		ChatUser ud = this.getUsrByEusr(userName);
		if (null == ud) throw new UsernameNotFoundException(userName);
		return ud;
	}
	
}
