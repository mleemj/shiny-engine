package chat.occ.data;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.annotation.Order;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.security.web.authentication.www.BasicAuthenticationFilter;

import chat.occ.data.model.ChatAuthFilter;
import chat.occ.data.model.ChatJwtFilter;
import chat.occ.data.model.ChatLSHandler;

@Configuration
@ComponentScan(basePackageClasses = { ChatUsrPersistence.class })
@EnableWebSecurity
public class SecurityConfig {
	
	@Configuration
	@Order(1)
	public static class ApiWebSecurityConfigurerAdapter extends WebSecurityConfigurerAdapter{
		private ChatUsrPersistence userDetailsService;

		@Autowired
		public ApiWebSecurityConfigurerAdapter(@Qualifier("chatUsrPersistence") ChatUsrPersistence persistenceService) {
			userDetailsService = persistenceService;
		}
		
		@Override
		protected void configure(AuthenticationManagerBuilder auth) throws Exception {
				auth.userDetailsService(userDetailsService);
		}

		/**
		 * Override method to expose AuthenticationManager to
		 * ChatJwtFilter.setAuthenticationManager
		 * 
		 * Filter override setAuthenticationManager so that Manager can be injected
		 * 
		 * ChatJwtFilter adds token to response header for successful authentication
		 * ChatJwtFilter observes logoutHandler and remove token
		 * 
		 */
		@Override
		public AuthenticationManager authenticationManagerBean() throws Exception {
			return super.authenticationManagerBean();
		}
		
		protected void configure(HttpSecurity http) throws Exception{
			ChatAuthFilter chatAuthFilter = new ChatAuthFilter(authenticationManager());
			http
				.csrf().disable()
				.antMatcher("/api/**")
				.authorizeRequests()
				.anyRequest()
				.authenticated()
					.and()
				.httpBasic()
					.and()
				.addFilterAt(chatAuthFilter, BasicAuthenticationFilter.class);		
		}
	}
	
	@Configuration
	public static class FormLoginWebSecurityConfigurereAdapter extends WebSecurityConfigurerAdapter{
		private ChatUsrPersistence userDetailsService;
		private ChatLSHandler logoutHandler;
		private ChatJwtFilter chatJwtFilter;
		
		
		@Autowired
		@Qualifier("chatJwtFilter")
		public void setChatJwtFilter(ChatJwtFilter jwtFilter){
			chatJwtFilter = jwtFilter;
		}

		@Autowired
		@Qualifier("chatLSHandler")
		public void setChatLSHandler(ChatLSHandler chatLsHandler) {
			logoutHandler = chatLsHandler;
		}

		@Autowired
		public FormLoginWebSecurityConfigurereAdapter(@Qualifier("chatUsrPersistence") ChatUsrPersistence persistenceService) {
			userDetailsService = persistenceService;
		}
		
		@Override
		protected void configure(AuthenticationManagerBuilder auth) throws Exception {
				auth.userDetailsService(userDetailsService);
		}

		/**
		 * Override method to expose AuthenticationManager to
		 * ChatJwtFilter.setAuthenticationManager
		 * 
		 * Filter override setAuthenticationManager so that Manager can be injected
		 * 
		 * ChatJwtFilter adds token to response header for successful authentication
		 * ChatJwtFilter observes logoutHandler and remove token
		 * 
		 */
		@Override
		public AuthenticationManager authenticationManagerBean() throws Exception {
			return super.authenticationManagerBean();
		}

		//LoginPage points to custom login.html in resources/static folder
		//
		//Choose either setting defaultSuccessUrl or successHandler.
		//Add successHandler to UsrSecConfig AuthenticationManager will result in viewroom.html
		//not rendered properly.
		@Override
		protected void configure(HttpSecurity http) throws Exception {
			http
					.csrf().disable()
					.authorizeRequests()
					.antMatchers("/view/**","/")
					.authenticated()
				.and()
					.formLogin()
					.loginPage("/login")
					.permitAll()
				.and()
					.logout()
					.addLogoutHandler(this.logoutHandler)
					.permitAll()
				.and()
					.addFilterAt(this.chatJwtFilter, UsernamePasswordAuthenticationFilter.class);
			this.logoutHandler.addObserver(this.chatJwtFilter);
		}
	}
	
}
