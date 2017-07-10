package chat.occ.data.model;

import java.util.Observable;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.authentication.logout.LogoutHandler;
import org.springframework.stereotype.Component;

@Component("chatLSHandler")
public class ChatLSHandler extends Observable implements LogoutHandler{
	Logger logger = LoggerFactory.getLogger(ChatLSHandler.class);

	@Override
	public void logout(HttpServletRequest request, HttpServletResponse response, Authentication authentication) {
		logger.info("----- inside ChatLSHandler -----");
		ChatUser chatUser = (ChatUser)authentication.getPrincipal();
		authentication.setAuthenticated(false);
		notify(chatUser);
		logger.info(authentication.isAuthenticated() 
				+ " :Principal class: " + authentication.getPrincipal().getClass()
				+ " :Authentication class: " + authentication.getClass()
				+ " :Principal: " + authentication.getPrincipal());
	}
	
	private void notify(ChatUser chatUser){
		super.setChanged();
		super.notifyObservers(chatUser);
		super.clearChanged();
	}
	
}
