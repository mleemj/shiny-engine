package com.conf;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    private AbstractTokenRepository customCookieCsrTokenRepository;

    /**
     * TokenRepository @Component("token-repository") inform Spring
     */
    @Autowired
    @Qualifier("token-repository")
    public void setTokenRepository(AbstractTokenRepository
                                           repository) {
        this.customCookieCsrTokenRepository = repository;
    }
    
	@Override
	public void configure(HttpSecurity http) throws Exception {		
        http.csrf()
        .requireCsrfProtectionMatcher(
                customCookieCsrTokenRepository
                        .getRequireCsrfRequestMatcher())
        .csrfTokenRepository(
                customCookieCsrTokenRepository
                        .getTokenRepository());
	}
	
	@Bean
	public UserDetailsService userDetailsService() {
		InMemoryUserDetailsManager manager = new InMemoryUserDetailsManager();
		SimpleGrantedAuthority simple = new SimpleGrantedAuthority("USER");
		List<SimpleGrantedAuthority> authorities = new ArrayList<SimpleGrantedAuthority>();
		authorities.add(simple);
		String username = "user";
		String password = "password";
		UserDetails user = new User(username, password, authorities);
		manager.createUser(user);
		return manager;
	}
}
