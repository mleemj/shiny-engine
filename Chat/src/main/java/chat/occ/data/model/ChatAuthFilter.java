package chat.occ.data.model;

import java.io.IOException;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.AuthenticationEntryPoint;
import org.springframework.security.web.authentication.www.BasicAuthenticationFilter;

public class ChatAuthFilter extends BasicAuthenticationFilter {
	private Logger logger;

	public ChatAuthFilter(AuthenticationManager authMgr, AuthenticationEntryPoint authEntryPt) {
		super(authMgr, authEntryPt);
		logger = LoggerFactory.getLogger(ChatAuthFilter.class);
	}

	@Override
	protected void onSuccessfulAuthentication(HttpServletRequest request,
			HttpServletResponse response, Authentication authResult) throws IOException {
		logger.info("+++++ inside ChatAuthFilter +++++");
		logger.info(authResult.getPrincipal().toString());
	}
	
}
