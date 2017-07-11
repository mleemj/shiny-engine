package chat.occ.data.model;

import java.io.IOException;

import javax.servlet.FilterChain;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.web.authentication.www.BasicAuthenticationFilter;

public class ChatAuthFilter extends BasicAuthenticationFilter {
	private Logger logger;

	public ChatAuthFilter(AuthenticationManager authMgr) {
		super(authMgr);
		logger = LoggerFactory.getLogger(ChatAuthFilter.class);
	}

	@Override
	protected void doFilterInternal(HttpServletRequest request,
            HttpServletResponse response,
            FilterChain chain)
     throws IOException,
            javax.servlet.ServletException{
		logger.info("------ inside ChatAuthFilter -----");
		logger.info(request.getParameter("username") + " :: " + request.getParameter("password"));
	}
}
