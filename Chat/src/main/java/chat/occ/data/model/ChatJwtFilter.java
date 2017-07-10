package chat.occ.data.model;

import java.util.HashMap;
import java.util.Map;
import java.util.Observable;
import java.util.Observer;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.http.HttpHeaders;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.stereotype.Component;

@Component("chatJwtFilter")
public class ChatJwtFilter extends UsernamePasswordAuthenticationFilter implements Observer{
	private Map<Long, String> tokenMap = new HashMap<Long, String>();
	Logger logger = LoggerFactory.getLogger(ChatJwtFilter.class);

	@Override
	public Authentication attemptAuthentication(HttpServletRequest request,
			HttpServletResponse response) throws AuthenticationException {
		Authentication authRequest = super.attemptAuthentication(request, response);
		logger.info("===== inside chatJwtFilter.attemptAuthentication =====");
		if (authRequest.isAuthenticated()){
			ChatUser chatUser = (ChatUser)authRequest.getPrincipal();
			String jwtToken = ChatJwtHelper.getToken(chatUser);
			tokenMap.put(chatUser.getUsrId(), jwtToken);
			response.addHeader(HttpHeaders.AUTHORIZATION, jwtToken);
			logger.info(jwtToken);
		}
		logger.info(authRequest.isAuthenticated() 
				+ " :Principal class: " + authRequest.getPrincipal().getClass()
				+ " :Authentication class: " + authRequest.getClass()
				+ " :Principal: " + ((ChatUser)authRequest.getPrincipal()).getChatUsrJwtKey().toString());
		return authRequest;
	}
	
	/**
	 * ChatJwtFilter override setAuthenticationManager so that Manager can be injected
	 * into parent class
	 * 
	 * ChatJwtFilter adds token to response header for successful authentication
	 * ChatJwtFilter observes logoutHandler and remove token
	 */
	@Override
	@Autowired
	public void setAuthenticationManager(AuthenticationManager authenticationManager) {
		super.setAuthenticationManager(authenticationManager);
	}

	public void update(Observable o, Object arg) {
		logger.info("===== inside chatJwtFilter.update =====");
		if (!(arg instanceof ChatUser)) {
			return;
		}
		ChatUser chatUser = (ChatUser)arg;
		Long userId = chatUser.getUsrId();
		String jwtToken = tokenMap.get(userId);
		logger.info("------ removing jwtToken for user: " + chatUser.getUsername() + " :: " + jwtToken);
		tokenMap.remove(userId);
	}
}